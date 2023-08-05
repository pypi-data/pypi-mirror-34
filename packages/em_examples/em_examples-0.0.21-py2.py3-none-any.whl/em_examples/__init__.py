from __future__ import print_function
from __future__ import absolute_import
from __future__ import unicode_literals
import sys

from . import Attenuation
from . import BiotSavart
from . import CondUtils
from . import DC_cylinder
from . import DCLayers
from . import DCsphere
from . import DC_Pseudosections
from . import DCIP_overburden_PseudoSection
from . import DCWidget_Overburden_2_5D
from . import DCWidgetPlate2_5D
from . import DCWidgetPlate_2D
from . import DCWidgetResLayer2_5D
from . import DCWidgetResLayer2D
from . import DipoleWidget1D
from . import DipoleWidgetFD
from . import DipoleWidgetTD
from . import EMcircuit
from . import FDEMDipolarfields
from . import FDEMPlanewave
from . import FreqtoTime
from . import HarmonicVMDCylWidget
from . import InductionLoop
from . import InductionSphereFEM
from . import InductionSphereTEM
from . import Loop
from . import MT
from . import PlanewaveWidgetFD
from . import Reflection
from . import sphereElectrostatic_example
from . import TransientVMDCylWidget
from . import View
from . import VolumeWidget
from . import VolumeWidgetPlane
if sys.version_info[0] > 2:
    from . import MarineCSEM1D
from . import TDEMGroundedSource
from . import LinearInversion

__version__ = '0.0.21'
__author__ = 'GeoScixyz developers'
__license__ = 'MIT'
__copyright__ = 'Copyright 2017 GeoScixyz developers'
