import sys
from A1.lib.graph import Graph
from busca import busca

if __name__ == "__main__":
    graph_name = sys.argv[1]
    vertice_origem = int(sys.argv[2])

    graph = Graph(graph_name)

    busca(graph, 1)
