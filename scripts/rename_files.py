import os

files = os.listdir()

for i, f in enumerate(files):
    new = f"file_{i}.txt"
    try:
        os.rename(f, new)
    except:
        pass

print("done")

.................

unintended sometimes