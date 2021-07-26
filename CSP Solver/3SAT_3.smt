(declare-const P Bool)
(declare-const Q Bool)
(declare-const R Bool)

(assert 
    (and 
        (or (not (and 
                    (not P) 
                    (or R (not Q)))) 
            (not (and R (not Q))))
        (or (and 
                (not P) 
                (or R (not Q))) 
            (and R (not Q)))
        (or P R (not Q))
        (or Q (and (not P) Q))
    )
)

(check-sat)
(get-model)

(exit)