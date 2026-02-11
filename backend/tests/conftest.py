import sys
from pathlib import Path
import pytest
from fastapi.testclient import TestClient

# Add backend directory to sys.path so 'app' and 'main' can be found
backend_path = Path(__file__).parent.parent
sys.path.append(str(backend_path))

from main import app

@pytest.fixture
def client():
    with TestClient(app) as c:
        yield c
