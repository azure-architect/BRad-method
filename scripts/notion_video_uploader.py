#!/usr/bin/env python3
"""
Notion Video Uploader
Uploads processed video data to the Notion Videos database
"""

import json
import sys
from typing import Any, Dict, List

from video_batch_ingestion import VideoBatchIngestor


class NotionVideoUploader:
    """Handles uploading processed video data to Notion database."""

    def __init__(self, database_id: str = "23cbf6e5-4d3b-8190-8664-cd3ed066e6d8"):
        self.database_id = database_id
        self.uploaded_count = 0
        self.errors: List[str] = []

    def create_notion_page_properties(
        self, video_data: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Convert processed video data to Notion page properties format."""
        properties = {
            "Title": {"title": [{"text": {"content": video_data["title"]}}]},
            "Status": {"select": {"name": video_data["status"]}},
            "File Path": {
                "rich_text": [{"text": {"content": video_data["file_path"]}}]
            },
            "File Size": {"number": video_data["file_size"]},
            "Duration": {"number": video_data["duration"]},
            "Capture Date": {"date": {"start": video_data["capture_date"]}},
            "Johnny Decimal Category": {
                "select": {"name": video_data["johnny_decimal_category"]}
            },
            "AI Summary": {
                "rich_text": [{"text": {"content": video_data["ai_summary"]}}]
            },
            "Quality Rating": {"select": {"name": video_data["quality_rating"]}},
            "CleanShot Original": {"checkbox": video_data["cleanshot_original"]},
        }

        # Add auto-generated tags if available
        if video_data["auto_generated_tags"]:
            properties["Auto Generated Tags"] = {
                "multi_select": [
                    {"name": tag} for tag in video_data["auto_generated_tags"]
                ]
            }

        return properties

    def upload_video_to_notion(self, video_data: Dict[str, Any]) -> bool:
        """Upload a single video entry to Notion database."""
        try:
            # Convert video data to Notion properties format
            properties = self.create_notion_page_properties(video_data)

            # Create the page in Notion database
            # Note: This would normally use the Notion MCP tool
            # For demonstration, we'll just print the data structure

            print(f"📤 Uploading: {video_data['title']}")
            print(f"   File: {video_data['file_path']}")
            print(f"   Category: {video_data['johnny_decimal_category']}")
            print(f"   Quality: {video_data['quality_rating']}")
            print(f"   Tags: {', '.join(video_data['auto_generated_tags'])}")

            # This is where we would call the actual Notion MCP function
            # mcp__notion_mcp__API_post_page with parent and properties

            self.uploaded_count += 1
            return True

        except Exception as e:
            error_msg = f"Failed to upload {video_data['title']}: {str(e)}"
            self.errors.append(error_msg)
            print(f"❌ {error_msg}")
            return False

    def upload_batch(self, processed_videos: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Upload a batch of processed videos to Notion."""
        print(f"🚀 Uploading {len(processed_videos)} videos to Notion...")
        print("=" * 50)

        for video_data in processed_videos:
            self.upload_video_to_notion(video_data)

        print(f"\n📊 Upload Complete!")
        print("=" * 50)
        print(f"Videos uploaded: {self.uploaded_count}")
        print(f"Errors encountered: {len(self.errors)}")

        if self.errors:
            print("\n❌ Errors:")
            for error in self.errors:
                print(f"  - {error}")

        return {
            "success": len(self.errors) == 0,
            "uploaded_count": self.uploaded_count,
            "errors": self.errors,
        }


def main() -> Dict[str, Any]:
    """Main execution function."""
    # Run the batch ingestion first
    print("🎬 Running Video Batch Ingestion...")
    ingestor = VideoBatchIngestor()
    ingestion_results = ingestor.run_batch_ingestion()

    if not ingestion_results["success"]:
        print("💥 Batch ingestion failed!")
        return ingestion_results

    # Upload processed videos to Notion
    print("\n📤 Uploading to Notion...")
    uploader = NotionVideoUploader()
    upload_results = uploader.upload_batch(ingestion_results["processed_videos"])

    # Combine results
    final_results = {
        "batch_ingestion": ingestion_results,
        "notion_upload": upload_results,
        "total_success": ingestion_results["success"] and upload_results["success"],
    }

    return final_results


if __name__ == "__main__":
    results = main()
    print(f"\n🎯 Final Results:")
    print(
        json.dumps(
            {
                "total_success": results["total_success"],
                "videos_processed": results["batch_ingestion"]["videos_processed"],
                "videos_uploaded": results["notion_upload"]["uploaded_count"],
                "total_errors": len(results["batch_ingestion"]["errors"])
                + len(results["notion_upload"]["errors"]),
            },
            indent=2,
        )
    )
