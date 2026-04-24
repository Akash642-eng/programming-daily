import shutil
import os

src = "code"
dst = "backup_code"

try:
    shutil.copytree(src, dst)
except:
    print("already exists or error")

print("backup done")