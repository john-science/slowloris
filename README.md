## Slow Loris

> A simple, interpreted LISP, written in Python.

### What Slow Loris Is

A simple, but fun language. Features include:

- A handful of data types (integers, floats, booleans, strings, and symbols)
- Variables
- First class functions with lexical scoping
- Basic error handling
- A nice, homemade-quality feeling

Initially, it will *not* have:

- A proper type system
- Good performance
- keyword function arguments
- And much, much more

The [syntax](parts/language.md) is in the Lisp family:

```lisp
(def fact 
    # Factorial function
    (lambda (n) 
        (if (eq n 0) 
            1 # Factorial of 0 is 1
            (* n (fact (- n 1))))))

# When parsing the file, the last statement is returned
(fact 5)
```

### Prerequisites

To use Slow Loris, make sure you have installed [Python](http://www.python.org/), [Pip](https://pypi.python.org/pypi/pip), and Nose (pip install nose). 
*For long-term stabilibility, the language is based on Python 2.7. No other Python version will be tested.*

### API Documentation

The full documentation to this little language can be found here:

- [Part 1: Parsing Slow Loris](parts/1.md)
- [Part 2: Evaluating Slow Loris](parts/2.md)
- [Part 3: REPL](parts/3.md)
- [Part 4: Variables and Types](parts/4.md)
- [Part 5: Functions](parts/5.md)
- [Part 6: Lists](parts/6.md)
- [Part 7: The Standard Library](parts/7.md)
