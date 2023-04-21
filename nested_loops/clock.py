import time

# hours = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
# minutes = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

for h in range(0, 24):
    for m in range(0, 60):
        for s in range(0, 60):
            print(f"{h:02d}:{m:02d}:{s:02d}")
            time.sleep(1)
