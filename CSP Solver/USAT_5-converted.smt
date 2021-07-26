; (S ∨ P) ∧ (S ∨ Q) ∧ (¬P ∨ Q ∨ S) ∧ (S ∨ ¬R) ∧ (¬P ∨ ¬R ∨ S) ∧ (¬Q ∨ R ∨ P) ∧ (¬P ∨ Q ∨ R)

(declare-const p Bool)
(declare-const q Bool)
(declare-const r Bool)
(declare-const s Bool)

(assert
    (and 
        (or (not p) q s)
        (or (not p) (not r) s)
        (or (not q) r p)
        (or (not p) q r)
        (or s p)
        (or s q)
        (or s (not r))
    )
)

(check-sat)
(get-model)

(exit)