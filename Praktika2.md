# Практическое занятие №2. Менеджеры пакетов

П.Н. Советов, РТУ МИРЭА

Разобраться, что представляет собой менеджер пакетов, как устроен пакет, как читать версии стандарта semver. Привести примеры программ, в которых имеется встроенный пакетный менеджер.

## Задача 1

Вывести служебную информацию о пакете matplotlib (Python). Разобрать основные элементы содержимого файла со служебной информацией из пакета. Как получить пакет без менеджера пакетов, прямо из репозитория?

Служебная информация о пакете:
```
C:\Users\Anastasia>pip show matplotlib
Name: matplotlib
Version: 3.11.2
Summary: Python plotting package
Home-page: https://matplotlib.org
Author: John D. Hunter, Michael Droettboom
Author-email: Unknown <matplotlib-users@python.org>
License: License agreement for matplotlib versions 1.3.0 and later
 =========================================================

 1. This LICENSE AGREEMENT is between the Matplotlib Development Team
 ("MDT"), and the Individual or Organization ("Licensee") accessing and
 otherwise using matplotlib software in source or binary form and its
 associated documentation.

..........

           AUTHOR

   David H. Munro wrote Yorick and Gist.  Berkeley Yacc (byacc) generated
   the Yorick parser.  The routines in Math are from LAPACK and FFTPACK;
   MathC contains C translations by David H. Munro.  The algorithms for
   Yorick's random number generator and several special functions in
   Yorick/include were taken from Numerical Recipes by Press, et. al.,
   although the Yorick implementations are unrelated to those in
   Numerical Recipes.  A small amount of code in Gist was adapted from
   the X11R4 release, copyright M.I.T. -- the complete copyright notice
   may be found in the (unused) file Gist/host.c.

Location: C:\Users\Anastasia\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages
Requires: contourpy, cycler, fonttools, kiwisolver, numpy, packaging, pillow, pyparsing, python-dateutil
Required-by:
```

Список файлов пакета:
```
C:\Users\Anastasia>pip show -f matplotlib
Files:
  __pycache__\pylab.cpython-314.pyc
  matplotlib-3.11.2.dist-info\INSTALLER
  matplotlib-3.11.2.dist-info\LICENSE
  matplotlib-3.11.2.dist-info\METADATA
  matplotlib-3.11.2.dist-info\RECORD
  matplotlib-3.11.2.dist-info\REQUESTED
  matplotlib-3.11.2.dist-info\WHEEL
  matplotlib\__init__.py
  matplotlib\__init__.pyi
  matplotlib\__pycache__\__init__.cpython-314.pyc
  matplotlib\__pycache__\_afm.cpython-314.pyc
  matplotlib\__pycache__\_animation_data.cpython-314.pyc
  matplotlib\__pycache__\_blocking_input.cpython-314.pyc
  matplotlib\__pycache__\_cm.cpython-314.pyc

.......................................


  mpl_toolkits\mplot3d\tests\__init__.py
  mpl_toolkits\mplot3d\tests\__pycache__\__init__.cpython-314.pyc
  mpl_toolkits\mplot3d\tests\__pycache__\conftest.cpython-314.pyc
  mpl_toolkits\mplot3d\tests\__pycache__\test_art3d.cpython-314.pyc
  mpl_toolkits\mplot3d\tests\__pycache__\test_axes3d.cpython-314.pyc
  mpl_toolkits\mplot3d\tests\__pycache__\test_legend3d.cpython-314.pyc
  mpl_toolkits\mplot3d\tests\conftest.py
  mpl_toolkits\mplot3d\tests\test_art3d.py
  mpl_toolkits\mplot3d\tests\test_axes3d.py
  mpl_toolkits\mplot3d\tests\test_legend3d.py
  pylab.py
```

Основные элементы содержимого файла со служебной информацией:
```
Metadata-Version	- версия формата самого файла метаданных
Name	- имя пакета
Version	- версия пакета
Summary	- краткое описание
Home-page / Project-URL	- ссылки на сайт, репозиторий, документацию, трекер ошибок
Author	- автор 
License	- лицензия
Requires-Python	- поддерживаемые версии Python
Requires-Dist	- зависимости с ограничениями версий и условиями 
Provides-Extra	- необязательные группы зависимостей
Classifier	- классификаторы PyPI: ОС, версии Python, тематика, лицензия
```

Как получить пакет без менеджера пакетов:
```
C:\Users\Anastasia>git clone https://github.com/matplotlib/matplotlib.git
Cloning into 'matplotlib'...
remote: Enumerating objects: 357975, done.
remote: Counting objects: 100% (1417/1417), done.
remote: Compressing objects: 100% (759/759), done.
remote: Total 357975 (delta 1155), reused 665 (delta 658), pack-reused 356558 (from 4)
Receiving objects: 100% (357975/357975), 481.35 MiB | 8.72 MiB/s, done.
Resolving deltas: 100% (247472/247472), done.
Updating files: 100% (4595/4595), done.

C:\Users\Anastasia>cd matplotlib

C:\Users\Anastasia\matplotlib>git tag --list "v3.*"
v3.0.0
v3.0.0rc1
v3.0.0rc2
v3.0.1
v3.0.2
v3.0.3
v3.1.0
v3.1.0rc1
v3.1.0rc2
v3.1.1
...........

git checkout <v3.1.0>
```


## Задача 2

Вывести служебную информацию о пакете express (JavaScript). Разобрать основные элементы содержимого файла со служебной информацией из пакета. Как получить пакет без менеджера пакетов, прямо из репозитория?

## Задача 3

Сформировать graphviz-код и получить изображения зависимостей matplotlib и express.

## Задача 4

**Следующие задачи можно решать с помощью инструментов на выбор:**

* Решатель задачи удовлетворения ограничениям (MiniZinc).
* SAT-решатель (MiniSAT).
* SMT-решатель (Z3).

Изучить основы программирования в ограничениях. Установить MiniZinc, разобраться с основами его синтаксиса и работы в IDE.

Решить на MiniZinc задачу о счастливых билетах. Добавить ограничение на то, что все цифры билета должны быть различными (подсказка: используйте all_different). Найти минимальное решение для суммы 3 цифр.

## Задача 5

Решить на MiniZinc задачу о зависимостях пакетов для рисунка, приведенного ниже.

![](images/pubgrub.png)

## Задача 6

Решить на MiniZinc задачу о зависимостях пакетов для следующих данных:

```
root 1.0.0 зависит от foo ^1.0.0 и target ^2.0.0.
foo 1.1.0 зависит от left ^1.0.0 и right ^1.0.0.
foo 1.0.0 не имеет зависимостей.
left 1.0.0 зависит от shared >=1.0.0.
right 1.0.0 зависит от shared <2.0.0.
shared 2.0.0 не имеет зависимостей.
shared 1.0.0 зависит от target ^1.0.0.
target 2.0.0 и 1.0.0 не имеют зависимостей.
```

## Задача 7

Представить задачу о зависимостях пакетов в общей форме. Здесь необходимо действовать аналогично реальному менеджеру пакетов. То есть получить описание пакета, а также его зависимости в виде структуры данных. Например, в виде словаря. В предыдущих задачах зависимости были явно заданы в системе ограничений. Теперь же систему ограничений надо построить автоматически, по метаданным.

## Полезные ссылки

Semver: https://devhints.io/semver

Удовлетворение ограничений и программирование в ограничениях: http://intsys.msu.ru/magazine/archive/v15(1-4)/shcherbina-053-170.pdf

Скачать MiniZinc: https://www.minizinc.org/software.html

Документация на MiniZinc: https://www.minizinc.org/doc-2.5.5/en/part_2_tutorial.html

Задача о счастливых билетах: https://ru.wikipedia.org/wiki/%D0%A1%D1%87%D0%B0%D1%81%D1%82%D0%BB%D0%B8%D0%B2%D1%8B%D0%B9_%D0%B1%D0%B8%D0%BB%D0%B5%D1%82
