# [El-Bilet_main-page](https://el-bilet.github.io/El-Bilet_main-page/)

Инструкция по установке Django.
1 Создаем каталог:
  a) Если Windows запускаем cmd(командная строка) и набираем там:
     d:
     mkdir El-Bilet_main-page
     cd El-Bilet_main-page
  b) Если MacOS запускаем терминал и набираем там:
     mkdir ~/El-Bilet_main-page
     cd ~/El-Bilet_main-page
2 Скачиваем Python3:
  a) Если Windows скачиваем здесь https://www.python.org/downloads/windows/
  b) Если MasOS скачиваем здесь https://www.python.org/downloads/macos/
3 Устанавливаем Python3:
  Запускаем установочный пакет Python3 и при установке Python3 ставим галочку "Add Python 3.8 to path".
  a) Пример для Windows https://www.c-sharpcorner.com/article/how-to-install-python-3-8-in-windows/ 
  b) Пример для MacOS https://www.laptopmag.com/how-to/install-python-on-macos
4 Создаем виртуальное окружение для Django и активизируем:
  a) Если Windows в cmd(командная строка) и набираем: 
    cd D:\El-Bilet_main-page> 
    python -m venv venv
    venv\Scripts\activate
    python3 -m pip install --upgrade pip
  b) Если MacOS запускаем терминал и набираем:
    cd ~/El-Bilet_main-page
    python3 -m venv venv
    source venv/bin/activate
    python3 -m pip install --upgrade pip
5 Клонируем git:
  Если Windows в cmd(командная строка), если MacOS в терминале и набираем:
    git clone https://github.com/El-Bilet/El-Bilet_main-page .
    git checkout chyngyz
6 Устанавливаем Веб-фреймворк Django (Python):
  Если Windows в cmd(командная строка), если MacOS в терминале и набираем:
    pip install -r requirements.txt
7 Запускаем Веб-фреймворк Django (Python):
  Если Windows в cmd(командная строка), если MacOS в терминале и набираем:
    python3 manage.py runserver

