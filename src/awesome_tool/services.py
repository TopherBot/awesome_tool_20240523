from .models import Person
from .config import load_config

def greet(name: str) -> str:
    """Generate a greeting string using configuration.

    Parameters
    ----------
    name: str
        Name of the person to greet.
    """
    cfg = load_config()
    prefix = cfg.get("GREETING_PREFIX", "Hello")
    person = Person(name=name)
    return f"{prefix}, {person.name}!"
