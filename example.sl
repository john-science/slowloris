;; Some example Slow Loris-lisp code.

;; To execute the code:
;;
;;    ./sl example.sl
;;

(def fact 
    ;; This is a Factorial function
    (lambda (n) 
        (if (eq n 0) 
            1 ; Factorial of 0 is 1
            (* n (fact (- n 1))))))

;; When parsing the file, the last statement is returned
(fact 5)
