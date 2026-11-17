import sys
from importlib.metadata import PackageNotFoundError, metadata as package_metadata, version as package_version
from pathlib import Path
from typing import Dict, Any, Optional

try:
    if sys.version_info >= (3, 11):
        import tomllib
    else:
        import tomli as tomllib
except ImportError:
    raise ImportError("tomli is required for Python < 3.11")

_metadata_cache: Optional[Dict[str, Any]] = None

# [tool.internalurls] is not copied into an installed wheel. These values
# match pyproject.toml and are used only for that installed copy.
_INSTALLED_INTERNAL_URLS = {
    "author_username": "ysskrishna",
    "author_name": "Y. Siva Sai Krishna",
    "author_github": "https://github.com/ysskrishna",
    "author_linkedin": "https://linkedin.com/in/ysskrishna",
}


def _parse_pyproject(path: Path) -> Dict[str, Any]:
    try:
        with path.open("rb") as f:
            return tomllib.load(f)
    except FileNotFoundError:
        raise FileNotFoundError(f"{path} not found.")
    except tomllib.TOMLDecodeError as e:
        raise ValueError(f"Error parsing TOML: {e}")
    except Exception as e:
        raise Exception(f"Unexpected error reading {path}: {e}")


def _project_urls(meta) -> Dict[str, str]:
    urls = {}
    for entry in meta.get_all("Project-URL") or []:
        label, separator, url = entry.partition(",")
        if separator:
            urls[label.strip()] = url.strip()
    return urls


def _from_installed_distribution() -> Dict[str, Any]:
    meta = package_metadata("dbconvert")
    urls = _project_urls(meta)
    return {
        "internalurls": dict(_INSTALLED_INTERNAL_URLS),
        "repository": urls.get("Repository", ""),
        "name": meta.get("Name", ""),
        "version": package_version("dbconvert"),
    }


def _from_source_pyproject(path: Path) -> Dict[str, Any]:
    data = _parse_pyproject(path)
    return {
        "internalurls": data.get("tool", {}).get("internalurls", {}),
        "repository": data.get("project", {}).get("urls", {}).get("Repository", ""),
        "name": data.get("project", {}).get("name", ""),
        "version": data.get("project", {}).get("version", ""),
    }


def load_pyproject_metadata() -> Dict[str, Any]:
    """Return the project name, version, repository, and author links.

    A source checkout reads pyproject.toml two directories above this
    module, so the current working directory does not matter. An installed
    copy has no pyproject.toml; its version comes from
    importlib.metadata.version("dbconvert").
    """
    global _metadata_cache
    if _metadata_cache is not None:
        return _metadata_cache

    source_pyproject = Path(__file__).resolve().parents[2] / "pyproject.toml"
    if source_pyproject.is_file():
        _metadata_cache = _from_source_pyproject(source_pyproject)
        return _metadata_cache

    try:
        _metadata_cache = _from_installed_distribution()
    except PackageNotFoundError as exc:
        raise FileNotFoundError(
            "dbconvert package metadata was not found, and pyproject.toml is not beside the source tree."
        ) from exc
    return _metadata_cache
