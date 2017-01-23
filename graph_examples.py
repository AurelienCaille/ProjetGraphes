from Graph import Graph

#####################################
#Creation of a Guido van Russo graph#


guido_s_graph = Graph()

#Adding nodes
guido_s_graph.add_a_node("A")
guido_s_graph.add_a_node("B")
guido_s_graph.add_a_node("C")
guido_s_graph.add_a_node("D")
guido_s_graph.add_a_node("E")
guido_s_graph.add_a_node("F")

#Adding edges
guido_s_graph.add_an_edge("A", "B", "")
guido_s_graph.add_an_edge("A", "C", "")
guido_s_graph.add_an_edge("B", "D", "")
guido_s_graph.add_an_edge("B", "C", "")
guido_s_graph.add_an_edge("C", "D", "")
guido_s_graph.add_an_edge("D", "C", "")
guido_s_graph.add_an_edge("E", "F", "")
guido_s_graph.add_an_edge("F", "C", "")

####################################
tobe = Graph()
tobe.add_a_node("A")
tobe.add_a_node("B")
tobe.add_a_node("C")
tobe.add_a_node("D")
tobe.add_a_node("E")

tobe.add_an_edge("A", "B", "")
tobe.add_an_edge("B", "A", "")
tobe.add_an_edge("B", "C", "")
tobe.add_an_edge("C", "B", "")
tobe.add_an_edge("A", "C", "")
tobe.add_an_edge("C", "A", "")
tobe.add_an_edge("D", "E", "")
tobe.add_an_edge("E", "D", "")




#####################################
#Creation of chain graph            #
#with 4 nodes

chain_4 = Graph()

#Adding nodes
chain_4.add_a_node("A")
chain_4.add_a_node("B")
chain_4.add_a_node("C")
chain_4.add_a_node("D")

#Adding edges
chain_4.add_an_edge("A", "B", "")
chain_4.add_an_edge("B", "C", "")
chain_4.add_an_edge("C", "D", "")


print (tobe)
