def main():
    # basic use of for statements
    num=[1,2,3,4,5,6]
    sum=0
    for value in num:
        sum+=value
    print("The sum of number is: ", sum)

    #using range in for loops
    sum=0
    for value in range(1,20,2):
        sum+=value
    print("The sum of number is: ", sum)

    #use of enumerate
    x=['chennai','mumbai','delhi','kolkata']
    for i in enumerate(x,10):
        print(i)

    #list comprehension to find the transpose of a matrix
    matrix=[[1,2],[3,4],[5,6]]
    tm=[[row[i] for row in matrix] for i in len(matrix[0])]
    print(tm)

if __name__ == '__main__':
    main()
