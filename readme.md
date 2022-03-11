# Hamiltonian Grid Solver
An AI built to solve a game of visiting every square at least once in the grid.

### History
- Initially tried using the backtracking algorithm to solve for the hamiltonian path, but quickly realized that for a 12x12 grid, it would take too long
- Proceeded to try and build an AI using reinforcement learning
- Based on the SentDex [Reinforcement Learning with Stable Baselines 3](https://www.youtube.com/watch?v=XbWhJdQgi7E&list=PLQVvvaa0QuDf0O2DWwLZBfJeYY-JOeZB1) tutorial series

### AI
- Game was initially set up as a 10x10 square grid, where there were 4 node holes in the grid
- Win condition: Find a hamiltonian path in the grid
- Algorithm used is PPO with default parameters
- tinkered with the entropy coefficient and learning rate to help improve the model
- The AI would always eventually end up in a corner where the best tactic was to just continually shove itself into that corner
