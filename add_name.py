print("hello")
mylist_1 = []
mylist_2 = ["hassan","ali"]
mylist_1.append(mylist_2)
first = input("Enter a first name: ")
last = input("Enter a last name: ")
search_the_name=input("Enter a name to search for: ")
if search_the_name in mylist_1:
    print("The name is in the list")
else:
    print("The name is not in the list")