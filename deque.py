"""
Modul sadrzi implementaciju deka na osnovu liste.

Implementirati dek (deque) sa ograničenim kapacitetom sa cirkularnim smeštanjem elemenata.
Kapacitet se zadaje prilikom kreiranja deka i nije proširiv.
U slučaju pokušaja dodavanja elementa u već popunjen dek baca se FullDequeException.
Dozvoljeno je bazirati implementaciju na implementaciji deka neograničenog kapaciteta sa vežbi.
"""

class DequeException(Exception):
    pass


class EmptyDequeException(DequeException):
    """
    Klasa modeluje izuzetke vezane za klasu Deque.
    """
    pass


class FullDequeException(DequeException):
    """
    Klasa modeluje izuzetke vezane za klasu Deque.
    """
    pass


class Deque(object):
    """
    Implementacija deka na osnovu liste sa ograničenim kapacitetom.
    """

    def __init__(self, granica=10):
        """
        Konstruktor.
        """
        self._granica = granica
        self._data = [None] * granica
        self._duzina = 0
        self._pocetak = 0
        self._kraj = 0

    def __len__(self):
        """
        Metoda vraca duzinu deka.
        """
        return self._duzina

    def is_empty(self):
        """
        Metoda proverava da li je dek prazan.
        """
        return self._duzina == 0

    def is_full(self):
        """
        Metoda proverava da li je dek pun.
        """
        if self._duzina == self._granica:
            raise FullDequeException("Dek je pun.")
        return self._duzina == self._granica

    def first(self):
        """
        Metoda omogucava pristup prvom elementu deka.
        """
        if self.is_empty():
            raise EmptyDequeException('Dek je prazan.')
        return self._data[self._pocetak]

    def last(self):
        """
        Metoda omogucava pristup poslednjem elementu deka.
        """
        if self.is_empty():
            raise EmptyDequeException('Dek je prazan.')
        return self._data[self._kraj]

    def add_first(self, e):
        """
        Metoda dodaje element na pocetak deka.

        Argument:
        - `e`: novi element
        """
        if self.is_full():
            raise FullDequeException("Dek je pun")
        self._pocetak = (self._pocetak + 1) % self._granica
        self._data[self._pocetak] = e
        self._duzina += 1
        if self._kraj == 0 and self._data[self._kraj] is None:
            self._kraj = self._pocetak

    def add_last(self, e):
        """
        Metoda dodaje element na kraj deka.

        Argument:
        - `e`: novi element
        """
        if self.is_full():
            raise FullDequeException("Dek je pun")
        self._kraj = (self._kraj - 1) % self._granica
        self._data[self._kraj] = e
        self._duzina += 1
        if self._pocetak == 0 and self._data[self._pocetak] is None:
            self._pocetak = self._kraj

    def delete_first(self):
        """
        Metoda izbacuje prvi element iz deka.
        """
        if self.is_empty():
            raise EmptyDequeException('Dek je prazan.')
        e = self._data[self._pocetak]
        self._data[self._pocetak] = None
        self._duzina -= 1
        self._pocetak = (self._pocetak - 1) % self._granica
        return e

    def delete_last(self):
        """
        Metoda izbacuje poslednji element iz deka.
        """
        if self.is_empty():
            raise EmptyDequeException('Dek je prazan.')
        e = self._data[self._kraj]
        self._data[self._kraj] = None
        self._kraj = (self._kraj + 1) % self._granica
        self._duzina -= 1
        return e

    def __str__(self):
        return str(self._data)

    @property
    def data(self):
        return self._data


if __name__ == '__main__':
    d = Deque(5)
    d.add_last(5)
    d.add_first(7)
    d.add_first(3)
    print(d.first())  # Output: 3

    d.delete_last()
    print(len(d))  # Output: 2

    d.delete_last()
    d.delete_last()
    d.add_first(6)
    print(d.last())  # Output: 6

    d.add_first(8)
    print(d.is_empty())  # Output: False
    print(d.last())  # Output: 6
