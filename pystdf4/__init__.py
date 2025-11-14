from pathlib import Path

import tomli as toml

from .IO.stfd4write import Stfd4Writer

pyproject = toml.loads((Path(__file__).parent.parent / "pyproject.toml").read_text())
__version__ = pyproject["project"]["version"]
__all__ = ["Stfd4Writer"]
