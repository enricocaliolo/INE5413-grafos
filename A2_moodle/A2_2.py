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

    def ordenacao_topologica(self, graph: Graph):

        vertices = {
            item[0].index: VerticeInfo() for item in zip(graph.traverseVertices())
        }
        self.tempo = 0
        ordenacao = []

        for v in graph.traverseVertices():
            if vertices[v.index].isKnown == False:
                self.dfs_visit_ot(graph, v, vertices, ordenacao)

        result = ""
        for v in ordenacao:
            if v == ordenacao[len(ordenacao) - 1]:
                result += v.replace('"', "", 2) + "."
            else:
                result += v.replace('"', "", 2) + "->"

        print(result)

    def dfs_visit_ot(
        self,
        graph: Graph,
        v: Vertice,
        vertices,
        ordenacao,
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
                    ordenacao,
                )

        self.tempo += 1
        vertices[v.index].f = self.tempo

        ordenacao.insert(0, v.rotulo)



import sys

if __name__ == "__main__":

    file = sys.argv[1]

    graph = Graph(file)
    ordenacao_topologica(graph)
