import unittest

from src.DiGraph import DiGraph
from src.NodeData import NodeData


class MyTestCase(unittest.TestCase):
    def test_AddNode(self):
        g0 = DiGraph()
        node0 = NodeData(0,(0,1,2))
        node1 = NodeData(1, (2.4,7.1,3.5))
        g0.add_node(node0.getkey())
        g0.add_node(node1.getkey())
        self.assertEqual(g0.v_size(),2)

    def test_AddEdge(self):
        g0 = DiGraph()
        node0 = NodeData(0, (0, 1, 2))
        node1 = NodeData(1, (2.4, 7.1, 3.5))
        g0.add_edge(node0.getkey(),node1.getkey(),4)
        self.assertEqual(g0.e_size(),1)

    def test_removeNode(self):
        g0 = DiGraph()
        node0 = NodeData(0, (0, 1, 2))
        node1 = NodeData(1, (2, 7, 3))
        g0.add_node(node0.getkey())
        g0.add_node(node1.getkey())
        g0.remove_node(0)
        self.assertEqual(g0.v_size(),1)

    def test_removeEdge(self):
        g0 = DiGraph()
        node0 = NodeData(0, (0, 1, 2))
        node1 = NodeData(1, (2.4, 7.1, 3.5))
        g0.add_node(node0.getkey())
        g0.add_node(node1.getkey())
        g0.add_edge(node0.getkey(),node1.getkey(),7)
        g0.remove_edge(node0.getkey(),node1.getkey())
        self.assertEqual(g0.e_size(), 1)

    def test_getMC(self):
        g0 = DiGraph()
        node0 = NodeData(0, (0, 1, 2))
        node1 = NodeData(1, (2.4, 7.1, 3.5))
        g0.add_node(node0.getkey())
        g0.add_node(node1.getkey())
        g0.add_edge(node0.getkey(), node1.getkey(), 7)
        g0.remove_edge(node0.getkey(), node1.getkey())
        self.assertEqual(g0.get_mc(), 4)

if __name__ == '__main__':
    unittest.main()

