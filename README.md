# Simple Flask App

Aplikacja wyświetlająca tekst 'Hello world'

- W projekcie wykorzystamy wirtualne środowisko:

  ```
  # tworzymy wirtualne środowisko dla bibliotek aplikacji:
  $ python3 -m venv my_venv

  # aktywowanie wirtualnego środowiska
  $ source my_venv/Scripts/activate

  # instalacja potrzebnych bibliotek
  $ pip install -r requirements.txt

  # zobacz
  $ pip list
  ```

  Sprawdź: [tutorial venv](https://docs.python.org/3/tutorial/venv.html) oraz [biblioteki flask](http://flask.pocoo.org).

- Uruchamianie applikacji:

  ```
  $ python main.py
  ```

- Kontynuując pracę z projektem, aktywowanie hermetycznego środowiska dla aplikacji py:
```
  # deaktywacja
  $ deactivate
  ```

  ```
  ...

  # aktywacja 
  $ source my_venv/Scripts/activate
  ```