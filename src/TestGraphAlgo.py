import unittest

from src.DiGraph import DiGraph
from src.GraphAlgo import GraphAlgo
from src.NodeData import NodeData


class MyTestCase(unittest.TestCase):

    def test_initGraph(self):
        g0 = DiGraph()
        node0 = NodeData(0, (0, 1, 2))
        node1 = NodeData(1, (2.4, 7.1, 3.5))
        g0.add_node(node0.getkey())
        g0.add_node(node1.getkey())
        g1 = GraphAlgo(g0)
        self.assertEqual(g0.v_size(), g1.graph.v_size())

    def test_save_and_load(self):
        g0 = DiGraph()
        node0 = NodeData(0, (0, 1, 2))
        node1 = NodeData(1, (2.4, 7.1, 3.5))
        g0.add_node(node0.getkey())
        g0.add_node(node1.getkey())
        g1 = GraphAlgo(g0)
        g1.save_to_json("graph.json")
        g2 = GraphAlgo()
        g2.load_from_json("graph.json")
        self.assertEqual(g1.graph.v_size(), g2.graph.v_size())

    def test_shortest_path(self):
        g0 = DiGraph()
        node0 = NodeData(0, (0, 1, 2))
        node1 = NodeData(1, (2.4, 7.1, 3.5))
        node2 = NodeData(2, (1, 7, 8))
        node3 = NodeData(3, (7, 1.3, 6.3))

        g0.add_node(node0.getkey())
        g0.add_node(node1.getkey())
        g0.add_node(node2.getkey())
        g0.add_node(node3.getkey())

        g0.add_edge(0, 1, 1)
        g0.add_edge(1, 2, 3)
        g0.add_edge(2, 3, 4)
        g0.add_edge(3, 0, 1)

        g1 = GraphAlgo(g0)

        dist, path = g1.shortest_path(0, 1)
        self.assertEqual(dist, 1)
        dist, path = g1.shortest_path(1, 3)
        self.assertEqual(dist, 7)

    def test_connected_component(self):
        g1 = DiGraph()
        g1.add_node(0, (1, 2, 3))
        g1.add_node(1, (7, 8, 9))
        g1.add_node(2, (2, 1, 7))
        g1.add_node(3, (9, 5, 7))
        g1.add_node(4, (1, 5, 7))
        g1.add_node(5, (2, 3, 7))
        g1.add_node(6, (11, 5, 7))
        g1.add_node(7, (3.78, 7, 7))
        g1.add_edge(0, 1, 1234)
        g1.add_edge(1, 2, 2)
        g1.add_edge(2, 0, 1)
        g1.add_edge(2, 3, 1)
        g1.add_edge(3, 4, 1)
        g1.add_edge(4, 5, 1)
        g1.add_edge(5, 6, 1)
        g1.add_edge(6, 7, 1)
        g1.add_edge(4, 7, 1)
        g1.add_edge(6, 4, 1)
        alg2 = GraphAlgo(g1)
        self.assertEqual(len(alg2.connected_component(0)),3)
        self.assertEqual(len(alg2.connected_component(6)),3)

    def test_connected_components(self):
        g1 = DiGraph()
        g1.add_node(0, (1, 2, 3))
        g1.add_node(1, (7, 8, 9))
        g1.add_node(2, (2, 1, 7))
        g1.add_node(3, (9, 5, 7))
        g1.add_node(4, (1, 5, 7))
        g1.add_node(5, (2, 3, 7))
        g1.add_node(6, (11, 5, 7))
        g1.add_node(7, (3.78, 7, 7))
        g1.add_edge(0, 1, 1234)
        g1.add_edge(1, 2, 2)
        g1.add_edge(2, 0, 1)
        g1.add_edge(2, 3, 1)
        g1.add_edge(3, 4, 1)
        g1.add_edge(4, 5, 1)
        g1.add_edge(5, 6, 1)
        g1.add_edge(6, 7, 1)
        g1.add_edge(4, 7, 1)
        g1.add_edge(6, 4, 1)
        alg2 = GraphAlgo(g1)

        self.assertEqual(len(alg2.connected_components()),4)

if __name__ == '__main__':
    unittest.main()
