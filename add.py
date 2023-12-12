import slugify
from pathlib import Path
from stop_words import get_stop_words

title = input("title:")
lang, title = title.split(':')
lang = lang.lower()
filtered_words = [word for word in title.split(' ') if word not in get_stop_words('portuguese')]
slug = lang + '-' + slugify.slugify(' '.join(filtered_words))
path = Path(slug)
if not path.exists(): path.mkdir()

import sys
print("content:")
content = "#{}\n".format(title.title()) + sys.stdin.read();

readmef = path / "README.md"
pendingf = path / "pending"
pendingf.touch()

with open(readmef, "w") as f:
    f.write(content)


from subprocess import check_output
def run(*args):
    print(check_output(args))

run("python3", "mkreadme.py")
run("git","add","-u")
run("git","add",readmef)
run("git","add",pendingf)
run("git","add","README.md")
run("git","commit","-m","Add tutorial: "+title)
run("git","push","origin","master")

print(readmef)
