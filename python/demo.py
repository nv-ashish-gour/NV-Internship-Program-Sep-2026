##Write basic python code and build logical thinking skills.


# Q. Write a program and continuously ask the user to enter different names, 
# until the user presses Enter (without supplying a name). 
# Depending on the number of names provided, display a message based on the above pattern.

# name=[]

# while True:
#     n = input("enter the name")
#     if n == "":
#         break

#     name.append(n)
# print(len(name))


# 1 - Write a program and ask the user to enter a few numbers separated by a hyphen.
# Work out if the numbers are consecutive. 
# For example, if the input is "5-6-7-8-9" or "20-19-18-17-16", display a message: "Consecutive"; otherwise, display "Not Consecutive".


value = input("Enter numbers separated hyphen: ")

numbers = value.split('-') #split " -" hyphen ke basis par string ko todta hai.

numbers = [int(x) for x in value] #so the value is converted into integer in list ex[1,2,3,4,5]

diff = numbers[1] - numbers[0] #here hame difference nikala hai ki consecutive hai ya nahi

if numbers [i + 1] - numbers[i] != diff: #agar difference same nahi hai to consecutive nahi hai
    print("Not Consecutive")
    
else:
    print("Consecutive")
    
    
    # 
# values = input("Enter numbers separated by hyphen: ")

# numbers = values.split("-")

# numbers = [int(x) for x in numbers]

# difference = numbers[1] - numbers[0]

# is_consecutive = True

# for i in range(len(numbers) - 1):
#     if numbers[i + 1] - numbers[i] != difference:
#         is_consecutive = False
#         break

# if is_consecutive:
#     print("Consecutive")
# else:
#     print("Not Consecutive")