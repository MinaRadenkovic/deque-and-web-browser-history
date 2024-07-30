import unittest
from web_pretrazivac import BrowserHistory


class TestHistory(unittest.TestCase):
    def setUp(self):
        self.HOMEPAGE = 'homepage.com'
        self.my_history = BrowserHistory(self.HOMEPAGE, 4)

    def test_back_1(self):
        """
        Testira vracanje jednog po jednog url-a
        """
        self.my_history.visit('ftn.uns.ac.rs')
        self.my_history.visit('youtube.com')
        self.my_history.visit('facebook.com')
        self.assertEqual('youtube.com', self.my_history.back(1))
        self.assertEqual('ftn.uns.ac.rs', self.my_history.back(1))

    def test_back_2(self):
        """
        Testira vracanje vise od jednog url-a u nazad
        """
        self.my_history.visit('ftn.uns.ac.rs')
        self.my_history.visit('youtube.com')
        self.my_history.visit('facebook.com')
        self.assertEqual(self.my_history.back(2), 'ftn.uns.ac.rs')

    def test_back_forward(self):
        """
        Testira vracanje u nazad pa u napred
        """
        self.my_history.visit('ftn.uns.ac.rs')
        self.my_history.visit('youtube.com')
        self.my_history.visit('facebook.com')
        self.assertEqual(self.my_history.back(1), 'youtube.com')
        self.assertEqual(self.my_history.back(1), 'ftn.uns.ac.rs')
        self.assertEqual(self.my_history.forward(1), 'youtube.com')

    def test_back_2_forward_2(self):
        """
        Testira visestruko vracanje u nazad pa u napred
        """
        self.my_history.visit('ftn.uns.ac.rs')
        self.my_history.visit('youtube.com')
        self.my_history.visit('facebook.com')
        self.assertEqual(self.my_history.back(2), 'ftn.uns.ac.rs')
        self.assertEqual(self.my_history.forward(2), 'facebook.com')

    def test_exact_back(self):
        """
        Testira vracanje tacno n u nazad gde je n broj unetih url-ova od pocetka aplikacije,
        treba da budemo na homepage-u
        """
        self.my_history.visit('ftn.uns.ac.rs')
        self.my_history.visit('youtube.com')
        self.my_history.visit('facebook.com')
        self.assertEqual(self.my_history.back(3), self.HOMEPAGE)

    def test_exact_forward(self):
        """
        Testira idjenje tacno n u napred gde je n broj unetih url-ova od pocetka aplikacije
        tako sto se prvo vrati n u nazad
        :return:
        """
        self.my_history.visit('ftn.uns.ac.rs')
        self.my_history.visit('youtube.com')
        self.my_history.visit('facebook.com')
        self.assertEqual(self.my_history.back(3), self.HOMEPAGE)
        self.assertEqual(self.my_history.forward(3), 'facebook.com')

    def test_back_more_steps(self):
        """
        Testira preterano vracanje u nazad, uvek treba da ostanemo na homepage-u
        """
        self.my_history.visit('ftn.uns.ac.rs')
        self.my_history.visit('youtube.com')
        self.my_history.visit('facebook.com')
        self.my_history.visit('reddit.com')
        self.my_history.visit('gsp.rs')
        self.assertEqual(self.my_history.back(6), self.HOMEPAGE)
        self.assertEqual(self.my_history.back(17), self.HOMEPAGE)

    def test_forward_more_steps(self):
        """
        Testira preterano idjenje u napred
        """
        self.my_history.visit('ftn.uns.ac.rs')
        self.my_history.visit('youtube.com')
        self.my_history.visit('facebook.com')
        self.my_history.visit('reddit.com')
        self.my_history.visit('gsp.rs')
        self.assertEqual(self.my_history.back(2), 'facebook.com')
        self.assertEqual(self.my_history.forward(17), 'gsp.rs')
        self.assertEqual(self.my_history.forward(34), 'gsp.rs')

    def test_no_forward_after_new_page(self):
        """
        Testira postojanje forward istorije nakon posecenja nove stranice,
        ne treba nista da se desi [ PO MENI ]
        """
        self.my_history.visit('youtube.com')
        self.my_history.visit('facebook.com')
        self.my_history.visit('reddit.com')
        self.my_history.visit('gsp.rs')
        self.my_history.back(3)
        self.my_history.visit('ftn.uns.ac.rs')
        self.assertEqual(self.my_history.forward(1), 'ftn.uns.ac.rs')
        self.assertEqual(self.my_history.forward(57), 'ftn.uns.ac.rs')

    def test_more_than_max_pages(self):
        """
        Testira posecivanje vise od MAX_PAGES stranica, [ PO MENI ] treba da se prepise preko
        skroz leve tj homepage stranice kada se prekoraci MAX_PAGES i onda da se operacija
        normalno nastavlja samo su stranice iza izgubljene tj ne moze se vratiti na njih
        """
        for page in range(BrowserHistory.MAX_PAGES + 10):
            self.my_history.visit(f'{page}.com')

        self.assertEqual(self.my_history.back(100), '10.com')

    def test_more_than_max_pages_visit_remove(self):
        """
        Testira postojanje forward istorije nakon prekoracenja MAX_PAGES i posecivanja nove stranice,
        ne treba nista da se desi [ PO MENI ]
        """
        for page in range(BrowserHistory.MAX_PAGES + 10):
            self.my_history.visit(f'{page}.com')

        self.assertEqual(self.my_history.back(100), '10.com')
        self.my_history.visit('new.net')
        for i in range(10):
            self.assertEqual('new.net', self.my_history.forward(i))


if __name__ == '__main__':
    unittest.main()