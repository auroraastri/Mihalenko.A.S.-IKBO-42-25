# Практическое занятие №1. Введение, основы работы в командной строке

П.Н. Советов, РТУ МИРЭА

Научиться выполнять простые действия с файлами и каталогами в Linux из командной строки. Сравнить работу в командной строке Windows и Linux.

## Задача 1

Вывести отсортированный в алфавитном порядке список имен пользователей в файле passwd (вам понадобится grep).

Ответ: labex:/etc/ $ cut -d : -f1 passwd | sort

## Задача 2

Вывести данные /etc/protocols в отформатированном и отсортированном порядке для 5 наибольших портов, как показано в примере ниже:

```
[root@localhost etc]# cat /etc/protocols ...
142 rohc
141 wesp
140 shim6
139 hip
138 manet
```

Ответ:
```
labex:project/ $ awk '{print $2, $1}' /etc/protocols | sort -nr | head -5
142 rohc
141 wesp
140 shim6
139 hip
138 manet
```
## Задача 3

Написать программу banner средствами bash для вывода текстов, как в следующем примере (размер баннера должен меняться!):

```
[root@localhost ~]# ./banner "Hello from RTU MIREA!"
+-----------------------+
| Hello from RTU MIREA! |
+-----------------------+
```

Перед отправкой решения проверьте его в ShellCheck на предупреждения.

Код файла баннер, созданного в консоли:
```
if [ $# -eq 0 ]; then
    echo "Usage: $0 <text>" >&2
    exit 1
fi

text="$*"
len=${#text}
width=$((len + 2))

printf -v dashes '%*s' "$width" ''
dashes=${dashes// /-}

printf '+%s+\n' "$dashes"
printf '| %s |\n' "$text"
printf '+%s+\n' "$dashes"
```
Ответ:
```
labex:project/ $ ./banner "YAY"
+-----+
| YAY |
+-----+
labex:project/ $ ./banner "Hello from RTU MIREA!"
+-----------------------+
| Hello from RTU MIREA! |
+-----------------------+
```

## Задача 4

Написать программу для вывода всех идентификаторов (по правилам C/C++ или Java) в файле (без повторений).

Пример для hello.c:

```
h hello include int main n printf return stdio void world
```

код внутри файла yippee на языке c++
```
#include <iostream>

using namespace std;

int main(){
    cout << "lalalalalala" << endl;
    return 0;
}
```
Ответ:
```
grep -oE '[a-za-Z_][a-zA-Z0-9_]*' yippee | sort -u | xargs
```
Вывод:
```
cout endl include int iostream lalalalalala main namespace return std using
```

## Задача 5

Написать программу для регистрации пользовательской команды (правильные права доступа и копирование в /usr/local/bin).

Например, пусть программа называется reg:

```
./reg banner
```

Код файла pyat:
```
#!/bin/bash
if [ $# -ne 1 ]; then
    echo "Usage: $0 <file>" >&2
    exit 1
fi

if [ ! -f "$1" ]; then
    echo "Файл $1 не найден" >&2
    exit 1
fi

sudo install -m 755 "$1" /usr/local/bin/
```

Ответ:
```
labex:project/ $ nano pyat
abex:project/ $ chmod +x pyat
labex:project/ $ ./pyat banner

labex:project/ $ ls -l /usr/local/bin/banner
```
Вывод:
```
-rwxr-xr-x 1 root root 0 Sep 30 23:02 /usr/local/bin/banner
```

В результате для banner задаются правильные права доступа и сам banner копируется в /usr/local/bin.

## Задача 6

Написать программу для проверки наличия комментария в первой строке файлов с расширением c, js и py.

Код файла six, созданного в консоли:
```
#!/bin/bash
dir="${1:-.}"

find "$dir" -type f \( -name '*.c' -o -name '*.js' -o -name '*.py' \) | while IFS= read -r f; do
    first=$(head -n 1 "$f")
    case "$f" in
        *.c|*.js) pattern='^[[:space:]]*(//|/\*)' ;;
        *.py)     pattern='^[[:space:]]*#' ;;
    esac
    if [[ $first =~ $pattern ]]; then
        echo "$f: комментарий есть"
    else
        echo "$f: комментария нет"
    fi
done
```

Ответ:
```
labex:project/ $ nano six
labex:project/ $ chmod +x six
labex:project/ $ shellcheck six
```

## Задача 7

Написать программу для нахождения файлов-дубликатов (имеющих 1 или более копий содержимого) по заданному пути (и подкаталогам).

Код файла seven, созданного в консоли:
```
#!/bin/bash
if [ $# -ne 1 ]; then
    echo "Usage: $0 <dir>" >&2
    exit 1
fi

find "$1" -type f -exec md5sum {} + | sort | uniq -w32 --all-repeated=separate
```

Создание и проверка файла seven через ShellCheck идентична заданию 6

Проверка кода:
```
labex:project/ $ nano seven
labex:project/ $ chmod +x seven
labex:project/ $ mkdir t7
labex:project/ $ echo hi > t7/a.txt
labex:project/ $ cp t7/a.txt t7/b.txt
labex:project/ $ echo other > t7/c.txt
labex:project/ $ ./seven t7
```
Вывод:
```
764efa883dda1e11db47671c4a3bbd9e  t7/a.txt
764efa883dda1e11db47671c4a3bbd9e  t7/b.txt
```

## Задача 8

Написать программу, которая находит все файлы в данном каталоге с расширением, указанным в качестве аргумента и архивирует все эти файлы в архив tar.

Код файла eight, созданного в консоли:
```
#!/bin/bash
if [ $# -ne 2 ]; then
    echo "Usage: $0 <dir> <extension>" >&2
    exit 1
fi

dir="$1"
ext="$2"

find "$dir" -maxdepth 1 -type f -name "*.$ext" -print0 | tar --null -T - -cf "archive_$ext.tar"
```

Проверка кода:
```
labex:project/ $ nano eight
labex:project/ $ chmod +x eight
labex:project/ $ shellcheck eight
labex:project/ $ mkdir t8 && cd t8
labex:project/ $ touch a.txt b.txt c.log
labex:project/ $ cd ..
labex:project/ $ ./eight t8 txt
labex:project/ $ tar -tf archive_txt.tar
```
Вывод:
```
764efa883dda1e11db47671c4a3bbd9e  t8/a.txt
764efa883dda1e11db47671c4a3bbd9e  t8/b.txt
```

## Задача 9

Написать программу, которая заменяет в файле последовательности из 4 пробелов на символ табуляции. Входной и выходной файлы задаются аргументами.

Код файла nine, созданного в консоли:
```
#!/bin/bash
if [ $# -ne 2 ]; then
    echo "Usage: $0 <input> <output>" >&2
    exit 1
fi

sed 's/    /\t/g' "$1" > "$2"
```

Проверка кода:
```
labex:project/ $ nano nine
labex:project/ $ chmod +x nine
labex:project/ $ shellcheck nine
labex:project/ $ printf 'a    b\n' > in.txt
labex:project/ $ ./nine in.txt out.txt
labex:project/ $ cat -A out.txt
```
Вывод:
```
a^Ib$
```

## Задача 10

Написать программу, которая выводит названия всех пустых текстовых файлов в указанной директории. Директория передается в программу параметром. 

Код файла ten, созданного в консоли:
```
#!/bin/bash
if [ $# -ne 1 ]; then
    echo "Usage: $0 <dir>" >&2
    exit 1
fi

find "$1" -type f -name '*.txt' -empty
```

Проверка кода:
```
nano empty_files.sh
chmod +x empty_files.sh
shellcheck empty_files.sh
mkdir t10
touch t10/empty.txt
echo hi > t10/full.txt
./empty_files.sh t10
```
Вывод:
```
t10/empty.txt
```

## Полезные ссылки

Линукс в браузере: https://bellard.org/jslinux/

ShellCheck: https://www.shellcheck.net/

Разработка CLI-приложений

Общие сведения

https://ru.wikipedia.org/wiki/Интерфейс_командной_строки
https://nullprogram.com/blog/2020/08/01/
https://habr.com/ru/post/150950/

Стандарты

https://www.gnu.org/prep/standards/standards.html#Command_002dLine-Interfaces
https://www.gnu.org/software/libc/manual/html_node/Argument-Syntax.html
https://pubs.opengroup.org/onlinepubs/9699919799/basedefs/V1_chap12.html

Реализация разбора опций

Питон

https://docs.python.org/3/library/argparse.html#module-argparse
https://click.palletsprojects.com/en/7.x/
