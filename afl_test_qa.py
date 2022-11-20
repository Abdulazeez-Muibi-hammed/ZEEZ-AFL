#1. Create a two-string variable, concatenate the two variables and print out the result.

food = "Egg"
color = "White"
concatenate = food+color
print (concatenate)


#2. Create a function that calculates the power of a number. Then write a unit test to check the correctness of the function.
def power (x, y):
    
    return x ** y


#3. Using the OOP feature Inheritance, create a class Animal with the method sound() and then create a Cat and Dog class that inherits from the Animal class.The Cat and Dog class should override the sound class and print a different sound.
class Animal(): 
  def sound (self):
    print ("Animal sound")
  
class Cat(Animal):
  def sound ():
    print ("Meow")
  
class Dog(Animal):
  def sound ():
    print ("Woof")

Cat.sound()
Dog.sound()


#4. Writing a well-documented code, create a function that calculates simple interest.
#simple_interest = PTR/100
#Where P = Principal, T = Time(in years), R = Rate(in percentage)

def simple_interest (Principal, Time, Rate):
    """
        This simple interest function helps calculate the amount of interest that would be paid on a particular amount, at a particular rate, and in a particular time period

        Parameters
        ----------
        Principal : int
            Initial Amount being given out
        Time : int
            Number of years it will take to repay
        Rate : int
            Interest rate being charged
        """
    return (Principal * Time * (Rate / 100))


#5. Write a Python program that checks if a string is a palindrome; optionally, write a unit test to check your program's correctness

def is_palindrome(palindrome):
    input = palindrome.lower().replace(" ","")
    return input == input[::-1]



#6. Write a function that removes repeated characters from a string. Sample strings are
#Hello: output should be Helo
#Concatenate: output should be Conate

def remove_duplicate (sample_word):

  dup1=""
  for char in sample_word:
    if char.lower() not in dup1 and char.upper() not in dup1:
      dup1=dup1+char
  return dup1
#print (remove_duplicate("Hello"))
#print (remove_duplicate("Concatenate"))


#7. Create a program that prints out the odd numbers in an array.
def print_odd (sample_array):
  odd_number = []
  for char in sample_array:
    if char % 2 == 1:
        odd_number.append(char)
  return odd_number
print (print_odd([1, 2, 3, 4, 5]))
print (print_odd([34, 2, 9, 91, 19, 401, 0 ]))

#8. Create a program that prints out the even numbers in an array.
def print_even (sample_array):
  even_number = []
  for char in sample_array:
    if char % 2 == 0:
        even_number.append(char)
  return even_number
print (print_even([1, 2, 3, 4, 5]))
print (print_even([34, 2, 9, 91, 19, 401, 0 ]))


#9. Create a function that converts any string value to upper case. Then write a unit test that checks the function's correctness.

def is_upper(sample):
    
    return sample.upper()

#10. Create a function that converts any string value to a Sentence case, then write a unit test that checks the function's correctness.


def is_sentence(sample): 
    words=sample.split(". ") 
    new=". ".join([word.capitalize() for word in words])  
  
    words=new.split("! ") 
    new="! ".join([word.split()[0][0].upper()+word[1:] for word in words])
  
    words=new.split("? ") 
    new="? ".join([word.split()[0][0].upper()+word[1:] for word in words])
  
    return new 



    #There is a separate file for the functions that require unittests and another one where the unit tests are located.
    #Script to run the unit tests: python -m unittest *nameoffile*