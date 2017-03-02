# Поиск дубликатов файлов

Скрипт находит в папке (и всех подпапках к ней) файлы-дубликаты т.е. файлы с одинаковым именем и размером

# Как запустить

Запуск на Linux:
python duplicates.py filepath

# Пример запуска:

```#!bash

$ E:\Users\user\11_duplicates>python duplicates.py E:\Users\user\11_duplicates\testcases
 text.txt (0) bytes are duplicates (2 files):
        E:\Users\user\11_duplicates\testcases\text.txt
        E:\Users\user\11_duplicates\testcases\somefolder\text.txt
 sometext2.docx (12614) bytes are duplicates (2 files):
        E:\Users\user\11_duplicates\testcases\sometext2.docx
        E:\Users\user\11_duplicates\testcases\somefolder\somefolder2\sometext2.docx

```

Запуск на Windows происходит аналогично.

# Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке - [DEVMAN.org](https://devman.org)
