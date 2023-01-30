# Introduction to Algorithm Design

**Algorithm Definition**: 
* A procedure to accomplish a specific task. 
* A procedure that takes any of the possible input instances and transforms it into the dsired output. 

An algorithmic problem is specified by describing the complete set of *instances* it must work on and ofi its output after running on one of those instances.

**Take-home lesson**: 
* There is a fundamental difference between algorithms, procedures that always produce a correct result, and heuristics, which may usually do a good job but provide no guarantee of correctness. 
* Reasonable-looking algorithms can easily be incorrect. Algorithm
correctness is a property that must be carefully demonstrated.
* An important and honorable technique in algorithm design is to narrow the set of allowable instances until there is a correct and efficient algorithm. For example, we can restrict a graph problem from general graphs down to trees, or a geometric problem from two dimensions down to one.
* The heart of any algorithm is an idea. If your idea is
not clearly revealed when you express an algorithm, then you are using too low-level a notation to describe it.

## Demonstrating Incorrectness

Techniques to use when seeking counterexamples to prove an algorithm is incorrect:

* Think Small: When algos fail, there's usually a simple example on which they fail. Small examples are easier to verify and reason about.
* Think Exhausively: 
* Hunt for the weakness: If looking at a greedy algorithm, think about why that might prove to be the wrong thing to do. 
* Go for a tie: One way to disprove a greedy algorithm is to provide instances where everything is the same size --> Heuristic has nothing to base its decision on and could return suboptimal result. 
* Seek extremes: Usually easier to verify or reason about extreme examples. 

**Take-home lesson**: 
* Searching for counterexamples is the best way to disprove correctness of a heuristic. 

## Combinatorial Objects
