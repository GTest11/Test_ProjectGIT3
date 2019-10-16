# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# TestCase ID:
# Description:
# Author:
# Date:
# Version:

# ''''''''''''''''''''AUTOGENERATED CODE - DO NOT MODIFY''''''''''''''''''''
import MobileScriptingLibrary
import clr
import sys
import os
import time
clr.AddReference("MobileScriptingLibrary")
dut = MobileScriptingLibrary.MobileDUT()
logger = MobileScriptingLibrary.Logger()
chkpt = MobileScriptingLibrary.CheckPoint()
config = MobileScriptingLibrary.DeviceConfig()

# ''''''''''''''''''''''''''''''''IMPORTS'''''''''''''''''''''''''''''''''''
# ''''''''''''''''''''''''''''''END IMPORTS'''''''''''''''''''''''''''''''''

# ''''''''''''''''''''''''''''''FOR iOS DEVICE''''''''''''''''''''''''''''''
config.DeviceType = "iOS"
config.AppName = "com.google.ios.youtube"
config.CreateNewServer = "true"

args = sys.argv
scriptPath = os.path.realpath(__file__)
dut.Configure(args[1], args[2], args[3], args[4], scriptPath)
logger.Configure(args[1], args[2], args[3], args[4], scriptPath)

logger.Log("Modified after scheduling a Job")