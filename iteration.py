x = iter(["apple", "banana", "cherry", "orange"])
print(next(x))
print(next(x))
print(next(x))
print(next(x))

mylist = iter(["apple", "banana", "cherry"])
x = next(mylist, "orange")
print(x)
x = next(mylist, "orange")
print(x)
x = next(mylist, "orange")
print(x)

