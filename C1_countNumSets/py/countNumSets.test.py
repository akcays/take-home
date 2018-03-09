import unittest
from countNumSets import count_num_sets
 
class Test(unittest.TestCase):

  def test_count_num_sets(self):
    self.assertEqual(0, count_num_sets([1,2,3]))
    self.assertEqual(0, count_num_sets([1,2,3]))
    self.assertEqual(3, count_num_sets([2,5,4,3]))
    self.assertEqual(7, count_num_sets([3,7,8,10,15,22]))

 
if __name__ == '__main__':
  unittest.main()
