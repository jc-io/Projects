"""
This program will find the shortest path from one European city to another European city.
"""
__author__ = 'Joseph Chen, jchen529@ucsc.edu'

import sys
import heapq
from math import radians, cos, sin, atan2, sqrt, inf


class Graph(dict):
  """
  This class will create an Adjacency List style-graph.
  """
  def __missing__(self, key):
    self[key] = Edges(self)
    return self[key]


class Edges(dict):
  """
  This class is referenced by Graph.
  """
  def __init__(self, graph=None):
    super().__init__()
    self.graph = graph


def dijkstra(self, start, end):
  """
  This function will find the shortest path from
  one city to another city.
  This was adapted from Jeffery Bergamini from Lecture week 9
  """
  if start == end and start in self:
    return [start]
  if start not in self:
    sys.stderr.write("Unknown city: " + start + "\n")
    sys.exit()
  distance = {}
  previous = {}
  pq = []
  heapq.heapify(pq)

  for v in self:
    distance[v] = inf
    previous[v] = None
  distance[start] = 0
  heapq.heappush(pq, (0, start))

  while len(pq) != 0:
    length, node = heapq.heappop(pq)
    for neighbor in g[node]:
      new_distance = length + g[node][neighbor]
      if new_distance < distance[neighbor]:
        distance[neighbor] = new_distance
        previous[neighbor] = node
        heapq.heappush(pq, (new_distance, neighbor))

  reverse_res = []
  while end is not None:
    reverse_res.append(end)
    if end not in previous:
      sys.stderr.write("Unknown city: " + end + "\n")
      sys.exit()
    end = previous[end]
  res = reverse_res[::-1]
  if len(res) == 1:
    sys.stderr.write("No path from " + start + " to" + " " + res[0] + "!" + "\n")
    sys.exit()
  return res


def vertex_names(names):
  """
  This function takes the file "/srv/datasets/e-roads/vertex_names.txt"
  as an input and and turns it into a dictionary.
  key = node_number
  value = city name
  """
  names_dict = {}
  input_file = open(names)

  for line in input_file:
    key, value = line.split("\t")
    names_dict[int(key)] = value.strip()

  return names_dict


def vertex_locations(locations, names):
  """
  This function takes the file "/srv/datasets/e-roads/vertex_locations.txt"
  as an input and turns it into a dictionary.
  key = node_number
  value = {longitude, latitude}
  """
  loctions_dict = {}
  input_file = open(locations)

  for line in input_file:
    number, long, lat = line.split()
    loctions_dict[names[int(number)]] = [float(long), float(lat.strip())]

  return loctions_dict


def network(net, names):
  """
  This function takes the file "/srv/datasets/e-roads/network.txt"
  as an input and turns it into a dictionary.
  key = node_number
  value = node
  """
  network_list = []
  input_file = open(net)

  for line in input_file:
    key, value = line.split()
    network_list.append([names[int(key)], names[int(value.strip())]])

  return network_list


def reverse_network(net, names):
  """
  This does the same as def network, but in reverse
  for bidirectional.
  """
  network_list = []
  input_file = open(net)

  for line in input_file:
    key, value = line.split()
    network_list.append([names[int(value)], names[int(key.strip())]])

  return network_list


def haversine(src_lon, src_lat, dst_lon, dst_lat):
  """
  this code was adapted from the website "https://www.movable-type.co.uk/scripts/latlong.html"
  """
  src_lon, src_lat, dst_lon, dst_lat = map(radians, [src_lon, src_lat, dst_lon, dst_lat])
  dlon = abs(dst_lon - src_lon)
  dlat = abs(dst_lat - src_lat)
  a = sin(dlat / 2)**2 + cos(src_lat) * cos(dst_lat) * sin(dlon / 2)**2
  c = 2 * atan2(sqrt(a), sqrt(1 - a))
  r = 6371

  return c * r


vertex_names = vertex_names("/srv/datasets/e-roads/vertex_names.txt")
vertex_locations = vertex_locations("/srv/datasets/e-roads/vertex_locations.txt", vertex_names)
vertex_network = network("/srv/datasets/e-roads/network.txt", vertex_names)
reverse = reverse_network("/srv/datasets/e-roads/network.txt", vertex_names)
bidirectional = vertex_network + reverse

all_weight_list = []

for cities in bidirectional:
  vertex = []
  for city in cities:
    vertex += vertex_locations[city]
  all_weight_list.append(vertex)

for index, ll_list in enumerate(all_weight_list):
  lat1 = ll_list[0]
  lon1 = ll_list[1]
  lat2 = ll_list[2]
  lon2 = ll_list[3]
  formula = haversine(lon1, lat1, lon2, lat2)
  bidirectional[index].append(float(formula))

g = Graph()

for (v_from, v_to, weight) in bidirectional:
  g[v_from][v_to] = weight

if __name__ == '__main__':
  src = sys.argv[1]
  dst = sys.argv[2]
  x = dijkstra(g, src, dst)
  http = "https://www.google.com/maps/dir"
  if len(sys.argv) == 3:
    for i in x:
      print(i)
  if len(sys.argv) > 3:
    for i in x:
      coord = vertex_locations[i]
      long_coord = "{:.3f}".format(coord[0])
      lat_coord = "{:.3f}".format(coord[1])
      add_str = "/{},{}".format(long_coord, lat_coord)
      http += add_str
    print(http)
