; (¬Y ∨ X) ∧ (¬Z ∨ X) ∧ (¬X ∨ Y ∨ Z) ∧ (¬Y ∨ ¬Z)

(declare-const x Bool)
(declare-const y Bool)
(declare-const z Bool)

(assert
    (and 
        (or y (not x) z)
        (or (not y) x)
        (or (not y) (not z))
        (or (not z) x))
)

(check-sat)
(get-model)

(exit)