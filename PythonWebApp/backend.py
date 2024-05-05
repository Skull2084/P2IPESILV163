class DijkstraResult:
    def __init__(self, distance, path):
        self.distance = distance
        self.path = path

class Edge:
    def __init__(self, destination, distance):
        self._destination = destination
        self._distance = distance

    @property
    def destination(self):
        return self._destination

    @destination.setter
    def destination(self, value):
        self._destination = value

    @property
    def distance(self):
        return self._distance

    @distance.setter
    def distance(self, value):
        self._distance = value


graph = {
    "BatERDCD": [Edge("BatE-1D", 4), Edge("BatE1D", 4), Edge("BatERDCG", 16), Edge("BatERDCM", 8)],
    "BatERDCG": [Edge("BatERDCD", 16), Edge("BatE-1G", 4), Edge("BatE1G", 4), Edge("BatERDCM", 8)],
    "BatERDCM": [Edge("BatERDCD", 8), Edge("BatERDCG", 8), Edge("BatE-1M", 4), Edge("BatE1M", 4)],
    "BatE1M": [Edge("BatE1D", 8), Edge("BatE1G", 8), Edge("BatERDCM", 4), Edge("BatE2M", 4)],
    "BatE1D": [Edge("BatERDCD", 4), Edge("BatE2D", 4), Edge("BatE162", 1), Edge("BatE1G", 16), Edge("BatE1M", 8)],
    "BatE1G": [Edge("BatERDCG", 4), Edge("BatE2G", 4), Edge("BatE1D", 16), Edge("BatE1M", 8), Edge("BatE102", 1)],
    "BatE-1G": [Edge("BatE-1D", 16), Edge("BatERDCG", 4), Edge("BatE-1M", 8)],
    "BatE-1M": [Edge("BatE-1G", 8), Edge("BatERDCM", 4), Edge("BatE-1D", 8)],
    "BatE-1D": [Edge("BatE-1G", 16), Edge("BatERDCD", 4), Edge("BatE-1M", 8)],
    "BatE2M": [Edge("BatE2D", 8), Edge("BatE2G", 8), Edge("BatE1M", 4)],
    "BatE2D": [Edge("BatE1D", 4), Edge("BatE2G", 16), Edge("BatE2M", 8)],
    "BatE2G": [Edge("BatE1G", 20), Edge("BatE2D", 16), Edge("BatE2M", 8)],
    "BatE162": [Edge("BatE1D", 1), Edge("BatE160", 2)],
}




def dijkstra(graph, start, target):
    distances = {vertex: float('inf') for vertex in graph}
    previous = {}
    nodes = list(graph.keys())
    path = []

    distances[start] = 0

    while nodes:
        nodes.sort(key=lambda x: distances[x])
        smallest = nodes.pop(0)

        if smallest == target:
            while smallest in previous:
                path.insert(0, smallest)
                smallest = previous[smallest]
            break

        if distances[smallest] == float('inf'):
            break

        for neighbor in graph[smallest]:
            alt = distances[smallest] + neighbor.distance
            if alt < distances[neighbor.destination]:
                distances[neighbor.destination] = alt
                previous[neighbor.destination] = smallest

    path.insert(0, start)
    return DijkstraResult(distances[target], path)

# Utilisation de la fonction


# You can continue to add the rest of your nodes and edges in the same format.


result = dijkstra(graph, "BatE-1G", "BatE162")
print("Distance:", result.distance)
for step in result.path:
    print(step)
