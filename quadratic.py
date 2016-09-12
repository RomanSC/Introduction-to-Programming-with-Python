def main():
    print("This program finds the real solutions to a quadratic:")
    print()

    import math

    a, b, c = input("Please enter the coefficients (a, b, c,): ")

    discRoot = math.sqrt(b * b - 4 * a * c)
    root1 = (-b + discRoot) / (2 * a)
    root2 = (-b - discRoot) / (2 * a)
    print()

    print("The solutions are:", root1, root2)

main()
