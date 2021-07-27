Solving CSPs (constraint satisfaction problems) using [Z3 Theorem Prover](https://github.com/Z3Prover/z3) and CSP algorithm (using backtracking / forward checking)

Problems specified in SMT-LIB standard

### 3-SAT problems: 

3SAT_1

(x or y) and
(y or (x and z)) and
(z or (x and not y and not z)) and
((not x and y and w and (k or not z)) or (x and (w or not z or t or x)))

--------------------------

3SAT_2

(T or not (not K or L or M or not N) or ((M and K) or (N and M) or (not T and L))) and
((M and L) or (not L and not M))

--------------------------

3SAT_3

(not (not P and (R or not Q)) or not (R and not Q)) and
((not P and (not Q or R)) or (R and not Q)) and
(P or R or not Q) and
(Q or (not P and Q))

---------------------------

3SAT_4

(z or (w and not y and (not x or y))) and
(x or not (y or z)) and
(not x or (y and x and not z)) and
(z or w or (not x or y)) and
(w or y or not x or (w and z))

----------------------------

3SAT_5

(z and q and x) and
((x and p) or (not q or x) or (p and y)) and
((z and y) or (x and not r)) and
(not y or not z or p) and
(x or not y or (z and p and r)) and
((x and p and z) or not r) and
(y or r)

### USAT example
original: (((¬S → P) → R) ∨ Q) ∧ (Q ∨ R ∨ P) ∧ (¬P ∨ (R ∧ ¬S) ∨ ¬Q)

converted into CNF / 3-SAT problem: (¬S ∨ R ∨ Q) ∧ (¬P ∨ R ∨ Q) ∧ (Q ∨ R ∨ P) ∧ (R ∨ ¬P ∨ ¬Q) ∧ (¬S ∨ ¬P ∨ ¬Q)


*CSP algorithm: https://github.com/szulcmaciej/CSP/blob/master/model.py
