from graph import Graph, Aresta


def kruskal(graph: Graph):
    arvore: list[Aresta] = []
    s: dict[int, set] = {i: {i} for i in range(1, graph.qtdVertices() + 1)}

    sorted_arestas: dict[tuple[int, int], Aresta] = dict(
        sorted(graph.arestas.items(), key=lambda item: item[1].peso)
    )

    peso_total = 0
    arestas_adicionadas = 0

    for key, aresta in sorted_arestas.items():
        if s[aresta.u] != s[aresta.v]:
            arvore.append(aresta)
            arestas_adicionadas += 1
            peso_total += aresta.peso
            x = s[aresta.u].union(s[aresta.v])

            for y in x:
                s[y] = x

        if arestas_adicionadas == graph.qtdVertices():
            break

    print(peso_total)
    retStr = ""
    for aresta in arvore:
        if aresta == arvore[-1]:
            retStr += f"{aresta.u}-{aresta.v}"
        else:
            retStr += f"{aresta.u}-{aresta.v}, "

    print(retStr.rstrip())


if __name__ == "__main__":
    graph = Graph("testes/agm_tiny.net")
    kruskal(graph)
