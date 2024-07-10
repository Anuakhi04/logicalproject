# # tuples are an immutable data type, meaning their elements cannot be changed after they are generated
# # each element in a tuple has a specific order that will never change because tuples are ordered sequences
#
# # creating an empty tuple
# empty_tuple = ()
# print("empty tuple:", empty_tuple)
#
# # creating tuple having integers
# int_tuple = (4, 6, 8, 10, 12, 14)
# print("Tuple with integers:", int_tuple)
#
# # creating a tuple having objects of different data types
# mixed_tuple = (4, "python", 9.3)
# print("tuple with different data types:", mixed_tuple)
#
# # creating a nested tuple
# nested_tuple = ("python", {4: 5, 6: 2, 8: 2}, (5, 3, 5, 6))
# print("A nested tuple:", nested_tuple)
#
# # checking the data types of object tuple_
# int_tuples = (4, 6, 8, 10, 12, 14)
# print(type(int_tuples))
#
# tuple_ = ("python", "Tuple", "Ordered", "Collection")
# print(tuple_[0])
# print(tuple_[1])
#
# nested_tuple = ("Tuple", [4, 6, 2, 6], (6, 2, 6, 7))
# # Accessing the index of a nested tuple
# print(nested_tuple[0][3])
# print(nested_tuple[1][1])
#
# tuple_ = ("Python", "Tuple", "Ordered", "Collection")
# # printing elements using negative indices
# print("Elements at -1 index:", tuple_[-1])
# print("Elements between -4 and -1 are:", tuple_[-4:-1])
#
# tuple_ = ("Python", "Tuples", "Ordered", "Immutable", "Collection", "Objects")
# # using slicing to access elements of the tuple
# print(tuple_[1:3])
# # using negative indexing in slicing
# print(tuple_[:4])
# # printing the entire tuple by using the default start and end values
# print(tuple_[:])
#
# tuple_ = ("python", "Tuples", "Ordered", "Immutable", "Collection", "Objects")
# # Deleting the varable from the global space of the program
# del tuple_
# print(tuple_)
#
# tuple_ = ('python', "Tuples")
# # Repeating the tuple elements
# tuple_ = tuple_ * 3
# print("New tuple is:", tuple_)
#
# T1 = (0, 1, 5, 6, 7, 2, 2, 4, 2, 3, 2, 3, 1, 3, 2)
# res = T1.count(2)
# print('count of 2 in T1 is:', res)
#
# t = ("python", "tuples", "ordered", "Immutable", "collection", "Ordered")
# # in operator
# print('Tuple' in t)
# # Not in operator
# print('Immutable' not in t)
#
# tuple = ("Python", "Tuple", "Ordered", "Immutable")
# # Iterating over tuple elements using a for loop for item in tuple:
# for i in tuple:
#     print(i)
#
# # The tuple() constructor
# # it is also possible to use the tuple() constructor to make a tuple
# thistuple = tuple(("apple", "banana", "cherry"))
# # Note the double round-brackets
# print(thistuple)
#
# # convert the tuple into a list to be able to change it:
# x = ("apple", "banana", "cherry")
# y = list(x)
# y[1] = "kiwi"
# x = tuple(y)
# print(x)
#
# thistuple = ("apple", "banana", "cherry")
# y = list(thistuple)
# y.append("orange")
# thistuple = tuple(y)
#
# thistuple = ("apple", "banana", "cherry")
# y = list(thistuple)
# y.remove("apple")
# thistuple = tuple(y)
#
# tuple1 = ("a", "b", "c")
# tuple2 = (1, 2, 3)
# tuple3 = tuple1 + tuple2
# print(tuple3)

x = ("hello",)
print(type(x))
