from copy import deepcopy

class Graph(object):
    """
    Class representing a graph
    """
    def __init__(self):
        
        self.nodes = set()
        self.edges = []
        self.adjacency_list = {}
        self.adjacency_list_valued = {}
        self.open_graph()

    def add_a_node(self, node_name):
        """
        Add a node to the current graph
        Param:
        node_name : string, representing the name of the node
        """

        self.nodes.add(node_name)
        self.adjacency_list[node_name] = self.adjacency_list.get(node_name, [])
        self.adjacency_list_valued[node_name] = self.adjacency_list_valued.get(node_name, [])

    def add_an_edge(self, from_node, to_node, value):
        """
        Add an edge between to node
        Param:
        from_node : string, representing the name of the starting node
        to_node : string, representing the name of the ending node
        """

        if from_node in self.nodes and to_node in self.nodes:
            self.edges.append((from_node, to_node, value))
            self.adjacency_list[from_node].append(to_node)
            self.adjacency_list_valued[from_node].append((to_node, value))
        else:
            raise NameError('Nodes dosnt exist in this current graph')

    def dijkstra(self, departure):
        """
        Parcours le graphe et donne le chemin le plus court pour chaque autre sommet
        """
        colors_nodes = {}
        distance = {}
        parent_node = {}

        # On initialise en coloriant les nodes en blanc et en les mettant en distance infinie
        # Le depart est mis a distance 0 de lui meme btw
        for node in self.nodes:
            colors_nodes[node] = "white"
            distance[node] = float('inf')

        distance[departure] = 0
        colors_nodes[departure] = "grey"

        while all(colors_nodes != "black"):

            # Selection du node gris le plus proche
            distance_min = float('inf')
            for nodes in distance:
                if distance[nodes] < distance_min and colors_nodes[nodes] == "grey":
                    actual_node = nodes

            # Etablir les distances le plus courte a partir du node selectione:
            for voisins, value in self.adjacency_list_valued[actual_node]:
                if colors_nodes[voisins] == "white":
                    distance[voisins] = distance[actual_node] + int(value)
                    parent_node[voisins] = actual_node
                    colors_nodes[voisins] = "grey"

                elif colors_nodes[voisins] == "grey":
                    if distance[actual_node] + int(value) < distance[voisins]:
                        distance[voisins] = distance[actual_node] + int(value)
                        parent_node[voisins] = actual_node

            colors_nodes[actual_node] = "black"

        # Remonter // Determiner le return!!!!!!!!

    def composantes_connexes(self, departure):
        """
        (graphe non oriente uniquement)
        Retourne une liste de liste de sommets apparatenant aux memes composantes connexes
        """
        parents = {}
        colors = {}
        fifo = []
        composantes = []
        indice_composante = 0

        fifo.append(departure)
        composantes.append([departure])
        parents[departure] = None

        for node in self.nodes:
            colors[node] = "white"

        while len(fifo) != False:
            actual = fifo[0]

            new_child = 0


            #Child courses: Add new node in the fifo list
            for child in self.adjacency_list[actual]:
                if colors[child] == "white":

                    fifo.append(child)
                    colors[child] == "grey"
                    parents[child] = parents.get(child, actual)

                    #ajout de l'enfant dans la composantes
                    if child not in composantes[indice_composante]:
                        composantes[indice_composante].append(child)
                    new_child += 1

            colors[actual] = "black"
            fifo.pop(0)


            #Check if fifo list empty but still rest node to search

            if ((len(fifo) == False) and \
                (not all(color == "black" for color in colors.values()))):

                for node in sorted(self.nodes):
                    if colors[node] == "white":
                        fifo.append(node)
                        parents[node] = None
                        indice_composante += 1
                        composantes.append([fifo[0]])
                        break


        return composantes


    def breadth_first_search(self, departure):
        """
        Make a journey from the "departure" in the graph
        use breadth method
        return a parent tree (dictonary)
        """

        parents = {}
        colors = {}
        fifo = []

        fifo.append(departure)
        parents[departure] = None

        for node in self.nodes:
            colors[node] = "white"

        while len(fifo) != False:
            actual = fifo[0]

            new_child = 0

            #Child courses: Add new node in the fifo list
            for child in self.adjacency_list[actual]:
                if colors[child] == "white":

                    fifo.append(child)
                    colors[child] == "grey"
                    parents[child] = parents.get(child, actual)

                    new_child += 1

            colors[actual] = "black"
            fifo.pop(0)


            #Check if fifo list empty but still rest node to search

            if ((len(fifo) == False) and \
                (not all(color == "black" for color in colors.values()))):

                for node in sorted(self.nodes):
                    if colors[node] == "white":
                        fifo.append(node)
                        parents[node] = None
                        break


        return parents


    def is_bipartite(self):
        """
        Make a journey from the "departure" in the graph
        use breadth method
        return a parent tree (dictonary)
        """

        fifo = []
        partite = {} #can be -1 or 1

        #create adjacency list non oriented
        adjacency_list_non_oriented = deepcopy(self.adjacency_list)
        for from_node, to_nodes in self.adjacency_list.items():
            for node in to_nodes:
                adjacency_list_non_oriented[node].append(from_node)



        departure = sorted(self.nodes)[0]

        fifo.append(departure)


        for node in self.nodes:

            partite[node] = 0

        while len(fifo) != False:

            actual = fifo[0]

            if partite[actual] == 0:
                partite[actual] = -1 #Hail the defaut -1 partite :)

            new_child = 0

            #Child courses: Add new node in the fifo list 
            for child in adjacency_list_non_oriented[actual]:
                if partite[child] == 0:

                    #Next node to explore and add to the opposite partite
                    fifo.append(child)
                    partite[child] = - partite[actual]

                    #Check bipartite (non neighbor with the same partite)

                    for neighbor in adjacency_list_non_oriented[child]:

                        if partite[child] == partite[neighbor]:
                            return False

                
            fifo.pop(0)


            #Check if fifo list empty but still rest node to search

            if ((len(fifo) == False) and \
                (not all(color == -1 or color == 1  for color in partite.values()))):

                for node in sorted(self.nodes):
                    if partite[node] == 0:
                        fifo.append(node)
                        break



            return True

                

    def __str__(self):
        """
        Return a string for a visual representation of the current graph
        """
        #Display effects
        strGraph = ""
        strGraph += "*"*24
        strGraph +="\n"
        strGraph += "* Display of the graph *"
        strGraph +="\n"
        strGraph += "*"*24
        strGraph +="\n"
        strGraph += "Nodes:"
        strGraph +="\n"
        strGraph += "_"*6
        strGraph +="\n"

        #Display nodes

        for node in self.nodes:
            strGraph += str(node)
            strGraph += ","

        #Display another effects
        strGraph += "\n"
        strGraph +="\n"
        strGraph += "Edges:"
        strGraph +="\n"
        strGraph += "_"*6
        strGraph += "\n"

        #Display edges:
        for from_node, to_node, value in self.edges:
            strGraph += from_node
            strGraph += "-- "
            strGraph += value[0]
            strGraph += " ->"
            strGraph += to_node
            strGraph += " "
            strGraph += value[1]
            strGraph += "\n"

        #Display ending display :)

        strGraph += "="*25


        #Return

        return strGraph

    def open_graph(self):
        """ 
        Methode to open and read the map and transform it in graph 
        """
        file = open("cartes_bretagne_-_version_epuree.csv", "r", encoding = 'utf8')
        cbe = file.read()
        cbe = cbe.split("\n")
        del(cbe[0])
        for elt in cbe:
            cbe = elt.split(":")
            if len(cbe) == 4:
                self.add_a_node(cbe[0])
                self.add_a_node(cbe[1])
                self.add_an_edge(cbe[0], cbe[1], (cbe[2], cbe[3]))

G = Graph()
print(G)