# Australia Map Coloring using CSP

## Problem Statement

* Solve the map coloring problem for Australia using Constraint Satisfaction Problem (CSP).
* States considered: WA, NT, SA, Q, NSW, V, T.

## Concepts Used

* Constraint Satisfaction Problem (CSP)
* Backtracking algorithm

## CSP Formulation

* Variables:

  * WA, NT, SA, Q, NSW, V, T
* Domain:

  * {Red, Green, Blue}
* Constraints:

  * Adjacent states must not have the same color.

## Adjacency (Constraint Graph)

* WA: NT, SA
* NT: WA, SA, Q
* SA: WA, NT, Q, NSW, V
* Q: NT, SA, NSW
* NSW: Q, SA, V
* V: SA, NSW
* T: No adjacent states

## How to Run

```bash
python australia_map_csp.py
```

## Sample Output

```
Australia Map Coloring:
{'WA': 'Red', 'NT': 'Green', 'SA': 'Blue', ...}
```

## Learning Outcome

* Understanding CSP representation
* Applying backtracking to satisfy 


# Telangana Map Coloring using CSP

## Problem Statement

* Apply map coloring using CSP for districts of Telangana.
* Ensure no adjacent districts share the same color.

## Concepts Used

* Constraint Satisfaction Problem (CSP)
* Backtracking algorithm

## CSP Formulation

* Variables:

  * Districts of Telangana (simplified subset used)
* Domain:

  * {Red, Green, Blue, Yellow}
* Constraints:

  * Adjacent districts must have different colors.

## Notes

* A simplified adjacency graph is used.
* Can be extended to all 33 districts with full adjacency data.

## How to Run

```bash
python telangana_map_csp.py
```

## Sample Output

```
Telangana Map Coloring:
{'Adilabad': 'Red', 'Nirmal': 'Green', ...}
```

## Learning Outcome

* Modeling real-world problems as CSP
* Graph-based constraint handling



# Sudoku Solver using CSP

## Problem Statement

* Solve a 9x9 Sudoku puzzle using CSP techniques.

## Concepts Used

* Backtracking search
* Constraint Satisfaction Problem

## Constraints

* Each row must contain digits 1–9 without repetition.
* Each column must contain digits 1–9 without repetition.
* Each 3x3 subgrid must contain digits 1–9 without repetition.

## How to Run

```bash
python sudoku_csp.py
```

## Sample Output

```
Sudoku Solution:
[5, 3, 4, 6, 7, 8, 9, 1, 2]
...
```

## Learning Outcome

* Applying CSP to structured puzzles
* Recursive backtracking implementation



# Crypt_analysis Puzzle (SEND + MORE = MONEY)

## Problem Statement

* Solve the cryptarithmetic equation:
  SEND + MORE = MONEY

## Concepts Used

* Constraint Satisfaction Problem (CSP)
* Permutations and backtracking

## Constraints

* Each letter represents a unique digit (0–9).
* Leading digits (S and M) cannot be zero.
* The arithmetic equation must be satisfied.

## How to Run

```bash
python crypt_analysis_puzzle_csp.py
```

## Sample Output

```
Solution:
{'S': 9, 'E': 5, 'N': 6, 'D': 7, ...}
```

## Learning Outcome

* Solving logical puzzles using CSP
* Handling combinatorial constraints


