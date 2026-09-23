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


""" 1 - Write a program and ask the user to enter a few numbers separated by a hyphen.
# Work out if the numbers are consecutive. 
# For example, if the input is "5-6-7-8-9" or "20-19-18-17-16", display a message: "Consecutive"; otherwise, display "Not Consecutive"."""


# value = input("Enter numbers separated hyphen: ")

# numbers = value.split('-') #split " -" hyphen ke basis par string ko todta hai.

# numbers = [int(x) for x in value] #so the value is converted into integer in list ex[1,2,3,4,5]

# diff = numbers[1] - numbers[0] #here hame difference nikala hai ki consecutive hai ya nahi

# if numbers [i + 1] - numbers[i] != diff: #agar difference same nahi hai to consecutive nahi hai
#     print("Not Consecutive")
    
# else:
#     print("Consecutive")
    
    
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



""" 2 - Write a program to create a room class, the attributes of this class is roomno, roomtype, roomarea and ACmachine. 
In this class the member functions are setdata and displaydata."""

# class Room:
#     def __init__(self,roomno, roomtype, roomarea, ACmachine):
#         self.roomno = roomno
#         self.roomtype = roomtype
#         self.roomarea = roomarea
#         self.ACmachine = ACmachine
        
#     def setdata(self):
#         self.roomno = input("Enter room number: ")
#         self.roomtype = input("Enter room type: ")
#         self.roomarea = input("Enter room area: ")
#         self.ACmachine = input("Is there an AC machine? (yes/no): ")
        
#     def displaydata(self):
#         print("Room Number:", self.roomno)
#         print("Room Type:", self.roomtype)
#         print("Room Area:", self.roomarea)
#         print("AC Machine:", self.ACmachine)
        
# r1 = Room( )
# r1.setdata()
# r1.displaydata()



"""3 - Write a program create a class ‘simpleobject‘. Using constructor display the message."""
# class SimpleObject:
    
#     def __init__(self):
#         print("This is a simple object created using a constructor.")
        
# obj = SimpleObject()
# print(obj)

"""4 - Write a program to give the example for method overriding concepts."""
# Overriding means: Child class parent class ke existing method ko same name se dobara define karti hai, but apna different behavior deti hai.

# class Animal:
#     def sound(self):
#         print("Animal make a sound")
    
# class Dog(Animal):
#     def sound(self):
#         print("Dog barks")
        
# a1 = Animal()
# a1.sound()

# a2 = Dog()
# a2.sound()

"""5 - Write a program to create a class named shape. In this class we have three sub classes circle, 
triangle and square each class has two member function named draw () and erase ().
Create these using polymorphism concepts"""

# class Shape:
#     def draw(self):
#         print("Drawing a shape")

#     def erase(self):
#         print("Erasing a shape")


# class Circle(Shape):
#     def draw(self):
#         print("Drawing a circle")

#     def erase(self):
#         print("Erasing a circle")


# class Triangle(Shape):
#     def draw(self):
#         print("Drawing a triangle")

#     def erase(self):
#         print("Erasing a triangle")


# class Square(Shape):
#     def draw(self):
#         print("Drawing a square")

#     def erase(self):
#         print("Erasing a square")


# c = Circle()   #Circle → class,  c → object,  Circle() → Circle class ka object create karta hai
# t = Triangle()
# s = Square()


# a1 = Shape()
# a1.draw(),a1.erase()

# a2=Circle()
# a2.draw(), a2.erase()

# a3=Triangle()
# a3.draw(), a3.erase()

#a4=Square()
# a4.draw(), a4.erase()

"""6 Write a program to give a simple example for abstract class."""



"""7 - Write a program to create interface A in this interface we have two method meth1 and meth2. 
Implements this interface in another class named MyClass."""

