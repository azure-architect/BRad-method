# Process Unprocessed Ideas Task

**Task ID:** process-unprocessed-ideas  
**Agent:** Idea-Man  
**Purpose:** Batch process all unprocessed ideas from Notion Ideas database

## Database Configuration

**Target Database:** Ideas (Ideations Page)  
**Database ID:** `23ebf6e5-4d3b-8157-9b7d-c4048e5b6f6f`  
**Properties Schema:**
- Title (title)
- Status (select: Raw, Processing, Processed, Content Ready)
- Category (select: Insight, Metaphor, Framework, Distinction, Story, Question, Contrarian View)
- Raw Content (rich_text)
- AI Summary (rich_text)
- Key Topics (multi_select)
- Tags (multi_select)
- Capture Method (select)
- Processed (checkbox)
- Created/Modified (timestamps)

## Quick Command Access

**User Intent:** "Go process my unprocessed ideas"  
**Command Match:** `*process` or `*process-unprocessed`  
**Elicit:** false (fully automated)

## Task Definition

This is the main task that enables the workflow: "Hey Idea-Man, go process my unprocessed ideas." It automatically finds and processes all raw ideas in your Notion database.

## Execution Flow

### 1. Discovery Phase
```bash
# Query Notion for unprocessed ideas
notion_query = {
  "database_id": "23ebf6e5-4d3b-8157-9b7d-c4048e5b6f6f",
  "filter": {
    "and": [
      {
        "property": "Status",
        "select": {
          "equals": "Raw"
        }
      },
      {
        "property": "Processed", 
        "checkbox": {
          "equals": false
        }
      }
    ]
  },
  "sorts": [
    {
      "property": "Created",
      "direction": "ascending"
    }
  ]
}
```

### 2. Batch Processing
- Process in batches of 5-10 ideas to avoid overwhelming
- Use process-dictation.md workflow for each idea
- Track progress and provide updates

### 3. Intelligence Layer
Apply Idea-Man's enhanced processing:
- **Voice Pattern Learning** - Adapt to user's style
- **Semantic Analysis** - Deep content understanding  
- **Connection Discovery** - Link related concepts
- **Pattern Recognition** - Identify thinking themes

### 4. Update & Organize
For each processed idea:
```notion-update
Status: "Raw" → "Processed"
AI Summary: [Generated insight summary]
Key Topics: [Add discovered categories]
Tags: [Apply semantic tags]
Processed: true
Modified: [timestamp]
```

## Sample Execution

**User:** "Go process my unprocessed ideas"

**Idea-Man Response:**
```
🧠 Processing your unprocessed ideas...

🔍 Discovery: Found 7 unprocessed ideas
📊 Categories detected: insights(3), frameworks(2), metaphors(1), questions(1)

Processing batch 1 (5 ideas)...
✅ "Marketing automation thoughts" → Framework
✅ "Customer journey insights" → Insight  
✅ "Like building a house analogy" → Metaphor
✅ "What if we approached this differently?" → Question
✅ "Sales process improvements" → Framework

Processing batch 2 (2 ideas)...
✅ "User onboarding revelations" → Insight
✅ "Product positioning clarity" → Insight

🎯 Processing Complete!
- 7 ideas processed
- 3 insights discovered
- 2 frameworks identified  
- 1 powerful metaphor captured
- 1 exploration question noted
- 12 new semantic connections made

💡 Content Opportunities:
- Framework content ready: Sales process, Marketing automation
- Blog post potential: Customer journey insights, User onboarding
- Social content: House building metaphor

Ready for content generation or further exploration!
```

## Integration Requirements

### Notion MCP Access
- Database query capabilities
- Page retrieval and updates
- Property manipulation

### Processing Intelligence
- NLP analysis for categorization
- Semantic similarity detection
- Voice pattern preservation
- Content structure recognition

### Knowledge Graph
- Connection identification
- Relationship mapping
- Insight clustering
- Pattern analysis

## Error Handling

### API Failures
- Graceful degradation with retry logic
- Preserve processing state between attempts
- Log failures for manual review

### Content Issues
- Handle malformed or empty content
- Preserve original raw content always
- Flag problematic entries for review

### Processing Errors
- Continue processing other ideas if one fails
- Provide partial success reports
- Enable resume functionality

## Success Metrics

- **Processing Rate** - Ideas processed per minute
- **Categorization Accuracy** - Proper category assignment
- **Connection Discovery** - New relationships found
- **Content Readiness** - Ideas ready for content generation
- **User Satisfaction** - Preserved voice and intent

## Customization

**Processing Depth:**
- `quick` - Basic categorization and tagging
- `standard` - Full analysis with connections (default)
- `deep` - Comprehensive analysis with content suggestions

**Batch Size:**
- Small (3-5) - For detailed processing
- Medium (5-10) - Balanced approach (default)
- Large (10-20) - Fast bulk processing

**Focus Areas:**
- `insights` - Prioritize breakthrough moments
- `frameworks` - Focus on systematic approaches
- `content` - Optimize for content generation
- `connections` - Emphasize relationship discovery