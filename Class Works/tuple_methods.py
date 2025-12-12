# t = ()
# t = tuple()
# t = (1, 2, 3)
# print(t)
# t = (1, "hello", 3.4, True)
# print(t)
# t = ((1, 2, 3, 4), (5, 6, 7, 8))
# print(t)

# t = (1, 2, 3, 4, 5)
# s = (6, 7, 8, 9, 10)

# print(t + s)
# print(t * 3)
# print(len(t))
# print(4 in t)

# languages = ("Python", "Java", "C++", "JavaScript", "Ruby")

# print(languages[:3])
# print(languages[-3:])
# print(languages[3:5])
# print(languages[::2])
# print(languages.index("JavaScript"))
# print(languages.count("JavaScript"))
# print(languages.index("JavaScript", 2))


a = 1, 2, 3, 4, 5 # Stores as Tuple
print(a)

a, b, c, d, e = 1, 2, 3, 4, 5 # Unpacking
print(a)

dict = {"name": "Alice", "age": 25, "city": "New York"}
name, age, city = dict.values()
print(name, age, city)

t = (1, 2, 3, 4, 5, 6, 7, 8, 9, [10, 11, 12])
t[9].append(13)
print(t)

t = {1: "a", 2: "b", 3: "c"}
t = tuple(t.items())
print(t)