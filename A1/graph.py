import os


class Vertice:
    def __init__(self, index: int, rotulo: str) -> None:
        self.index = index
        self.rotulo = rotulo
        self.vizinhos = {}

    def __str__(self) -> str:
        return f"({self.rotulo})"

    def __eq__(self, other: object) -> bool:
        if isinstance(other, self.__class__):
            if self.index == other.index:
                return True

        return False

    def add_vizinhos(self, vizinho, peso=0):
        self.vizinhos[vizinho] = peso


class Aresta:
    def __init__(self, u: int, v: int, peso=0) -> None:
        self.u = u
        self.v = v
        self.peso = peso


class Graph:
    def __init__(self, path) -> None:
        self.vertices: dict[int, Vertice] = {}
        self.arestas: dict[tuple[int, int], Aresta] = {}
        self.n_vertices = 0
        self.n_arestas = 0

        self.init(path)

    def init(self, path):

        # here = os.path.dirname(os.path.abspath(__file__))
        # filename = os.path.join(here, path)

        with open(path) as f:
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

                    u = int(edges[0])
                    v = int(edges[1])
                    peso = float(edges[2])

                    aresta = Aresta(u, v, peso)

                    self.arestas[(u, v)] = aresta

                    self.vertices[u].add_vizinhos(v, peso)
                    self.vertices[v].add_vizinhos(u, peso)

                    arestas += 1

                elif not edges:
                    vertice = line.split('"')
                    index = int(vertice[0].strip())
                    rotulo = vertice[1]
                    self.vertices[index] = Vertice(index, rotulo)

            self.n_arestas = arestas

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
        if (u, v) in self.arestas:
            return True
        return False

    def peso(self, u, v):
        return self.arestas[(u, v)].peso if (u, v) in self.arestas else float("inf")

    def findAresta(self, v: int, u: int):
        if (v, u) in self.arestas:
            return (v, u)
        elif (u, v) in self.arestas:
            return (u, v)

        return None

    def findVertice(self, v: int):
        return self.vertices[v] if v in self.vertices else False

    def traverseArestas(self):
        for a in self.arestas.values():
            yield a

    def traverseVertices(self):
        for v in self.vertices.values():
            yield v
