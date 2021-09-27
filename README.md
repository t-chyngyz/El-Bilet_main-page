# [El-Bilet_main-page](https://el-bilet.github.io/El-Bilet_main-page/)

Инструкция по установке Django. <br />
1) Создаем каталог: <br />
  a) Если Windows запускаем cmd(командная строка) и набираем там: <br />
     d: <br />
     mkdir El-Bilet_main-page <br />
     cd El-Bilet_main-page <br />
  b) Если MacOS запускаем терминал и набираем там: <br />
     mkdir ~/El-Bilet_main-page <br />
     cd ~/El-Bilet_main-page <br />
2) Скачиваем Python3: <br />
  a) Если Windows скачиваем здесь https://www.python.org/downloads/windows/ <br />
  b) Если MasOS скачиваем здесь https://www.python.org/downloads/macos/ <br />
3 Устанавливаем Python3: <br />
  Запускаем установочный пакет Python3 и при установке Python3 ставим галочку "Add Python 3.8 to path". <br />
  a) Пример для Windows https://www.c-sharpcorner.com/article/how-to-install-python-3-8-in-windows/  <br />
  b) Пример для MacOS https://www.laptopmag.com/how-to/install-python-on-macos <br />
4) Создаем виртуальное окружение для Django и активизируем: <br />
  a) Если Windows в cmd(командная строка) и набираем:  <br />
    cd D:\El-Bilet_main-page>  <br />
    python -m venv venv <br />
    venv\Scripts\activate <br />
    python3 -m pip install --upgrade pip <br />
  b) Если MacOS запускаем терминал и набираем: <br />
    cd ~/El-Bilet_main-page <br />
    python3 -m venv venv <br />
    source venv/bin/activate <br />
    python3 -m pip install --upgrade pip <br />
5) Клонируем git: <br />
  Если Windows в cmd(командная строка), если MacOS в терминале и набираем: <br />
    git clone https://github.com/El-Bilet/El-Bilet_main-page . <br />
    git checkout chyngyz <br />
6) Устанавливаем Веб-фреймворк Django (Python): <br />
  Если Windows в cmd(командная строка), если MacOS в терминале и набираем: <br />
    pip install -r requirements.txt <br />
7) Запускаем Веб-фреймворк Django (Python): <br />
  Если Windows в cmd(командная строка), если MacOS в терминале и набираем: <br />
    python3 manage.py runserver <br />

