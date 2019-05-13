#***FalconEyeCUBE - Logger module for FCPE-DBS and FCPE-CUBE interactions
#*************************************************************************************************************************************************
#@Author : Rithumol R S
#@Version: FalconEyeCUBE version 2.0
#@Date   : 27-02-2018
#*************************************************************************************************************************************************


import logging
import sys
import os
import os.path
import datetime
from logging.handlers import TimedRotatingFileHandler


log = logging.getLogger()
log.setLevel(logging.DEBUG)
logFormatter = logging.Formatter("%(asctime)s :[%(filename)s]:[%(funcName)s]:[%(lineno)s][%(levelname)s] --> %(message)s")

log_folder = sys.executable[0:sys.executable.rfind('\\')] + r'\ScriptingLibraryLogs\CubeLogs'

if not os.path.exists(log_folder):
	os.makedirs(log_folder)
else:
	pass

fileHandler = TimedRotatingFileHandler(log_folder+"\CubeLog", when="midnight", interval=1)
fileHandler.setFormatter(logFormatter)

log.addHandler(fileHandler)
