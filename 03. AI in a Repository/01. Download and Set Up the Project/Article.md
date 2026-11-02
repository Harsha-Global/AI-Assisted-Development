# Download and Set Up the Project

Use the [AI-Assisted Development student repository](https://github.com/Harsha-Global/AI-Assisted-Development). It contains the course notes and exact source snapshots organized by section and lecture.

## 1. Download the materials

Choose Code > Download ZIP on GitHub and extract it. Alternatively, run:

```text
git clone https://github.com/Harsha-Global/AI-Assisted-Development.git
cd AI-Assisted-Development
```

The commands below start from the extracted repository's top folder.

## 2. Make your practice copy

For Meet Your Demo Project, Understand Code with Claude Code and Your First AI Code Change, start with:

```text
03. AI in a Repository/02. Meet Your Demo Project/Starter
```

On macOS/Linux:

```text
cp -R "03. AI in a Repository/02. Meet Your Demo Project/Starter" ../developer-notes-search-practice
cd ../developer-notes-search-practice
```

On Windows PowerShell:

```text
Copy-Item -Recurse "03. AI in a Repository/02. Meet Your Demo Project/Starter" ../developer-notes-search-practice
Set-Location ../developer-notes-search-practice
```

Choose a fresh destination name if that folder already exists. Open the resulting practice folder in your editor. You should see search.py, demo.py, notes.json and check_search.py directly inside it.

## 3. Run the starting checks

On macOS/Linux:

```text
python3 demo.py
python3 check_search.py
```

On Windows with the Python launcher:

```text
py -3 demo.py
py -3 check_search.py
```

The Starter should report 6/7 checks passed. The padded-query case fails because surrounding spaces have not yet been removed. This is the issue you will fix. No Python packages need installing.

To follow the Git review in your own practice folder, create a starting commit:

```text
git init -b main
git add .
git commit -m "Start AI-assisted development practice"
```

If Git asks for your identity, configure your own name and email. Start Claude Code from this same practice folder with `claude`. Use the prompts from the matching lecture resource folder; inspect any permission request before continuing.

## 4. Continue through the course

After the search fix, keep working in your own practice folder. All 7 checks should now pass. Turn a Request into a Plan and Build a Feature You Can Use start from that reviewed fix.

If you need a clean reference, [Reviewed search fix](https://github.com/Harsha-Global/AI-Assisted-Development/tree/main/03.%20AI%20in%20a%20Repository/04.%20Your%20First%20AI%20Code%20Change/Completed) contains the reviewed fix. [Completed command-line feature](https://github.com/Harsha-Global/AI-Assisted-Development/tree/main/04.%20Review%20and%20Next%20Steps/03.%20Build%20a%20Feature%20You%20Can%20Use/Completed) contains the finished command-line feature. Copy either to a fresh practice folder when needed. These are separate source snapshots, not branches of one working project.

The feature command is `python3 search_notes.py "  GIT  "` (Windows: `py -3 search_notes.py "  GIT  "`). It should print Git basics. Missing input should display usage and exit nonzero.

## 5. Save work to your own GitHub account

Commit your reviewed changes locally. If you want to push, create an empty repository in your own GitHub account and use its HTTPS URL as origin. Do not push to the instructor's repository. The Git command references in the lecture folders explain the review and commit steps.
