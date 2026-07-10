"""exiobase_concordances: read the published EXIOBASE concordance tables.

"""

from __future__ import annotations

from . import schema
from .loaders import has_wide, list_concordances, load, load_wide

__version__ = "0.1.0"

__all__ = ["load", "load_wide", "list_concordances", "has_wide", "schema"]
