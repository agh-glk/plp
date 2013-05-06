PLP
===

Wrapper dla Pythona 3 biblioteki CLP (Polski słownik języka fleksyjnego).

Oryginalny wrapper dla Pythona 2 autorstwa Krzysztofa Dorosza <cypreess@gmail.com> dostępny jest pod adresem
`github.com/kgadek/plpy3 <https://github.com/kgadek/plpy3>`_ . Port wykonany przez Konrada Gądka <kgadek@gmail.com>.


Instalacja
----------

Przy użyciu ``pip`` (najlepiej z użyciem virtualenv)::

    $ pip install -e git+https://github.com/kgadek/plpy3.git#egg=plpy3


Uwaga: moduł do działania wymaga posiadania licencjonowanej biblioteki CLP w systemie.

Użycie
------

Wszystkie metody (których nazwy analogiczne są do funkcji z biblioteki CLP) dostępne są z poziomu obiektu klasy PLP::

    from plp import PLP
    p = PLP()


lub::

    p = PLP('/sciezka/inna/do/clp.so')


Biblioteka przyjmuje tekstowe argumenty typu ``unicode`` oraz zwraca także type ``unicode`` 
tam gdzie wymagane są napisy (przykrywa tym samym fakt, że CLP pracuje wewnętrznie w kodowaniu ISO-8859-2).

Typowe użycie modułu to próba identyfikacji napisu jako formy fleksyjnej konkretnego wyrazu słownika. Wyrazy słownika
identyfikowane są za pomocą liczby typu ``integer`` za pomocą metody ``rec(forma)``::

    >>> p.rec('żółwiem')
    [18660912]
    >>> p.rec('zamkowi')
    [18539600, 18539616, 18541616]

Możliwe jest tez odpytanie się biblioteki o wyraz z uwzględnieniem błędów typu polonica. Służy do tego metoda ``orec(forma)``
(ogonkowy rec)::

    >>> p.rec('zolwiem')
    []
    >>> p.orec('zolwiem')
    [18660912]
    >>> p.orec('żólwiem')
    [18660912]


Zwracana jest lista identyfikatorów, ponieważ jeden napis może odpowiadać więcej niż jednemu elementowi słownika
(element słownika stanowi jedna grupa fleksyjna).

Następnie za pomocą ``bform(id)`` możemy odpytać się o formę podstawową wyrazu, znając jego identyfikator::

    >>> p.bform(18660912)
    '\u017c\xf3\u0142w'
    >>> print(p.bform(18660912))
    żółw
    >>> [p.bform(x) for x in p.rec('zamkowi')]
    ['zamek', 'zamek', 'zamkowy']

Za pomocą metody ``label(id)`` można otrzymać etykietę gramatyczną wyrazu. Pierwsza litera etykiety koduje część mowy::

    >>> p.label(18660912)
    'ABAABA'
    >>> p.label(18660912)[0] == PLP.CZESCI_MOWY.RZECZOWNIK
    True

Możliwe jest także uzyskanie informacji na temat wektora odmiany danego wyrazu. Metoda ``forms(id)`` zwraca wektor
odmiany w postaci listy napisów::


    >>> p.forms(17724032)
    ['pies', 'psa', 'ps', 'psem', 'psie', 'psy', 'ps\xf3w', 'psom', 'psami', 'psach']


Metoda ``vec(id, forma)`` zwraca listę zawierającą pozycję wektora fleksyjnego na której występuje dla 
danego wyrazu dana forma::

    >>> p.vec(17724032, 'psu')
    [3]

Uwaga: Wektor odmiany liczony jest od 1 (a nie jak index listy od 0). Wynika to z konwencji lingwistycznej w przyjętej w CLP.


