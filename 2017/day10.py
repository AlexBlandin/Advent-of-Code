from itertools import count
from pathlib import Path
from typing import SupportsIndex

from circular import Circular

lst = Path("day10.txt").read_text().strip().split(",")
