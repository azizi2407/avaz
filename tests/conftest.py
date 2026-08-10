import importlib.util
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parents[1]
SCRIPT = REPO / "scripts" / "analyze_turkish.py"


@pytest.fixture(scope="session")
def az():
    """Betiği modül olarak yükle; paket kurulumu gerektirmez."""
    spec = importlib.util.spec_from_file_location("analyze_turkish", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    sys.modules["analyze_turkish"] = module
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope="session")
def script_path():
    return SCRIPT


@pytest.fixture(scope="session")
def repo():
    return REPO
