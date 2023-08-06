# -*- coding: utf-8 -*-
VERSION = "0.2.1"
RELEASE = VERSION + "b1"
PACKAGENAME = "pygeostandards"
AUTHOR = "Matteo Angeloni"
AUTHOR_EMAIL = "mattange@gmail.com"
COPYRIGHT = "2018, " + AUTHOR

from pathlib import Path
PACKAGEDIR = Path(__file__).parent
DATADIR = 'database'
DATABASEDIR = PACKAGEDIR / DATADIR


