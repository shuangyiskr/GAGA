class Graph:
    def __init__(self):
        self.graph_dict = {}

    def add_vertex(self, vertex):
        if vertex not in self.graph_dict:
            self.graph_dict[vertex] = []

    def add_edge(self, vertex1, vertex2, weight=1):
        if vertex1 not in self.graph_dict:
            self.graph_dict[vertex1] = [(vertex2, weight)]
        else:
            self.graph_dict[vertex1].append((vertex2, weight))

        if vertex2 not in self.graph_dict:
            self.graph_dict[vertex2] = [(vertex1, weight)]
        else:
            self.graph_dict[vertex2].append((vertex1, weight))

    def get_neighbors(self, vertex):
        return self.graph_dict[vertex]

    def __str__(self):
        res = ""
        for vertex in self.graph_dict:
            res += str(vertex) + " --> " + str(self.graph_dict[vertex]) + "\n"
        return res

# 测试代码
if __name__ == "__main__":
    graph = Graph()
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_edge(1, 2, 5)
    graph.add_edge(1, 3, 2)
    graph.add_edge(2, 3, 1)
    graph.add_edge(2, 4, 6)
    print(graph.get_neighbors(1))
    print("邻接表：")
    print(graph)
