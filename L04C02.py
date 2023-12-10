import os.path

count = 1
flag = ""

while os.path.isfile(f"/tmp/agent-{count}.txt"):
    fname = f"/tmp/agent-{count}.txt"
    with open(fname, 'r') as content_file:
        content = content_file.read()
        flag += content.rstrip()
    count += 1

print(flag)
