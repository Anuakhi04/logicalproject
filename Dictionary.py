# Employee = {"Name": "Johny", "Age" :32, "Salary": 26000, "Company": "^TCS"}
# print(type(Employee))
# print(Employee)
#
# #creating an empty dictionary
# Dict = {}
# print("Empty Dictionary :")
# print(Dict)
#
# Employee = {"Name": "Dev", "Age": 20, "Salary": 45000, "Company": "Wipro"}
# print(type(Employee))
# print(Employee["Name"])
#
# #creating an empty Dictionary
# dict = {}
# #Adding elements to dictionary one at a time
# dict[0] = 'peter'
# dict[2] = 'joseph'
# dict[3] = 'ricky'
# print(dict)
#
#
# employee ={"Name": "Dev", "Age": 20, "Salary": 45000, "Company": "Wipro"}
# employee["Name"] = input("Name: ")
# print(employee)
#
# employee ={"Name": "David", "Age": 30, "Salary": 55000, "Company": "Wipro"}
# del employee["Name"]
# print(employee)
# del employee
# # print(employee)
#
# #creating a dictionary
# Dict1 = {1: 'javaTpoint', 2: 'Educational', 3: 'Website'}
# pop_key = Dict1.pop(2)
# print(Dict1)
#
# #for loop to print all the key of a dictionary
# employee ={"Name": "John", "Age": 29, "Salary": 25000, "Company": "Wipro"}
# for x in employee:
#     print(x)
#
# #for loop to print all the keys of a dictionary
# employee ={"Name": "John", "Age": 29, "Salary": 25000, "Company": "Wipro"}
# for x in employee:
#     print(employee[x])
#
# #for loop to print the values of the dictionary by using values() method.
# employee ={"Name": "John", "Age": 29, "Salary": 25000, "Company": "Wipro"}
# for x in employee.values():
#     print(x)
#
# #for loop to print the items of the dictionary by using items() method
# employee ={"Name": "John", "Age": 29, "Salary": 25000, "Company": "WIPRO"}
# for x in employee.items():
#     print(x)
#
# employee ={"Name": "John", "Age": 29, "Salary": 25000, "Company": "Wipro"}
# for x,y, in employee.items():
#     print(x,y)
#
# dict = {1: "Ayan", 2: "Bunny", 3: "Ram", 4: "Bheem"}
# print(len(dict))
#
# dict = {1: "HCL", 2: "WIPRO", 3: "Facebook", 4: "Flipkart"}
# #values() method
# print(dict.values())
#
# dict = {1: "HCL", 2: "WIPRO", 3: "Facebook", 4: "Flipkart"}
# dict.update({3: "TCS"})
# print(dict)
#
# dict = {1: "HCL", 2: "WIPRO", 3: "Facebook", 4: "Flipkart"}
# #get () method
# print(dict.get(3))
#
# dict = {1: "HCL", 2: "WIPRO", 3: "Facebook", 4: "Flipkart"}
# #items()method
# print(dict.items())
#
# dict = {1: "HCL", 2: "WIPRO", 3: "Facebook", 4: "Flipkart"}
# #key() method
# print(dict.keys())
#
# dict = {1: "HCL", 2: "WIPRO", 3: "Facebook", 4: "Flipkart"}
# #copy() method
# dict_demo = dict.copy()
# print(dict_demo)
#
# dict = {1: "HCL", 2: "WIPRO", 3: "Facebook", 4: "Flipkart"}
# #clear () method
# dict.clear()
# print(dict)

#using the dict() method to make a dictionary:
x = dict(name = "john", age = 36, country = "norway")
print(x)

#nested dictionaries
myfamily = {
    "child1" : {
    "name" :"Emil",
        "year" : 2004
    },
    "child2" : {
        "name" :"Tobias",
    "year" : 2007
},
"child3" : {
    "name" : "Linus",
    "year" : 2011
}
}
print(myfamily)