import time

start = int(input("How many seconds?: "))

for seconds in range(start,0,-1):
    print(seconds)
    time.sleep(1)
print(f"You did it in {start} secs, well done!")
