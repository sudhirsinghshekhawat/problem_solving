import time

with open("t1.txt") as file_r:
    while True:
        line = file_r.readline()
        if not line:
            time.sleep(1)
        else:
            print(line)
