from typing import List

from GraphAlgoInterface import GraphAlgoInterface
from src import GraphInterface
from src.DiGraph import DiGraph

from src.NodeData import NodeData
import json
import heapq
from matplotlib import pyplot as plt
import random
import math


class GraphAlgo(GraphAlgoInterface):
    graph = GraphInterface

    # a constractor of this class
    def __init__(self, g: DiGraph = DiGraph()):
        if g is None:
            self.graph = DiGraph()
        else:
            self.graph = g

    # this method returns the graph which this class #
    # is working on
    def get_graph(self) -> GraphInterface:
        return self.graph

    # this method loads the graph from a JSON file
    def load_from_json(self, file_name: str) -> bool:
        try:
            with open(file_name ,"r") as file:
                json_file = json.load(file)

            self.graph = DiGraph()

            for i in json_file.get("Nodes"):
                if i.get("pos") is None:

                    self.graph.add_node(i.get("id"))
                else:
                    postion = i.get("pos").split(",")
                    pos = tuple(map(float, postion))
                    self.graph.add_node(i.get("id"), pos)
            for i in json_file.get("Edges"):
                self.graph.add_edge(i.get("src"), i.get("dest") ,i.get("w"))
            return True
        except FileNotFoundError:
            return False

    # this method saves the graph as a JSON file
    def save_to_json(self, file_name: str) -> bool:
        nodesarray = []
        Edgearray = []
        grapharray = {}
        for i in self.graph.get_all_v().values():
            node: NodeData = i
            if node.pos is None:
                nodesarray.append({"id": node.getkey()})
            else:
                stringofpos = str(str(node.pos[0])+","+str(node.pos[1])+","+str(node.pos[2]))
                nodesarray.append({"pos": stringofpos, "id": node.getkey()})
        for i in self.graph.get_all_v():
            for j ,v in self.graph.all_out_edges_of_node(i).items():
                Edgearray.append({"src": i, "dest": j ,"w":v })

        grapharray = {"Nodes": nodesarray,"Edges": Edgearray }

        try:
            with open(file_name, "w") as json_file:
                json.dump(grapharray,json_file)
                return True
        except FileNotFoundError:
            return False

    # this method gets two keys in the argument and returns
    # the shortest path between the nodes which their keys
    # were given in the argument.
    def shortest_path(self, id1: int, id2: int) -> (float, list):
        self.graph.NodeMap[id1].distance = 0
        unvisited = []
        for k in self.graph.NodeMap.keys():
            unvisited.append(k)
            heapq.heapify(unvisited)
        while len(unvisited) > 0:
            v = heapq.heappop(unvisited)
            dicc = self.graph.all_out_edges_of_node(v)
            for neighbour in dicc.keys():
                neighbour_vertex, neighbour_distance = (neighbour, dicc[neighbour])
                distance = self.graph.NodeMap[v].distance + neighbour_distance
                if distance < self.graph.NodeMap[neighbour_vertex].distance:
                    self.graph.NodeMap[neighbour_vertex].distance = distance
                    self.graph.NodeMap[neighbour_vertex].previous = v
                    heapq.heapify(unvisited)
        retdict = (self.graph.NodeMap[id2].distance, [self.graph.NodeMap[id2].key])
        tmp = self.graph.NodeMap[id2]

        while tmp is not NodeData:
            try:
                retdict[1].append(tmp.previous)
                tmp = self.graph.NodeMap[tmp.previous]
            except KeyError:
                retdict[1].pop()
                res = (self.graph.NodeMap[id2].distance,retdict[1][::-1])
                return res


        return retdict

    # this method resets all the visited value of the nodes
    # that were added to the graph
    # the use of this method is in the connected_components method
    # and in connected_component method
    def clearV(self):
        for key in self.graph.NodeMap.keys():
            self.graph.NodeMap[key].visited = False

    # this method return a list of all the nodes from this graph
    # the use of this method is in the connected_components method
    # and in connected_component method
    def kickassfunc(self, stack: [], id1: int):
        if self.graph.NodeMap[id1].visited is False:
            self.graph.NodeMap[id1].visited = True
            neighbours = self.graph.all_out_edges_of_node(id1)
            for n in neighbours.keys():
                self.kickassfunc(stack, n)
            stack.append(id1)
        return stack

    # this method returns the list of all the (SCC) in this graph
    # the use of this method is in the connected_components method
    # and in connected_component method
    def afterreversed(self, stack: [], g, scc: [], sccbyind: [], curr: int):
        if g.NodeMap[curr].visited is False:
            g.NodeMap[curr].visited = True
            sccbyind.append(curr)
            neighbours = g.all_out_edges_of_node(curr)
            for n in neighbours.keys():
                if self.graph.NodeMap[n].visited is False:
                    self.afterreversed(stack, g, scc, sccbyind, n)
            nsccbyind = []
            length = len(stack)
            try:
                if sccbyind not in scc:
                    scc.append(sccbyind)
                d = stack.pop(length - 1)
                self.afterreversed(stack, g,scc, nsccbyind, d)
            except IndexError:
                return scc

        return scc

    # this method makes a a reversed graph
    # the use of this method is in the connected_components method
    # and in connected_component method
    def reversegraph(self, graph):
        newgraph = DiGraph()
        for n in self.graph.NodeMap.keys():
            newgraph.add_node(n)
        for i in self.graph.NodeMap.keys():
            for e in self.graph.all_out_edges_of_node(i).keys():
                newgraph.add_edge(e, i, self.graph.all_out_edges_of_node(i).get(e))
        return newgraph

    # this method return a list of all the Strongly Connected Components in the graph
    def connected_components(self):
        stack = []
        firstelem = list(self.graph.NodeMap.keys())[0]
        nums = self.kickassfunc(stack, firstelem)
        lent = len(nums)
        firstpoped = nums.pop(lent-1)
        self.clearV()
        g = self.reversegraph(self.graph)
        scc = []
        sccbyind = []
        scc = self.afterreversed(nums, g, scc, sccbyind, firstpoped)
        self.clearV()
        return scc

    # this method gets a key in the argument and returns all the
    # Strongly Connected Component that this node with the specified key
    # that is given in the argument taking part of
    def connected_component(self, id1: int):
        lstx = self.connected_components()
        lstret = []
        lent = len(lstx)
        for i in lstx:
            if id1 in i:
                return i
        return lstret

    # this method shows the graph (all the nodes and all the edges)
    # on a graphic window
    def plot_graph(self) -> None:
        xver = []
        yver = []
        max_x = 0
        min_x = math.inf
        max_y = 0
        min_y = math.inf
        for key in self.graph.NodeMap.keys():  # draws all nodes that have pos
            if self.graph.NodeMap.get(key).pos is not None:
                xver.append(self.graph.NodeMap.get(key).pos[0])
                yver.append(self.graph.NodeMap.get(key).pos[1])
                if self.graph.NodeMap.get(key).pos[0] > max_x:
                    max_x = self.graph.NodeMap.get(key).pos[0]
                if self.graph.NodeMap.get(key).pos[0] < min_x:
                    min_x = self.graph.NodeMap.get(key).pos[0]
                if self.graph.NodeMap.get(key).pos[1] > max_y:
                    max_y = self.graph.NodeMap.get(key).pos[1]
                if self.graph.NodeMap.get(key).pos[1] < min_y:
                    min_y = self.graph.NodeMap.get(key).pos[1]
            else:
                r_x = random.uniform(0, 100)
                r_y = random.uniform(0, 100)
                self.graph.NodeMap.get(key).pos = (r_x, r_y, 0)
                xver.append(self.graph.NodeMap.get(key).pos[0])
                yver.append(self.graph.NodeMap.get(key).pos[1])
        plt.plot(xver, yver, "og", markersize=8)  # draws the nodes
        for k in self.graph.NodeMap.keys():
            src_x = self.graph.NodeMap.get(k).pos[0]
            src_y = self.graph.NodeMap.get(k).pos[1]
            for neighbour in self.graph.all_out_edges_of_node(k):
                dest_x = self.graph.NodeMap.get(neighbour).pos[0]
                dest_y = self.graph.NodeMap.get(neighbour).pos[1]
                plt.arrow(src_x, src_y, dest_x - src_x, dest_y - src_y)

        plt.show()

