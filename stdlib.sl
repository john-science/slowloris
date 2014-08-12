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

;; DIY -- Implement the rest of your standard library
;; here as part 7 of the workshop.

;; IDEAS

;; list operations: prepend, append
;; set: an unsorted list object with setters that demand uniqueness
;; dictionaries and arrays?
;; str(), int(), float(), len(), exit(), raise?, try, except?
;; map, reduce (accumulate/fold), filter, flatmap
