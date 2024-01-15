def main():
    print("This is standard output (stdout).")

    try:
        result = 10 / 0
        print(f"Result: {result}")
    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)

if __name__ == "__main__":
    main()
