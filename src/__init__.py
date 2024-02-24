import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

import pygame
from pygame.locals import *
import sys

from .scripts.math import *
from .scripts.exceptions import *
from .image_types import *
from .loaders import *

from .shapes import *
from .sprites import *
from .scripts.group import *

from .scripts.collision import *

from .scripts.loop import *

from .config import *

print("Welcome! (SwitchGame: v0.1.0)")