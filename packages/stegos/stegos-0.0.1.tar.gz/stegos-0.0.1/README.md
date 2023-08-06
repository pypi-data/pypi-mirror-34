
# stegos

модуль для python, скрывающий информацию стеганографическим способом
Использование


**Установка:**

pip(3) install stegos

**Подключение:**

from stegos import urlImg, readFile, hideMsg

**Описание функций:**

readFile('file_path') считывает байты файла

urlImg('url_path') скачивает картинку по указаному url в папку img (Создается автоматически если ее нету)

hideMsg('file_name','msg') скрывает текст на уровне байтов

hideArh('file_name','arhive_name') скрывает архивы в файлах

