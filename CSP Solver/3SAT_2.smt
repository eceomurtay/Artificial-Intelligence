(declare-const K Bool)
(declare-const L Bool)
(declare-const M Bool)
(declare-const N Bool)
(declare-const T Bool)

(assert
  (and
    (or T
      (not (or (not K) L M (not N)))
      (or (and M K) 
          (and N M)
          (and (not T) L)))
    (or 
      (and M L)
      (and (not L) (not M))
    )
  )
)

(check-sat)
(get-model)

(exit)

; Z3 -smt2 file