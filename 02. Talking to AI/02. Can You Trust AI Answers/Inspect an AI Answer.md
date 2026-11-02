# Inspect an AI answer

- Compare the explanation with the actual relevant source.
- Separate supplied facts from assumptions about unseen code or callers.
- Check the input path when it affects where the change belongs.
- Run a focused check and inspect the actual result.
- Keep the conclusion within the evidence; a later code change needs its own checks.

In this example, a second answer agreeing does not replace running the local function. The three baseline inputs establish three observed cases, not a complete specification or production-ready fix.
