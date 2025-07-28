# Search Ideations Task

**Task ID:** search-ideations  
**Agent:** Idea-Man  
**Purpose:** Search and retrieve ideas from your Notion Notes database using semantic and keyword search

## Task Overview

Enables Idea-Man to search your processed ideations library using various search strategies including semantic similarity, keyword matching, category filtering, and tag-based retrieval.

## Prerequisites

- Notion MCP access to Notes v1.0 database
- Processed ideas with AI summaries and categorization
- Search query from user

## Search Strategies

### 1. Semantic Search
```notion-query
# Search AI Summary and Raw Content for conceptual matches
Database: Notes v1.0 (23bbf6e5-4d3b-81d1-beb5-e1016a65db65)
Filter:
  - Status = "Processed"
  - AI Summary contains semantic matches for query
  - Raw Content contains related concepts
```

### 2. Category Search
```notion-query
# Search by specific insight categories
Filter:
  - Key Topics contains [insights|metaphors|frameworks|distinctions|etc.]
  - Tags contain category-specific terms
```

### 3. Keyword Search
```notion-query
# Direct text matching
Filter:
  - Title contains query terms
  - Raw Content contains exact phrases
  - Tags contain matching keywords
```

### 4. Time-based Search
```notion-query
# Search within time ranges
Filter:
  - Created date range
  - Modified date range
  - Recent processing activity
```

## Search Execution

### Input Processing
1. **Parse Search Query**
   - Extract keywords and phrases
   - Identify category hints (e.g., "framework about X")
   - Detect semantic intent

2. **Determine Search Strategy**
   - Exact match for specific titles/phrases
   - Semantic search for conceptual queries
   - Category search for type-specific requests
   - Combined approach for complex queries

3. **Execute Multi-layered Search**
   ```typescript
   search_results = {
     exact_matches: [],      // Direct title/content matches
     semantic_matches: [],   // Conceptually related
     category_matches: [],   // Same category/type
     related_ideas: []       // Connected concepts
   }
   ```

### Result Processing

#### Relevance Scoring
- **Exact Title Match**: 100 points
- **AI Summary Match**: 80 points  
- **Raw Content Match**: 60 points
- **Tag Match**: 40 points
- **Category Match**: 30 points
- **Related Connection**: 20 points

#### Result Enrichment
For each result, provide:
- **Original Idea**: Title and key content
- **Category**: insight/metaphor/framework/etc.
- **AI Summary**: Processed insights
- **Relevance Score**: Why it matched
- **Related Ideas**: Connected concepts
- **Content Potential**: Generation opportunities

## Output Formats

### Standard Search Results
```markdown
🔍 **Search Results for:** "{query}"

**Found {count} matching ideas:**

1. **[Idea Title]** (Score: {relevance}/100)
   - **Category:** {insight/metaphor/framework}
   - **Summary:** {AI-generated summary}
   - **Match:** {why it matched your query}
   - **Related:** {connected ideas}

2. **[Next Idea]** ...

💡 **Content Opportunities:**
- {suggestions for using these ideas}

🔗 **Related Searches:**
- {suggested follow-up queries}
```

### Category-Specific Results
```markdown
🧠 **{Category} Ideas about:** "{query}"

**Frameworks ({count}):**
- {framework ideas with structured approaches}

**Insights ({count}):**
- {breakthrough realizations and epiphanies}

**Metaphors ({count}):**
- {analogies that simplify concepts}
```

### Quick Reference Format
```markdown
📝 **Quick Reference:**
• {Idea 1} - {one-line summary}
• {Idea 2} - {one-line summary}
• {Idea 3} - {one-line summary}

Type `generate blog` to create content from these ideas.
```

## Advanced Features

### Connection Discovery
- **Related Ideas**: Find conceptually similar content
- **Idea Clusters**: Group related concepts together
- **Pattern Recognition**: Identify recurring themes
- **Knowledge Gaps**: Suggest unexplored areas

### Content Preparation
- **Content-Ready Ideas**: Flag ideas ready for development
- **Combination Opportunities**: Suggest idea combinations
- **Format Recommendations**: Best content format for ideas
- **Audience Targeting**: Match ideas to audiences

### Learning Integration
- **Usage Tracking**: Which ideas get searched most
- **Pattern Analysis**: Common search patterns
- **Relevance Feedback**: Improve future searches
- **Content Performance**: Track idea-to-content success

## Search Examples

### Semantic Queries
- "marketing automation ideas" → frameworks, insights about marketing systems
- "customer journey thoughts" → insights, stories about customer experience
- "scaling challenges" → frameworks, distinctions about growth

### Category Queries  
- "frameworks about leadership" → structured approaches to leadership
- "metaphors for explaining complex concepts" → analogies and comparisons
- "contrarian views on productivity" → alternative perspectives

### Content-Focused Queries
- "blog post ideas" → processed ideas ready for long-form content
- "social media content" → insights suitable for short-form posts
- "speaking points" → ideas that work well for presentations

## Integration Points

### Notion API Functions
- `mcp__notion-mcp__API-post-database-query` - Search and filter
- `mcp__notion-mcp__API-retrieve-a-page` - Get full content
- Advanced filtering and sorting capabilities

### Knowledge Graph
- Semantic similarity scoring
- Connection traversal
- Cluster identification
- Pattern recognition

### Content Generation Bridge
- Prepare ideas for content creation
- Suggest optimal formats
- Enable seamless workflow to generation