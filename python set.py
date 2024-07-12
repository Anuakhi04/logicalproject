# A python set is  the collection of the unordered items.
#Each element in the set must be unique, immutable, and the sets remove the duplicate elements.sets are mutable
#which means we can modify it after its creation.

days = {"january","February","march","April","May","June"}
print(days)
print(type(days))
for i in days:
    print(i)

#using set() method
days =set({"january","February","march","April","May","June"})
print(days)
print(type(days))
print("looping through the set elements . . .")

#the add() method is used to add a single element whereas the update() method is used to add multiple elements
#to the set add() method
months = {"january","February","march","April","May","June"}
print(months)
months.add("july")
months.add("august")
print(months)
for i in months:
    print(i)

# update() function
months = {"january","February","march","April","May","June"}
print(months)
months.update(["july","august","september","october"])
print(months)

#the difference between these function,using discard() function
#if the item does not exist in the set then the set remain unchanged whreas remove() method will through an error
#discard() method
months = {"january","February","march","April","May","June"}
print(months)
months.discard("january")
months.discard("may")
print(months)

#remove() function
months = {"january","February","march","April","May","June"}
print(months)
months.remove("january")
months.remove("May")
print(months)

#the pop() method will always remove the last item but the set is unordered,
#we can't determine which element will be popped from set.
months = {"january","february","march","april","may","june"}
print(months)
months.pop()
months.pop()
print(months)

months = {"january","february","march","april","may","june"}
print(months)
months.clear()
print(months)

#set operstions
#union | operator

days1 = {"monday","tuesday","wednesday","thursday","sunday"}
days2 = {"friday","saturday","sunday"}
print(days1 | days2)

days1 = {"monday","tuesday","wednesday","thursday"}
days2 = {"friday","saturday","sunday"}
print(days1.union(days2))

#intersection() function
days1 = {"monday","tuesday","wednesday","thursday"}
days2 = {"monday","tuesday","sunday","friday"}
print(days1&days2)

set1 = {"devansh","john","david","martin"}
set2 = {"Steve","Milan","david","Martin"}
print(set1.intersection(set2))

#using substraction (-) operator
days1 = {"Monday","Tuesday","Wednesday","Thursday"}
days2 = {"Monday","Tuesday","Sunday"}
print(days1-days2)

#using difference() method
days1 = {"Monday","Tuesday","Wednesday","Thursday"}
days2 = {"Monday","Tuesday","Sunday"}
print(days1.difference(days2))