from web_pretrazivac import BrowserHistory
import unittest


class TestBrowserHistory(unittest.TestCase):
    def setUp(self):
        # MAX_PAGES = 10
        self.instance = BrowserHistory("homepage", 10)
        for i in range(9):
            self.instance.visit(f"site{i}")

    def test_new_visit(self):
        self.instance.visit("site9")
        ret = self.instance.forward()
        self.assertEqual(ret, "site9")

    def test_mutiple_new_visits(self):
        for i in range(5):
            self.instance.visit(f"site1{i}")
        ret = self.instance.forward()
        self.assertEqual(ret, "site14")

    def test_new_visit_after_back(self):
        self.instance.back(10)
        self.instance.visit("site1")
        ret = self.instance.forward()
        self.assertEqual(ret, "site1")

    def test_back_more_steps(self):
        ret = self.instance.back(5)
        self.assertEqual(ret, 'site3')

    def test_forward_more_steps(self):
        self.instance.back(5)
        ret = self.instance.forward(3)
        self.assertEqual(ret, 'site6')

    def test_new_visit_back(self):
        self.instance.visit("site9")
        ret = self.instance.back()
        self.assertEqual(ret, 'site8')

    def test_new_visit_back_forward_back(self):
        self.instance.visit('site9')
        self.instance.back()
        self.instance.forward()
        ret = self.instance.back()
        self.assertEqual(ret, 'site8')

    def test_max_forward(self):
        self.instance.back(10)
        ret = self.instance.forward(100)
        self.assertEqual(ret, "site8")

    def test_max_forward_not_full(self):
        bh = BrowserHistory("homepage")
        for i in range(5):
            bh.visit(f"site{i}")
        bh.back(2)
        ret = bh.forward(100)
        self.assertEqual("site4", ret)

    def test_max_back(self):
        ret = self.instance.back(100)
        self.assertEqual(ret, "homepage")

    def test_max_back_not_full(self):
        bh = BrowserHistory("homepage")
        bh.visit("site0")
        bh.visit("site1")
        ret = bh.back(5)
        self.assertEqual(ret, "homepage")

    def test_max_pages_back(self):
        self.instance.visit("site9")
        ret = self.instance.back(100)
        self.assertEqual(ret, "site0")

    def test_max_pages_back_multiple(self):
        for i in range(5):
            self.instance.visit(f"site1{i}")
        ret = self.instance.back(100)
        self.assertEqual(ret, 'site4')

    def test_homepage_back_forward(self):
        bh = BrowserHistory("homepage")
        ret_back = bh.back()
        ret_forward = bh.forward()
        self.assertEqual(ret_back, "homepage")
        self.assertEqual(ret_forward, "homepage")

    # head < current_page < tail
    def test_back_hct(self):
        bh = BrowserHistory("homepage")
        for i in range(4):
            bh.visit(i)

        bh.back(2)
        ret = bh.back(4)
        self.assertEqual(ret, "homepage")
        bh.forward(4)
        ret = bh.back(11)
        self.assertEqual(ret, "homepage")

    # tail < head < current_page
    def test_back_thc(self):
        bh = BrowserHistory("homepage")
        bh.visit("0")
        for i in range(10):
            bh.visit(i)
        ret = bh.back(5)
        self.assertEqual(ret, 4)
        ret = bh.back(5)
        self.assertEqual(ret, 0)
        bh.forward(4)
        ret = bh.back(8)
        self.assertEqual(ret, 0)
        bh.forward(8)
        ret = bh.back(10)
        self.assertEqual(ret, 0)

    # current_page < tail < head
    def test_back_cth(self):
        bh = BrowserHistory("homepage")
        for i in range(5):
            bh.visit(i)
        for i in range(10):
            bh.visit(i)
        ret = bh.back(2)
        self.assertEqual(ret, 7)
        ret = bh.back(8)
        self.assertEqual(ret, 0)
        bh.forward(8)
        ret = bh.back(10)
        self.assertEqual(ret, 0)


if __name__ == "__main__":
    unittest.main()