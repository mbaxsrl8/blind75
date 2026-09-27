# Repository Instructions

- Problem files use a first-line `# Tags:` comment for searchable tags.
- Keep tags lowercase and use hyphens for multi-word tags.
- Whenever tags are added or changed in a problem file, update the matching sections in `README.md`.
- Mark problems needing focused review with the `needs-review` tag and add them to the matching README section.
- Use `README.md`'s existing tag names when possible; for example, use `depth-first-search` for DFS.
- For dynamic programming implementations and explanations, do not use caching decorators such as `@cache` or `@lru_cache`. Store states explicitly in basic Python collections such as dictionaries or lists, and show the memoization lookup and storage logic without shortcuts.
- When generating Python code, including explanatory examples and nested helper functions, annotate all function and method parameters (except `self` and `cls`) and return types. Use Python's `bool` type for boolean values.
