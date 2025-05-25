import sys
from typing import Dict, Any, Optional

try:
    if sys.version_info >= (3, 11):
        import tomllib
    else:
        import tomli as tomllib
except ImportError:
    raise ImportError("tomli is required for Python < 3.11")

def load_project_metadata() -> Dict[str, Any]:
    """Load project metadata from pyproject.toml"""
    try:
        with open("pyproject.toml", "rb") as f:
            data = tomllib.load(f)
            
        return data.get("project", {})
    except FileNotFoundError:
        raise FileNotFoundError("pyproject.toml not found in the current directory")
    except Exception as e:
        raise Exception(f"Error loading project metadata: {str(e)}")