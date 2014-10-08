;; This is an example file to prove that the 'import' feature is working.


;; We need to be able to raise LispErrors

(def raise
    (lambda (str)
        (print (str_append "LispError: " str) (exit))))

