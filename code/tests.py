import unittest
from code.url_utility import is_valid_url

class ProjectsTests(unittest.TestCase):

    def test_url_validator(self):
        self.assertTrue(is_valid_url('https://www.youtube.com/watch?v=M-mtdN6R3bQ'))
        self.assertFalse(is_valid_url(''))
        self.assertFalse(is_valid_url('dfsgsgf'))

if __name__ == '__main__':
    unittest.main()
