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
# g