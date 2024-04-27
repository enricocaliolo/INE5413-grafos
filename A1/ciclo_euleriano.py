from graph import Graph, Vertice


def hasEdgeNotVisited(vertice: Vertice, arestas_visitadas: dict[tuple[int, int], bool]):

    for vizinho in vertice.vizinhos:
        if (vertice.index, vizinho) in arestas_visitadas:
            if arestas_visitadas[(vertice.index, vizinho)] == False:
                return True

        elif (vizinho, vertice.index) in arestas_visitadas:
            if arestas_visitadas[(vizinho, vertice.index)] == False:
                return True

    return False


def buscarSubcicloEuleriano(
    graph: Graph,
    v: Vertice,
    arestas_visitadas: dict[tuple[int, int], bool],
):
    ciclo: list[int] = [v.index]
    t = v

    while v == t:

        if not hasEdgeNotVisited(v, arestas_visitadas):
            return False, 0

        for u in v.vizinhos:
            aresta = graph.findAresta(v.index, u)
            if aresta and not arestas_visitadas[aresta]:
                arestas_visitadas[aresta] = True
                v = graph.vertices[u]
                ciclo.append(v.index)

    for x in ciclo:
        for v in graph.vertices[x].vizinhos:
            aresta = graph.findAresta(x, v)
            if (
                x != ciclo[0]
                and aresta
                and hasEdgeNotVisited(graph.vertices[x], arestas_visitadas)
            ):
                r, ciclo_ = buscarSubcicloEuleriano(
                    graph, graph.vertices[x], arestas_visitadas
                )

                if not r:
                    return (False, 0)

                index = ciclo.index(x)
                ciclo = ciclo[:index] + ciclo_ + ciclo[index + 1 :]

    return True, ciclo


def ciclo_euleriano(graph: Graph) -> tuple[bool, int]:
    arestas_visitadas = {}

    for aresta in graph.arestas:
        arestas_visitadas[aresta] = False

    for vertice in graph.vertices.values():
        if not vertice.vizinhos:
            continue
        break

    r, c = buscarSubcicloEuleriano(graph, graph.vertices[1], arestas_visitadas)

    return r, c


if __name__ == "__main__":
    graph = Graph("SemCicloEuleriano.net")
    r, c = ciclo_euleriano(graph)

    if r:
        for v in c:
            print(v)
