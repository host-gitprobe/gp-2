"""Return a friendly greeting."""


def greet(name: str) -> str:
    if not isinstance(name, str) or not name:
        raise ValueError("name must be a non-empty string")
    return f"Hello, {name}!"
