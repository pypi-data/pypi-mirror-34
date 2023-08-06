<p align="center">
<img src="readme_images/logo.svg"></br>
<b>S</b>mall <b>U</b>ncomplicated <b>P</b>lugin <b>E</b>xtensible <b>R</b>eliable <b>S</b>hell in <b>PY</b>thon
</p>

[![PEP8](https://img.shields.io/badge/code%20style-pep8-orange.svg)](https://www.python.org/dev/peps/pep-0008/)
[![pypiversion](https://img.shields.io/pypi/v/superspy.svg)](https://pypi.org/project/superspy/)
[![pypipythonversion](https://img.shields.io/pypi/pyversions/superspy.svg)](https://python.org)

<!---START--->

<!---PYPI
![logo](https://raw.githubusercontent.com/Kamik423/superspy/master/readme_images/logo.svg?sanitize=true)

**S**mall **U**ncomplicated **P**lugin **E**xtensible **R**eliable **S**hell in **PY**thon
PYPI--->

# About

**`SUPERSPY`** is a implementation of a shell and programming language written completely in Python. It is meant as a replacement of the builtin `cmd` module which allows scripting and advanced flow control functions.

```python
[SUPERSPY DEMO] >>> i = 4 + 3
[SUPERSPY DEMO] >>> spam 3
SPAM
SPAM
SPAM
[SUPERSPY DEMO] >>> while i {
[SUPERSPY DEMO] >>>     printnl i
[SUPERSPY DEMO] >>>     printnl " to go: "
[SUPERSPY DEMO] >>>     joke
[SUPERSPY DEMO] >>>     i = i - 1
[SUPERSPY DEMO] >>> }
7.0 to go: Wenn ist das Nunstück git und Slotermeyer? Ja! Beiherhund das Oder die Flipperwaldt gersput!
6.0 to go: Wenn ist das Nunstück git und Slotermeyer? Ja! Beiherhund das Oder die Flipperwaldt gersput!
5.0 to go: Wenn ist das Nunstück git und Slotermeyer? Ja! Beiherhund das Oder die Flipperwaldt gersput!
4.0 to go: Wenn ist das Nunstück git und Slotermeyer? Ja! Beiherhund das Oder die Flipperwaldt gersput!
3.0 to go: Wenn ist das Nunstück git und Slotermeyer? Ja! Beiherhund das Oder die Flipperwaldt gersput!
2.0 to go: Wenn ist das Nunstück git und Slotermeyer? Ja! Beiherhund das Oder die Flipperwaldt gersput!
1.0 to go: Wenn ist das Nunstück git und Slotermeyer? Ja! Beiherhund das Oder die Flipperwaldt gersput!
```

`joke` and `spam` here are funktions easily defined in Python code:

```python
from superspy import ast, language

@language.register_function('joke', 0)
class Joke(ast.Function):
    funniest_joke_in_the_world = 'Wenn ist das Nunstück git und Slotermeyer?'\
        'Ja! Beiherhund das Oder die Flipperwaldt gersput!'
    def execute(self):
        print(self.funniest_joke_in_the_world)

@language.register_function('spam')
class Spam(ast.Function):
    def execute(self):
        for _ in range(int(self.argument.execute())):
            print('SPAM')
```

It also allows for the execution of entire scripts:

```python
printnl "COMPUTE FACTORIAL OF: "
base = getnum
base_backup = base

factorial = 1
while base {
    factorial = factorial * base
    base = base - 1
}

printnl base_backup
printnl "! = "
print factorial
```

# Getting started

Superspy is meant to, in true Python fashion, be very easy to use.

## Prerequisites

Superspy was developed in Python 3.7. Older versions cannot be guaranteed to work.

If you get it working on an older version please let me know!

## Installing

Setup manually from this repository or just type

```bash
pip3 install superspy
```

## Basic usage

To understand how to run a script from file check out the [file_factorial](examples/file_factorial.py) script and its corresponding [factorial script](examples/factorial_script.spy), that also illustrates basic language functionality.

To learn how to run an interactive shell check out the [shell_demo](examples/shell_demo.py) script, that is being exanded upon by the [plugin_demo](examples/plugin_demo.py) and its [example implementation of a plugin](examples/demo_plugins/demo_plugin.py).

### Superspy Language

Superspy is primarily a shell language, however it uses braces.
Commands can be separated by lines or semicolons.
Superspy supports **strings** and **numbers**, which are always stored as float.

**Variables** can be used in a similar way to Python:

```python
a = 5
b = 2 * a
```

Basic **Arithmetic** and **Logic** is also supported, in (mostly) the correct order of operations (see [the Bugfixes section of the Roadmap](#Roadmap):

```python
b = 2 * a - 3 / 4
c = a == 9.25
d = a != 10
```

Basic **IO** is also supported:

```python
my_num_from_input = getnum
my_str_from_input = getstr
printnl "Your inputed number was"
printnl my_num_from_input
printnl " and your string was "
print my_str_from_input
```

Here `printnl` means **Print** **N**o **L**line, since the normal `print` has a line break.
Also `dis` prints the entire token tree and should be used for debugging.

However, one of the primary reasons for Superspy's existence is the **Flow Control**:

```python
while base != 0 {
    factorial = factorial * base
    base = base - 1
}
if factorial == 120 {
    print "Your number was 5"
} else {
    print "Your number was not 5"
}
```

For further features, that are not mentioned in the (roadmap)[#Roadmap], like running scripts from a shell, please create an issue (or even a pull request)!

### Python

The way a new Ast/Interpreter is created will get further simplified in the future.

Currently you have to create a `Language` object, because a custom language might be defined.
Then a `CodeSource` object has to be defined to be created to feed that Ast lines. Those can for example come from a file, string, or shell. 
Finally an `Ast` object, that does all the parsing and interpreting has to be created and executed.

```python
from superspy import ast, code_source, language

# Run file
lang = language.SuperSpyLanguage()
source = code_source.FileSource(f'path/to/my/script.spy')
my_ast = ast.Ast(source, lang)
exit_code = my_ast.complete_run()

# Run shell
lang = language.SuperSpyLanguage(['path/to/my/plugin/folder']) # Plugin folder can be left out
source = code_source.ShellSource()
my_ast = ast.Ast(source, lang)
my_ast.error_mode = ast.ErrorMode.PRINT
exit_code = my_ast.complete_run(run_after_each_line=True)
```

## Advanced Usage

The `complete_run` method is an abstraction for something similar to this:

```python
my_ast.build_token_list()
my_ast.guess_variables()
my_ast.build_token_tree()
my_ast.interpret()
exit_code: int = my_ast.get_exit_code()
```

It can obviously be executed manually in this order and then customized any way.
Everything is open source and the source code is hopefully documented very clearly, so if there are any questions of how something is implemented by default you check out the source code.

To implement custom functions available inside the language specify a plugin search path with custom python files inside. Check out the [plugin_demo](examples/plugin_demo.py) example and its [example implementation of a plugin](examples/demo_plugins/demo_plugin.py).

```python
from superspy import language

@language.register_function('my_function_name_inside_the_shell', number_of_arguments)
class MyFunction(ast.Function):
    def execute(self):
        # Run code
```

# Rationale

This module was created because I wanted scripting functionality inside the `cmd` module, that was not there. I have also been toying around with creating my own programming language for a few years and never got around to it. But most of all I needed a distraction during the exams this year.

<!---END--->

# Roadmap

## Language

- [ ] More math functions
    - [ ] Trigonometry (`sin`, `cos`, `tan`, `atan`, ...)
    - [ ] Exponential (`pow`, `log`)
    - [ ] Constants (`e`, `tau`, `pi`, `phi`)
- [ ] More flow control
    - [ ] `elif`/`elsif`/`elseif`/`else if`
    - [ ] `for`
    - [ ] `catch`
    - [ ] `break`
- [ ] Logical operators (`and`, `or`, `xor`)
- [ ] Parentheses
- [ ] arrays
- [ ] `help`
- [ ] `script` executability
- [ ] functions

## Implementation

- [ ] Full drop in `cmd` replacement
- [ ] Single line shell creation without having to define a language and source first
- [ ] Ability to define commands in the main script before creating alanguage object

## Bugfixes

- [ ] Order of Operations: Make `3 - 1 - 1` not equal `3`.

## Other

- [ ] Integrate with
    - [ ] TravisCI
    - [ ] codecov.io
    - [ ] Read the docs
    - [ ] lgtm

# Contributing

If you want to contribute, please feel free to suggest features or implement some from the (roadmap)[#Roadmap], other ones that are still lacking, or bugfixes.

Also **please encounter any issues and bugs you might find!**

# Authors

* Currently this entire project is just by me.

# License

The project is licensed under the [MIT-License](license.md).

# Acknowledgments

* This project uses the module [PluginBase](http://pluginbase.pocoo.org) for loading language syntax python files, which makes my job so much easier.
* Thank you also to all the people who have supported me in this endeavor.

---

Thanks for reading this to the end.

*GNU Terry Pratchett*
