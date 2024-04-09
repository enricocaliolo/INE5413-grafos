import os


class Vertice:
    def __init__(self, index: int, rotulo: str) -> None:
        self.index = index
        self.rotulo = rotulo
        self.vizinhos = {}

    def __str__(self) -> str:
        return f"({self.rotulo})"

    def add_vizinhos(self, vizinho, peso=0):
        self.vizinhos[vizinho] = peso


# class Aresta:
#     def __init__(self, vertice1, vertice2, peso=0) -> None:
#         self.vertice1 = vertice1
#         self.vertice2 = vertice2
#         self.peso = peso


class Graph:
    def __init__(self, path) -> None:
        self.vertices: dict[Vertice] = {}
        self.arestas: dict[tuple[int, int]] = {}
        self.n_vertices = 0
        self.n_arestas = 0

        self.init(path)

    def qtdVertices(self):
        return self.n_vertices

    def qtdArestas(self):
        return self.n_arestas

    def grau(self, v: int):
        return len(self.vertices[v].vizinhos)

    def rotulo(self, v: int):
        return self.vertices[v].rotulo

    def vizinhos(self, v: int):
        return self.vertices[v].vizinhos

    def haAresta(self, u, v):
        return (u, v) in self.arestas

    def peso(self, u, v):
        return self.arestas[(u, v)].peso if (u, v) in self.arestas else float("inf")

    def init(self, path):

        here = os.path.dirname(os.path.abspath(__file__))
        filename = os.path.join(here, path)

        with open(filename) as f:
            lines = f.readlines()
            edges = False

            arestas = 0

            for line in lines:
                if "vertices" in line:
                    self.n_vertices = int(line.split(" ")[1])

                elif "edges" in line:
                    edges = True
                    continue

                elif edges:
                    edges = line.split(" ")

                    # aresta = Aresta(int(edges[0]), int(edges[1]), float(edges[2]))
                    u = int(edges[0])
                    v = int(edges[1])
                    peso = float(edges[2])

                    self.arestas[(u, v)] = peso

                    vertice: Vertice = self.vertices[u]
                    vertice.add_vizinhos(v, peso)

                    arestas += 1

                elif not edges:
                    vertice = line.split('"')
                    index = int(vertice[0].strip())
                    rotulo = vertice[1]
                    self.vertices[index] = Vertice(index, rotulo)

            self.n_arestas = arestas


graph = Graph("facebook_santiago.net")
print(graph.haAresta(3, 260))
