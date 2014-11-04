# list functions


# very generic function to accumulate the values of a list, given a summing function
(def foldleft
    (lambda (f acc lst)
        (if (empty lst)
            acc
            (foldleft f (f acc (head lst)) (tail lst)))))

# add all the elements of a list
(def sum
    (lambda (lst)
        (foldleft (lambda (x y) (+ x y)) 0 lst)))

# determines how many elements a list has
(def length
    (lambda (lst)
        (foldleft (lambda (x y) (+ x 1)) 0 lst)))

# concatanates two lists together
(def append
    (lambda (lst1 lst2)
        (if (empty lst1) lst2
            (cons (head lst1) (append (tail lst1) lst2)))))

# selects all the elements of a list for which a given predicate is true
(def filter
    (lambda (pred lst)
        (if (empty lst) '()
            (if (pred (head lst))
                (cons (head lst) (filter pred (tail lst)))
                (filter pred (tail lst))))))

# applies a function to all the elements of a list
(def map
    (lambda (f lst)
        (if (empty lst) '()
            (cons (f (head lst)) (map f (tail lst))))))

# inverts the order of the elements of a list
(def reverse
    (lambda (lst)
        (let reverse-acc
            (lambda (l1 acc)
                (if (empty l1) acc
                    (reverse-acc (tail l1) (cons (head l1) acc))))
        (reverse-acc lst '()))))

# creates a list of numbers, from a start to an end point, with a step of one
(def range
    (lambda (start end)
        (if (> start end) '()
            (cons start (range (+ 1 start) end)))))

# creates a list of numbers, from a start to an end point, with a given step size
(def range-step
    (lambda (start end step)
        (if (> start end) '()
            (cons start (range-step (+ step start) end step)))))

# flatten all the elments of a tree into a list
# (a "tree" here is a list where each element can also be a list)
(def flatten
    (lambda (lst)
        (if (empty lst)
            '()
            (if (eq (type (head lst)) (type '()))
                (append (flatten (head lst)) (flatten (tail lst)))
                (cons (head lst) (flatten (tail lst)))))))

# select an element from a list by index (indexes start with zero)
(def select-by-index
    (lambda (lst n)
        (if (= n 0)
            (head lst)
            (if (empty lst)
                (raise "Index out of range")
                (select-by-index (tail lst) (- n 1))))))

# find the smallest element of a list
(def min
    (lambda (lst)
        (head (quick-sort lst))))


# find the largest element of a list
(def max
    (lambda (lst)
        (rhead (quick-sort lst))))


# find the average of the elements of a list
(def avg
    (lambda (lst)
        (/ (sum lst) (length lst))))
