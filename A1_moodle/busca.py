from graph import Graph, Vertice


class VerticeInfo:
    def __init__(
        self,
        vertice: Vertice,
        isKnown: bool,
        distance: int = 0,
        previousVertice: Vertice = None,
    ) -> None:
        self.vertice = vertice
        self.isKnown = isKnown
        self.distance = distance
        self.previousVertice = previousVertice
        pass


def busca(graph: Graph, v_origem):
    vertices: dict[str, VerticeInfo] = {}

    for item in graph.vertices.items():
        vertices[item[0]] = VerticeInfo(item[1], False, 0, None)

    vertices[v_origem].isKnown = True

    fila_visitas: list[VerticeInfo] = []
    fila_visitas.append(vertices[v_origem])

    retData: dict[int, list] = {}

    while len(fila_visitas) != 0:
        u: VerticeInfo = fila_visitas.pop(0)

        for vizinho in u.vertice.vizinhos:
            if vertices[vizinho].isKnown == False:
                vertices[vizinho].isKnown = True
                vertices[vizinho].distance = u.distance + 1
                vertices[vizinho].previousVertice = u.vertice

                fila_visitas.append(vertices[vizinho])

                distance = u.distance + 1

                if distance in retData:
                    retData[distance] = [
                        *retData[distance],
                        vertices[vizinho].vertice.index,
                    ]

                else:
                    retData[distance] = [vertices[vizinho].vertice.index]

    # just for the return from the input
    print(f"0: {v_origem}")
    for key, value in retData.items():
        print(f"{key}: {','.join(str(e) for e in value)}")


import sys

if __name__ == "__main__":

    file = sys.argv[1]
    vertice = int(sys.argv[2])

    graph = Graph(file)
    busca(graph, vertice)
