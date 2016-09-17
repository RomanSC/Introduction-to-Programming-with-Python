def main():
    # total is 0, or "empty" for use in the expression
    total = 0

    # this is a for loop that runs 10 times
    for i in range(10):
        # "total +=" is the same as "total = total"
        # so total equals itself
        # i to the third power 10 times?
        total += i ** 3

    print(total)

main()
