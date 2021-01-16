from GraphInterface import GraphInteface
# import collections
from NodeData import NodeData


class DiGraph(GraphInteface):
    sizeOfEdge = 0
    MC = 0

    # a constractor of the graph
    def __init__(self):
        self.NodeMap = {}
        self.EdgeMap = []

    # this method return the number of the nodes in the graph
    def v_size(self) -> int:
        return len(self.NodeMap)

    # this method return the number of edges in the graph
    def e_size(self) -> int:
        return self.sizeOfEdge

    # the method return all the nodes from the graph
    def get_all_v(self) -> dict:
        return self.NodeMap

    # the method gets a key in the argument and returns
    # all the edges that are connected to this specifed vertex
    def all_in_edges_of_node(self, id1: int) -> dict:
        listofedge = {}
        if id1 in self.NodeMap:
            for i in self.EdgeMap:
                if i[1] == id1:
                    listofedge[i[0]] = i[2]

        return listofedge

    # this method return all the edges that are connected to this node
    def all_out_edges_of_node(self, id1: int) -> dict:
        listofedge = {}
        if id1 in self.NodeMap:
            for i in self.EdgeMap:
                if i[0] == id1:
                    listofedge[i[1]] = i[2]
        return listofedge

    # this method return all the changes that were done
    # on the graph
    def get_mc(self) -> int:
        return self.MC

    # this method gets two keys in the argument and connects
    # them with the weight that is also given in the argument
    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        listofedges = [id1,id2,weight]
        n = self.e_size()
        for i in self.EdgeMap:
            if i[0] == id1 and i[1] == id2 and i[2] != weight:
                i[2] = weight
            elif i[0] == id1 and i[1] == id2 and i[2] == weight:
                return False
        else:
            self.EdgeMap.append(listofedges)
            self.MC +=1
            self.sizeOfEdge +=1
            return True

    # this method gets a key and a position and adds the node
    # with the key that is given in the argument and also
    # updates the position of the node
    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        if node_id not in self.NodeMap:
            node = NodeData(node_id, pos)
            self.NodeMap[node_id] = node
            self.MC = self.MC + 1
            return True

        else:
            return False

    # this method gets a key and removes the specified node
    # with the given key
    def remove_node(self, node_id: int) -> bool:
        for key in self.NodeMap:
            if key == node_id:
                self.NodeMap.pop(node_id)
                self.remove_edge(key, node_id)
                self.MC -=1
                return True
        return False

    # this method gets two keys in the argument and removes the edge
    # between those nodes with the given keys
    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        ans = bool(False)
        place = 0
        for i in self.EdgeMap:
            if i[0] == node_id1 and i[1] == node_id2:
                self.EdgeMap.pop(place)
                self.MC +=1
                self.sizeOfEdge -=1
                ans = True
            elif i[0] == node_id2 and i[1] == node_id1:
                self.EdgeMap.pop(place)
                self.sizeOfEdge -=1
                self.MC +=1
                ans = True
            place = place + 1
        return ans

    # this method prints the node
    def __str__(self):
        return str(self.NodeMap.keys()) +"," + str(self.NodeMap.values())

    def __repr__(self):
        return str(self.NodeMap.keys()) +"," + str(self.NodeMap.values())
