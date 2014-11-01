# Selected Examples from `Structure and Interpretation of Computer Programs`
# (A wonderful text for new software engineers, and the best way to learn a LISP.)


# Exponentiation - Simple Resursion [pg 44]
(def exp
    (lambda (b n)
        (if (= n 0)
            1
            (* b (exp b (- n 1))))))

(print "Exponent of 2 to the 4th power" '())
(print (exp 2 4) '())


# Exponentiation - Linear Iteration [pg 45]
(def expt
    (lambda (b n)
        (expt-iter b n 1)))

(def expt-iter
    (lambda (b counter product)
        (if (= counter 0)
            product
            (expt-iter b
                (- counter 1)
                (* b product)))))

(print "Exponent of 2 to the 4th power" '())
(print (expt 2 4) '())


# Euclid's Algorithm for finding Greatest Common Divisors (pg 49)

(def gcd
    (lambda (a b)
        (if (= b 0)
            a
            (gcd b (mod a b)))))

(print "Greatest Common Divisor of 360 and 153" '())
(print (gcd 360 153) '())


# Fermat's Primality Test (pg 51)

(def square
    (lambda (n)
        (* n n)))

(def expmod
    (lambda (base exp m)
        (if (= exp 0) 1
            (if (= (mod exp 2) 0)
                (mod (square (expmod base (/ exp 2) m)) m)
                (mod (* base (expmod base (- exp 1) m)) m)))))

# TODO: Move these 3 functions to std libs
# TODO: Floor/ceiling doe not case to int... I need type casting.
(def floor
    (lambda (d)
        (- d (mod d 1))))

(def ceiling
    (lambda (d)
        (if (= d (floor d)) d
            (+ d (- 1 (- d (floor d)))))))

(def randint
    (lambda (bottom top)
        (floor (+ bottom (* (random) (- top bottom))))))

(def fermat-test
    (lambda (n)
        (let try-it
            (lambda (a n)
                (= (expmod a n n) a))
        (try-it (+ 1 (randint 1 (- n 1))) n))))

(def fast-prime?
    (lambda (n times)
        (if (= times 0) True
            (if (fermat-test n) (fast-prime? n (- times 1))
                False))))

(print "Is 1709 prime?" '())
(print (fast-prime? 1709 20) '())


# General Equation for an Integral (pg 60)

# Helper function for Integrals
(def int-sum
    (lambda (term a next b)
        (if (> a b)
            0
            (+ (term a)
                (int-sum term (next a) next b)))))

# Just three example functions, to show off the Integral
(def inc
    (lambda (n)
        (+ n 1)))

(def cube
    (lambda (n)
        (* n n n)))

(def sum-cubes
    (lambda (a b)
        (int-sum cube a inc b)))

(print "sum of cubes from n=3 to n=5" '())
(print (sum-cubes 3 5) '())

(def integral
    (lambda (f a b dx)
        (let add-dx
            (lambda (x)
                (+ x dx))
        (* (int-sum f (+ a (/ dx 2.0)) add-dx b) dx))))

# TODO: I seem to be printing the quotes around a string, but not \n characters.
(print "Integral of y=x^3 from 3 to 5" '())
(print (integral cube 3 5 0.1) '())


# General Equation for Numeric Derivative (pg 74)

(def DELTA 0.0000001)

(def deriv
    (lambda (g x)
        (/ (- (g (+ x DELTA)) (g x))
            DELTA)))

(print "Derivative of y=x^3 at x=3" '())
(print (deriv cube 3) '())
#(print (map cube '(1 3 5 9)) '())

# Tree Reduce as a LISP Accumulate (pg 116)

(def accumulate
    (lambda (op init seq)
        (if (empty seq)
            init
            (op (head seq)
                (accumulate op init (tail seq))))))

(def square-tree '(1 (4 (9 16) 25) (36 49)))

(def odd?
    (lambda (n)
        (= (mod n 2) 0)))

(def plus
    (lambda (a b)
        (+ a b)))

(def sum-odd-squares
    (lambda (tree)
        (accumulate plus 0 (map square (filter odd? (enumerate-tree tree))))))

(print "Sum of Odd Squares" '())
(print (sum-odd-squares square-tree) '())

