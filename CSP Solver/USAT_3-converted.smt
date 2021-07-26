; (¬X ∨ Y) ∧ (Y ∨ Z) ∧ (¬Z ∨ ¬Y) ∧ (Z ∨ ¬X)

(declare-const x Bool)
(declare-const y Bool)
(declare-const z Bool)
(declare-const w Bool)

(assert
    (and 
        (or (not x) y)
        (or (not z) (not y))
        (or y z)
        (or z (not x))
    )
)

(check-sat)
(get-model)

(exit)