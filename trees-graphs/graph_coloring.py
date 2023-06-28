class GraphNode:

    def __init__(self, label):
        self.label = label
        self.neighbors = set()
        self.color = None


def color_graph(graph, colors):

    # Create a valid coloring for the graph
    illegal=[]
    
    for node in graph:
        
        for neigh in node.neighbors:
            if neigh == node:
                raise Exception("error")
            if neigh.color:
                illegal.append(neigh.color)
        
        
        for color in colors:
            if color not in illegal:
                node.color = color
                break
        illegal=[]
           

    return 0