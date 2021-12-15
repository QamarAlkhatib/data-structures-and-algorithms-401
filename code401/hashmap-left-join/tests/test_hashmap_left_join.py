from hashmap_left_join import __version__
from hashmap_left_join.left_join import left_join

def test_version():
    assert __version__ == '0.1.0'

def test_result():
    h1 = {
        'diligent':'employed'
    }

    h2 = {
        'diligent':'idle'
    }

    actual = left_join(h1,h2)
    expected = [['diligent', 'employed', 'idle']]
    assert actual == expected

def test_None():
    h1 = {
        'diligent':'employed'
    }

    h2 = {
        'flow':'idle'
    }

    actual = left_join(h1,h2)
    expected = [['diligent', 'employed', None]]
    assert actual == expected

def test_all():
    h1 = {
    'diligent':'employed',
    'fond':'enamored',
    'guide': 'usher',
    'outfit': 'garb',
    'wrath':'anger'
    }

    h2 = {
        'diligent':'idle',
        'fond':'averse',
        'guide': 'follow',
        'flow': 'jam',
        'wrath':'delight'
    }

    actual = left_join(h1,h2)
    expected = [['diligent', 'employed', 'idle'], ['fond', 'enamored', 'averse'], ['guide', 'usher', 'follow'], ['outfit', 'garb', None], ['wrath', 'anger', 'delight']]
    assert actual == expected