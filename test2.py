import random
N_MAX = 10**2
M_MAX = 2 * N_MAX

def main():
    import networkx as nx
    import matplotlib.pyplot as plt
    
    
    for _ in range(1):
        n = random.randrange(1, N_MAX)
        graph = nx.DiGraph()
        graph.add_nodes_from(range(1, n+1))
        
        m = random.randrange(n, M_MAX)
        
        # ノード1を親としてランダムなツリーを生成
        parents = [1] + [random.randint(1, i) for i in range(2, n+1)]
        edges = [(parents[i], i + 1) for i in range(n)]
        graph.add_edges_from(edges)
        
        # cycle = set([random(1, n+1)]*random(1, n+1))
        # nx.add_cycle(graph, list(cycle))
        
        nx.draw_networkx(graph)
        plt.show()
        


if __name__ == '__main__':
    main()
