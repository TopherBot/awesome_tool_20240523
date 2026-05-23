import os
from awesome_tool.services import greet
from awesome_tool.config import load_config

def test_greet_uses_default_prefix(monkeypatch):
    monkeypatch.delenv("GREETING_PREFIX", raising=False)
    assert greet("Bob") == "Hello, Bob!"

def test_greet_respects_env_prefix(monkeypatch):
    monkeypatch.setenv("GREETING_PREFIX", "Hi")
    assert greet("Bob") == "Hi, Bob!"
