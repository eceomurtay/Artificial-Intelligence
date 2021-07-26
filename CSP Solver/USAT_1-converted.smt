; CNF, 3-SAT : (¬S ∨ R ∨ Q) ∧ (¬P ∨ R ∨ Q) ∧ (Q ∨ R ∨ P) ∧ (R ∨ ¬P ∨ ¬Q) ∧ (¬S ∨ ¬P ∨ ¬Q)

(declare-const p Bool)
(declare-const q Bool)
(declare-const r Bool)
(declare-const s Bool)

(assert
    (and 
        (or (not s) r q)
        (or (not p) r q)
        (or q r p)
        (or r (not p) (not q))
        (or (not s) (not p) (not q))
    )
)

(check-sat)
(get-model)

(exit)