#1. Create a two-string variable, concatenate the two variables and print out the result.

food = "Egg"
color = "White"
concatenate = food+color
print (concatenate)


#2. Create a function that calculates the power of a number. Then write a unit test to check the correctness of the function.

Number = int(input("Enter a valid number: "))
power = int(input("Enter a valid number: "))
print (Number ** power)


#3. Using the OOP feature Inheritance, create a class Animal with the method sound() and then create a Cat and Dog class that inherits from the Animal class.The Cat and Dog class should override the sound class and print a different sound.


class Animal(): 
  def sound ():
    print ("Animal sound")
  
class Cat(Animal):
  def sound ():
    print ("Cat noise")
  
class Dog(Animal):
  def sound ():
    print ("Dog sound")

Cat.sound()
Dog.sound()


#4. Writing a well-documented code, create a function that calculates simple interest.
#SI = PTR/100
#Where P = Principal, T = Time(in years), R = Rate(in percentage)

Principal = float(input("Enter your Principal: "))
Time= float(input("Enter the no. of years: "))
Rate= float(input("Enter the rate: "))

Simple_interest = Principal * Time * (Rate / 100)
print (float(Simple_interest))


#5. Write a Python program that checks if a string is a palindrome; optionally, write a unit test to check your program's correctness

def isPalindrome(Palindrome):
    input = Palindrome.lower().replace(" ","")
    return input == input[::-1]

Palindrome = input("Enter a valid Palindrome: ")
answer = isPalindrome(Palindrome)

if answer:
    print("Yes")
else:
    print("No")


#6. Write a function that removes repeated characters from a string. Sample strings are
#Hello: output should be Hello
#Concatenate: output should be Conaten
input_1 = "Hello"
input_lower= input_1.lower()
dup1=""
for char in input_lower:
    if char not in dup1:
        dup1=dup1+char
print(dup1)

input_2 = "Concatenate"
input_lower2= input_2.lower()
dup2=""
for char in input_lower2:
    if char not in dup2:
        dup2=dup2+char
print(dup2)


#7. Create a program that prints out the odd numbers in an array.
A = [1, 2, 3, 4, 5, 6]

A2 = []

for char in A:
    if char % 2 == 1:
        A2.append(char)
print (A2)
      

B = [ 34, 2, 9, 91, 19, 401, 0 ]

B2 = []

for char in B:
    if char % 2 == 1:
        B2.append(char)
print (B2)

#8. Create a program that prints out the even numbers in an array.
A = [1, 2, 3, 4, 5, 6]

A2 = []

for char in A:
    if char % 2 == 0:
        A2.append(char)
print (A2)
      

B = [ 34, 2, 9, 91, 19, 401, 0 ]

B2 = []

for char in B:
    if char % 2 == 0:
        B2.append(char)
print (B2)


#9. Create a function that converts any string value to upper case. Then write a unit test that checks the function's correctness.

Sample = "this is a string"
SampleUpper= Sample.upper()
print (SampleUpper)

#10. Create a function that converts any string value to a Sentence case, then write a unit test that checks the function's correctness.


def proper(Sample): 
	words=Sample.split(". ") 
	new=". ".join([word.capitalize() for word in words])  
  
	words=new.split("! ") 
	new="! ".join([word.split()[0][0].upper()+word[1:] for word in words])
  
	words=new.split("? ") 
	new="? ".join([word.split()[0][0].upper()+word[1:] for word in words])
  
	return new 
Sample = "THIS IS A STRING. THIS ALSO. WHILE THIS IS NOT. EUREKA! DO YOU NOW KNOW WHAT A STRING IS? OFCOURSE YOU DO"
#n=proper(Sample)
print (proper(Sample))
#Sample = Sample.capitalize()
#print (Sample)