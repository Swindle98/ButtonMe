import importlib
import types
import pytest
from ButtonMe import main

def _reload_main():
    importlib.reload(main)
    from ButtonMe.main import run  # relative import as required
    return run

def test_run_raises_when_no_functions():
    run = _reload_main()
    # Ensure explicit empty functions list to test the ValueError path
    main.functions = []
    with pytest.raises(ValueError):
        run()

def test_run_initializes_qapplication_and_window_and_calls_exit():
    run = _reload_main()

    # Prepare a dummy function registration so run proceeds
    def sample(): 
        return "ok"
    main.functions = [(sample, (), {})]

    # Dummy QApplication to capture argv and provide exec() return value
    class DummyQApplication:
        instantiated = False
        argv_passed = None
        def __init__(self, argv):
            DummyQApplication.instantiated = True
            DummyQApplication.argv_passed = argv
        def exec(self):
            return 99

    # Dummy window to capture constructor args and show() call
    class DummyWindow:
        constructed = False
        title = None
        functions = None
        shown = False
        def __init__(self, title, functions):
            DummyWindow.constructed = True
            DummyWindow.title = title
            DummyWindow.functions = functions
        def show(self):
            DummyWindow.shown = True

    # Replace GUI-related objects in the module under test
    main.QApplication = DummyQApplication
    main.ButtonMeApp = DummyWindow

    # Capture calls to sys.exit without actually exiting the test process
    exit_called = {}
    def fake_exit(code):
        exit_called['code'] = code
    main.sys.exit = fake_exit

    # Call run and assert behavior
    run(title="My Test Title")

    assert DummyQApplication.instantiated is True
    assert DummyWindow.constructed is True
    assert DummyWindow.title == "My Test Title"
    # functions passed to window should be the same object we set on the module
    assert DummyWindow.functions is main.functions
    # show() should have been called
    assert DummyWindow.shown is True
    # sys.exit should have been called with the value returned by exec()
    assert exit_called.get('code') == 99