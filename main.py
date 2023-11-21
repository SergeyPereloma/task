import sys

def main():
    print("This is standard output (stdout).")

    # Intentionally create an error to produce stderr output
    try:
        # Example error: division by zero
        result = 10 / 0
        print(f"Result: {result}")
    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)

if __name__ == "__main__":
    main()
