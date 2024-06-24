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
print(couStr)  # 1

#endswith
str5 = "Hello, welcome to my world."
endStr = str5.endswith("my world.", 5, 11)
print(endStr)  # True, False

#find vs index
str6 = "Hello, welcome to my world."
findStr = str6.find("e", 5, 10)
indStr = str6.index("e", 2, 17)
print(findStr)  # return -1 if there is not
print(indStr)  # return ValueError if there is not

#format
txt1 = "My name is {fname}, I'm {age}".format(fname="John", age=36)
txt2 = "My name is {0}, I'm {1}".format("John", 36)
txt3 = "My name is {}, I'm {}".format("John", 36)

#isidentifier
str7 = "Demo1_2"
isidStr = str7.isidentifier()
print(isidStr)

# isdigit(): Recognizes only decimal digits (0-9).
# isnumeric(): Recognizes a broader range of numeric characters including decimal digits, Unicode numeric characters, fractions, subscripts, superscripts, etc.

# there is join method, returns added tuples
str9 = ("John", "Peter", "Vicky")
joinstr = "#".join(str9)
print(joinstr)
# if dict, they join only keys, not values