from typing import List, Type

from .MyCog import MyCog
from .MoveCommands import MoveCommands
from .MoveSlashCommands import MoveSlashCommands

cogs: List[Type[MyCog]] = [MoveCommands, MoveSlashCommands]

__all__ = ["cogs"]
