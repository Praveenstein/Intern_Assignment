#simple functions to find the sum of given numbers
def add(*args):
    sum=0
    for num in args:
        sum+=num
    return sum
sum=add(1,2,3,4,5)
print(sum)
sum=add(5,6,8)
print(sum)

#simple function to use variable length keyword arguments
def data(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} is {value}")
data(name="Praveen", Age= 25)
data(First_Name="Rahul", Last_Name='Rocky', Age= 24)

#understanding scope of variables in functions
z='Global'
def outer():
    k='Local'
    def inner():
        l='Inner Local'
        nonlocal k
        global z
        z=z*2
        k='Nonlocal K'
        print('Value of l inside inner: ',l)
    print('K before calling inner: ', k)
    print('Z before calling inner: ', z)
    inner()
    print('K After calling inner: ', k)
    print('Z after calling inner: ', z)
outer()

#higher order functions- Functions as objects
    #accepting functions as arguments
def square(n):
    return n*n
def map_fun(func,arr):
    result=[]
    for i in arr:
        result.append(func(i))
    return result

result= map_fun(square, [1,2,3,4,5,6])
print(result)

    #returning function from a function
def html_tag(tag):
    def wrap_text(msg):
        print(f'<{tag}> {msg} </{tag}>')
    return wrap_text
print_h1=html_tag('h1')
print_h1('This is a heading tag')
print_p=html_tag('p')
print_p("This is a paragraph tag")

