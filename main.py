"""Entry point for the simple calculator demo."""

from calculator import Calculator


def main():
    """Demonstrate all four calculator operations across multiple input pairs."""
    calc = Calculator()
    pairs = [(10, 3), (7, 2), (0, 5)]

    print("Simple Calculator Demo")
    print("=" * 30)

    for a, b in pairs:
        print(f"\n  a={a}, b={b}")
        print(f"    add      : {calc.add(a, b)}")
        print(f"    subtract : {calc.subtract(a, b)}")
        print(f"    multiply : {calc.multiply(a, b)}")
        if b != 0:
            print(f"    divide   : {calc.divide(a, b):.4f}")


if __name__ == "__main__":
    main()
