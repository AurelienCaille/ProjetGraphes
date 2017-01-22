from copy import deepcopy

class Graph(object):
    """
    Class representing a graph
    """
    def __init__(self):

        self.nodes = set()
        self.edges = []
        self.adjacency_list = {}


    def add_a_node(self, node_name):
        """
        Add a node to the current graph
        Param:
        node_name : string, representing the name of the node
        """

        self.nodes.add(node_name)
        self.adjacency_list[node_name] = self.adjacency_list.get(node_name, [])

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
        else:
            raise NameError('Nodes dosnt exist in this current graph')

    def composantes_connexes(self, departure):
        """
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

    def depth_first_search(self, departure):
        """
        Make a journey from the "departure" in the graph
        use depth method
        return a parent tree (dictonary)
        """

        parents = {}
        colors = {}
        lifo = []

        lifo.append(departure)
        parents[departure] = None

        for node in self.nodes:
            colors[node] = "white"

        while len(lifo) != False:
            actual = lifo[-1]

            new_child = 0

            #Add new node in the lifo list
            for child in self.adjacency_list[actual]:
                if colors[child] == "white":

                    lifo.append(child)
                    colors[child] == "grey"
                    parents[child] = parents.get(child, actual)

                    new_child += 1

            colors[actual] = "black"
            lifo.remove(actual)


            #Check if lifo list empty but still rest node to search

            if ((len(lifo) == False) and \
                (not all(color == "black" for color in colors.values()))):

                for node in sorted(self.nodes):
                    if colors[node] == "white":
                        lifo.append(node)
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
            strGraph += value
            strGraph += " ->"
            strGraph += to_node
            strGraph += "\n"

        #Display ending display :)

        strGraph += "="*25


        #Return

        return strGraph


        
        

        

        
            

        

        
        
