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

    def __str__(self) -> str:
        return f"({self.u}, {self.v}): {self.peso}"


class Graph:
    def __init__(self, path, isDriven=False) -> None:
        self.vertices: dict[int, Vertice] = {}
        self.arestas: dict[tuple[int, int], Aresta] = {}
        self.n_vertices = 0
        self.n_arestas = 0
        self.isDriven = isDriven

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

                elif "edges" in line or "arcs" in line:
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

                    if not self.isDriven:
                        self.vertices[v].add_vizinhos(u, peso)

                    arestas += 1

                elif not edges:
                    vertice = line.split(" ", maxsplit=1)
                    index = int(vertice[0].strip())
                    rotulo = vertice[1].strip()
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

        if self.isDriven and (u, v) in self.arestas:
            return True

        elif not (self.isDriven) and (v, u) in self.arestas:
            return True

        return False

    def peso(self, u, v):
        if self.isDriven and (u, v) in self.arestas:
            return self.arestas[(u, v)].peso

        elif not (self.isDriven) and (v, u) in self.arestas:
            return self.arestas[(v, u)].peso

        return None

    def findAresta(self, v: int, u: int):
        if (v, u) in self.arestas:
            return self.arestas[(v, u)]

        if not self.isDriven:
            if (u, v) in self.arestas:
                return self.arestas[(u, v)]

        return None

    def findVertice(self, v: int):
        return self.vertices[v] if v in self.vertices else False

    def traverseArestas(self):
        for a in self.arestas.values():
            yield a

    def traverseVertices(self):
        for v in self.vertices.values():
            yield v

    def transporGrafo(self):
        for v in self.traverseVertices():
            v.vizinhos.clear()

        arestas: dict[tuple[int, int], Aresta] = {}
        for aresta in self.traverseArestas():
            v = self.findVertice(aresta.v)

            v.add_vizinhos(aresta.u)
            arestas[(aresta.v, aresta.u)] = Aresta(aresta.v, aresta.u, aresta.peso)

        self.arestas = arestas
