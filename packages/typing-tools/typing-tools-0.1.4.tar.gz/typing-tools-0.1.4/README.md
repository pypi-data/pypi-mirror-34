# Typing Tools
This is a library for Python 3.6+ that adds some dict-like classes supporting attributes like in JavaScript' objects. 

This module provides 2 classes - _DictStruct_ and _AssignmentSupportable_.
Inherit your class from it and all the featues will enable.
The example below for more details.

### Example Usage

##### DictStruct
Let's declare a _Circle_ and a _Point_ classes:
```code=python
import json
from typing import List, Dict, Tuple
from typing_tools import DictStruct, AssignmentSupportable

class Point(DictStruct):
    x: int
    y: int

class Circle(DictStruct):
    r: int
    c: Point
```

Let's create a Circle object.
It is both a dictionary and a namespace, so the `.attribute` and `['attribute']` calls are allowed.
```code=python
_point_dict = { 'x': 5, 'y': 18 }
_circle_dict = { 'c': _point_dict, 'r': 6 }
p = Point(_point_dict)
o = Circle(_circle_dict)
```
Note that this could also work:
`o = Circle(r=4, c=Point(x=2, y=15))`

And, now, print it:
```code=python
print(f"Circle is: {o}")
print(f"Circle Radius is: {o.r}")
print(f"Circle Center is: {o.c}")
print(f"Circle Center X is: {o.c.x}")
print(f"Circle Center Y is: {o.c.x}")
print(json.dumps(o))
```

This will print:
```
Circle is: {'r': 4, 'c': {'x': 2, 'y': 15}}
Circle Radius is: 4
Circle Center is: {'x': 2, 'y': 15}
Circle Center X is: 2
Circle Center Y is: 2
{"r": 4, "c": {"x": 2, "y": 15}}
```

It also supports default values and methods:
```code=python
class PointWithDefaults(DictStruct):
    x: int = 0
    y: int = 0
    
    def print_me(self):
        print(f"PointWithDefaults is: {self}")
        print(f"PointWithDefaults X is: {self.x} and {self['x']} and {self.get('x')}")
        print(f"PointWithDefaults Y is: {self.y} and {self['y']} and {self.get('y')}")

...

p = PointWithDefaults(y=6)
p.print_me()

p.x = 8
p.y = 4
p.print_me()
print()
```

Note that methods are not included in the dictionary.
Output:
```
PointWithDefaults is: {'y': 6, 'x': 0}
PointWithDefaults X is: 0 and 0 and 0
PointWithDefaults Y is: 6 and 6 and 6
PointWithDefaults is: {'y': 4, 'x': 8}
PointWithDefaults X is: 8 and 8 and 8
PointWithDefaults Y is: 4 and 4 and 4
```
##### AssignmentSupportable
Okay, i got it. But how could I use it in my custom classes?
Just add a AssignmentSupportable to its parents! 
```code=python
class Figure(AssignmentSupportable):
    points: List[Point]

class NamedFigure(AssignmentSupportable):
    points_dict: Dict[str, Point]
```

```code=python
f = Figure()
f.points = [{ 'x': 5, 'y': 18 }, Point(x=2, y=15), dict(x=1, y=22)]
print(f"Figure is: {f}")
print(f"Figure Points are: {f.points}")
for i, _p in enumerate(f.points):
    print(f"Figure Point #{i+1} is: {_p}")
    print(f"Figure Point #{i+1} X is: {_p.x}")
    print(f"Figure Point #{i+1} Y is: {_p.y}")
print()

f2 = NamedFigure()
f2.points_dict = { 'A': { 'x': 5, 'y': 18 }, 'PointB': Point(x=2, y=15), 'p.C': dict(x=1, y=22) }
print(f"NamedFigure is: {f2}")
print(f"NamedFigure Points are: {f2.points_dict}")
for _name, _p in f2.points_dict.items():
    print(f"NamedFigure Point '{_name}' is: {_p}")
    print(f"NamedFigure Point '{_name}' X is: {_p.x}")
    print(f"NamedFigure Point '{_name}' Y is: {_p.y}")
print()
```
Output:
```
Figure is: <__main__.Figure object at 0x7fe838cf09e8>
Figure Points are: [{'x': 5, 'y': 18}, {'x': 2, 'y': 15}, {'x': 1, 'y': 22}]
Figure Point #1 is: {'x': 5, 'y': 18}
Figure Point #1 X is: 5
Figure Point #1 Y is: 18
Figure Point #2 is: {'x': 2, 'y': 15}
Figure Point #2 X is: 2
Figure Point #2 Y is: 15
Figure Point #3 is: {'x': 1, 'y': 22}
Figure Point #3 X is: 1
Figure Point #3 Y is: 22

NamedFigure is: <__main__.NamedFigure object at 0x7fe838cf0a58>
NamedFigure Points are: {'A': {'x': 5, 'y': 18}, 'PointB': {'x': 2, 'y': 15}, 'p.C': {'x': 1, 'y': 22}}
NamedFigure Point 'A' is: {'x': 5, 'y': 18}
NamedFigure Point 'A' X is: 5
NamedFigure Point 'A' Y is: 18
NamedFigure Point 'PointB' is: {'x': 2, 'y': 15}
NamedFigure Point 'PointB' X is: 2
NamedFigure Point 'PointB' Y is: 15
NamedFigure Point 'p.C' is: {'x': 1, 'y': 22}
NamedFigure Point 'p.C' X is: 1
NamedFigure Point 'p.C' Y is: 22
```
