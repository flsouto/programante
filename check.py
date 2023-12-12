from glob import glob
from sys import argv
from subprocess import check_output

def run(*args):
    print(check_output(args))

pending = glob("*/pending")

if len(argv) < 2:

    for i,f in enumerate(pending):
        print("{} - {}".format(i, f))
else:
    run(["rm",pending[i]])
    run(["git","add",pending[i]])
    run(["git","commit", "--author", "flsouto <flsouto666@gmail.com>", "-m", "resolve"])

    i = int(argv[1])
    url = "https://github.com/flsouto/programante/tree/master/"
    url+= pending[i].split("/")[0]
    print(url)
