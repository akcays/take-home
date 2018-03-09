import unittest
from numberInEnglish import number_in_english
 
class Test(unittest.TestCase):

    def test_input_type(self):
        self.assertRaises(Exception, number_in_english, "145")
        self.assertRaises(Exception, number_in_english, "num")
        self.assertRaises(Exception, number_in_english, True)
        self.assertRaises(Exception, number_in_english, None)
        self.assertRaises(Exception, number_in_english, 100.95)
        self.assertRaises(Exception, number_in_english, [100.95])
        self.assertRaises(Exception, number_in_english, (10, 11, 12))

    def test_single_digits(self):
 
        self.assertEqual("one", number_in_english(1))
        self.assertEqual("two", number_in_english(2))
        self.assertEqual("three", number_in_english(3))
        self.assertEqual("four", number_in_english(4))
        self.assertEqual("five", number_in_english(5))
        self.assertEqual("six", number_in_english(6))
        self.assertEqual("seven", number_in_english(7))
        self.assertEqual("eight", number_in_english(8))
        self.assertEqual("nine", number_in_english(9))

    def test_teens(self):
 
        self.assertEqual("eleven", number_in_english(11))
        self.assertEqual("twelve", number_in_english(12))
        self.assertEqual("thirteen", number_in_english(13))
        self.assertEqual("fourteen", number_in_english(14))
        self.assertEqual("fifteen", number_in_english(15))
        self.assertEqual("sixteen", number_in_english(16))
        self.assertEqual("seventeen", number_in_english(17))
        self.assertEqual("eighteen", number_in_english(18))
        self.assertEqual("nineteen", number_in_english(19))

    def test_tens(self):
 
        self.assertEqual("ten", number_in_english(10))
        self.assertEqual("twenty", number_in_english(20))
        self.assertEqual("thirty", number_in_english(30))
        self.assertEqual("forty", number_in_english(40))
        self.assertEqual("fifty", number_in_english(50))
        self.assertEqual("sixty", number_in_english(60))
        self.assertEqual("seventy", number_in_english(70))
        self.assertEqual("eighty", number_in_english(80))
        self.assertEqual("ninety", number_in_english(90))

    def test_hundreds(self):
 
        self.assertEqual("one hundred", number_in_english(100))
        self.assertEqual("two hundred", number_in_english(200))
        self.assertEqual("three hundred", number_in_english(300))
        self.assertEqual("four hundred", number_in_english(400))
        self.assertEqual("five hundred", number_in_english(500))
        self.assertEqual("six hundred", number_in_english(600))
        self.assertEqual("seven hundred", number_in_english(700))
        self.assertEqual("eight hundred", number_in_english(800))
        self.assertEqual("nine hundred", number_in_english(900))
        self.assertEqual("one hundred twenty five", number_in_english(125))
        self.assertEqual("four hundred sixty eight", number_in_english(468))
        self.assertEqual("nine hundred ten", number_in_english(910))

    def test_thousands(self):
 
        self.assertEqual("one thousand", number_in_english(1000))
        self.assertEqual("two thousand", number_in_english(2000))
        self.assertEqual("three thousand", number_in_english(3000))
        self.assertEqual("four thousand", number_in_english(4000))
        self.assertEqual("five thousand", number_in_english(5000))
        self.assertEqual("six thousand", number_in_english(6000))
        self.assertEqual("seven thousand", number_in_english(7000))
        self.assertEqual("eight thousand", number_in_english(8000))
        self.assertEqual("nine thousand", number_in_english(9000))
        self.assertEqual("two thousand one hundred twenty five", number_in_english(2125))
        self.assertEqual("nine thousand four hundred sixty eight", number_in_english(9468))
        self.assertEqual("three thousand nine hundred ten", number_in_english(3910))
        self.assertEqual("seventy six thousand three hundred ninety two", number_in_english(76392))
        self.assertEqual("five hundred five thousand seven hundred twenty", number_in_english(505720))

    def test_large_numbers(self):
 
        self.assertEqual("nine hundred ninety nine thousand nine hundred ninety eight", number_in_english(999998))
        self.assertEqual("twelve million forty three", number_in_english(12000043))
        self.assertEqual("ten million five hundred twenty six thousand six hundred thirty three", number_in_english(10526633))
        self.assertEqual("three million five hundred sixty thousand seventy eight", number_in_english(3560078))
        self.assertEqual("one billion", number_in_english(1000000000))
        self.assertEqual("nine billion nine hundred eighty three million one hundred thousand two hundred twenty five", number_in_english(9983100225))
        self.assertEqual("nine billion nine hundred ninety nine million nine hundred ninety nine thousand nine hundred ninety nine", number_in_english(9999999999))        
 
if __name__ == '__main__':
  unittest.main()
