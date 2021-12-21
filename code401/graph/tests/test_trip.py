from graph import __version__

from graph.graph import Graph,Vertex,business_trip

def test_trip_cost():
    graph = Graph()
    a = graph.add_node('Pandora')
    b = graph.add_node('Arendelle')
    c = graph.add_node('Metroville')
    d = graph.add_node('Monstropolis')
    e = graph.add_node('Narnia')
    f = graph.add_node('Naboo')
    graph.add_edge(b,d,42)
    graph.add_edge(a,b,150)
    graph.add_edge(a,c,82)
    graph.add_edge(b,c,99)
    graph.add_edge(c,e,37)
    graph.add_edge(c,d,105)
    graph.add_edge(d,f,73)
    graph.add_edge(e,f,250)
    graph.add_edge(c,f,26)
    cities = [a,b,c]
    actual = business_trip(graph,cities)
    expected = actual
    assert expected == actual
    

def test_trip_cost_false():
    graph = Graph()
    a = graph.add_node('Pandora')
    b = graph.add_node('Arendelle')
    c = graph.add_node('Metroville')
    d = graph.add_node('Monstropolis')
    e = graph.add_node('Narnia')
    f = graph.add_node('Naboo')
    graph.add_edge(b,d,42)
    graph.add_edge(a,b,150)
    graph.add_edge(a,c,82)
    graph.add_edge(b,c,99)
    graph.add_edge(c,e,37)
    graph.add_edge(c,d,105)
    graph.add_edge(d,f,73)
    graph.add_edge(e,f,250)
    graph.add_edge(c,f,26)
    cities = [a,d,c]
    assert business_trip(graph,cities) == (False, '$0')