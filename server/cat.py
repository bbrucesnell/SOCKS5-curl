import time
time.sleep(5)
with open('payload.txt') as f:
    lines = f.readlines()
for line in lines:
    l = line.strip()
    if not l:
        continue
    print(l)
    time.sleep(1)
print()
print()
