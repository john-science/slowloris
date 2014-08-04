;; Some logical operators.

(define not
    (lambda (b)
        (if b #f #t)))

;; DIY -- Implement the rest of your standard library
;; here as part 7 of the workshop.

;; IDEAS

;; list operations: head, tail, prepend, append
;; set: an unsorted list object with setters that demand uniqueness
;; dictionaries and arrays?
;; 
