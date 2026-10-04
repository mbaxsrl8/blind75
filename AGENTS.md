# Repository Instructions

- Problem files use a first-line `# Tags:` comment for searchable tags.
- Keep tags lowercase and use hyphens for multi-word tags.
- When the user asks how to improve a current solution, explain the improvements without editing their code. Only edit code when the user explicitly requests changes.
- When the user asks to add tags, update both the problem file and the matching `README.md` section. For other changes, update `README.md` only when the user explicitly requests it.
- Mark problems needing focused review with the `needs-review` tag. When the user asks to add this tag, update the matching README section as well; otherwise, update that section only when explicitly requested.
- Use `README.md`'s existing tag names when possible; for example, use `depth-first-search` for DFS.
- For dynamic programming implementations and explanations, do not use caching decorators such as `@cache` or `@lru_cache`. Store states explicitly in basic Python collections such as dictionaries or lists, and show the memoization lookup and storage logic without shortcuts.
- When generating Python code, including explanatory examples and nested helper functions, annotate all function and method parameters (except `self` and `cls`) and return types. Use Python's `bool` type for boolean values.
