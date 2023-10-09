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
  
 
