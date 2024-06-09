from twttr import shorten


def test_cap_vowels():
    assert shorten('HOlA')=='Hl'

def test_punctiations():
    assert shorten('hola?')=='hl?'

def test_numbers():
    assert shorten('HoLa7')=='HL7'

def test_returns_empty():
    assert shorten('aeiouUUoO')==''
