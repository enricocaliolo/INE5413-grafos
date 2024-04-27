from lib.graph import Graph, Vertice


class VerticeInfo:
    def __init__(
        self, d: int = float("Inf"), a: Vertice = None, v: Vertice = None
    ) -> None:
        self.distancia = d
        self.antecessor = a
        self.v = v
        self.index = None

    def __str__(self) -> str:
        return f"index: {self.v.index}, distancia: {self.distancia}, antecessor: {self.antecessor}"


def bellman_ford(graph: Graph, vertice_origem: int):
    verticesInfo: dict[int, VerticeInfo] = {}
    for v in graph.traverseVertices():
        verticesInfo[v.index] = VerticeInfo(v=v)

    if not graph.findVertice(vertice_origem):
        return False

    verticesInfo[vertice_origem].distancia = 0
    verticesInfo[vertice_origem].index = graph.findVertice(vertice_origem)

    for _ in range(graph.qtdVertices() - 1):
        for aresta in graph.traverseArestas():
            distancia_u = verticesInfo[aresta.u].distancia
            distancia_v = verticesInfo[aresta.v].distancia

            if distancia_u != float("Inf") and distancia_u + aresta.peso < distancia_v:
                verticesInfo[aresta.v].distancia = (
                    verticesInfo[aresta.u].distancia + aresta.peso
                )
                verticesInfo[aresta.v].antecessor = graph.findVertice(aresta.u)

    for aresta in graph.traverseArestas():
        distancia_v = verticesInfo[aresta.v].distancia
        distancia_u = verticesInfo[aresta.u].distancia

        if distancia_u != float("Inf") and distancia_u + aresta.peso < distancia_v:
            return (False, None, None)

    for index, v in verticesInfo.items():
        head = f"{index}: "
        retData = [index]
        t = v
        while t.antecessor:
            retData.append(t.antecessor.index)
            t = verticesInfo.get(t.antecessor.index)

        retData.reverse()

        retDataStr = ",".join(str(x) for x in retData)
        print(head + retDataStr + f"; d={v.distancia}")

    return (True, verticesInfo)


if __name__ == "__main__":
    graph = Graph("arquivo_menor_teste.net")
    result = bellman_ford(graph, 3)
