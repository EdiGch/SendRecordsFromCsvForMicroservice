
Aplikacja wysyła dane do mikroserwisu validation w celu przetestowania poprawności działania 
walidacji oraz statystyk walidacji.

## Przygotowanie do pierwszego uruchomienia 
Przed pierwszym uruchomieniem należy uzupełnić zmienną ```ENDPOINT_ADDRESS``` 
w pliku ```backend.env``` o adres mikroserwisu lub 
stworzyć nowy plik o nazwię ```.env.local```. Nowo stworzony plik musi zawierać zmienną
```ENDPOINT_ADDRESS``` z wartością wskazującą adres mikroserwisu.
### Linux

1. Instalacja wietualnego środowiska 
```shell
pip install virtualenv
```
2. Instalacja virtualenv w katalogu projektu
```shell
virtualenv -p python3.10 env
```
3. Wejście/uruchomienie środowiska wirtualnego:
```shell
source env/bin/activate
```
4. Instalacja zależności z pliku
```shell
pip install -r requirements.txt
```
5. Uruchomienie programu
```shell
 python main.py
```