PLP
===

Wrapper dla Pythona biblioteki CLP (Polski słownik języka fleksyjnego)


Instalacja
----------

Przy użyciu ``pip`` (najlepiej z virtualenv'a)::

    $ pip install -e git+https://github.com/agh-glk/plp.git


Uwaga: moduł do działania wymaga posiadania licencjonowanej bilbioteki CLP w systemie.

Użycie
------

Wszystkie metody (których nazwy analogiczne są do funkcji z bilbioteki CLP) dostępne są z poziomu obiektu klasy PLP::

    from plp import PLP
    p = PLP()


lub::

    p = PLP('/sciezka/inna/do/clp.so')


Biblioteka przyjmuje tekstowe argumenty typu ``unicode`` oraz zwraca także type ``unicode`` 
tam gdzie wymagane są napisy (przykrywa tym samym fakt, że CLP pracuje wewnętrznie w kodowaniu ISO-8859-2).

Typowe użycie modułu to próba identyfikacji napisu jako formy fleksyjnej konkretnego wyrazu słownika. Wyrazy słownika
identyfikowane są za pomocą liczby typu ``integer`` za pomocą metody ``rec(forma)``::

    >>> p.rec(u'żółwiem')
    [18660912]
    >>> p.rec(u'zamkowi')
    [18539600, 18539616, 18541616]

Możliwe jest tez odpytanie się bilbioteki o wyraz z uwzględnieniem błędów typu polonica. Służy do tego metoda ``orec(forma)``
(ogonkowy rec)::

    >>> p.rec(u'zolwiem')
    []
    >>> p.orec(u'zolwiem')
    [18660912]
    >>> p.orec(u'żólwiem')
    [18660912]


Zwracana jest lista identyfikatorów, ponieważ jeden napis moze odpowiadać wiecej niż jednemu elementowi słownika
(element słownika stanowi jedna grupa fleksyjna).

Następnie za pomocą ``bform(id)`` możemy odpytać się o formę podstawową wyrazu, znając jego identyfikator::

    >>> p.bform(18660912)
    u'\u017c\xf3\u0142w'
    >>> print p.bform(18660912)
    żółw
    >>> map(lambda x: p.bform(x), p.rec(u'zamkowi'))
    [u'zamek', u'zamek', u'zamkowy']

Za pomocą metody ``label(id)`` można otrzymać etykiete gramatyczną wyrazu. Pierwsza litera etykiety koduje część mowy::

    >>> p.label(18660912)
    u'ABAABA'
    >>> p.label(18660912)[0] == plp.PLP.CZESCI_MOWY.RZECZOWNIK
    True

Możliwe jest także uzyskanie informacji na temat wektora odmiany danego wyrazu. Metoda ``forms(id)`` zwraca wektor
odmiany w postaci listy napisów::


    >>> p.forms(17724032)
    [u'pies', u'psa', u'psu', u'psem', u'psie', u'psy', u'ps\xf3w', u'psom', u'psami', u'psach']


Metoda ``vec(id, forma)`` zwraca listę zawierającą pozycję wektora fleksyjnego na której występuje dla 
danego wyrazu dana forma::

    >>> p.vec(17724032, u'psu')
    [3]

Uwaga: Wektor odmiany liczony jest od 1 (a nie jak index listy od 0). Wynika to z konwencji lingiwstycznej w przyjętej w CLP.


