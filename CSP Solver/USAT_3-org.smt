; (x → y) ∧ (z ↔ ¬y) ∧ (w ∨ x ∨ (z → x)) ∧ (¬x ∨ (w ∧ z))

(declare-const x Bool)
(declare-const y Bool)
(declare-const z Bool)
(declare-const w Bool)

(assert
    (and
        (=> x y)
        (= z (not y))
        (or w x (=> z x))
        (or (not x) (and w z))
    )
)

(check-sat)
(get-model)

(exit)