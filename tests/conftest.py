import pytest
import os
import sys
import shutil

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import app
from app import app as flask_app, DATA_DIR


@pytest.fixture
def client():
    flask_app.config["TESTING"] = True

    if DATA_DIR.exists():
        shutil.rmtree(DATA_DIR)
    DATA_DIR.mkdir()

    with flask_app.test_client() as client:
        yield client
