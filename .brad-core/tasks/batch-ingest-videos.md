# Batch Ingest Videos Task

## Task Definition
```yaml
task:
  name: batch-ingest-videos
  agent: video-ingestion
  description: Process all videos in the ingestion directory
  
parameters:
  ingestion_path: "/Volumes/Samsung/mo/vid_in"
  
workflow:
  1. scan_directory:
     - Check ingestion path accessibility
     - List all video files (MP4, MOV, AVI, MKV, WebM)
     - Log found videos for processing
     
  2. process_each_video:
     - Extract metadata (duration, size, capture date)
     - Generate transcript via speech-to-text
     - Create AI summary of content
     - Auto-generate content tags
     - Assess quality rating
     - Assign Johnny Decimal category
     
  3. notion_integration:
     - Create entry in Videos database
     - Populate all fields:
       - Title (from filename or content)
       - Status: "Raw"
       - File Path: Original location
       - File Size, Duration
       - Transcript, AI Summary
       - Auto-generated tags
       - Quality rating
     - Link to related projects/tasks if detected
     
  4. file_organization:
     - Move processed files to archive
     - Generate thumbnails
     - Update file paths in Notion
     - Clean up temporary files

error_handling:
  - Skip corrupted/unsupported files
  - Log processing errors
  - Continue with remaining videos
  - Report summary at end
```

## Usage
```bash
# Process all videos in ingestion directory
/BRad video-ingestion batch-ingest

# Process with specific options
/BRad video-ingestion batch-ingest --path="/Volumes/Samsung/mo/vid_in" --auto-archive

# Dry run to see what would be processed
/BRad video-ingestion batch-ingest --dry-run
```

## Expected Output
- Number of videos found
- Processing status for each
- Notion entries created
- Any errors encountered
- Total processing time