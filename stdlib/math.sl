# useful mathematical operations

# lowers a float value to the nearest integer
(def floor
    (lambda (d)
        (- d (mod d 1))))

# raises a float value to the nearest integer
(def ceiling
    (lambda (d)
        (if (= d (floor d)) d
            (+ d (- 1 (- d (floor d)))))))

# takes the absolute value of a number
(def abs
    (lambda (n)
        (if (< n 0)
            (* n -1)
            n)))

# round a float to the nearest integer
(def round
    (lambda (n)
        (if (>= (mod n 1) 0.5)
            (ceiling n)
            (floor n))))

# takes the square root of a number
(def sqrt
    (lambda (n)
        (** n 0.5)))

# produces a random integer, in some given range
(def randint
    (lambda (bottom top)
        (int (+ bottom (* (random) (- top bottom))))))

# produces a random float, in some given range
(def randrange
    (lambda (bottom top)
        (+ bottom (* (random) (- top bottom)))))

# randomly select an item from a list
(def randchoice
    (lambda (lst)
        (select-by-index lst (randint 0 (- (length lst) 1)))))
