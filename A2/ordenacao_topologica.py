from graph import Graph, Vertice


class VerticeInfo:
    def __init__(
        self,
    ) -> None:
        self.isKnown = False
        self.t = float("inf")
        self.f = float("inf")


class OrdenacaoTopologica:
    def __init__(self) -> None:
        self.tempo = 0
        self.ordenacao = []

    def ordenacao_topologica(self, graph: Graph):

        vertices: dict[int, VerticeInfo] = {
            item[0].index: VerticeInfo() for item in zip(graph.traverseVertices())
        }
        self.tempo = 0
        self.ordenacao: list[str] = []

        for v in graph.traverseVertices():
            if vertices[v.index].isKnown == False:
                self.dfs_visit_ot(graph, v, vertices)

        result = ""
        for v in self.ordenacao:
            if v == self.ordenacao[len(self.ordenacao) - 1]:
                result += v.replace('"', "", 2) + "."
            else:
                result += v.replace('"', "", 2) + " -> "

        print(result)

    def dfs_visit_ot(
        self,
        graph: Graph,
        v: Vertice,
        vertices: dict[int, VerticeInfo],
    ):
        vertices[v.index].isKnown = True
        self.tempo += 1
        vertices[v.index].t = self.tempo

        for vizinho in v.vizinhos:
            vizinho_vertice = graph.findVertice(vizinho)
            if vertices[vizinho_vertice.index].isKnown == False:
                self.dfs_visit_ot(
                    graph,
                    vizinho_vertice,
                    vertices,
                )

        self.tempo += 1
        vertices[v.index].f = self.tempo

        self.ordenacao.insert(0, v.rotulo)


if __name__ == "__main__":
    graph = Graph("testes/ordenacao.net", isDriven=True)
    ordenacao = OrdenacaoTopologica()
    ordenacao.ordenacao_topologica(graph)
