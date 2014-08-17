;; Some logical operators.

(define not
    (lambda (b)
        (if b #f #t)))

(define or
    (lambda (a b)
        (if a #t (if b #t #f))))

(define and
    (lambda (a b)
        (if a (if b #t #f) #f)))

(define xor
    (lambda (a b)
        (if a (if b #f #t) (if b #t #f))))

(define sum
    (lambda (a)
        ((define sum-acc
            (lambda (a acc)
                (if (empty a) acc
                    (sum-acc (tail a) (+ acc (head a))))))
         sum-acc a 0)))

;;(define xxx
;;    (lambda (a)
;;        ())


;; IDEAS

;; sum, length, filter, map, append, range, sort
;; list operations: prepend, append
;; set: an unsorted list object with setters that demand uniqueness
;; dictionaries and arrays?
;; str(), int(), float(), len(), exit(), raise?, try, except?
;; map, reduce (accumulate/fold), filter, flatmap
