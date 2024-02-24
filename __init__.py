"""Switch Game - is an Engine to create games based on python.
It supports many sprites like a StaticSprite, AnimatedSprite, AbsoluteSprite and
many useful classes such as Image, Animation, Tileset and other.
This project is in development, but you can already use it in your games."""

import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

import pygame
from pygame.locals import *
import sys

from .scripts.math import *
from .scripts.exceptions import *
from .scripts.image import *

# from .scripts.event import *
from .scripts.shape import *
from .scripts.sprites import *
from .scripts.group import *

from .scripts.collision import *

from .scripts.loop import *

from .config import *

print("Welcome! (SwitchGame: v0.1)")