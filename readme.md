> We are about to study the idea of a computational process. Computational processes are abstract beings that inhabit computers. As they evolve, processes manipulate other abstract things called data. The evolution of a process is directed by a pattern of rules called a program. People create programs to direct processes. In effect, we conjure the spirits of the computer with our spells. > > The programs we use to conjure processes are like a sorcerer's spells. They are carefully composed from symbolic expressions in arcane and esoteric programming languages that prescribe the tasks we want our processes to perform. > > A computational process, in a correctly working computer, executes programs precisely and accurately. Thus, like the sorcerer's apprentice, novice programmers must learn to understand and to anticipate the consequences of their conjuring. > > —Abelson and Sussman, SICP (1993)


### Python Resources: 

- how to think like a CS in python
- Data Structures and algorithms in python
- Hitch Hiker's Guide to python
- SCIP in python: https://wizardforcel.gitbooks.io/sicp-in-python/content/1.html
- python env https://jacobian.org/2018/feb/21/python-environment-2018/
- Cheatsheet https://github.com/gto76/python-cheatsheet?utm_source=hackernewsletter&utm_medium=email&utm_term=code </li


---------------------------

### Data Structures 

- A data structure (DS) is a way of organizing data so that it can be used effectively.
- An abstract data type (ADT) is an abstraction of a data structure which provides only the interface to which a data structure must adhere to. The interface does not give any specific details about how something should be implemented or in what programming language.
- 


| Algorithm                | Code      | 
|--------------------------|-----------|
| LinkedList               |           |  
| Stack                    |           |
| Queue                    |           |  
| Priority Queue           |           |
| Hashing                  |           |
| Hash Indexes             |           |
| SSTables and LSM-Trees   |           |
| B-Trees                  |           |
| Comparing B-Trees and LSM-Trees|           |
| Other Indexing Structures|           |



### Graph Algorithms 

Introduction to graph algorithms 
      Storage and representation of graphs (networks) on a computer
      Common graph theory problems
      Breadth first search algorithm
      Depth first search algorithm

| Algorithm                | Code | 
|--------------------------|------|
| Dijkstra's algorithm     |      |
| Topological sort                        |      |
|  \Shortest/longest path on a acyclic graph                         |      |
| Bellman Ford's algorithm                         |      |
| Floyd-Warshall all pairs shortest path algorithm |     |
| Finding bridges/articulation points             |     | 
| Finding strongly connected components (Tarjan's) |   | 
|  Travelling salesman problem (TSP)   |    |


-----------------------------------------------------------------------------


## Useful Data Algorithms for Building Data Products 

A data product provides actionable information without exposing decision makers to the underlying
data or analytics. Examples include: Movie Recommendations, Production Process Improvements, Targeted Advertising etc. For more details see [Rise of data Products](https://asjadkhan.ghost.io/ghost/#/site) 


### Data Mining Algorithms 

| Algorithm                | Notebooks | Description |   |   |
|--------------------------|-----------|-------------|---|---|
| Assoicative Rule Mining  |           |             |   |   |
| Alpha Miner              |           |             |   |   |
| Flexible Heuristic Miner |           |             |   |   |

###  Matrix Algorithms 

| Latent Semantic Indexing                      | [Code] <https://gist.github.com/asjad99/e87a695df10b0859ee943b8e661f0fc3> |
|-----------------------------------------------|-------------------------------------------------------------------------------------------|
| Principal Component Analysis (PCA)            |                                                                                           |
| Probabilistic Latent Semantic Indexing (PLSA) |                                                                                           |
| Latent Dirchlet Allocation (LDA)              |                                                                                           |
| Logistic Matrix Factorization                 |                                                                                           |
| Restricted Boltzmann Machines                 |                                                                                           |
| Collaborative Filtering                       |                                                                                           |
| Compressive sensing                           |                                                                                           |
| Linear and convex programming                 |                                                                                           |

-----------------------------------------------------------------------------






------------------------------------------------------------------------------------------------------------------------------


## What is Computer Science? 


> Knuth (1974b) said that CS is the study of algorithms and surrounding phenomena such as the computers that they run on. CS is the the study both of algorithms and of the computers that execute them. 


CS can have multiple definitions: 

    - natural science of procedure 
    - “artificial science” (as opposed to the “natural science”) of the phenomena surrounding computers
    - CS is the study of how to represent and process information and of the machines and systems that do this
    - said that it is a new kind of science (neither a physical, a biological, nor a social science) of natural and artificial information processes
    - Loui (1987) suggested that CS is a new kind of engineering that studies the theory, design, analysis, and implementation of information-processing algorithms
    - "CS is “a sort of spectrum . . . with ‘science’ on the one end and ‘engineering’ on the other” 

If we want to pick one then we can settle on the following: 

> CS is the scientific study of what problems can be solved, what tasks can be accomplished, and what features of the world can be understood “computationally”—that is, using the minimal language of a Turing Machine—and then to provide algorithms to show how this can be done efficiently, practically, physically, and ethically. 


## Theoratical Computer Science concerns itself with the following questions: 

0. What is computation? 
1. What can be computed, and how? 
2. What can be computed efficiently, and how? 
3. What can be computed practically, and how? 
4. What can be computed physically, and how? 
5. What can be computed ethically, and how?


## Great Ideas/Insights of CS: 

   - A (programmable) computer is a physically plausible implementation of anything logically equivalent to a universal Turing machine.

   - An automaton (plural: automata) is a mathematical model of a computing device.

   - Turing machines are an abstraction of computers with unbounded resources.

   - Finite automata are an abstraction of computers with finite resource constraints.
   
   - DFAs are the simplest type of automaton

### That “minimal language” can be described by four “great insights of CS”: 

1. The representational insight: Only two nouns are needed to express any algorithm. 


> All the information about any computable problem can be represented using only two nouns: ‘0’ and ‘1’

Up until that time [that is, the time of publication of Shannon’s “Mathematical
Theory of Communication” (Shannon, 1948)], everyone thought that communication was involved in trying to find ways of communicating written language, spoken language, pictures, video, and all of these different things— that all of these would require different ways of communicating. Claude said
no, you can turn all of them into binary digits. And then you can find ways
of communicating the binary digits. (Robert Gallager, quoted in Soni and
Goodman 2017)


2. The processing insight: Only three verbs are needed. 

3. The structural insight: Only three rules of grammar are needed. 

4. A “closure” insight: Nothing else is needed. This is the import of the ChurchTuring Computability Thesis that anything logically equivalent to a Turing Machine (or the lambda calculus, or recursive functions, or . . . ) suffices for computation.


And there is a fifth insight that links this abstract language to computers: 

5. The implementation insight: Algorithms can be carried out by physical devices
------------------------------------------------------------------------------------------------------------------------------

## Big-0 Notation


Big-0 Notation gives an upper bound of the complexity in the worst case, helping to quantify performance as the input size becomes arbitrarily large.


Let $f$ be a function that describes the running time of a particular algorithm for an input of size n:
$$
\begin{array}{c}
f(n)=7 \log (n)^{3}+15 n^{2}+2 n^{3}+8 \\
0(f(n))=0\left(n^{3}\right)
\end{array}
$$




------------------------------------------------------------------------------------------------------------------------------
## Problem Solving and Algorithms 

"Problem-Solving is a holistic blend of complex skills and finely tuned attitudes. It requires a balance of intutiion and formal rigour, of resilience and creativity. It depends too on collaboration and the ability to see out feedback and act on it. And so much more: certainly too for a single test to do justice.'


"In its purest form, mathematics is the perfect expression of human thought that marries logic with creative thought". 

"[The Euclidean algorithm] is the granddaddy of all algorithms, because it is the oldest nontrivial algorithm that has survived to the present day." - Donald Knuth, The Art of Computer Programming


Learning the art of solving new problems by mapping them to existing solved problems

"Reduction is a way of converting one problem to another problem in such a way that the solution to the second problem can be used to solve the first problem" - Theory-Of-Computation-Michael-Sipser

------------------------------------------------------------------------------------------------------------------------------


### Do I really understand the problem?
(a) What exactly does the input consist of?
(b) What exactly are the desired results or output?
(c) Can I construct an input example small enough to solve by hand?

### What happens when I try to solve it?
(d) How important is it to my application that I always find the optimalanswer? Can I settle for something close to the optimal answer?
(e) How large is a typical instance of my problem? Will I be working on10items? 1,000 items? 1,000,000 items?
(f) How important is speed in my application? Must the problem be solved within one second? One minute? One hour? One day?
(g) How much time and effort can I invest in implementation? Will I belimited to simple algorithms that can be coded up in a day, or do I have thefreedom to experiment with a couple of approaches and see which is best?
(h) Am I trying to solve a numerical problem? A graph algorithm problem? A geometric problem? A string problem? A set problem? Which formulation seems easiest?

### Can I find a simple algorithm or heuristic for my problem?

(a) Will brute force solve my problem correctly by searching through allsubsets or arrangements and picking the best one?
    i. If so, why am I sure that this algorithm always gives the correct answer?
    ii. How do I measure the quality of a solution once I construct it?
    iii. Doesthis simple, slow solution run in polynomial or exponential time? Is my problemsmall enough that this brute-force solution will suffice?
    iv. Am I certain that myproblem is sufficiently well defined to actually have a correct solution?
    
(b) Can I solve my problem by repeatedly trying some simple rule, likepicking the biggest item first? The smallest item first? A random item first? 
    i. If so, on what types of inputs does this heuristic work well? Do thesecor-respond to the data that might arise in my application? 
    ii. On what types of inputs does this heuristic work badly? If no suchexam-ples can be found, can I show that it always works well? 
    iii. How fast does my heuristic come up with an answer? Does it have a simple implementation?

other hacks 
    See Cracking the coding interview 

------------------------------------------------------------------------------------------------------------------------------
## RESOURCES

Philosophy of CS 
Algorithms by Sadwick 
https://computationbook.com/ 
https://www.destroyallsoftware.com/screencasts
https://www.mvanga.com/blog/basic-music-theory-in-200-lines-of-python?utm_source=hackernewsletter&utm_medium=email&utm_term=fav
