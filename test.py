import unittest
from Script import FS 
class TestMethods(unittest.TestCase):
  def test_fs(self):
  	self.assertEqual(FS(1),[1])
  	self.assertEqual(FS(2),[1,1])
  	self.assertEqual(FS(3),[1,1,2])
if __name__ == '__main__':
    unittest.main()