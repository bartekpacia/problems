
import time


def main():
    for i in range(0, 1_000_000):
        pass


start_time = time.time()
main()
duration = round((time.time() - start_time) * 1000, 2)
print(f"Program execution took {duration} miliseconds")
