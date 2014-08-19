## Slow Loris

> A clone of DIY-LISP. The goal is to learn.

### What Slow Loris Is

A relatively simple, but neat language. Features include:

- A handful of datatypes (integers, booleans and symbols)
- Variables
- First class functions with lexical scoping
- A nice, homemade-quality feeling

Initially, it will *not* have:

- A proper type system
- Error handling
- Good performance
- And much, much more

The syntax is that of the languages in the [Lisp family](parts/language.md):

```lisp
(def fact 
    ;; Factorial function
    (lambda (n) 
        (if (eq n 0) 
            1 ; Factorial of 0 is 1
            (* n (fact (- n 1))))))

;; When parsing the file, the last statement is returned
(fact 5)
```

### Prerequisites

Before we get started, make sure you have installed [Python](http://www.python.org/), [Pip](https://pypi.python.org/pypi/pip), and Nose (pip install nose). 
*For long-term stabilibility, the language is based on Python 2.7, as the Python 3.x flavors are being continuously improved.*

### API Documentation

A full guide to this little language can be found in the API:

- [Part 1: Parsing Slow Loris](parts/1.md)
- [Part 2: Evaluating Simple Expressions](parts/2.md)
- [Part 3: Evaluating Complex Expressions](parts/3.md)
- [Part 4: Variables](parts/4.md)
- [Part 5: Functions](parts/5.md)
- [Part 6: Lists](parts/6.md)
- [Part 7: The Standard Library](parts/7.md)
