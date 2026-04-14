import sys
from pathlib import Path

# Make the `bot` package importable when running `pytest` from the
# forex_bot/ directory or the repository root.
ROOT = Path(__file__).resolve().parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
