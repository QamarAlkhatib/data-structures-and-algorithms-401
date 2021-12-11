from hash_table import __version__
import pytest
from hash_table.hash_tables import HashTable


def test_version():
    assert __version__ == '0.1.0'

def test_add(hash_table):
    hash_table.add("Dog",10)
    actual = hash_table.num_elements
    expected = 4
    assert actual == expected

def test_get_key_hash(hash_table):
    actual = hash_table.get('Cat')
    expected = 80
    assert actual == expected

def test_size_hash(hash_table):
    actual = hash_table.num_elements
    expected = 3
    assert actual == expected

def test_key_not_exists(hash_table):
    actual = hash_table.get('some key')
    expected =  "KeyError"
    assert actual == expected

def test_key_is_contains(hash_table):
    actual = hash_table.contains('Oscar')
    expected =  True
    assert actual == expected


def test_key_is_not_contains(hash_table):
    actual = hash_table.contains('some key')
    expected =  False
    assert actual == expected

def test_hashed(hash_table):
    actual = hash_table.hash('Fofo')
    expected = 318
    assert actual == expected

def test_collision(hash_table):
    hash_table.add("Cat",2)
    actual = hash_table.get('Cat')
    expected = 2
    assert actual == expected

@pytest.fixture
def hash_table():
    Hash_table = HashTable()
    Hash_table.add("Cat",80)
    Hash_table.add("Fofo",30)
    Hash_table.add("Oscar",20)
    return Hash_table

