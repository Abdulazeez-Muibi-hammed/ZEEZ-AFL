#2 Unit test to check for the powers of given number
import unittest
import afl_test_functions
class TestPower(unittest.TestCase):
    def test_power(self):        
        self.assertEqual(afl_test_functions.power(-1, 2), 1)
        self.assertEqual(afl_test_functions.power(100, 2), 10000)
        self.assertEqual(afl_test_functions.power(0, 3), 0)
        self.assertEqual(afl_test_functions.power(2, 0), 1)
        self.assertEqual(afl_test_functions.power(2, -3), 0.125)
    def test_power_neg(self):
        self.assertNotEqual(afl_test_functions.power(3, 3), 6)
        self.assertNotEqual(afl_test_functions.power(-1, 2), 5)
        self.assertNotEqual(afl_test_functions.power(0, 0), 0)

#5 Unit test to check for palindromes
class TestPalindrome(unittest.TestCase):
    def test_palindrome(self):
        self.assertEqual(afl_test_functions.is_palindrome("Radar"), True)
        self.assertEqual(afl_test_functions.is_palindrome("Oozy Rat in a sanItaRy ZoO"), True)
        self.assertEqual(afl_test_functions.is_palindrome("UFo tofu"), True)
        self.assertEqual(afl_test_functions.is_palindrome("Uf0 tofu"), False)
        self.assertEqual(afl_test_functions.is_palindrome("WePanicInaPew"), True)
        self.assertEqual(afl_test_functions.is_palindrome("Ready"), False)
        self.assertEqual(afl_test_functions.is_palindrome("Rad"), False)

#9 Unit test to check for upper case conversion
class TestUpperCase(unittest.TestCase):
    def test_uppercase(self):
        self.assertEqual(afl_test_functions.is_upper("This is a string"), "THIS IS A STRING")
        self.assertEqual(afl_test_functions.is_upper("Ready"), "READY")
        self.assertEqual(afl_test_functions.is_upper("convert to upper case"), "CONVERT TO UPPER CASE")
        self.assertEqual(afl_test_functions.is_upper("UFO TOFU"), "UFO TOFU")
        self.assertEqual(afl_test_functions.is_upper("We have 2 slots left, but 5 contestants"), "WE HAVE 2 SLOTS LEFT, BUT 5 CONTESTANTS")

#10 Unit test to check for sentence case conversion
class TestSentenceCase(unittest.TestCase):
    def test_sentence_case(self):
        self.assertEqual(afl_test_functions.is_sentence("THIS IS A STRING. THIS ALSO. WHILE THIS IS NOT. EUREKA! DO YOU NOW KNOW WHAT A STRING IS? OFCOURSE YOU DO."), "This is a string. This also. While this is not. Eureka! Do you now know what a string is? Ofcourse you do.")
        self.assertEqual(afl_test_functions.is_sentence("Ready"), "Ready")
        self.assertEqual(afl_test_functions.is_sentence("oozy Rat. in a, sanItaRy ZoO"), "Oozy rat. In a, sanitary zoo")
        self.assertEqual(afl_test_functions.is_sentence("you said what? she asked. the test is due on monday! he screamed"), "You said what? She asked. The test is due on monday! He screamed")
        self.assertEqual(afl_test_functions.is_sentence("WePanicInaPew"), "Wepanicinapew")

