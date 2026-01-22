# API Documentation Generator Skill

Generate comprehensive, developer-friendly API documentation automatically from your codebase.

## What This Skill Does

This skill helps you create professional API documentation that includes:
- Endpoint descriptions with full details
- Request/response examples in multiple languages
- Authentication and authorization guides
- Error handling documentation
- Interactive examples and collections

## Quick Start

```
@api-documentation-generator Document my REST API endpoints
```

The AI will:
1. Analyze your API structure
2. Generate documentation for each endpoint
3. Include code examples in multiple languages
4. Document authentication and errors
5. Provide best practices and guidelines

## Use Cases

### 1. New API Documentation
Starting from scratch with a new API:
```
@api-documentation-generator I have a new REST API for user management. 
Help me create complete documentation.
```

### 2. Update Existing Docs
Keeping documentation in sync:
```
@api-documentation-generator I added new endpoints for payments. 
Update the API documentation.
```

### 3. Generate OpenAPI Spec
Creating machine-readable specifications:
```
@api-documentation-generator Generate an OpenAPI 3.0 specification 
for my API endpoints.
```

### 4. Create Postman Collection
Making it easy to test:
```
@api-documentation-generator Create a Postman collection for all 
my API endpoints.
```

## What You'll Get

### For Each Endpoint
- HTTP method and URL
- Description and purpose
- Authentication requirements
- Request parameters (path, query, body)
- Response formats (success and errors)
- Code examples (cURL, JavaScript, Python, etc.)

### Additional Documentation
- Getting started guide
- Authentication setup
- Error code reference
- Rate limiting details
- Best practices
- Common use cases

## Examples

### REST API
```
@api-documentation-generator Document this Express.js route:

app.post('/api/users', async (req, res) => {
  const { email, password, name } = req.body;
  // ... implementation
});
```

### GraphQL API
```
@api-documentation-generator Document this GraphQL schema:

type Query {
  user(id: ID!): User
  users(limit: Int, offset: Int): [User!]!
}
```

### WebSocket API
```
@api-documentation-generator Document this WebSocket event:

socket.on('message:send', (data) => {
  // ... implementation
});
```

## Best Practices

1. **Keep It Updated** - Regenerate docs when API changes
2. **Test Examples** - Ensure all code examples work
3. **Be Comprehensive** - Document all endpoints, not just the happy path
4. **Use Standards** - Follow OpenAPI/Swagger specifications
5. **Provide Context** - Explain why, not just what

## Tips

- Provide your API code or route definitions for best results
- Mention your tech stack (Express, FastAPI, GraphQL, etc.)
- Specify which programming languages you want examples in
- Include any existing documentation to maintain consistency

## Related Skills

- `@doc-coauthoring` - Collaborative documentation
- `@copywriting` - Clear, user-friendly writing
- `@test-driven-development` - Ensure API behavior matches docs

## Output Formats

This skill can generate documentation in:
- Markdown (for GitHub, GitBook, etc.)
- OpenAPI/Swagger YAML
- Postman Collection JSON
- HTML (for static sites)
- ReDoc/Swagger UI compatible formats

---

**Pro Tip:** Use this skill early in development to establish documentation patterns, then keep it updated as your API evolves!
