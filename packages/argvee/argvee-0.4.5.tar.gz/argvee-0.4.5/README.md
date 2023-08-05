argvee
======

Easily parse command line argument by virtue of the functions defined in 
the module. Simplifies command line argument parsing for positional args,
optional args, integer/float types, lists of args.

All kwargs become optional args, True/False default values will make them 
flags. It will create the one letter options on its own (`-d/--debug`), 
using a capital letter if it already exists (`-d/--debug -D/--dupitydoo`)

For kwargs with default values of type boolean, int, float, or list, it 
will have special behavior. booleans become flags which flips the default
value if passed in, ints or floats are type checked and passed in as that
type, and lists will have 0 or more possible arguments (`nargs='*'`). For 
varargs like *args, it will be one or more arguments (`nargs='+'`), but as 
it shows above, you can't use varargs (`*args`) and keyword args (`--debug`)
together. You would need to specify `args=[]`

```python
from argvee import Application
app = Application()

@app.cmd
def add(a, b):
    ''' Add two numbers '''
    print('%s + %s = %s' % (a, b, int(a) + int(b)))

@app.cmd
def add_int_float(a=0, b=0.0):
    ''' Enforce type '''
    print('%d + %f = %f' % (a, b, a+b))

# $ python test.py add_int_float 1 2.5
# 1 + 2.5 = 3.5

@app.cmd
def someflags(debug=False, verbose=True):
    ''' I have flags '''
    print('debug = %s' % debug)
    print('verbose = %s' % verbose)

# $ python test.py someflags
# debug = False
# verbose = True

# $ python test.py someflags -d --verbose
# debug = True
# verbose = False

@app.cmd
def sayhello(names=[]):
    for name in names:
        print('Hello, %s!' % name)

# $ python test.py sayhello -n foo bar baz
# Hello, foo!
# Hello, bar!
# Hello, baz!

# You can even use variable number of arguments.
@app.cmd
def sayhello2(*names):
    for name in names:
        print('Hello, %s!' % name)

# Unimplemented if you combine *args with kwargs like debug=True
def bad_args(alpha, beta=5, *names): ...
# Instead, do this:
def bad_args(alpha, beta=5, names=[])
# behavior will be as you'd expect, except nargs='*' not '+'

# Start argument parsing and run the command with:
app.run()

# Get the function return value with
status = app.run()

```

```bash
# docstring goes in help for command
$ python test.py -h
usage: test.py [-h] {someflags,add,sayhello} ...

positional arguments:
  {someflags,add,sayhello}
    someflags           I have flags
    add                 Add two numbers
    sayhello
    sayhello2

optional arguments:
  -h, --help            show this help message and exit

# debug and verbose are kwargs
# Any kwarg with default True/False becomes flags
$ python test.py someflags -h
usage: test.py someflags [-h] [--debug] [--verbose]

optional arguments:
  -h, --help  show this help message and exit
  --debug
  --verbose

$ python test.py someflags
debug = False
verbose = True

$ python test.py someflags --debug
debug = True
verbose = True

# Positional arg with kwargs
$ python test.py sayhello
usage: test.py sayhello [-h] [--debug] name
test.py sayhello: error: too few arguments
fusion@ultralisk:~$ python test.py sayhello joe
Hello, joe!
fusion@ultralisk:~$ python test.py sayhello joe --debug
In debug mode
Hello, joe!
done
```
