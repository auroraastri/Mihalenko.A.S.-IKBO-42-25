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

git checkout v3.1.0
```


## Задача 2

Вывести служебную информацию о пакете express (JavaScript). Разобрать основные элементы содержимого файла со служебной информацией из пакета. Как получить пакет без менеджера пакетов, прямо из репозитория?

Служебная информация о пакете:
```
C:\Users\Anastasia>npm view express

express@5.2.1 | MIT | deps: 28 | versions: 289
Fast, unopinionated, minimalist web framework
https://expressjs.com/

keywords: express, framework, sinatra, web, http, rest, restful, router, app, api

dist
.tarball: https://registry.npmjs.org/express/-/express-5.2.1.tgz
.shasum: 8f21d15b6d327f92b4794ecf8cb08a72f956ac04
.integrity: sha512-hIS4idWWai69NezIdRt2xFVofaF4j+6INOpJlVOLDO8zXGpUVEVzIYk12UUi2JzjEzWL3IOAxcTubgz9Po0yXw==
.unpackedSize: 75.4 kB

dependencies:
qs: ^6.14.0, depd: ^2.0.0, etag: ^1.8.1, once: ^1.4.0, send: ^1.1.0, vary: ^1.1.2, debug: ^4.4.0, fresh: ^2.0.0, cookie: ^0.7.1, router: ^2.2.0, accepts: ^2.0.0, type-is: ^2.0.1, parseurl: ^1.3.3, statuses: ^2.0.1, encodeurl: ^2.0.0, mime-types: ^3.0.0, proxy-addr: ^2.0.7, body-parser: ^2.2.1, escape-html: ^1.0.3, http-errors: ^2.0.0, on-finished: ^2.4.1, content-type: ^1.0.5, finalhandler: ^2.1.0, range-parser: ^1.2.1
(...and 4 more.)

maintainers:
- wesleytodd <wes@wesleytodd.com>
- jonchurch <npm@jonchurch.com>
- ctcpip <c@labsector.com>
- ulisesgascon <ulisesgascondev@gmail.com>
- sheplu <jean.burellier@gmail.com>

dist-tags:
latest: 5.2.1
latest-4: 4.22.3

published 10 months ago by jonchurch <npm@jonchurch.com>
```
Также можно получить и более расширенную версию:
```
C:\Users\Anastasia>npm view express --json
{
  "_id": "express@5.2.1",
  "_rev": "4391-d323566757f92741b5209ac354c093b3",
  "name": "express",
  "dist-tags": {
    "latest": "5.2.1",
    "latest-4": "4.22.3"
  },
  "versions": [
    "0.14.0",
    "0.14.1",
    "1.0.0-beta",

................

  "_npmOperationalInternal": {
    "tmp": "tmp/express_5.2.1_1764622183077_0.4726542587013707",
    "host": "s3://npm-registry-packages-npm-production"
  }
}
```
Основные элементы содержимого файла со служебной информацией:
```
name	- имя пакета
version	- версия пакета
description	- краткое описание
main	- точка входа: файл, который загружается при подключении пакета
dependencies	- зависимости времени выполнения с диапазонами версий
devDependencies	- зависимости для разработки и тестирования
engines	- поддерживаемые версии Node.js
scripts	- команды для тестов и сборки (например, npm test)
files	- какие файлы входят в публикуемый пакет
repository	- адрес репозитория
license	- лицензия
```
Как получить пакет без менеджера пакетов:
```
C:\Users\Anastasia>git clone https://github.com/expressjs/express.git
Cloning into 'express'...
remote: Enumerating objects: 33588, done.
remote: Counting objects: 100% (6/6), done.
remote: Compressing objects: 100% (6/6), done.
remote: Total 33588 (delta 1), reused 0 (delta 0), pack-reused 33582 (from 2)
Receiving objects: 100% (33588/33588), 9.77 MiB | 7.81 MiB/s, done.
Resolving deltas: 100% (19105/19105), done.
```


## Задача 3

Сформировать graphviz-код и получить изображения зависимостей matplotlib и express.

Код на языке Питон для решения задачи:
```
from importlib.metadata import requires, PackageNotFoundError
from packaging.requirements import Requirement

def deps(name):
    try:
        reqs = requires(name) or []
    except PackageNotFoundError:
        return []
    out = set()
    for r in reqs:
        req = Requirement(r)
        if req.marker and not req.marker.evaluate({"extra": ""}):
            continue  
        out.add(req.name.lower())
    return sorted(out)

edges, seen, stack = [], set(), ["matplotlib"]
while stack:
    p = stack.pop()
    if p in seen:
        continue
    seen.add(p)
    for d in deps(p):
        edges.append((p, d))
        stack.append(d)

with open("matplotlib.dot", "w") as f:
    f.write("digraph G {\n  rankdir=LR;\n")
    for a, b in edges:
        f.write(f'  "{a}" -> "{b}";\n')
    f.write("}\n")
```
Код на языке Джава для решения задачи:
```
const fs = require('fs');
const path = require('path');
 
const seen = new Set();
const edges = [];
 
function walk(name) {
  if (seen.has(name)) return;
  seen.add(name);
  const f = path.join('node_modules', name, 'package.json');
  if (!fs.existsSync(f)) return;
  const deps = Object.keys(JSON.parse(fs.readFileSync(f)).dependencies || {});
  for (const d of deps) {
    edges.push([name, d]);
    walk(d);
  }
}
 
walk('express');
 
let s = 'digraph G {\n  rankdir=LR;\n';
for (const [a, b] of edges) s += `  "${a}" -> "${b}";\n`;
fs.writeFileSync('express.dot', s + '}\n');
```

Получение изображений:
```
C:\Users\Anastasia>python deps_py.py
C:\Users\Anastasia>dot -Tpng matplotlib.dot -o matplotlib.png

C:\Users\Anastasia>node deps_js.js
C:\Users\Anastasia>dot -Tpng express.dot -o express.png
```
Результат:
<img width="599" height="124" alt="{49A9E3FA-AF52-4114-8157-F4848D358CB9}" src="https://github.com/user-attachments/assets/f5fe4e4f-7ab2-4677-85b2-3bf965f49977" />
<img width="821" height="1167" alt="{0886ADE4-8DD9-429E-B668-68F263EF848B}" src="https://github.com/user-attachments/assets/a0bf3e51-ff50-487c-9af6-b478904bcd73" />
<img width="1581" height="1182" alt="{BBEC7F82-9C2F-427C-B1E7-0F3C0F9DA3DB}" src="https://github.com/user-attachments/assets/01c07bef-b6d8-46fc-9161-41e484051738" />

## Задача 4

**Следующие задачи можно решать с помощью инструментов на выбор:**

* Решатель задачи удовлетворения ограничениям (MiniZinc).
* SAT-решатель (MiniSAT).
* SMT-решатель (Z3).

Изучить основы программирования в ограничениях. Установить MiniZinc, разобраться с основами его синтаксиса и работы в IDE.

Решить на MiniZinc задачу о счастливых билетах. Добавить ограничение на то, что все цифры билета должны быть различными (подсказка: используйте all_different). Найти минимальное решение для суммы 3 цифр.

Код на MiniZinc для решения задачи:
```
include "globals.mzn";

array[1..6] of var 0..9: d;
var 0..27: s = d[1] + d[2] + d[3];

constraint s = d[4] + d[5] + d[6];
constraint all_different(d);

solve minimize s;
output ["билет: \(d), сумма трёх цифр = \(s)\n"];
```
Вывод:
<img width="540" height="161" alt="{5C46DBF9-FD34-4510-A148-252CC56C59FF}" src="https://github.com/user-attachments/assets/4d32f567-0021-45c7-a235-74748abd7a7b" />

## Задача 5

Решить на MiniZinc задачу о зависимостях пакетов для рисунка, приведенного ниже.

![](images/pubgrub.png)
Код на MiniZinc для решения задачи:
```
var 1..6: menu;
var 1..5: dropdown;
var 1..2: icons;

constraint icons = 1;

constraint menu >= 2 -> dropdown >= 2;

constraint menu = 1 -> dropdown = 1;

constraint dropdown >= 2 -> icons = 2;

solve maximize menu * 100 + dropdown * 10 + icons;

output [
  "menu = ", show(["1.0.0","1.1.0","1.2.0","1.3.0","1.4.0","1.5.0"][fix(menu)]), "\n",
  "dropdown = ", show(["1.8.0","2.0.0","2.1.0","2.2.0","2.3.0"][fix(dropdown)]), "\n",
  "icons = ", show(["1.0.0","2.0.0"][fix(icons)]), "\n"
```
Вывод:
<img width="324" height="156" alt="{6F3FB4FD-8F10-4F9D-A2AD-7AE58D712B3D}" src="https://github.com/user-attachments/assets/1b3df868-8905-432b-9cdd-ded78ac78b7b" />

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
Код на MiniZinc для решения задачи:
```
var 0..2: foo;
var 0..1: left;      
var 0..1: right;     
var 0..2: shared;    
var 0..2: target;    

constraint foo >= 1;         
constraint target = 2;        

constraint foo = 2 -> (left = 1 /\ right = 1);
constraint left = 1 -> shared in {1, 2};
constraint right = 1 -> shared = 1;
constraint shared = 1 -> target = 1;

solve satisfy;
output ["foo=\(foo) left=\(left) right=\(right) shared=\(shared) target=\(target)\n"];
```
Вывод:
<img width="420" height="90" alt="{6933E20D-99BF-4454-9DA7-CDCBAFF88927}" src="https://github.com/user-attachments/assets/c6044d89-6a2b-4d6e-bc1b-c85ea118981c" />
## Задача 7

Представить задачу о зависимостях пакетов в общей форме. Здесь необходимо действовать аналогично реальному менеджеру пакетов. То есть получить описание пакета, а также его зависимости в виде структуры данных. Например, в виде словаря. В предыдущих задачах зависимости были явно заданы в системе ограничений. Теперь же систему ограничений надо построить автоматически, по метаданным.

Код на языке Питон для решения задачи:
```
import re, subprocess, tempfile

repo = {
    "root":   {"1.0.0": {"foo": "^1.0.0", "target": "^2.0.0"}},
    "foo":    {"1.1.0": {"left": "^1.0.0", "right": "^1.0.0"}, "1.0.0": {}},
    "left":   {"1.0.0": {"shared": ">=1.0.0"}},
    "right":  {"1.0.0": {"shared": "<2.0.0"}},
    "shared": {"2.0.0": {}, "1.0.0": {"target": "^1.0.0"}},
    "target": {"2.0.0": {}, "1.0.0": {}},
}

def parse(v): return tuple(int(x) for x in v.split("."))

def satisfies(ver, spec):
    v = parse(ver)
    for part in spec.split(","):
        op, base = re.match(r"\s*(\^|~|>=|<=|>|<|=)?\s*(\d+\.\d+\.\d+)", part).groups()
        op, b = op or "=", parse(base)
        if op == "^":
            up = (b[0]+1, 0, 0) if b[0] else (0, b[1]+1, 0) if b[1] else (0, 0, b[2]+1)
            ok = b <= v < up
        elif op == "~": ok = b <= v < (b[0], b[1]+1, 0)
        elif op == ">=": ok = v >= b
        elif op == "<=": ok = v <= b
        elif op == ">":  ok = v > b
        elif op == "<":  ok = v < b
        else:            ok = v == b
        if not ok:
            return False
    return True

vers = {p: sorted(vs, key=parse) for p, vs in repo.items()}

lines = [f"var 0..{len(vs)}: {p};" for p, vs in vers.items()]
lines.append("constraint root = 1;")
for p, vs in vers.items():
    for i, v in enumerate(vs, 1):
        for dep, spec in repo[p][v].items():
            ok = [j for j, dv in enumerate(vers[dep], 1) if satisfies(dv, spec)]
            allowed = "{" + ",".join(map(str, ok)) + "}" if ok else "{}"
            lines.append(f"constraint {p} = {i} -> {dep} in {allowed};")
lines.append("solve satisfy;")

with tempfile.NamedTemporaryFile("w", suffix=".mzn", delete=False) as f:
    f.write("\n".join(lines))
print(open(f.name).read())
print(subprocess.run(["minizinc", f.name], capture_output=True, text=True).stdout)
```
Вывод в командной строке:
```
C:\Users\Anastasia>python solve_deps.py
var 0..1: root;
var 0..2: foo;
var 0..1: left;
var 0..1: right;
var 0..2: shared;
var 0..2: target;
constraint root = 1;
constraint root = 1 -> foo in {1,2};
constraint root = 1 -> target in {2};
constraint foo = 2 -> left in {1};
constraint foo = 2 -> right in {1};
constraint left = 1 -> shared in {1,2};
constraint right = 1 -> shared in {1};
constraint shared = 1 -> target in {1};
solve satisfy;
```
## Полезные ссылки

Semver: https://devhints.io/semver

Удовлетворение ограничений и программирование в ограничениях: http://intsys.msu.ru/magazine/archive/v15(1-4)/shcherbina-053-170.pdf

Скачать MiniZinc: https://www.minizinc.org/software.html

Документация на MiniZinc: https://www.minizinc.org/doc-2.5.5/en/part_2_tutorial.html

Задача о счастливых билетах: https://ru.wikipedia.org/wiki/%D0%A1%D1%87%D0%B0%D1%81%D1%82%D0%BB%D0%B8%D0%B2%D1%8B%D0%B9_%D0%B1%D0%B8%D0%BB%D0%B5%D1%82
