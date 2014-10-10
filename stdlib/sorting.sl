# including sorting algorithms in the standard libraries

# list-sorting algorithms

# Quick Sort
(def smaller-or-equal-filter
    (lambda (lst pivot)
        (filter (lambda (v) (<= v pivot)) lst)))

(def greater-filter
    (lambda (lst pivot)
        (filter (lambda (v) (> v pivot)) lst)))

(def quick-sort
    (lambda (lst)
        (if (empty lst) lst
            (append (append (quick-sort (smaller-or-equal-filter (tail lst) (head lst)))
                (cons (head lst) '()))
                (quick-sort (greater-filter (tail lst) (head lst)))))))

# Insert Sort
# inserts an item into an ordered list, preserving the order
(def insert-into-ordered
    (lambda (lst item)
        (if (empty lst) (cons item '())
            (if (> item (head lst)) (cons (head lst) (insert-into-ordered (tail lst) item))
                (cons item lst)))))

#S insert sort, build a progressively larger sorted list, from an unordered one
(def insert-sort
    (lambda (lst)
        (let insert-sort-acc
            (lambda (sorted unsorted)
                (if (empty unsorted) sorted
                    (insert-sort-acc (insert-into-ordered sorted 
                                    (head unsorted))
                                    (tail unsorted))))
        (if (empty lst) '()
            (insert-sort-acc (cons (head lst) '()) (tail lst))))))
