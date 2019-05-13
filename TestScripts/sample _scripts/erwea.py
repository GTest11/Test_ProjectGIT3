import clr, sys, os
clr.AddReference("MobileScriptingLibrary")
import MobileScriptingLibrary
logger = MobileScriptingLibrary.Logger()
args = sys.argv
scriptPath = os.path.realpath(__file__)
logger.Configure(args[1], args[2], args[3], args[4], scriptPath)

logger.Log("successfully pushed qoe data to DB")