mylist = ["sufyan","hammad","jazib"]
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
mylist.append(first_name)
mylist.append(last_name)
search_for_name=input("plz search the name: ")
if first_name in mylist:
    print("The name is in the list")
else:
    print("The name is not in the list")