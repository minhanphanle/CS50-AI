# CS50-AI
This repository contains all Projects in the CS 50 Introduction to Artificial Intelligence with Python course.

## Course Overview & Project Outline
The course covers various concepts, algorithms, and AI libraries that lay a strong foundation for a general understanding of what Artificial Intelligence is. Every week requires students to submit a quiz and hands-on projects to demonstrate their understanding of the topic.

### Week 0: Search
The course starts off with search, introducing foundational concepts of how an agent could find a solution to a problem such as navigating from a point to a destination or playing a chess game.

- Concepts: agent, state, actions, transition model, state space, goal test, path cost
- Algorithms: Depth-first Search (DFS), Breadth-first Search (BFS), Greedy best-first search, A* search with Manhatten distance heuristic, Minimax (adversarial search)
- Projects:
  - #### Degrees: [Link](Week0/minhanphanle-ai50-projects-2020-x-degrees/degrees.py)
          ```$ python degrees.py large
            Loading data...
            Data loaded.
            Name: Emma Watson
            Name: Jennifer Lawrence
            3 degrees of separation.
            1: Emma Watson and Brendan Gleeson starred in Harry Potter and the Order of the Phoenix
            2: Brendan Gleeson and Michael Fassbender starred in Trespass Against Us
            3: Michael Fassbender and Jennifer Lawrence starred in X-Men: First Class```
    - A program that determines how many "degrees of separation" apart two actors are aka the shortest path between any two actors through their movies
    - **_Algorithm & Data Structure used_**: BFS, Queue
  - #### Tic-Tac-Toe: [Link](https://github.com/minhanphanle/CS50-AI/blob/main/Week0/minhanphanle-ai50-projects-2020-x-tictactoe/tictactoe.py)

    ![image](https://github.com/minhanphanle/CS50-AI/assets/83915952/86e95362-7e53-4e2a-b898-37c8378af88c)
    - Implement an AI that plays TicTacToe optimally
    - _**Algorithm & Data Structure used**_: Minimax with alpha-beta pruning, two-dimensional list to represent the board
   
### Week 1: Knowledge
Week 1 is about how the AI agent could represent knowledge about the world, which is esstential for inference later on.

- Concepts: propositional logic, first-order logic, knowledge-based (KB) agensts, logical connectives, truth table, model, entailment, inference rules (De Morgan, Double Negation, Distributed Property, Implication Elimination, Modus Ponens), conjunctive normal form, inference by resolution
- Algorithms: Model checking by enumerating all possible models and check if KB true for every model (Big question: $` \text{KB} \models \alpha \implies`$ Can we conclude that $` \alpha `$ is true based on knowledge base), Inference algorithm
- Projects:
  - #### Knights: [Link](https://github.com/minhanphanle/CS50-AI/blob/main/Week1/minhanphanle-ai50-projects-2023-x-knights/puzzle.py)
  - Represent the "Knights and Knaves" puzzle using propositional logic and solve the following puzzles:

    ![image](https://github.com/minhanphanle/CS50-AI/assets/83915952/165d41dd-2a4b-40af-9075-8e89270b72f8)
  - **_Algorithm & Data Structure used_**: Model Checking, tuple
 
- #### Minesweeper: [Link](https://github.com/minhanphanle/CS50-AI/blob/main/Week1/minhanphanle-ai50-projects-2023-x-minesweeper/minesweeper.py)

  ![image](https://github.com/minhanphanle/CS50-AI/assets/83915952/0d9e5584-f325-4cfe-9056-f266315c5e46)

  - An AI that could play Minesweeper using propositional logic to make deductions / decisions based on has-mine status of the individual cell and their corresponding neighbors
  - _**Algorithm & Data Structure used**_: iterative logical inference, set, list

### Week 2: Uncertainty
Week 2 takes Week 1's AI knowledge inference to another level by adding probability.

- Concepts: probability theory (independence, marginalization, disjoint probability, conditional probability, Bayes Rules, chain rule, total probaility, normalization), Bayesian Network, Hidden Markov Model, Markov chain
- Algorithms: Inference by Enumeration (pomegranate library), sampling, likelihood weighting
- Projects:
  - #### PageRank: [Link](https://github.com/minhanphanle/CS50-AI/blob/main/Week2/minhanphanle-ai50-projects-2023-x-pagerank/pagerank.py)
  - Simulate Google's PageRank algorithm to rank web pages by importance
   
        ```$ python pagerank.py corpus0
          PageRank Results from Sampling (n = 10000)
            1.html: 0.2223
            2.html: 0.4303
            3.html: 0.2145
            4.html: 0.1329
          PageRank Results from Iteration
            1.html: 0.2202
            2.html: 0.4289
            3.html: 0.2202
            4.html: 0.1307```
  - **_Algorithm & Data Structure used_**: Sampling pages from Markov Chain random surfer and iteratively apply PageRank formula, dictionary, set

    PageRank formula for a page `p`
    
    ![image](https://github.com/minhanphanle/CS50-AI/assets/83915952/4f62b1b7-e97d-4bcf-92e9-c7082a1395ef)

  - #### Heredity: [Link](https://github.com/minhanphanle/CS50-AI/blob/main/Week2/minhanphanle-ai50-projects-2023-x-heredity/heredity.py)
  - Write an AI to assess the likelihood that a person will have a particular genetic trait.
          ```$ python heredity.py data/family0.csv
            Harry:
              Gene:
                2: 0.0092
                1: 0.4557
                0: 0.5351
              Trait:
                True: 0.2665
                False: 0.7335
            James:
              Gene:
                2: 0.1976
                1: 0.5106
                0: 0.2918
              Trait:
                True: 1.0000
                False: 0.0000
            Lily:
              Gene:
                2: 0.0036
                1: 0.0136
                0: 0.9827
              Trait:
                True: 0.0000
                False: 1.0000```
    - **_Algorithm & Data Structure used_**: joint probability, normalization, dictionary, set
   



  
 
