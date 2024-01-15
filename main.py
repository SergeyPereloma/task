import sys
import time

def main():
    print("Starting the count...")

    for i in range(1, 11):
        print(f"Count: {i}")
        time.sleep(3)

    try:
        result = 10 / 0
        print(f"Result: {result}")
    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)

if __name__ == "__main__":
    main()
