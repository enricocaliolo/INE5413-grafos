from graph import Graph, Vertice, Aresta


class VerticeInfo:

    def __init__(
        self,
        index: Vertice = None,
        isKnown: bool = False,
        d: int = float("inf"),
        a: Vertice = None,
    ) -> None:
        self.isKnown = isKnown
        self.distancia = d
        self.antecessor = a
        self.index = index

    def __str__(self) -> str:
        return f"index: {self.index}, distancia: {self.distancia}, antecessor: {self.antecessor}"


def getMinPath(verticesInfo: dict[int, VerticeInfo]):
    min_distance = float("inf")
    curr_v = None

    for v in verticesInfo.values():
        if not v.isKnown and v.distancia < min_distance:
            min_distance = v.distancia
            curr_v = v

    return curr_v


def dijkstra(graph: Graph, v_origem):
    verticesInfo: dict[int, VerticeInfo] = {}
    for v in graph.traverseVertices():
        verticesInfo[v.index] = VerticeInfo(index=v.index)

    verticesInfo[v_origem].distancia = 0

    for v in graph.vertices:
        u = getMinPath(verticesInfo)
        u = graph.vertices[u.index]

        verticesInfo[u.index].isKnown = True

        for w in u.vizinhos:
            if not verticesInfo[w].isKnown:
                aresta: Aresta = graph.findAresta(u.index, w)
                if (
                    verticesInfo[w].distancia
                    > verticesInfo[u.index].distancia + aresta.peso
                ):
                    verticesInfo[w].distancia = (
                        verticesInfo[u.index].distancia + aresta.peso
                    )
                    verticesInfo[w].antecessor = u.index

    for key, v in verticesInfo.items():
        head = f"{key}"
        custo = v.distancia
        antecessores = [v.index]
        t = v
        while t.antecessor:
            antecessores.append(t.antecessor)
            t = verticesInfo.get(t.antecessor)

        antecessores.reverse()

        antecessoresStr = ",".join(str(x) for x in antecessores)

        print(f"{head}: {antecessoresStr}; d={custo}")


import sys

if __name__ == "__main__":

    graph = Graph("fln_pequena.net")
    r = dijkstra(graph, 1)
