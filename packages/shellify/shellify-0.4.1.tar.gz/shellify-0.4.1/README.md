shellify
========

Turn any python module into a shell!

Credit to reddit user /u/zahlman for the idea of creating a cmd.Cmd shell
dynamically with decorators.

```python
from shellify import Shell

shell = Shell('MyShell', version='1.0.1')

@shell
def say_hi(name):
    print('Hello, %s!' % name)

@shell
def add_floats(float1_f, float2_f):
    ''' Docstring goes in help string for the command
    _f appended will enforce type to be float
    _i/_n enforce int type, and _b boolean which coerces "no,nil,none,false,0' into False and the rest, True
    '''
    print float1_f + float2_f

@shell
def kwarg_args(foo, bar="barrr", baz="bazzz"):
    ''' to run this, you run `kwarg_arg 100 bar=something baz=somethingelse`
    You can omit bar and/or baz but you must include foo.
    '''
    print foo,bar,baz

@shell.json
def even_json(works, foo="bar", baz_f=1.0):
    ''' In JSON style parsing, it will take comma delimited args with
    an optional last argument of a json dictionary.
    Anything in "quotes" is a string like JSON, ints and floats work 
    as you would expect.
    '''
    print works, foo, baz_f

# Don't forget to run it
shell.run()
```

```
MyShell v1.0.1
> say_hi World
Hello, World!
> say_hi "World! Quotes work"
Hello, World! Quotes work!
> add_floats 1.0
Requires more arguments: add_floats float1_f float2_f
> add_floats 1.0 2
3.0
> add_floats 1.0 f
Arguments with _i,_n,_f are typed: add_floats float1_f float2_f
> kwarg_args zzz
zzz barrr bazzz
> kwarg_args zzz bar=bor baz=boz
zzz bor boz
> even_json "this works", {"foo": "boar", "baz_f": 5.0}
this works boar 5.0
```
