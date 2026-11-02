import argparse
import json
from pathlib import Path

from search import find_notes

parser = argparse.ArgumentParser(description="Search developer note titles.")
parser.add_argument("query", help="text to look for in note titles")
parser.add_argument("--count", action="store_true", help="print the number of matches")
args = parser.parse_args()

notes = json.loads(Path(__file__).with_name("notes.json").read_text(encoding="utf-8"))
matches = find_notes(notes, args.query)

if args.count:
    print(len(matches))
elif matches:
    for title in matches:
        print(title)
else:
    print("No matching notes.")
