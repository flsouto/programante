import glob
from pathlib import Path
import re
from random import shuffle

readmes = glob.glob("*/README.md")
shuffle(readmes)

groups = {}

for r in readmes:
    lang = r.split('-')[0]
    if lang == 'php8': lang = 'php'
    if not lang in groups: groups[lang] = ""
    text = Path(r).read_text()
    match = re.search(r'#(.*)',text)
    if not match or not '?' in match.group(1):
        print("This post does not contain question mark in the heading: "+r)
        continue
    groups[lang] += "### "+match.group(1)+"\n[Veja a resposta]("+r+") \n"

result = "# Questões para os amantes de programação\n"
for lang in groups:
    result += "## Questões de "+lang+"\n"
    result += groups[lang]

Path("README.md").write_text(result)
