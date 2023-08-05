Wint - dependency injection with type hints.
============================================

[![Build Status](https://travis-ci.org/asyncee/wint.svg?branch=master)](https://travis-ci.org/asyncee/wint)
[![Coverage Status](https://coveralls.io/repos/github/asyncee/wint/badge.svg?branch=master)](https://coveralls.io/github/asyncee/wint?branch=master)

Intro
-----

Wint is a lightweight library that implements dependency injection via type hinting.

Installation
------------

Just use pip:
```
$ pip install wint
```

How it works
------------

There are a ton of approaches to DI, and this library implements only property injection.

When ``autowired`` decorator is applied then class is inspected for all
annotated properties. If property has no value, then it is replaced with ``DependencyDescriptor``.

Dependency is resolved when attribute is accessed on instantiated class instance.

This behaviour allows to resolve dependencies in lazy manner with the downside of a side effect — instance
receives a descriptor property that was not existed earlier.

Example
-------

```python
from wint import autowired, ContainerProvider


class Printer:
    """Abstract class for printing messages."""

    def print(self, message):
        raise NotImplementedError


class RealPrinter(Printer):
    """Implementation of `Printer` which uses `print` to output messages."""

    def print(self, message):
        print(message)


@autowired()
class PrintService:
    # RealPrinter will be automatically injected on property access.
    printer: Printer

    def run(self, msg):
        self.printer.print(f"{msg}, i'm running!")


if __name__ == "__main__":
    container = ContainerProvider.get()
    # Register RealPrinter as singleton implementation of Printer.
    container.register(Printer, RealPrinter())

    PrintService().run('hey')
```

```bash
$ python example.py
hey, i'm running!
```

Notes
-----
This library is built on [punq](https://github.com/bobthemighty/punq)
(MIT License) and uses it's vendored version.
