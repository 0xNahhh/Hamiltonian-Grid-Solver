import numpy as np
import gym
from gym import spaces

def graph_constructor(node_holes, n = 12):
    def get_edges(node):
        ## Top left corner
        if (node == 0):
            return [node + 1, node + n]
        ## Top right corner
        if (node == n - 1):
            return [node - 1, node + n]
        ## Bottom left corner
        if (node == n * (n - 1)):
            return [node - n, node + 1]
        ## Bottom right corner
        if (node == n**2 - 1):
            return [node - 1, node - n]

        ## Left column
        if (node % n == 0):
            return [node - n, node + 1, node + n]
        ## Top row
        if (node < n):
            return [node - 1, node + n, node + 1]
        ## Right column
        if (node % n == n - 1):
            return [node - n, node - 1, node + n]
        ## Bottom column
        if (n**2 - n <= node and node < n**2):
            return [node - 1, node - n, node + 1]

        return [node - 1, node - n, node + 1, node + n]

    graph = { i: get_edges(i) for i in range(n**2) }
 
    def remove_edges(node):
        left = node - 1
        top = node - n
        right = node + 1
        bottom = node + n
        direction_nodes = [left, top, right, bottom]

        for direction_node in direction_nodes:
            direction_edges = graph.get(direction_node, [])
            if node in direction_edges:
                graph[direction_node].remove(node)

        del graph[node]

    for node_hole in node_holes:
        hole_index = (node_hole[0] * n) + node_hole[1]
        remove_edges(hole_index)

    return graph


class HamiltonianGrid(gym.Env):
  LEFT = 0
  UP = 1
  RIGHT = 2
  DOWN = 3

  def __init__(self, cell_holes, n = 12):
    super(HamiltonianGrid, self).__init__()

    self.cell_holes = cell_holes
    self.n = n
    self.action_space = spaces.Discrete(4)
    self.observation_space = spaces.Box(low = 0, high = n**2 - 1, shape = (n**2 + 1,), dtype = np.uint8)

  def check_edge_exists(self, node):
    return node in self.graph.get(self.position, [])
  
  def step(self, action):
    self.prev_actions.append(action)
    new_position = self.position
    
    if (action == self.LEFT and self.check_edge_exists(self.position - 1)):
      new_position -= 1
    if (action == self.UP and self.check_edge_exists(self.position - self.n)):
      new_position -= self.n
    if (action == self.RIGHT and self.check_edge_exists(self.position + 1)):
      new_position += 1
    if (action == self.DOWN and self.check_edge_exists(self.position + self.n)):
      new_position += self.n
    
    ## if its the same position, then it hasn't moved.
    ## Else, then it's visiting a node that's already been visited
    ## Or it has finished the board
    if (sum(self.visited) == self.n**2 - len(self.cell_holes) or (new_position != self.position and self.visited[new_position] == 1)):
      self.done = True

    if (not self.done and new_position != self.position):
      self.reward = 1
    if (not self.done and new_position == self.position):
      self.reward = -0.5
    if (self.done and sum(self.visited) == self.n**2 - len(self.cell_holes)):
      self.reward = 1000
    if (self.done and sum(self.visited) != self.n**2 - len(self.cell_holes)):
      self.reward = -2
    if (len(self.prev_actions) >= self.n**2):
      self.reward = -10
      self.done = True

    self.visited[new_position] = 1
    self.position = new_position

    self.total_reward += self.reward
    self.prev_reward = self.total_reward

    info = {}   
    observation = [self.position] + self.visited
    observation = np.array(observation)
    print("prev actions: ", self.prev_actions)
    print("action: ", action)
    print("obs: ", observation)
    print("reward: ", self.reward)
    print("done: ", self.done)
    print("")
    print("=======================================")
    print("")

    return observation, self.reward, self.done, info

  def reset(self):
    self.graph = graph_constructor(self.cell_holes)
    self.total_reward = 0
    self.done = False
    self.prev_reward = 0
    self.position = 0
    self.visited = [0 for _ in range(self.n**2)]
    self.visited[0] = 1 ## first index is initial position
    self.prev_actions = []

    observation = [self.position] + self.visited
    observation = np.array(observation)

    return observation
