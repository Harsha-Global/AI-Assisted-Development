# One small task

Change only search.py so find_notes ignores leading/trailing whitespace in the query. Preserve case-insensitive substring matching and the original note order. Empty and whitespace-only queries return an empty list.

| Query | Expected after the change |
| --- | --- |
| `git` | Git basics |
| `GIT` | Git basics |
| `  git  ` (two spaces each side) | Git basics |
| `python` | Python tips |
| Empty string | No matches |
| Three spaces | No matches |
| `missing-note` | No matches |

The note data, caller, supplied checks and dependencies stay unchanged. The checks cover these examples; inspecting the unchanged iteration also supports the note-order requirement. A larger project's test strategy is beyond this introductory task.
