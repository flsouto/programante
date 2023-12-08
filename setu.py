import base64
import os

arr = open('users').read()
arr = base64.b64decode(arr.encode('ascii')).decode('ascii').split()
u = arr.pop()
print("picked %s" % u)
arr = "\n".join(arr)

open('users','w').write(
    base64.b64encode(arr.encode('ascii')).decode('ascii')
)

os.system("./set-user.sh "+u)

