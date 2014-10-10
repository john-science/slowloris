# including basic error and exception logic in Slow Loris

# We need to be able to raise LispErrors

(def raise
    (lambda (str)
        (print (str_append "LispError: " str) (exit))))

