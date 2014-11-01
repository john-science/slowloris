# useful mathematical operations

(def floor
    (lambda (d)
        (- d (mod d 1))))

(def ceiling
    (lambda (d)
        (if (= d (floor d)) d
            (+ d (- 1 (- d (floor d)))))))

# TODO: This needs to produce an int, not a float.
(def randint
    (lambda (bottom top)
        (floor (+ bottom (* (random) (- top bottom))))))

(def randrange
    (lambda (bottom top)
        (+ bottom (* (random) (- top bottom)))))
        
