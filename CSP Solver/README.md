Solving CSPs (constraint satisfaction problems) using [Z3 Theorem Prover](https://github.com/Z3Prover/z3) and CSP algorithm

Problems specified in SMT-LIB standard

### USAT example
original: (((¬S → P) → R) ∨ Q) ∧ (Q ∨ R ∨ P) ∧ (¬P ∨ (R ∧ ¬S) ∨ ¬Q)
converted into CNF / 3-SAT problem: (¬S ∨ R ∨ Q) ∧ (¬P ∨ R ∨ Q) ∧ (Q ∨ R ∨ P) ∧ (R ∨ ¬P ∨ ¬Q) ∧ (¬S ∨ ¬P ∨ ¬Q)
