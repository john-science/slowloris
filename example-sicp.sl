# Excerpt Examples from Structure and Interpretation of Computer Programs
# (A wonderful starter on software, and a seminal text on functional programming.)


# Exponentiation - Simple Resursion (pg 44)
(def exp
    (lambda (b n)
        (if (= n 0)
            1
            (* b (exp b (- n 1))))))


# Exponentiation - Linear Iteration (pg 45)
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
