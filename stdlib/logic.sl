# logical operators

(def not
    (lambda (b)
        (if b False True)))

(def or
    (lambda (a b)
        (if a True (if b True False))))

(def and
    (lambda (a b)
        (if a (if b True False) False)))

(def xor
    (lambda (a b)
        (if a (if b False True) (if b True False))))
