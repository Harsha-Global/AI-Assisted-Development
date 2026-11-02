# Your Practice Task and Troubleshooting

You have seen a request become context, a plan, a file change and a checked result. Now try that loop on a small extension to the completed command-line project.

## Task: add a count option

Start from the completed project supplied with Build a Feature You Can Use, or use your own working version after its checks pass. Add an optional `--count` flag. With the flag, print the number of matching note titles. Without it, preserve the existing output.

Change search_notes.py and its README usage note only. Reuse find_notes and notes.json. Keep the existing matching rules, data, supplied checks and dependencies unchanged.

## Acceptance examples

- `python3 search_notes.py "git" --count` prints 1.
- `python3 search_notes.py "  GIT  " --count` prints 1.
- `python3 search_notes.py "missing-note" --count` prints 0.
- `python3 search_notes.py "   " --count` prints 0.
- Without --count, a git query still prints Git basics, and a missing match still prints No matching notes.
- Omitting the query still displays usage and exits nonzero.
- The original check_search.py still reports 7/7 checks passed.

On Windows, replace python3 with py -3.

## Follow the loop

Download the attached Practice Worksheet and fill in the intended behavior, context, permitted files and checks. Ask the assistant for a short plan first. Review it, then request implementation. Record the actual results and inspect new/untracked files as well as the Git diff before accepting the work.

The matching repository folder contains a Practice Starter and a Reference Solution. Try the task before comparing your result with the solution. The solution is a supplied practice example; your assistant may choose a different correct implementation.

## Common problems

- **Python command not found:** try python3 on macOS/Linux or py -3 on Windows; check your Python 3 installation.
- **Cannot find a file or import search:** open a terminal in the practice source folder, where search.py and notes.json are directly visible. The course repository root is a collection of lecture resources.
- **Starter reports a failed check:** the padded-query case intentionally fails before the whitespace fix. After the fix, investigate any remaining failure.
- **Claude Code cannot start or sign in:** check access and installation using the [official quickstart](https://code.claude.com/docs/en/quickstart). Account limits can interrupt a session; keep your files and resume after access is available.
- **Git diff looks empty:** inspect git status --short. A newly created file is untracked until staged and does not appear in an ordinary diff.
- **Push is rejected:** check git remote -v. Push to a repository you own; the instructor's resource repository is for downloading reference material.

Keep a record of the request, accepted changes, observed checks and your decision. That is the evidence you should be able to explain after the exercise.
