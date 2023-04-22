a, b, c = 1, 2, 3


def execute():
    return 1234


array = ["hello", 10, 2.4, -9, execute()]

print(array[4])


d = (4, 5, 6)
# d[0] = 3    #imutable
print(d[0])


dictionary = {"apple": 3, "bee": 6}
print(type(dictionary))
print(dictionary["bee"])
print("apple" in dictionary)
print("applee" in dictionary)
print(len(dictionary))

dic = {}
print(dic)


def abc():
    return "abc"


print(abc())


def abcd(x):
    return x


print(abcd("a"), abcd(1))


for i in range(5):
    print(i)

array = ["hello", 10, 2.4, -9, execute()]
for i in array:
    print(i)

for key, value in dictionary.items():
    print(key, value)

print("#################################")
for index, value in enumerate(dictionary):
    print(index, value)

print("#################################")

a = 1
if a:
    print(bool(a))

b = 0
if b:
    print
else:
    print(bool(b))


a, b = 1, 1
if a and b:
    print(a, b)

a, b = 1, 1

print("#################################")


print("#################################")
print("#################################")
print("#################################")
print("#################################")
print("#################################")
