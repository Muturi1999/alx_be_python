#!/usr/bin/env python3

import sys
from robust_division_calculator import safe_divide

def main():
    """
    Main function to handle command-line interaction for division calculation.
    """
    if len(sys.argv) != 3:
        print("Usage: ./main.py <numerator> <denominator>")
        sys.exit(1)

    numerator = sys.argv[1]
    denominator = sys.argv[2]

    result = safe_divide(numerator, denominator)
    print(result)

if __name__ == "__main__":
    main()
