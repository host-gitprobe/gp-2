from demo_greet import greet


def test_greet():
    assert greet("world") == "Hello, world!"
