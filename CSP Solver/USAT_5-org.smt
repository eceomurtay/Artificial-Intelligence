; (p ∧ q ∧ ¬r) ↔ ((q → r) ∧ s ∧ ¬p) ↔ (s ∧ r ∧ p)

(declare-const p Bool)
(declare-const q Bool)
(declare-const r Bool)
(declare-const s Bool)

(assert
    (= 
        (= 
            (and p q (not r))
            (and (=> q r) s (not p))
        )
        (and s r p)
    )
)

(check-sat)
(get-model)

(exit)