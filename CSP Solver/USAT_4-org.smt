; (a → ((b → c) ∧ (¬d ∨ c))) ∧ (d ∨ (a ↔ ¬b)) ∧ (d ∨ ¬c ∨ a) 

(declare-const a Bool)
(declare-const b Bool)
(declare-const c Bool)
(declare-const d Bool)

(assert
    (and
        (=> a (and (=> b c) (or (not d) c)))
        (or d (= a (not b)))
        (or d (not c) a)
    )
)

(check-sat)
(get-model)

(exit)