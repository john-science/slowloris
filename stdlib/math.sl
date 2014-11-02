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

# TODO: This needs to produce an int, not a float.
# produces a random integer, in some given range
(def randint
    (lambda (bottom top)
        (floor (+ bottom (* (random) (- top bottom))))))

# produces a random float, in some given range
(def randrange
    (lambda (bottom top)
        (+ bottom (* (random) (- top bottom)))))
        
