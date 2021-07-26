; (¬B ∨ C ∨ ¬A) ∧ (¬D ∨ C ∨ ¬A) ∧ (B ∨ A ∨ D) ∧ (¬A ∨ ¬B ∨ D) ∧ (D ∨ ¬C ∨ A)
 
(declare-const a Bool)
(declare-const b Bool)
(declare-const c Bool)
(declare-const d Bool)

(assert
    (and
        (or (not b) c (not a))
        (or (not d) c (not a))
        (or b a d)
        (or (not a) (not b) d)
        (or d (not c) a)
    )
)

(check-sat)
(get-model)

(exit)