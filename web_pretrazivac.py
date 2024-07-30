# Mina Radenkovic SV 76/2022

"""
Implementirati sistem za kretanje po istoriji veb-pregledača (web browser).
U veb-pregledaču korisnik pristupa veb-adresama (u daljem tekstu koristićemo i sinonim url)
sa mogućnošću vraćanja kroz istoriju na veb-stranice koje je prethodno posetio.
Maksimalni broj koraka za vraćanje unazad je određen, osim brojem posećenih stranica,
i kapacitetom istorije MAX_PAGES (maksimalni broj stranica koje istorija čuva).
Kada se korisnik vrati n koraka (odnosno n stranica) unazad,
postoji mogućnost da se korisnik kreće unapred u koracima sve dok ne dođe do stranice odakle je krenuo.
Posetom nove veb-adrese, brišu se sve stranice za kretanje unapred.
Implementirati klasu BrowserHistory.
Klasa se inicijalizuje navođenjem početne (homepage) web-adrese.
Implementirati metode:
visit(url) – Posećuje se veb-adresa url.
back(steps) – Korisnik bira da se vrati u istoriju steps broj koraka.
              Ukoliko je steps veći od broja posećenih stranica ili konstante MAX_PAGES,
              vraća se onoliko koraka unazad koliko je moguće.
              Povratna vrednost je trenutna veb-adresa (posle steps koraka).
forward(steps) – Korisnik bira da ide unapred kroz istoriju steps broj koraka.
                 Ukoliko je steps veće od broja koraka koliko je moguće ići unapred, uzeti taj broj.
                 Povratna vrednost je trenutna veb-adresa (posle steps koraka).
Pri pokretanju aplikacije, korisnik navodi početnu (homepage) adresu.
Zatim korisnik može da poseti novu veb-adresu navodeći je ili da unese komande back i forward
(uz opciono zadavanje broja koraka – pogledati primere)
za kretanje kroz istoriju pri čemu se ispisuje trenutna web-adresa.
Navođenjem komande exit, izlazi se iz aplikacije.
"""

from deque import Deque, FullDequeException, EmptyDequeException


class BrowserHistory:
    def __init__(self, homepage, max_pages=4):
        self.history = Deque(max_pages)
        self.history.add_last(homepage)
        self.future = Deque(max_pages)
        self.current_page = homepage
        self.max_pages = max_pages

    def visit(self, url):
        try:
            if not self.history.is_full():
                self.history.add_last(url)
            else:
                self.history.delete_first()
                self.history.add_last(self.current_page)
        except FullDequeException as e:
            self.history.delete_first()
            self.history.add_last(url)

        self.future = Deque(self.max_pages)  # Reset the future deque
        self.current_page = url
        print("Trenutna stranica: ", self.current_page)

    def back(self, steps):
        current = self.current_page
        try:
            while steps > 0 and not self.history.is_empty():
                self.future.add_first(self.current_page)
                self.history.delete_last()
                self.current_page = self.history.last()
                current = self.current_page
                steps -= 1
        except EmptyDequeException as e:
            self.current_page = current
        print("Trenutna stranica: ", self.current_page)
        return self.current_page

    def forward(self, steps):
        while steps > 0 and not self.future.is_empty():
            self.history.add_last(self.current_page)
            self.current_page = self.future.delete_first()
            steps -= 1
        print("Trenutna stranica: ", self.current_page)
        return self.current_page

if __name__ == "__main__":
    MAX_PAGES = 10
    istorija = BrowserHistory("Homepage", MAX_PAGES)
    print("===========================================================")
    print("Sistem za kretanje po istoriji veb-pregledača (web browser)")
    print("===========================================================")
    print("Za izlaz Enter \n")
    print("Trenutna stranica: Homepage")

    while True:
        odgovor = input(">> ")
        if "" == odgovor:
            break
        elif odgovor.startswith("back"):
            steps = int(odgovor.split()[1]) if len(odgovor.split()) > 1 else 1
            istorija.back(steps)
        elif odgovor.startswith("forward"):
            steps = int(odgovor.split()[1]) if len(odgovor.split()) > 1 else 1
            istorija.forward(steps)
        else:
            istorija.visit(odgovor)
