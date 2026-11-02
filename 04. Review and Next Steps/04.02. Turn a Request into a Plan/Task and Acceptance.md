# Feature ticket — search notes from the terminal

Outcome: a teammate can run `python3 search_notes.py "query"` to search the supplied fictional notes without editing Python source.

Scope: create search_notes.py and append concise usage instructions to README.md. Reuse find_notes and notes.json. Leave all earlier source, sample data, checks and dependencies unchanged. Resolve the notes file relative to the new script. Use standard-library argparse for one required positional query.

| Case | Required behavior |
| --- | --- |
| `"  GIT  "` | Prints Git basics; exit 0 |
| `"code"` | Prints Code review checklist; exit 0 |
| `"missing-note"` | Prints No matching notes.; exit 0 |
| `"   "` | Prints No matching notes.; exit 0 |
| No query argument | Usage and missing-argument explanation; nonzero exit (argparse normally 2) |
| Existing check_search.py | All seven acceptance cases still pass |

Print each matching title on its own line, retaining source order. Inspect the actual call to the existing function rather than duplicating its matching rules. These are the acceptance criteria for your own implementation.
