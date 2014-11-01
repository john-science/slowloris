# list functions

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

(def reverse
    (lambda (lst)
        (let reverse-acc
            (lambda (l1 acc)
                (if (empty l1) acc
                    (reverse-acc (tail l1) (cons (head l1) acc))))
        (reverse-acc lst '()))))

(def range
    (lambda (start end)
        (if (> start end) '()
            (cons start (range (+ 1 start) end)))))

(def range-step
    (lambda (start end step)
        (if (> start end) '()
            (cons start (range-step (+ step start) end step)))))
