;; logical operators

(def not
    (lambda (b)
        (if b #f #t)))

(def or
    (lambda (a b)
        (if a #t (if b #t #f))))

(def and
    (lambda (a b)
        (if a (if b #t #f) #f)))

(def xor
    (lambda (a b)
        (if a (if b #f #t) (if b #t #f))))

;; list functions

(def foldleft
    (lambda (f acc lst)
        (if (empty lst)
            acc
            (foldleft f (f acc (head lst)) (tail lst)))))

(def sum
    (lambda (lst)
        (foldleft (lambda (x y) (+ x y)) 0 lst)))

(def length
    (lambda (lst)
        (foldleft (lambda (x y) (+ x 1)) 0 lst)))

(def append
    (lambda (lst1 lst2)
        (if (empty lst1) lst2
            (cons (head lst1) (append (tail lst1) lst2)))))

(def filter
    (lambda (pred lst)
        (if (empty lst) '()
            (if (pred (head lst))
                (cons (head lst) (filter pred (tail lst)))
                (filter pred (tail lst))))))

(def map
    (lambda (f lst)
        (if (empty lst) '()
            (cons (f (head lst)) (map f (tail lst))))))

;; TODO: I want to be able to put `reverse-acc` inside `reverse`.
(def reverse-acc
    (lambda (l1 acc)
        (if (empty l1) acc
            (reverse-acc (tail l1) (cons (head l1) acc)))))

(def reverse
    (lambda (lst)
        (reverse-acc lst '())))

(def range
    (lambda (start end)
        (if (> start end) '()
            (cons start (range (+ 1 start) end)))))

(def range-step
    (lambda (start end step)
        (if (> start end) '()
            (cons start (range-step (+ step start) end step)))))

;; list-sorting algorithms

;; Quick Sort
(def small-or-equal-filter
    (lambda (lst pivot)
        (filter (lambda (v) (<= v pivot)) lst)))

(def greater-filter
    (lambda (lst pivot)
        (filter (lambda (v) (> v pivot)) lst)))

(def quick-sort
    (lambda (lst)
        (if (empty lst) lst
            (append (append (sort (smaller-or-equal-filter (tail lst) (head lst)))
                (cons (head lst) '()))
                (sort (greater-filter (tail lst) (head lst)))))))

;; Bubble Sort
(def bubble-sort
    (lambda (lst)
        (bubble-loop lst #t)))

(def bubble-loop
    (lambda (lst swapped)
        (if swapped (bubble (tail lst) '() (head lst) #t)
            (lst))))

(def bubble
    (lambda (lst new_lst current swapped)
        (if (empty lst) (bubble-loop new_lst swapped)
            (if (< (head lst) current) (bubble (tail lst) (cons (head lst) new_lst) current #f)
                (bubble (tail lst) (cons current new_lst) (head lst) #t)))))

;; Insert Sort
(def insert-sort
    (lambda (lst)
        (insert-loop lst '())))

(def insert-loop
    (lambda (i_list new_lst)
        (if (empty i_list) new_lst
            (insert-loop (tail i_list) (insert-ordered new_lst (head i_list))))))


;; (def merge-sort XXX)
;;
;;
;; IDEAS
;;
;; list operations: list-first-n, list-last-n, list-slice, nth, split, flatmap, accumulate/fold
;; set: an unsorted list object with setters that demand uniqueness
;; dictionaries and arrays?
;; str(), int(), float(), len(), exit(), raise?, try, except?
