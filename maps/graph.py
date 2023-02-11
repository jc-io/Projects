"""
This module will create a Graph Representation of directed/undirected weighted/unweighted data type.
"""
from copy import deepcopy


class Graph(dict):
  """
  This class will create an Adjacency List style-graph and check the patterns of it.
  """
  def __delitem__(self, key):
    key_list = list(self.keys())
    for i in key_list:
      if key in self[i]:
        self[i].pop(key)
    if key in self:
      self.pop(key)

  def __missing__(self, key):
    self[key] = Edges(self)
    return self[key]

  def copy(self):
    return deepcopy(self)

  def vertices(self):
    return set(self.keys())

  def edges(self):
    edge_list = []
    for i in self:
      for x in self[i]:
        edge_list.append((i, x, self[i][x]))
    return set(edge_list)

  def adjacent(self, src, dst):
    if src in self:
      if dst in self[src]:
        return True
    return False

  def neighbors(self, vertex):
    neighbors_list = []
    if vertex in self:
      for i in self[vertex]:
        neighbors_list.append(i)
    return set(neighbors_list)

  def degree(self, vertex):
    degree_list = []
    if vertex in self:
      for i in self[vertex]:
        degree_list.append(i)
    return len(degree_list)

  def path_valid(self, vertices):
    for i, vertex in enumerate(vertices):
      if i == 0:
        if vertex in self:
          continue
        else:
          return False
      if vertices[i] in self[vertices[i - 1]]:
        continue
      else:
        return False
    return True

  def path_length(self, vertices):
    if self.path_valid(vertices) is False:
      return None
    total_list = []

    if (len(vertices)) <= 1:
      return None

    for i, vertex in enumerate(vertices):
      if i == 0:
        if vertex in self:
          if vertices[i + 1] in self[vertices[i]]:
            num = self[vertices[i]][vertices[i + 1]]
            total_list.append(num)
          continue
        else:
          return None

      if vertices[i] in self[vertices[i - 1]] and i != len(vertices) - 1:
        if vertices[i + 1] in self[vertices[i]]:
          num = self[vertices[i]][vertices[i + 1]]
          total_list.append(num)
        continue
      if vertices[i] in self[vertices[i - 1]] and i == len(vertices) - 1:
        break
      else:
        return None

    if isinstance(total_list[0], (int, float)):
      total_weight = 0
      try:
        total_weight = sum(total_list)
        return total_weight
      except TypeError:
        return None

    if isinstance(total_list[0], str):
      total_weight = ""
      try:
        total_weight = "".join(total_list)
        return total_weight
      except TypeError:
        return None

    if isinstance(total_list[0], list):
      total_weight = list()
      try:
        for i in total_list:
          total_weight += i
      except TypeError:
        return None
      return total_weight

    if isinstance(total_list[0], dict):
      total_weight = dict()
      try:
        for i in total_list:
          total_weight.update(i)
      except TypeError:
        return None
      return total_weight

    if isinstance(total_list[0], set):
      total_weight = set()
      try:
        for i in total_list:
          total_weight.update(i)
      except TypeError:
        return None
      return total_weight
    if isinstance(total_list[0], frozenset):
      total_weight = set()
      try:
        for i in total_list:
          total_weight.update(i)
      except TypeError:
        return None
      return total_weight

    if isinstance(total_list[0], tuple):
      total_weight = tuple()
      try:
        for i in total_list:
          total_weight += i
      except TypeError:
        return None
      return total_weight

  def is_connected(self):
    all_nodes = self.vertices()
    for i in self.keys():
      check = Graph.dfs(self, i)
      if check != all_nodes:
        return False
    return True

  def dfs(self, start, visited=None):
    if visited is None:
      visited = set()
    if start not in visited:
      visited.add(start)
    for node in self[start].keys() - visited:
      Graph.dfs(self, node, visited)
    return visited


class Edges(dict):
  def __init__(self, graph=None):
    super().__init__()
    self.graph = graph

  def __setitem__(self, key, value):
    if key not in self.graph:
      self.graph[key]
    super().__setitem__(key, value)
