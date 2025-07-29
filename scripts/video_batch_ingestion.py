#!/usr/bin/env python3
"""
Video Batch Ingestion Script
Implements the Brad Method Video Ingestion Agent batch processing workflow
"""

import datetime
import json
import os
import re
import subprocess
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple


class VideoBatchIngestor:
    """Handles batch ingestion of video files for the Brad Method system."""

    def __init__(self, ingestion_path: str = "/Volumes/Samsung/mo/vid_in"):
        self.ingestion_path = Path(ingestion_path)
        self.supported_formats = {".mp4", ".mov", ".avi", ".mkv", ".webm"}
        self.notion_database_id = "23cbf6e5-4d3b-8190-8664-cd3ed066e6d8"
        self.processed_videos: List[Dict] = []
        self.errors: List[str] = []

    def scan_directory(self) -> List[Path]:
        """Scan the ingestion directory for video files."""
        print(f"🔍 Scanning directory: {self.ingestion_path}")

        if not self.ingestion_path.exists():
            raise FileNotFoundError(
                f"Ingestion directory not found: {self.ingestion_path}"
            )

        video_files = []
        for file_path in self.ingestion_path.iterdir():
            if (
                file_path.is_file()
                and file_path.suffix.lower() in self.supported_formats
            ):
                video_files.append(file_path)

        print(f"📹 Found {len(video_files)} video files:")
        for video in video_files:
            print(f"  - {video.name}")

        return video_files

    def extract_metadata(self, video_path: Path) -> Dict[str, Any]:
        """Extract metadata from a video file using ffprobe."""
        print(f"📊 Extracting metadata from: {video_path.name}")

        try:
            # Use ffprobe to get video metadata
            cmd = [
                "ffprobe",
                "-v",
                "quiet",
                "-print_format",
                "json",
                "-show_format",
                "-show_streams",
                str(video_path),
            ]
            result = subprocess.run(cmd, capture_output=True, text=True, check=True)
            metadata = json.loads(result.stdout)

            # Extract relevant information
            format_info = metadata.get("format", {})
            video_stream: Dict = next(
                (
                    s
                    for s in metadata.get("streams", [])
                    if s.get("codec_type") == "video"
                ),
                {},
            )

            # Calculate duration in seconds
            duration = float(format_info.get("duration", 0))

            # Get file size
            file_size = int(format_info.get("size", 0))

            # Get capture date from filename or file modification time
            capture_date = self._extract_capture_date(video_path)

            # Detect if it's a CleanShot recording
            is_cleanshot = "cleanshot" in video_path.name.lower()

            # Get resolution
            width = video_stream.get("width", 0)
            height = video_stream.get("height", 0)

            return {
                "duration": duration,
                "file_size": file_size,
                "capture_date": capture_date,
                "is_cleanshot": is_cleanshot,
                "width": width,
                "height": height,
                "codec": video_stream.get("codec_name", "unknown"),
                "file_path": str(video_path),
            }

        except subprocess.CalledProcessError as e:
            error_msg = f"Failed to extract metadata from {video_path.name}: {e}"
            self.errors.append(error_msg)
            print(f"❌ {error_msg}")
            return {}

    def _extract_capture_date(self, video_path: Path) -> str:
        """Extract capture date from filename or file modification time."""
        # Try to extract date from CleanShot filename format
        date_pattern = r"(\d{4}-\d{2}-\d{2})"
        match = re.search(date_pattern, video_path.name)

        if match:
            return match.group(1)
        else:
            # Fall back to file modification time
            mtime = video_path.stat().st_mtime
            return datetime.datetime.fromtimestamp(mtime).strftime("%Y-%m-%d")

    def generate_title(self, video_path: Path, metadata: Dict[str, Any]) -> str:
        """Generate a title for the video based on filename and metadata."""
        # Clean up the filename
        title = video_path.stem

        # Remove CleanShot prefix and timestamp
        title = re.sub(
            r"^CleanShot \d{4}-\d{2}-\d{2} at \d{2}\.\d{2}\.\d{2}", "", title
        ).strip()

        # If no meaningful title remains, create one based on date
        if not title:
            capture_date = metadata.get("capture_date", "Unknown Date")
            title = f"Screen Recording {capture_date}"

        return title

    def categorize_video(self, video_path: Path, metadata: Dict[str, Any]) -> Tuple[str, str]:
        """Assign Johnny Decimal category based on content analysis."""
        filename_lower = video_path.name.lower()

        # Auto-categorization rules based on filename patterns
        if any(word in filename_lower for word in ["tutorial", "how-to", "guide"]):
            return "60-69 Tutorials", "Tutorial content detected"
        elif any(word in filename_lower for word in ["demo", "demonstration"]):
            return "50-59 Demos", "Demo content detected"
        elif any(word in filename_lower for word in ["idea", "brainstorm", "concept"]):
            return "30-39 Ideas", "Idea/concept content detected"
        elif any(word in filename_lower for word in ["project", "meeting"]):
            return "10-19 Projects", "Project-related content detected"
        elif metadata.get("is_cleanshot", False):
            return "40-49 Documentation", "CleanShot screen recording detected"
        else:
            return "70-79 Archive", "Default categorization"

    def generate_auto_tags(self, video_path: Path, metadata: Dict[str, Any]) -> List[str]:
        """Generate automatic tags based on content analysis."""
        tags = []
        filename_lower = video_path.name.lower()

        # Add CleanShot tag if applicable
        if metadata.get("is_cleanshot", False):
            tags.extend(["cleanshot", "screen-recording"])

        # Add tags based on filename patterns
        if "demo" in filename_lower:
            tags.extend(["demo", "system-demo"])

        if "workflow" in filename_lower:
            tags.append("workflow")

        if "automation" in filename_lower:
            tags.append("automation")

        # Add format-based tags
        if video_path.suffix.lower() == ".mp4":
            tags.append("mp4")

        # Add quality-based tags
        if metadata.get("height", 0) >= 1080:
            tags.append("hd")

        return list(set(tags))  # Remove duplicates

    def assess_quality(self, metadata: Dict[str, Any]) -> str:
        """Assess video quality based on technical metrics."""
        height = metadata.get("height", 0)
        duration = metadata.get("duration", 0)
        file_size = metadata.get("file_size", 0)

        score = 0

        # Resolution scoring
        if height >= 1080:
            score += 2
        elif height >= 720:
            score += 1

        # Duration scoring (reasonable length)
        if 30 <= duration <= 1800:  # 30 seconds to 30 minutes
            score += 1

        # File size vs duration ratio (basic quality indicator)
        if duration > 0:
            bitrate = (file_size * 8) / duration  # bits per second
            if bitrate > 5000000:  # > 5 Mbps
                score += 1

        # Map score to star rating
        if score >= 4:
            return "⭐⭐⭐⭐⭐"
        elif score >= 3:
            return "⭐⭐⭐⭐☆"
        elif score >= 2:
            return "⭐⭐⭐☆☆"
        elif score >= 1:
            return "⭐⭐☆☆☆"
        else:
            return "⭐☆☆☆☆"

    def create_ai_summary(self, video_path: Path, metadata: Dict[str, Any]) -> str:
        """Generate AI summary based on available information."""
        # This is a simplified version - in a full implementation,
        # this would use actual speech-to-text and AI analysis

        title = self.generate_title(video_path, metadata)
        duration_min = int(metadata.get("duration", 0) // 60)
        duration_sec = int(metadata.get("duration", 0) % 60)

        summary = f"Video recording: {title}\n"
        summary += f"Duration: {duration_min}m {duration_sec}s\n"

        if metadata.get("is_cleanshot", False):
            summary += "CleanShot screen recording showing system interactions and workflows.\n"

        category, reason = self.categorize_video(video_path, metadata)
        summary += f"Content category: {category} ({reason})\n"

        return summary.strip()

    def process_single_video(self, video_path: Path) -> Dict[str, Any]:
        """Process a single video file through the complete pipeline."""
        print(f"\n🎬 Processing: {video_path.name}")

        try:
            # Extract metadata
            metadata = self.extract_metadata(video_path)
            if not metadata:
                return {}

            # Generate processed data
            title = self.generate_title(video_path, metadata)
            category, category_reason = self.categorize_video(video_path, metadata)
            auto_tags = self.generate_auto_tags(video_path, metadata)
            quality_rating = self.assess_quality(metadata)
            ai_summary = self.create_ai_summary(video_path, metadata)

            # Create processed video data
            processed_data = {
                "title": title,
                "file_path": str(video_path),
                "file_size": metadata["file_size"],
                "duration": metadata["duration"],
                "capture_date": metadata["capture_date"],
                "johnny_decimal_category": category,
                "auto_generated_tags": auto_tags,
                "quality_rating": quality_rating,
                "ai_summary": ai_summary,
                "cleanshot_original": metadata["is_cleanshot"],
                "status": "Raw",
                "metadata": metadata,
            }

            print(f"✅ Successfully processed: {title}")
            return processed_data

        except Exception as e:
            error_msg = f"Failed to process {video_path.name}: {str(e)}"
            self.errors.append(error_msg)
            print(f"❌ {error_msg}")
            return {}

    def run_batch_ingestion(self) -> Dict[str, Any]:
        """Execute the complete batch ingestion workflow."""
        print("🚀 Starting Video Batch Ingestion Workflow")
        print("=" * 50)

        start_time = datetime.datetime.now()

        try:
            # Step 1: Scan directory
            video_files = self.scan_directory()

            if not video_files:
                print("ℹ️ No video files found to process.")
                return {
                    "success": True,
                    "videos_found": 0,
                    "videos_processed": 0,
                    "errors": [],
                    "processing_time": 0,
                }

            # Step 2: Process each video
            print(f"\n🔄 Processing {len(video_files)} videos...")

            for video_path in video_files:
                processed_data = self.process_single_video(video_path)
                if processed_data:
                    self.processed_videos.append(processed_data)

            # Step 3: Report results
            end_time = datetime.datetime.now()
            processing_time = (end_time - start_time).total_seconds()

            print(f"\n📊 Batch Ingestion Complete!")
            print("=" * 50)
            print(f"Videos found: {len(video_files)}")
            print(f"Videos processed: {len(self.processed_videos)}")
            print(f"Errors encountered: {len(self.errors)}")
            print(f"Processing time: {processing_time:.2f} seconds")

            if self.errors:
                print("\n❌ Errors:")
                for error in self.errors:
                    print(f"  - {error}")

            return {
                "success": True,
                "videos_found": len(video_files),
                "videos_processed": len(self.processed_videos),
                "processed_videos": self.processed_videos,
                "errors": self.errors,
                "processing_time": processing_time,
            }

        except Exception as e:
            error_msg = f"Batch ingestion failed: {str(e)}"
            print(f"💥 {error_msg}")
            return {
                "success": False,
                "error": error_msg,
                "videos_found": 0,
                "videos_processed": 0,
                "errors": [error_msg],
                "processing_time": 0,
            }


def main() -> Dict[str, Any]:
    """Main execution function."""
    # Initialize the batch ingestor
    ingestor = VideoBatchIngestor()

    # Run the batch ingestion workflow
    results = ingestor.run_batch_ingestion()

    # Output results as JSON for further processing
    print(f"\n📋 Results Summary:")
    print(
        json.dumps(
            {
                "success": results["success"],
                "videos_found": results["videos_found"],
                "videos_processed": results["videos_processed"],
                "error_count": len(results["errors"]),
                "processing_time": results["processing_time"],
            },
            indent=2,
        )
    )

    return results


if __name__ == "__main__":
    main()
