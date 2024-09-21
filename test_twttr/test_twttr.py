from twttr import shorten


def test_assert():
    assert shorten("HELLO WORLD") == "HLL WRLD"
    assert shorten("hello world") == "hll wrld"
    assert shorten("he110 world") == "h110 wrld"
    assert shorten("h!llo wor@d!!!") == "h!ll wr@d!!!"
