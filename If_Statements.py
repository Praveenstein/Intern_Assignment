def if_else():
    # basic use of if statement
    num = 3
    if num > 0:
        print("Number is positive")
    else:
        print("Number is negative")

    # use of elif statements
    num = 0
    if num > 0:
        print("Number is positive")
    elif num < 0:
        print("Number is negative")
    else:
        print('Number is Zero')

    # Same example using nested if statements
    num = -6
    if num >= 0:
        if num == 0:
            print('Number is zero')
        else:
            print("Number is positive")
    else:
        print("Number is negative")


if __name__ == '__main__':
    if_else()
