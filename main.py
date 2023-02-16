import sys

def main() -> bool:
    return True

if __name__ == "__main__":
    r = main()
    if not r:
        sys.exit(1)
    sys.exit(0)
