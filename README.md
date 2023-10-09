# CS50-AI
This repository contains all Projects in the CS 50 Introduction to Artificial Intelligence with Python course.

## Course Overview & Project Outline
The course covers various concepts, algorithms, and AI libraries that lay a strong foundation for a general understanding of what Artificial Intelligence is. Every week requires students to submit a quiz and hands-on projects to demonstrate their understanding of the topic.

## Table of Content
- [Week 0: Search](###%20Week%200:%20Search)
- [Week 1: Knowledge](###%20Week%201:%20Knowledge)

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
   
### Week 3: Optimization
This week lecture talks about how to select the best option from a set of possible solutions the AI have derived from techniques outlined in the previous weeks.

- Concepts: local search, state-space landscape, objective function, cost function, constraint-satisfaction problem, linear programming, simulated annealing, selecting unassigned variables to restrict search space the most (minimum remaining value heuristic, degree heuristic - most connected nodes)
- Algorithms: hill climbing (steepest-ascent, stoachstic, first-choice, random-restart, local-beam search), AC-3 (arc consistency), back-tracking, simplex, interior-point
- Project:
  - #### Crossword: [Link](https://github.com/minhanphanle/CS50-AI/blob/main/Week3/minhanphanle-ai50-projects-2023-x-crossword/crossword.py)
  - Write an AI to generate crossword
 
      ```$ python generate.py data/structure1.txt data/words1.txt output.png
    ██████████████
    ███████M████R█
    █INTELLIGENCE█
    █N█████N████S█
    █F██LOGIC███O█
    █E█████M████L█
    █R███SEARCH█V█
    ███████X████E█
    ██████████████```

  - **_Algorithm & Data Structure used_**: AC-3, backtrack, dictionary
 
### Week 4: Learning
This week introduces three types of machine learning: supervised, unsupervised and reinforcement learning

- Concepts: classification, regression (perceptron learning rule), hypothesis function, threshold function, logistic function, over-fitting, hold-out cross validation, Markov decision process, trade off between explore and exploit (greedy algorithm), function approximation
- Algorithms: k-nearest-neighbor classification, support vector machines (SVM), Q-learning, Epsilon Greedy, K-means clustering
- Projects:
  - #### Shopping: [Link](https://github.com/minhanphanle/CS50-AI/blob/main/Week4/minhanphanle-ai50-projects-2023-x-shopping/shopping.py)
  - Write an AI to predict whether online shopping customers will complete a purchase, using sensitivity (true positive rate) and specificity (true negative rate) to evaluate the model
 
          ```$ python shopping.py shopping.csv
            Correct: 4088
            Incorrect: 844
            True Positive Rate: 41.02%
            True Negative Rate: 90.55%```

  - Library: Scikit-learn
  - #### Nim: [Link](https://github.com/minhanphanle/CS50-AI/blob/main/Week4/minhanphanle-ai50-projects-2023-x-nim/nim.py)
  - Write an AI that teaches itself to play Nim through reinforcement learning.

          ```$ python play.py
            Playing training game 1
            Playing training game 2
            Playing training game 3
            ...
            Playing training game 9999
            Playing training game 10000
            Done training
            
            Piles:
            Pile 0: 1
            Pile 1: 3
            Pile 2: 5
            Pile 3: 7
            
            AI's Turn
            AI chose to take 1 from pile 2.```
    - **_Algorithm & Data Structure used_**: Q-learning with epsilon
   
### Week 5: Neural Network
An artificial neural network is a mathematical model for AI learning inspired by biological neural network. This week introduces computer vision, recurrent neural network and TensorFlow library

- Concepts: activation functions (step function, logistics sigmoid, rectified linear unit (ReLU), neural network structure, multi-layer neural network, convolution neural network, feedforward neural network, recurrent neural networks
- Algorithms: gradient descent, backpropagation
- Projects:
  - #### Traffic: [Link](https://github.com/minhanphanle/CS50-AI/blob/main/Week5/minhanphanle-ai50-projects-2023-x-traffic/traffic.py)
  - The project utilizes the German Traffic Sign Recognition Benchmark (GTSRB) with 43 classes of traffic signs with around 50000 images including training and testing.
  - Demo video: [Link](https://youtu.be/WKhOrytB33s)
  - Library: Scikit-learn, Tensorflow, Numpy
  - Result table: 
  
  <img width="1011" alt="image" src="https://github.com/minhanphanle/CS50-AI/assets/83915952/e5b497cd-f833-4383-b901-ef5dd9127e81">

  - My best model is the heaviest model which has the specs of 17.62 MB, a total params of 4 618 539 with test accuracy of 0.9825 and 0.094 with 3 convolution layers of 32, 64, and       128 filters respectively.
 
### Week 6: Language
Natural Language Processing was introduced with the application of Markov Models, Naive Bayes, and Neural Network - concepts introduced in earlier weeks - to predict words in a sentence and other tasks in NLP, which beautifully tie together concepts in the course.

- Concepts: syntax and semantics, context-free grammar, n-grams, tokenization, Bag-of-Words model, Naive Bayes, Word Representation, Neural Network, Recurrent Neural Network, attention, self-attention, parallelism, transformer, one-hot representation, distributed representation
- Library: nltk, word2vec
- Algorithms: Markov model, additive smoothing, Laplace smoothing, skip-gram architecture
- Projects:
  - #### Parser: [Link](https://github.com/minhanphanle/CS50-AI/blob/main/Week6/minhanphanle-ai50-projects-2023-x-parser/parser.py)
  - Write an AI to parse sentences and extract noun phrases.

        ```$ python parser.py
        Sentence: Holmes sat.
                S
           _____|___
          NP        VP
          |         |
          N         V
          |         |
        holmes     sat
        
        Noun Phrase Chunks
        holmes```

  - Library: nltk
  - **_Algorithm & Data Structure used_**: tree-node traversing
  - #### Attention: [Link](https://github.com/minhanphanle/CS50-AI/blob/main/Week6/minhanphanle-ai50-projects-2023-x-attention/mask.py)
  - Write an AI to predict a masked word in a text sequence with attention-score visualizer

            ```$ python mask.py
        Text: We turned down a narrow lane and passed through a small [MASK].
        We turned down a narrow lane and passed through a small field.
        We turned down a narrow lane and passed through a small clearing.
        We turned down a narrow lane and passed through a small park.
        
        $ python mask.py
        Text: Then I picked up a [MASK] from the table.
        Then I picked up a book from the table.
        Then I picked up a bottle from the table.
        Then I picked up a plate from the table.```

  - Library: TFBertForMaskedLM, Tensorflow
  - Example of attention diagram, which shows that the adverb "slowly" attending mostly to the verb it modifies: "moved".
 
  ![image](https://github.com/minhanphanle/CS50-AI/assets/83915952/16201bf1-07e1-45ba-a0e9-7a31e3ac1775)




  
 
