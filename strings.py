Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> k="12345678"
>>> k.count("1",5,8)
0
>>> len(k)
8
>>> k.count("1",5,10)
0
>>> k.count("1",,10)
SyntaxError: invalid syntax
>>> k.count("1",int(input()),int(input()))
1
5
0
>>> 
KeyboardInterrupt
>>> k.count("1",int(input()),int(input()))
0
1
1
>>> k.count("1",int(input()),int(input()))
0
0
0
>>> k.endswith("8",5)
True
>>> k.endswith("7",5,7)
True
>>> k.endswith("7",5,8)
False
>>> k.expandtabs()
'12345678'
>>> k.expandtabs(/,9)
SyntaxError: invalid syntax
>>> k.expandtabs(tabsize=8)
'12345678'
>>> s.find('1',0,5)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    s.find('1',0,5)
NameError: name 's' is not defined
>>> k.find('1',0,5)
0
>>> k.find('3',0,5)
2
>>> s.find('1',1,5)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    s.find('1',1,5)
NameError: name 's' is not defined
>>> k.find('9',0,5)
-1
>>> k.alunum()
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    k.alunum()
AttributeError: 'str' object has no attribute 'alunum'
>>> k.isalnum()
True
>>> k=1234
>>> k.isalnum()
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    k.isalnum()
AttributeError: 'int' object has no attribute 'isalnum'
>>> k='1'
>>> k.isalnum()
True
>>> k.isalpha()
False
>>> k='@'
>>> k.isascii()
True
>>> k='12'
>>> k.isdecimal()
True
>>> k='12.00'
>>> k.isdecimal()
False
>>> k='str'
>>> k.isidentifier()
True
>>> k='134'
>>> k.isidentifier()
False
>>> k='\n'
>>> k.isprintable()
False
>>> k='\'
SyntaxError: EOL while scanning string literal
>>> k='\''
>>> k.isprintable()
True
>>> k.isspace()
False
>>> k='1 23441 12'
>>> k.isspace()
False
>>> k='1 2'
>>> k.isspace()
False
>>> k=' '
>>> k.isspace()
True
>>> k='"
SyntaxError: EOL while scanning string literal
>>> k=""
>>> k.isspace()
False
>>> k='abcd'
>>> k.tittle()
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    k.tittle()
AttributeError: 'str' object has no attribute 'tittle'
>>> k.istittle()
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    k.istittle()
AttributeError: 'str' object has no attribute 'istittle'
>>> k.istitle()
False
>>> "Abcd".istitle()
True
>>> "AVDF".istitle()
False
>>> str='123'
>>> str.ljust(20,1)
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    str.ljust(20,1)
TypeError: The fill character must be a unicode character, not int
>>> str1='123'
>>> str1.ljust(20,'1')
'12311111111111111111'
>>> str1.ljust(3,'1')
'123'
>>> str1.partition(1)
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    str1.partition(1)
TypeError: must be str, not int
>>> str1='abcdefgh'
>>> str1.partition(2)
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    str1.partition(2)
TypeError: must be str, not int
>>> str1.partition('c')
('ab', 'c', 'defgh')
>>> k='1111111'
>>> k.rfind('1')
6
>>> k.just(20,2)
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    k.just(20,2)
AttributeError: 'str' object has no attribute 'just'
>>> k.rjust(20,2)
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    k.rjust(20,2)
TypeError: The fill character must be a unicode character, not int
>>> k.just(20,'2')
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    k.just(20,'2')
AttributeError: 'str' object has no attribute 'just'
>>> k.rjust(20,'2')
'22222222222221111111'
>>> str1='abcdefcgh'
>>> str1.partition('c')
('ab', 'c', 'defcgh')
>>> str1.rpartition('c')
('abcdef', 'c', 'gh')
>>> str1.split('c')
['ab', 'def', 'gh']
>>> str1.split('c',5)
['ab', 'def', 'gh']
>>> str1.split('c',2)
['ab', 'def', 'gh']
>>> str1.rsplit('c',5)
['ab', 'def', 'gh']
>>> str1.rsplit('c',1)
['abcdef', 'gh']
>>> str1.splitlines('c')
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    str1.splitlines('c')
TypeError: an integer is required (got type str)
>>> str1.splitlines(2)
['abcdefcgh']
>>> str1.splitlines(1)
['abcdefcgh']
>>> str1.splitlines(0)
['abcdefcgh']
>>> str1.splitlines(10)
['abcdefcgh']
>>> str1.title()
'Abcdefcgh'
>>> sr1.translate()
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    sr1.translate()
NameError: name 'sr1' is not defined
>>> st1.translate()
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    st1.translate()
NameError: name 'st1' is not defined
>>> str1.translate()
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    str1.translate()
TypeError: translate() takes exactly one argument (0 given)
>>> sr1.translate(1)
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    sr1.translate(1)
NameError: name 'sr1' is not defined
>>> str1.translate(1)
Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    str1.translate(1)
TypeError: 'int' object is not subscriptable
>>> str1.translate('12')
'abcdefcgh'
>>> str1.translate('c')
'abcdefcgh'
>>> str1.translate('c','m')
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    str1.translate('c','m')
TypeError: translate() takes exactly one argument (2 given)
>>> str1.zfill(20)
'00000000000abcdefcgh'
>>> 
