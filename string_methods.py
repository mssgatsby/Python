# capitalize
str1 = "hello WORLD"
capStr = str1.capitalize()
print(capStr)  # Result: Hello world
# In Python string methods don't change original string, becuz they are immutable.

# casefold vs lower
str2 = "Hello World"
casStr = str2.casefold()
lowStr = str2.lower()
print(casStr)  # hello world
print(lowStr)  # hello world
# lower only converts ASCII based characters. casefold converts other (German based or other language unique characters)
# types to lowercase as well. Lower works faster

#center
str3 = "Hello"
cenStr = str3.center(20, "_")
print(cenStr)  # _______Hello________

#count
str4 = "I love apples, apple are my favorite fruit"
couStr = str4.count("apple", 10, 24)
print(couStr) # 1

#endswith
str5 = "Hello, welcome to my world."
endStr = str5.endswith("my world.", 5, 11)
print(endStr)  # True, False

#find
txt = "Hello, welcome to my world."
x = txt.find("e", 5, 10)
print(x)