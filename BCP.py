def main():
    # basic use of break and else statements
    var='Python'
    for v in var:
        if v=='o':
            print('\n')
            break
        print(v,end='')
    else:
        print("\n The break statements was not executed")

    var='Scala'
    for v in var:
        if v=='o':
            break
        print(v,end='')
    else:
        print("\nThe break statements was not executed\n")

    #basic use of continue statement to skip the current itertion
    var = 'Python'
    for v in var:
        if v == 'o':
            continue
        print(v, end='')

    #use of pass statements as a placeholder for future codes
    for i in range(100):
        pass

if __name__ == '__main__':
    main()
