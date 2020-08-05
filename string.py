def main():
    #basics of string
    st ='hello'
    print(st[0])
    print(st[0:3])
    str1='hello'
    str2='world'
    print(str1+' '+ str2)
    print(str2 * 3)

    #string membership testing
    if 'o' in str1:
        print("Yes")
    if 'o' not in str2:
        print("Yes")

    #string formatting
    print(f'{st} was created first, then {str1} and then {str2}')
    #escape sequence
    print("Spark was developed in, \"UC-Berkely\"")
    #using raw statements to ignore escape statements
    print(r"Spark was developed in, \"UC-Berkely\"")

    #string methods
    print('python'.upper())
    print("This will split all words into a list".split())
    print(' '.join(['This', 'will', 'join', 'all', 'words', 'into', 'a', 'string']))
    print('spark is 100 times faster than map reduce'.find('map'))
    print('spark is 100 times faster than map reduce'.replace('map', 'google maps'))

if __name__ == '__main__':
    main()
