import importlib
from ButtonMe import buttonize
import pytest


def test_buttonize_registers_and_returns_function():
    buttonize = _reload_main()
    def sample(): 
        return "ok"
    returned = buttonize(sample, 1, b=2)
    assert returned is sample
    assert hasattr(main, "functions")
    fn, args, kwargs = main.functions[-1]
    assert fn is sample
    assert args == (1,)
    assert kwargs == {"b": 2}

def test_buttonize_accumulates_multiple_registrations():
    buttonize = _reload_main()
    def a(): pass
    def b(): pass
    buttonize(a)
    buttonize(b, 42)
    assert main.functions[0][0] is a
    assert main.functions[1][0] is b
    assert main.functions[1][1] == (42,)

def test_buttonize_prints_registration_message(capsys):
    buttonize = _reload_main()
    def f(): pass
    buttonize(f)
    captured = capsys.readouterr()
    assert "Registered function: f" in captured.out