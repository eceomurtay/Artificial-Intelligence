; (x↔(y ∨ z)) ∧ ¬(y∧z) ∧ (z→x)

(declare-const x Bool)
(declare-const y Bool)
(declare-const z Bool)

(assert
    (and 
        (= x (or y z)) 
        (not (and y z))
        (=> z x))
)

(check-sat)
(get-model)

(exit)