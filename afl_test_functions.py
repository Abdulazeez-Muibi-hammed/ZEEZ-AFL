
#2. Create a function that calculates the power of a number. Then write a unit test to check the correctness of the function.
def power (x, y):
    
    return x ** y


#5 Palindrome
def is_palindrome(palindrome):
    input = palindrome.lower().replace(" ","")
    return input == input[::-1]


#9. Check for Upper case
def is_upper(sample):
    
    return sample.upper()


#10 Check for Sentence Case
def is_sentence(sample): 
	words=sample.split(". ") 
	new=". ".join([word.capitalize() for word in words])  
  
	words=new.split("! ") 
	new="! ".join([word.split()[0][0].upper()+word[1:] for word in words])
  
	words=new.split("? ") 
	new="? ".join([word.split()[0][0].upper()+word[1:] for word in words])
  
	return new 
