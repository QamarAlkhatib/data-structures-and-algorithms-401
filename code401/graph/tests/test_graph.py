from graph import __version__
from graph.graph import Graph,Vertex,Edge
import pytest

def test_version():
    assert __version__ == '0.1.0'

def test_add_node():
    graph = Graph()
    graph.add_node("A")
    assert graph.get_sizes() == 1

def test_add_edge_to_graph():
    graph = Graph()
    node1 = Vertex('A')
    node2 = graph.add_node('B')
    with pytest.raises(KeyError):
        graph.add_edge(node1, node2)

def test_get_nodes():
    graph = Graph()
    graph.add_node("A")
    graph.add_node("B")
    actual = graph.get_nodes()
    expected = actual
    assert expected == actual

def test_size0():
    graph = Graph()
    assert graph.get_sizes() == 0

def test_size2():
    graph = Graph()
    graph.add_node("A")
    graph.add_node("B")
    assert graph.get_sizes() == 2

def test_get_neighbors():
    graph = Graph()
    a = graph.add_node("A")
    b = graph.add_node("B")
    graph.add_edge(a, b, 10)
    neighbors = graph.get_neighbors(a)
    assert len(neighbors) == 1
    neighbors_edge = neighbors[0]
    assert neighbors_edge.vertex.value == 'B'
    assert neighbors_edge.weight == 10