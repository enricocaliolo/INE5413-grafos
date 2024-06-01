from graph import Graph, Vertice


class VerticeInfo:
    def __init__(self) -> None:
        self.isKnown = False
        self.t = float("inf")
        self.f = float("inf")
        self.antecessor = None

    def __str__(self) -> str:
        return f"isKnown: {self.isKnown} t: {self.t} f: {self.f} antecessores: {self.antecessor}  "


class ComponentesFortementeConexas:
    def __init__(self) -> None:
        self.tempo = 0

    def componentes_fortemente_conexas(self, graph: Graph):

        retData: dict[int, VerticeInfo] = self.dfs(graph)

        graph.transporGrafo()

        retData2: dict[int, VerticeInfo] = self.dfs(
            graph, alterado=True, vertices_anteriores=retData
        )

        florestas = {}
        antecessores = {}

        for index, data in retData2.items():
            antecessores[index] = data.antecessor
            if data.antecessor is None:
                florestas[index] = []

        for v, a in antecessores.items():
            v_atual = v

            while True:
                if a is None:
                    florestas[v_atual].append(v)
                    break

                v_atual, a = a, antecessores[v_atual]

        for floresta in florestas.values():
            print(",".join([str(i) for i in floresta]))

    def dfs(self, graph: Graph, alterado: bool = False, vertices_anteriores=None):

        vertices: dict[int, VerticeInfo] = {}

        for v in graph.traverseVertices():
            vertices[v.index] = VerticeInfo()

        self.tempo = 0

        if alterado:
            sorted_vertices = dict(
                sorted(
                    vertices_anteriores.items(),
                    key=lambda item: item[1].f,
                    reverse=True,
                )
            )

            for v in sorted_vertices:
                vertice = graph.findVertice(v)
                if vertices[vertice.index].isKnown == False:
                    self.dfs_visit(graph, vertice, vertices)

        else:
            for v in graph.traverseVertices():
                if vertices[v.index].isKnown == False:
                    self.dfs_visit(graph, v, vertices)

        return vertices

    def dfs_visit(self, graph: Graph, v: Vertice, vertices: dict[int, VerticeInfo]):
        vertices[v.index].isKnown = True
        self.tempo += 1
        vertices[v.index].t = self.tempo

        for u in v.vizinhos:
            if vertices[u].isKnown == False:
                vertices[u].antecessor = v.index
                u = graph.findVertice(u)
                self.dfs_visit(graph, u, vertices)

        self.tempo += 1
        vertices[v.index].f = self.tempo


if __name__ == "__main__":
    graph = Graph("testes/cfc.net", isDriven=True)
    algo = ComponentesFortementeConexas()
    algo.componentes_fortemente_conexas(graph)
