#!/usr/bin/env python

"""Test the mpu.datastructures.trie module."""

# Third party
import pytest

# First party
from mpu.datastructures.trie import Trie as DefaultTrie
from mpu.datastructures.trie.base import AbstractTrie
from mpu.datastructures.trie.char_trie import Trie as CharTrie
from mpu.datastructures.trie.full_prefix_dict import FullPrefixDict
from mpu.datastructures.trie.string_trie import Trie as StringTrie

all_tries = [CharTrie, StringTrie, FullPrefixDict, DefaultTrie]


def test_abstract_trie():
    with pytest.raises(TypeError) as exinfo:
        trie = AbstractTrie()
    msg = (
        "Can't instantiate abstract class AbstractTrie with abstract "
        "methods __contains__, __iter__, __len__, autocomplete"
    )
    assert str(exinfo.value) == msg


@pytest.mark.parametrize("Trie", all_tries)
def test_trie_creation(Trie):
    data = ["dog", "cat", "cattle", "tom", "dinosaur", "tomcat", "tomatoe"]
    trie = Trie(data)
    assert {element for element in trie} == set(data)


@pytest.mark.parametrize("Trie", all_tries)
def test_trie_add_same(Trie):
    trie = Trie(["dog", "cat", "dog"])
    assert sorted(word for word in trie) == ["cat", "dog", "dog"]


@pytest.mark.parametrize("Trie", all_tries)
def test_empty_trie_iter_empty(Trie):
    trie = Trie()
    assert [word for word in trie] == []


@pytest.mark.parametrize("Trie", all_tries)
def test_contains(Trie):
    words = ["dog", "cat", "cattle", "tom", "d", "tomcat", "tomatoe"]
    trie = Trie(words)
    for word in words:
        assert word in trie

    words = [
        "creeker",
        "creekfish",
        "creekfishes",
        "Creeks",
        "creekside",
        "creekstuff",
        "creeky",
    ]
    trie = Trie(words)
    for word in words:
        assert word in trie


@pytest.mark.parametrize("Trie", all_tries)
def test_len_initialization(Trie):
    words = ["dog", "cat", "cattle", "tom", "d", "tomcat", "tomatoe"]
    trie = Trie(words)
    assert len(trie) == len(words)


@pytest.mark.parametrize("Trie", all_tries)
def test_len_push(Trie):
    words = ["dog", "cat", "cattle", "tom", "d", "tomcat", "tomatoe"]
    trie = Trie()
    for word in words:
        trie.push(word)
    assert len(trie) == len(words)


@pytest.mark.parametrize("Trie", all_tries)
def test_autocomplete_empty(Trie):
    trie = Trie()
    assert list(trie.autocomplete("")) == []


@pytest.mark.parametrize("Trie", all_tries)
def test_contains_empty_true(Trie):
    trie = Trie([""])
    assert "" in trie


@pytest.mark.parametrize("Trie", all_tries)
def test_contains_empty_false(Trie):
    trie = Trie(["foo"])
    assert "" not in trie
