# naokraglo
Zagadka z Wiedzy i życia

Rozwiązanie "brute force"

Można optymalizować, i nie dzielić na każdy możliwy podział, ale na sensowne wg mnożenia, zwracając uwagę na to że długość iloczynu zawiera się między długością większego czynnika a sumą długości czynników , np:

`23 * 4 = 92 :: długości 2, 1, 2, albo 99 * 99 = 9801 :: długości 2, 2, 4`

i dzielić tylko na takie kawałki, gdize jest spełniony ten warunek.
