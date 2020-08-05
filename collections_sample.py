import collections
def main():
    #creating a list
    my_list = [1, "Hello", 3.4]
    print(my_list)
    #indexing schemes
    n_list = ["hello", [2, 0, 1, 5]]
        # Nested indexing
    print(n_list[0][1])
        #negative indexing
    my_list = ['p', 'r', 'o', 'b', 'e']
    print(my_list[-1])
    print(my_list[-5])
        #slicing
    print(my_list[2:5])
    print(my_list[:-2])

    #Mutating list
    odd = [2, 4, 6, 8]
        #changing a single value
    odd[0] = 1
    print(odd)
        #change a range of values
    odd[1:4] = [3, 5, 7]
    print(odd)
        #using append and extend
    # Appending and Extending lists in Python
    odd = [1, 3, 5]
    odd.append(7)
    print(odd)
    odd.extend([9, 11, 13])
    print(odd)
        #deleting, removing, pop
    my_list = ['p', 'r', 'o', 'b', 'l', 'e', 'm']
    # delete one item
    del my_list[2]
    print(my_list)
    # delete multiple items
    del my_list[1:5]
    print(my_list)
    # delete entire list
    del my_list
    my_list = ['p', 'r', 'o', 'b', 'l', 'e', 'm']
    my_list.remove('p')
    print(my_list)
    print(my_list.pop(1))
    print(my_list)
    print(my_list.pop())
    print(my_list)
    my_list.clear()
    print(my_list)

    #sets
    my_set = {1, 2, 3}
    print(my_set)
    my_set = {1.0, "Hello", (1, 2, 3)}
    print(my_set)
        #Mutating sets
    my_set = {1, 3}
    print(my_set)
    my_set.add(2)
    print(my_set)
    my_set.update([2, 3, 4])
    print(my_set)
    my_set.update([4, 5], {1, 6, 8})
    print(my_set)
    my_set = {1, 3, 4, 5, 6}
    print(my_set)
    my_set.discard(4)
    print(my_set)
    my_set.remove(6)
    print(my_set)
    my_set.discard(2)
    print(my_set)

    #set operations
    # Set union method
    A = {1, 2, 3, 4, 5}
    B = {4, 5, 6, 7, 8}
    print(A | B)
    print(A.union(B))
    # Intersection of sets
    A = {1, 2, 3, 4, 5}
    B = {4, 5, 6, 7, 8}
    print(A & B)
    print(A.intersection(B))
    # Difference of two sets
    A = {1, 2, 3, 4, 5}
    B = {4, 5, 6, 7, 8}
    print(A - B)
    print(A.difference(B))
    # Symmetric difference of two sets
    A = {1, 2, 3, 4, 5}
    B = {4, 5, 6, 7, 8}
    print(A ^ B)
    print(A.symmetric_difference(B))

    #dictionary
    #creating dictionary
    # empty dictionary
    my_dict = {}
    # dictionary with integer keys
    my_dict = {1: 'apple', 2: 'ball'}
    # dictionary with mixed keys
    my_dict = {'name': 'John', 1: [2, 4, 3]}
    # using dict()
    my_dict = dict({1: 'apple', 2: 'ball'})
    # from sequence having each item as a pair
    my_dict = dict([(1, 'apple'), (2, 'ball')])
    #Accessing elements
    my_dict = {'name': 'Jack', 'age': 26}
    print(my_dict['name'])
    print(my_dict.get('age'))
    #mutating dictionary
    my_dict = {'name': 'Jack', 'age': 26}
    # update value
    my_dict['age'] = 27
    print(my_dict)
    # add item
    my_dict['address'] = 'Downtown'
    print(my_dict)
    #removing from dictionary
    # Removing elements from a dictionary
    # create a dictionary
    squares = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
    # remove a particular item, returns its value
    print(squares.pop(4))
    print(squares)
    print(squares.popitem())
    print(squares)
    squares.clear()
    print(squares)
    del squares

    #list to sets
    listOfStudents = ['Mohan', 'John', 'Ramesh', 'Mohan', 'John']
    print("List of Students:", listOfStudents)
    uniqueNames = set(listOfStudents)
    print("Set of uniqueNames:", uniqueNames)

    #sets to list
    my_set = {'ram', 'sham', 'rahul'}
    s = list(my_set)
    print(s)

    #namedtuples
    # Declaring namedtuple()
    Student = collections.namedtuple('Student', ['name', 'age', 'DOB'])

    # Adding values
    S = Student('Rahul', '24', '06061995')

    # Access using index
    print("The Student age using index is : ", end="")
    print(S[1])

    # Access using name
    print("The Student name using keyname is : ", end="")
    print(S.name)

    # Access using getattr()
    print("The Student DOB using getattr() is : ", end="")
    print(getattr(S, 'DOB'))
    

if __name__ == '__main__':
    main()
