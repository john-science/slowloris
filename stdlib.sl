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

;;(define sum-acc
;;    (lambda (a acc)
;;        (if (empty a) acc
;;            (sum-acc (tail a) (+ acc (head a))))))

;;(define sum-acc
;;    (lambda (a)
;;        (if (empty a) 0
;;            (+ (head a) (sum-acc (tail a))))))

;;(define sum
;;    (lambda (a)
;;        5))
;;        sum-acc a))

(define foldleft
    (lambda (f z lst)
        (if (empty lst)
            z
            (foldleft f (f z (head lst)) (tail lst)))))

(define sum
    (lambda (lst)
        (foldleft (lambda (x y) (+ x y)) 0 lst)))

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
