


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
---------------------------------------------------------------

   "[The Euclidean algorithm] is the granddaddy of all algorithms, because it is the oldest nontrivial algorithm that has survived to the present day." - Donald Knuth, The Art of Computer Programming
   

### Useful data Structures 


Hash Indexes
SSTables and LSM-Trees
B-Trees
Comparing B-Trees and LSM-Trees
Other Indexing Structures


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



### Python Resources: 

- how to think like a CS in python
- Data Structures and algorithms in python
- Hitch Hiker's Guide to python
- SCIP in python: https://wizardforcel.gitbooks.io/sicp-in-python/content/1.html
- python env https://jacobian.org/2018/feb/21/python-environment-2018/
- Cheatsheet https://github.com/gto76/python-cheatsheet?utm_source=hackernewsletter&utm_medium=email&utm_term=code </li

