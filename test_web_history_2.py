import unittest
from web_pretrazivac import BrowserHistory


class TestDeque(unittest.TestCase):
    def setUp(self):
        self.browser_history = BrowserHistory('homepage.com')

    def test_back_single_step(self):
        self.browser_history.visit('ftn.uns.ac.rs')
        self.browser_history.visit('youtube.com')
        self.browser_history.visit('facebook.com')
        self.assertEqual(self.browser_history.back(1), 'youtube.com')
        self.assertEqual(self.browser_history.back(1), 'ftn.uns.ac.rs')

    def test_back_multiple_steps(self):
        self.browser_history.visit('ftn.uns.ac.rs')
        self.browser_history.visit('youtube.com')
        self.browser_history.visit('facebook.com')
        self.assertEqual(self.browser_history.back(2), 'ftn.uns.ac.rs')
        self.assertEqual(self.browser_history.back(1), 'homepage.com')

    def test_back_forward_multiple_steps(self):
        self.browser_history.visit('ftn.uns.ac.rs')
        self.browser_history.visit('youtube.com')
        self.browser_history.visit('facebook.com')
        self.assertEqual(self.browser_history.back(2), 'ftn.uns.ac.rs')
        self.assertEqual(self.browser_history.forward(2), 'facebook.com')
        self.assertEqual(self.browser_history.back(3), 'homepage.com')
        self.assertEqual(self.browser_history.forward(3), 'facebook.com')


if __name__ == '__main__':
    unittest.main()