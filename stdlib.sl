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

;; list functions

(define foldleft
    (lambda (f acc lst)
        (if (empty lst)
            acc
            (foldleft f (f acc (head lst)) (tail lst)))))

(define sum
    (lambda (lst)
        (foldleft (lambda (x y) (+ x y)) 0 lst)))

(define length
    (lambda (lst)
        (foldleft (lambda (x y) (+ x 1)) 0 lst)))

;; FUNCTION TEMPLATE
;;
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
