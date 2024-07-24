import unittest
from code.url_utility import is_valid_url, trim_url

class ProjectsTests(unittest.TestCase):

    def test_url_validator(self):
        self.assertTrue(is_valid_url('https://www.youtube.com/watch?v=M-mtdN6R3bQ'))
        self.assertFalse(is_valid_url(''))
        self.assertFalse(is_valid_url('dfsgsgf'))
        
    def test_trim_url(self):
        self.assertEqual(trim_url('https://www.youtube.com/watch?v=M-mtdN6R3bQ'), 'https://www.youtube.com/watch?v=M-mtdN6R3bQ')
        self.assertEqual(trim_url('https://www.youtube.com/watch?v=M-mtdN6R3bQ&list=PLw-VjHDlEOgvfn7wZ9I-9fZw0Ku8yZrQG&index=2'), 'https://www.youtube.com/watch?v=M-mtdN6R3bQ')
        self.assertEqual(trim_url('https://www.youtube.com/watch?v=M-mtdN6R3bQ&list=PLw-VjHDlEOgvfn7wZ9I-9fZw0Ku8yZrQG'), 'https://www.youtube.com/watch?v=M-mtdN6R3bQ')
        self.assertEqual(trim_url('https://www.youtube.com/watch'), 'https://www.youtube.com/watch')
        self.assertEqual(trim_url(''), '')

if __name__ == '__main__':
    unittest.main()
