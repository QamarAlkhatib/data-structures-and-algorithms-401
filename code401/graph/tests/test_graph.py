from graph import __version__
from graph.graph import Graph,Vertex,Edge


def test_version():
    assert __version__ == '0.1.0'

def test_add_node():
    graph = Graph()
    graph.add_node("A")
    assert graph.get_sizes() == 1

def test_add_edge_to_graph():
    graph = Graph()
    a = graph.add_node(1)
    b = graph.add_node(10)
    graph.add_edge(a, b, 10)
    actual = graph.get_neighbors(a)
    expected = [10]
    assert expected == actual


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
    actual = graph.get_neighbors(a)
    expected = ['B']
    assert actual == expected


def test_breadth_first():
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)
    actual = g.breadth_first(0)
    expected = actual # which is 0 1 2 3
    assert actual == expected

def test_breadth_first_none():
    g = Graph()
    actual = g.breadth_first(0)
    expected = None # which is edge case
    assert actual == expected