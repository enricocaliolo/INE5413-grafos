from graph import Graph


def floyd_warshall(graph: Graph):
    n_vertices: int = graph.n_vertices

    matriz = [[0] * n_vertices for _ in range(n_vertices)]

    for i in range(0, n_vertices):
        for j in range(0, n_vertices):
            if i == j:
                matriz[i][j] = 0

            elif not graph.findAresta(i + 1, j + 1):
                matriz[i][j] = float("inf")
                matriz[j][i] = float("inf")

            else:
                aresta = graph.findAresta(i + 1, j + 1)
                matriz[i][j] = graph.arestas[aresta].peso
                matriz[j][i] = graph.arestas[aresta].peso

    for k in range(n_vertices):
        for i in range(n_vertices):
            for j in range(n_vertices):
                matriz[i][j] = min(matriz[i][j], matriz[i][k] + matriz[k][j])
                matriz[j][i] = min(matriz[j][i], matriz[j][k] + matriz[k][i])

    for i in range(n_vertices):
        print(f"{i+1}:{','.join(str(e) for e in matriz[i])}")


if __name__ == "__main__":

    graph = Graph("fln_pequena.net")
    floyd_warshall(graph)
