import time
import sys
import argparse
import networkx as nx
from algo import Algo
from utils import memory_usage, Analyzer

def main(G,
         preG,
         edges_idx,
         dotpath,
         savepath,
         maxiter,
         octettree,
         draw,
         repulsiontype,
         attractiontype
         ):
    AlgoTimeAnalysis = Analyzer()

    assert isinstance(G, nx.classes.graph.Graph), "Not a networkx graph"

    algo = Algo(preG, G, edges_idx, iter=maxiter, octet=octettree)

    # run
    memory_usage(iter, message='before Algo run')
    before = time.time()
    Tree, newpos, IterTimeAnalyzer, RepulsionTimeAnalyzer, AttractionTimeAnalyzer, ApplyForceTimeAnalyzer =\
        algo.run(repulsiontype=repulsiontype,
                 attractiontype=attractiontype,
                 draw=draw,
                 savepath=savepath)
    after = time.time()
    AlgoTimeAnalysis.append((after - before))
    memory_usage(iter, message='after Algo run')

    return Tree, newpos, AlgoTimeAnalysis, IterTimeAnalyzer, RepulsionTimeAnalyzer, AttractionTimeAnalyzer, ApplyForceTimeAnalyzer

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Mettez des options que vous utiliserez.')

    # dots = ["CH4.dot", "H2O.dot", "benzène.dot"]
    # ajouter des arguments
    parser.add_argument('--dotpath', default="/Users/taeyeon/PycharmProjects/sda_projet/Molecules/benzène.dot", help='Mettez le path de .dot que vous appliquerez à l Algo.')
    parser.add_argument('--savepath', default="/Users/taeyeon/PycharmProjects/sda_projet/pos_change/", help='Mettez le path pour sauvegarder des résultats.')
    parser.add_argument('--octettree', action='store_true', help='Pour utiliser une structure de OctetTree utilisez cette option, sinon QuadTree.')
    parser.add_argument('--maxiter', default=300, required=True, help='Mettez le nombre maximal d iteration.')
    parser.add_argument('--repulsiontype', choices=['Eades', 'FR', 'RepulsionbyDegree'], required=True, help='Mettez le type de la force de repulsive.')
    # parser.add_argument('--')
    parser.add_argument('--attractiontype', choices=['Eades', 'FR', 'Normal', 'Linlog'], required=True, help='Mettez le type de la force de attractive.')
    parser.add_argument('--draw', action='store_true', help='Utilisez cette option pour tracer des graphes par chaque iter.')
    parser.add_argument('--nombrenode', default=0, help='Si vous n utiliserez pas dotpath et utiliserez une graphe que vous définissez.')

    args = parser.parse_args()

    # print(args.target)
    print(f"dotpath \t\t: {args.dotpath}")
    print(f"dotpath \t\t: {args.savepath}")
    print(f"octettree \t\t: {args.octettree}")
    print(f"maxiter \t\t: {args.maxiter}")
    print(f"repulsion type \t: {args.repulsiontype}")
    print(f"attraction type : {args.attractiontype}")
    print(f"drawing graphe \t: {args.draw}")
    if args.nombrenode:
        print(f"nombre de nodes \t: {args.nombrenode}")

    assert int(args.maxiter) > 0, "Il faut mettre un chiffre supérieur de 0 comme maxiter !"
    # repulsion - attraction type check
    if args.repulsiontype == 'RepulsionbyDegree':
        assert args.attractiontype in ['Normal', 'Linlog'], "Utilisez 'Normal' ou 'Linlog' comme attractiontype !"
    else:
        assert args.repulsiontype == args.attractiontype, "Utilisez les mêmes types de force !"

    # Read it as a graph in a networkx form
    preG = nx.Graph(nx.nx_pydot.read_dot(args.dotpath))
    G = nx.Graph()
    # G.add_nodes_from([nb for nb in nodes_dic.values()])
    if args.nombrenode:
        del preG
        del G
        preG = nx.random_geometric_graph(args.nombrenode, 0.2)
        G = nx.random_geometric_graph(args.nombrenode, 0.2)

    # Define the Nodes and their Edges and replace 'str' with 'number' ex) 'H1'(node) -> 0 (node number)
    nodes = [n for n in preG.nodes()]  # O(n)
    edges = [e for e in preG.edges()]  # O(n)

    nodes_dic = {i: n for n, i in enumerate(preG.nodes())}  # O(n)
    edges_idx = [(nodes_dic[edge[0]], nodes_dic[edge[1]]) for edge in [e for e in preG.edges()]]  # O(n)

    G.add_nodes_from(nodes)
    G.add_edges_from(edges)

    # run !
    Tree, newpos, AlgoTimeAnalysis, IterTimeAnalyzer, RepulsionTimeAnalyzer, AttractionTimeAnalyzer, ApplyForceTimeAnalyzer =\
        main(G,
             preG,
             edges_idx,
             dotpath=args.dotpath,
             savepath=args.savepath,
             maxiter=int(args.maxiter),
             octettree=args.octettree,
             draw=args.draw,
             repulsiontype=args.repulsiontype,
             attractiontype=args.attractiontype
            )

    sys.stderr.write("Total cost : " + str(AlgoTimeAnalysis.get_total_cost()) + "\n\n")

    sys.stderr.write("Iter cost : " + str(IterTimeAnalyzer.get_total_cost()) + "\n")
    sys.stderr.write("Iter Average cost : " + str(IterTimeAnalyzer.get_average_cost()) + "\n\n")

    sys.stderr.write("Repulsion cost : " + str(RepulsionTimeAnalyzer.get_total_cost()) + "\n")
    sys.stderr.write("Repulsion Average cost : " + str(RepulsionTimeAnalyzer.get_average_cost()) + "\n\n")

    sys.stderr.write("Attraction cost : " + str(AttractionTimeAnalyzer.get_total_cost()) + "\n")
    sys.stderr.write("Attraction Average cost : " + str(AttractionTimeAnalyzer.get_average_cost()) + "\n\n")

    sys.stderr.write("ApplyForce cost : " + str(ApplyForceTimeAnalyzer.get_total_cost()) + "\n")
    sys.stderr.write("ApplyForce Average cost : " + str(ApplyForceTimeAnalyzer.get_average_cost()) + "\n")