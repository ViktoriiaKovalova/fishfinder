from dataclasses import dataclass
from enum import Enum


class Diet(Enum):
    HERBIVOROUS = 1
    CARNIVOROUS = 2
    OMNIVOROUS = 3


@dataclass
class Fish:
    id: int = None
    name: str = None
    lifespan: float = None
    mass: float = None
    diet: Diet = None
    length: float = None
    height: float = None
    color: tuple = None
    length_fin: float = None
    height_fin: float = None


def str2diet(diet: str):
    return {'omnivorous': Diet.OMNIVOROUS, 'herbivorous': Diet.HERBIVOROUS, 'carnivorous': Diet.CARNIVOROUS}[diet]
