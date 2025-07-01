##############################
# Module to write MCDC input #
##############################
import logging
import math
from datetime import datetime
from pathlib import Path
from importlib.metadata import version

import FreeCAD

from ..utils.basic_functions_part1 import is_opposite, points_to_coeffs
from ..utils.functions import SurfacesDict
from .functions import CardLine, change_surf_sign, mcdc_surface, write_mcdc_cell_def

logger = logging.getLogger("general_logger")