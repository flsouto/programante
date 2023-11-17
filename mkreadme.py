import glob
from pathlib import Path
import re

readmes = glob.glob("*/README.md")

result = ""

for r in readmes:
    lang = r.split('-')[0]
    text = Path(r).read_text()
    match = re.search(r'#(.*)',text)
    if not match or not '?' in match.group(1):
        print("This post does not contain question mark in the heading: "+r)
        continue
    result += "## "+match.group(1)+"?"
