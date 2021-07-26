; (((¬S → P) → R) ∨ Q) ∧ (Q ∨ R ∨ P) ∧ (¬P ∨ (R ∧ ¬S) ∨ ¬Q)

(declare-const p Bool)
(declare-const q Bool)
(declare-const r Bool)
(declare-const s Bool)

(assert
    (and 
        (or (=> (=> (not s) p) r) q)
        (or q r p)
        (or (not p) (and r (not s)) (not q))
    )
)

(check-sat)
(get-model)

(exit)