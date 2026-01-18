from pathlib import Path
import sys

# Ensure the `src` directory is on sys.path so imports work during tests
ROOT = Path(__file__).resolve().parents[1]
SRC_DIR = ROOT / "src"
sys.path.insert(0, str(SRC_DIR))

from managers import TodoManager, AuthManager
from models import TodoItem, Priority, Status


def test_mark_completed():
    data_dir = Path("data_test")
    # ensure clean test dir
    if data_dir.exists():
        for f in data_dir.iterdir():
            f.unlink()
    else:
        data_dir.mkdir()

    auth = AuthManager(data_dir=str(data_dir))
    todo_mgr = TodoManager(data_dir=str(data_dir))

    # create user and todo
    username = "tester"
    assert auth.sign_up(username, "pass")

    todo = todo_mgr.create_todo(
        title="Test todo",
        details="details",
        priority=Priority.HIGH,
        owner=username,
    )

    # assert initially pending
    assert todo.status == Status.PENDING

    # mark as completed
    ok = todo_mgr.mark_as_completed(todo.id, username)
    assert ok, "mark_as_completed returned False"

    # reload and check status
    reloaded = todo_mgr.get_todo_by_id(todo.id)
    assert reloaded is not None
    assert reloaded.status == Status.COMPLETED
