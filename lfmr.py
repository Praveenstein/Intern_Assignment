from functools import reduce
def main():
    #lambda function to find the square of a number
    square=lambda x: x**2
    print(square(5))
    #filter function to remove odd values in a list
    lis=[1,2,3,4,5,6,7,8,9,10]
    new_lis=list(filter(lambda x: x%2 == 0, lis))
    print(new_lis)
    #use of map function to find square of given list
    lis = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    new_lis = list(map(lambda x: x**2, lis))
    print(new_lis)

    #reduce function to find the sum of number
    lis = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    add=(reduce(lambda a,b: a+b, lis))
    print("Sum using Reduce Function: ", add)

if __name__ == '__main__':
    main()
