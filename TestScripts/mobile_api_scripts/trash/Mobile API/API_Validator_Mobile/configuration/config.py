#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#TestScript ID  : FE_STB_API_Config
#Description    : config parameters for STB API test scripts
#Author         : Arya L
#Date           : 12 Mar 2018, 22 MArch 2018
#Script Version : 2.0
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#USER DEFINED VARIABLES AND CONFIG VALUES
################################################################################
import sys, os

sys.path.append('../')

#importing user defined modules
try:
    from configuration.constants import *
except ImportError:
    comLib.logger.Warn("Failed to import constants in config file")
    sys.exit()

try:
    from configuration.coordinates import *
except ImportError:
    comLib.logger.Log("Failed to import coordinates in config file")
    sys.exit()
# KEYS
################################################################################
#Roku and sky box keys
homeKey = "Home"
SkyMuteKey = "Mute"
SkyVolumeUpkey = "VolUp"
exitKey = "Back"
selectKey = "Ok"
skyExitKey = "Exit"
skySelectKey = "Select"



#CHECKPOINTS
################################################################################
#For validateCheckPoint.py, March 15 2018
VictoriaValidateCheckPointOCR = "Mobile_YouTube"
VictoriaValidateCheckPointMultiOCR = "valMultiOcrVictoriaHome"
VictoriaValidateCheckPointICpixel = "valIcPixelVictoriaHome"
VictoriaValidateCheckPointICrmsel = "valIcRmseVictoriaHome"

SkyValidateCheckPointOCR = "Mobile_YouTube"#"valOcrSkyHome"
SkyValidateCheckPointMultiOCR = "valMultiOcrSkyHome"
SkyValidateCheckPointICpixel = "valIcPixelSkyHome"
SkyValidateCheckPointICrmsel = "valIcRmseSkyHome"

#ImageSearch
imageSearchSingleOccurance = "CheckpointPatternSingleOccurance"
imageSearchMultipleOccurance = "CheckpointPatternMultipleOccurance"

#For GetScreenTransitionTime.py and WaitForCheckpoint.py, March 19 2018
#Both are same checkpoint, but different name is used in different script
CheckpointScreenForTransition = "GetScreenTransitionCheck"
CheckpointScreenToWait = "Mobile_YouTube" #"GetScreenTransitionCheck"#"CheckpointScreenToWait"


#SCREEN REGION CHECKPOINT MAPPING
################################################################################
screenKeyRegionMapping = {"iOS_getScreen":[[], 174,482,226,37],"android_getScreen":[[], 83,59,140,64],"getOcrVictoriaHome":[ ["Back","Home"], 0, 123, 375,
129, "Best of Catch Up"], imageSearchSingleOccurance :[ ["Back","Home", "Down", "Down"], 1159, 567,
77, 63, "Best of Catch Up" ], imageSearchMultipleOccurance :[ ["Back","Home", "Down", "Down"],
1207, 790, 37, 38, "Best of Catch Up"], CheckpointScreenForTransition : [["Home", "Ok"]],
"MotionScreen" :[["Home", "Exit"]], CheckpointScreenToWait
:[["Exit", "1", "0", "3", "Info"]], GET_OCR_SKY_HOME_SCREEN : [["Exit", "Home"], 507, 331, 226, 59]  }

#"MotionScreen" :[["Home", "Down", "Down", "Down", "Right", "Ok"]

#INPUT DICTIONARIES : InputDict
################################################################################
#IDUT

#ReadProperty
readPropertyTestCaseCount = 17
readPropertyInputDict = { 0:[ "Valid parameters, 0", API_PASS, 0] }
for i in range (1, 16):
    readPropertyInputDict.update({i:[ "Valid parameters, " + str(i), API_PASS, i] })

readPropertyInputDict.update({16:[ "InValid parameters, 16", API_FAIL, 16] })
#-------------------------------------------------------------------------------

#CacheImageFromUrl
cacheImageFromUrlTestCaseCount = 4
#inputDict = {key:[url,imageName, testScenario, expected] }
cacheImageFromUrlInputDict = {0:[ CACHE_VALID_URL, "testimage", "valid url", API_PASS],
 1:[ "https://invalidurl1234/","testimage", "Invalid url", API_FAIL],
 2:[ "https://invalidurl1234/","testimage", "Invalid url", API_FAIL],
 3:[ CACHE_VALID_URL, LONG_NAME, "lengthy image name", API_FAIL] }
#-------------------------------------------------------------------------------

#CaptureImage
captureImageTestCaseCount = 11
# inputDict = {key:[testScenario, expected, x, y, width, height, name, jpegQuality, , overWriteAction] }
captureImageInputDict =  { 0:["Valid parameters: overWriteAction: 0", API_PASS, Capt_x,
 Capt_y, Capt_width, Capt_height, CAP_IMAGE_NAME, CAP_DEFAULT_QUALITY, 0 ],
 1:[ "Valid parameters: overWriteAction: 1", API_FAIL, Capt_x, Capt_y, Capt_width,
 Capt_height, CAP_IMAGE_NAME, CAP_DEFAULT_QUALITY, 1 ], 2:[ "Valid parameters: overWriteAction: 2",
 API_PASS, Capt_x, Capt_y, Capt_width, Capt_height, CAP_IMAGE_NAME, CAP_DEFAULT_QUALITY, 2],
 3:[ "InValid parameters: overWriteAction: 5", API_FAIL, Capt_x, Capt_y, Capt_width,
 Capt_height, CAP_IMAGE_NAME, CAP_DEFAULT_QUALITY, 5], 4:[ "Valid parameters: jpegQuality: 100",
 API_PASS, Capt_x, Capt_y, Capt_width, Capt_height, CAP_IMAGE_NAME, 100, 2],
 5:[ "Valid parameters: jpegQuality: 0",API_PASS, Capt_x, Capt_y, Capt_width,
 Capt_height, CAP_IMAGE_NAME, 0, 2], 6:[ "InValid parameters: jpegQuality: -10",
 API_FAIL, Capt_x, Capt_y, Capt_width, Capt_height, CAP_IMAGE_NAME, -10, 2],
 7:[ "InValid parameters: jpegQuality: 200", API_FAIL, Capt_x, Capt_y, Capt_width,
 Capt_height, CAP_IMAGE_NAME, 200, 2], 8:[ "InValid parameters: lengthy image name",
 API_FAIL, Capt_x, Capt_y, Capt_width, Capt_height, LONG_NAME, CAP_DEFAULT_QUALITY, 2],
 9:[ "Valid parameters: another co ordinate", API_PASS, 10, 45, 50, 50, CAP_IMAGE_NAME,
 CAP_DEFAULT_QUALITY, 2 ], 10:[ "Valid parameters: whole frame", API_PASS, MAX_X, MAX_Y,
 MAX_WIDTH, MAX_HEIGHT, CAP_IMAGE_NAME, CAP_DEFAULT_QUALITY, 2 ]  }
#-------------------------------------------------------------------------------

#DetectMotion
detectMotionTestCaseCount = 4
#inputDict = {key:[testScenario, expected, x_coordinate, y_coordinate, width,
# height, timeout, waitGap, tolerance] }
#With motion API should fail on key = 1
#Without motion API should pass on key = 2
detectMotionInputDict = {0:[ "Valid parameters", API_PASS, det_x_coordinate,
det_y_coordinate, det_width, det_height, DEFAULT_TIMEOUT, DEFAULT_WAITGAP,
DEFAULT_STR_TOLERANCE], 1:[ "Valid: tolerance, boundary condition [100]", API_FAIL,
det_x_coordinate, det_y_coordinate, det_width, det_height, DEFAULT_TIMEOUT,
DEFAULT_WAITGAP, "100"], 2:[ "Valid: tolerance, boundary condition [0]", API_PASS,
det_x_coordinate, det_y_coordinate, det_width, det_height, DEFAULT_TIMEOUT,
DEFAULT_WAITGAP, "0"], 3:[ "InValid: wait gap greater than timeout", API_FAIL,
det_x_coordinate, det_y_coordinate, det_width, det_height, 5, 10, "0"] }

#-------------------------------------------------------------------------------

#DynamicImageCompare
dynamicImageCompareTestCaseCount = 4
#inputDict = {key:[testScenario, expected, referenceImageName, x_coordinate,
#y_coordinate, width, height, tolerance] }
dynamicImageCompareInputDict = {0:[ "Valid parameters", API_PASS, Capt_x, Capt_y,
Capt_width, Capt_height, DEFAULT_INT_TOLERANCE], 1:[ "Valid: tolerance, boundary \
condition [100]",API_PASS, Capt_x, Capt_y, Capt_width, Capt_height, 100], 2:
[ "Valid: tolerance, boundary condition [0]",API_FAIL, Capt_x, Capt_y, Capt_width,
Capt_height, 0], 3:[ "InValid referenceImageName",API_FAIL, Capt_x, Capt_y,
Capt_width, Capt_height, DEFAULT_INT_TOLERANCE] }
#-------------------------------------------------------------------------------

#GetAudioLevel and IsSilent
getAudioLevelIsSilentTestCaseCount = 2
#inputDict = {key:[testScenario, expected, noiseLevel, duration] }
getAudioLevelIsSilentInputDict = {0:[ "Valid parameters: getting the noise level \
treshold using GetAudioLevel API", API_PASS, 2, "00:00:50" ], 1:[ "InValid parameter: \
unsupported format for duration", API_PASS, 2, "1" ] }
#-------------------------------------------------------------------------------

#GetScreenTransitionTime
getScreenTransitionTimeTestCaseCount = 6
#inputDict = {key:[testScenario, expected, checkpointName, timeToWait, initialDelay] }
getScreenTransitionTimeInputDict = {0:[ "Valid parameters, DUT already in some other screen",
API_FAIL, CheckpointScreenForTransition, PERFORMANCE_TIME_TO_WAIT, PERFORMANCE_INITIAL_DELAY ],
1:[ "Valid parameters, No screen transition from the checkpoint screen.", API_FAIL,
CheckpointScreenForTransition, PERFORMANCE_TIME_TO_WAIT, PERFORMANCE_INITIAL_DELAY ],
2:[ "Valid parameters, screen transition from the checkpoint screen.", API_PASS,
CheckpointScreenForTransition, PERFORMANCE_TIME_TO_WAIT, PERFORMANCE_INITIAL_DELAY ],
3:[ "Valid parameters, very small time to wait, 2 sec.", API_FAIL, CheckpointScreenForTransition,
2, PERFORMANCE_INITIAL_DELAY ], 4:[ "InValid parameters, non existing checkpoint name.",
API_FAIL, "nonExisting", PERFORMANCE_TIME_TO_WAIT, PERFORMANCE_INITIAL_DELAY ],
5:[ "InValid parameters, negative time to wait, -20 sec", API_FAIL, CheckpointScreenForTransition,
-20, PERFORMANCE_INITIAL_DELAY ], 6:[ "InValid parameters, negative initial delay, -2 sec",
API_FAIL, CheckpointScreenForTransition, PERFORMANCE_TIME_TO_WAIT, -2 ] }
#-------------------------------------------------------------------------------

#WaitForCheckpoint
waitForCheckpointTestCaseCount = 7
#inputDict = {key:[testScenario, expected, checkpointName, timeToWait, initialDelay] }
waitForCheckpointInputDict =   {0:[ "Valid parameters, DUT already in checkpoint screen",
API_FAIL, CheckpointScreenToWait, PERFORMANCE_TIME_TO_WAIT, PERFORMANCE_INITIAL_DELAY ],
1:[ "Valid parameters, No screen transition to the checkpoint screen.", API_FAIL,
CheckpointScreenToWait, PERFORMANCE_TIME_TO_WAIT, PERFORMANCE_INITIAL_DELAY ],
2:[ "Valid parameters, screen transition to the checkpoint screen.", API_PASS,
CheckpointScreenToWait, PERFORMANCE_TIME_TO_WAIT, PERFORMANCE_INITIAL_DELAY ],
3:[ "Valid parameters, very small time to wait, 2 sec.", API_FAIL, CheckpointScreenToWait,
2, PERFORMANCE_INITIAL_DELAY ], 4:[ "InValid parameters, non existing checkpoint name.",
API_FAIL, "nonExisting", PERFORMANCE_TIME_TO_WAIT, PERFORMANCE_INITIAL_DELAY ],
5:[ "InValid parameters, negative time to wait, -20 sec", API_FAIL, CheckpointScreenToWait,
-20, PERFORMANCE_INITIAL_DELAY ], 6:[ "InValid parameters, negative initial delay, -2 sec",
API_FAIL, CheckpointScreenToWait, PERFORMANCE_TIME_TO_WAIT, -2 ] }
#-------------------------------------------------------------------------------

#WaitImageMatch
waitImageMatchTestCaseCount = 12
#inputDict = {key:[testScenario, expected, refImage,  x_coordinate, y_coordinate, width, height, timeToWait, waitGap, algorithm, tolerance (str)] }
waitImageMatchInputDict = {0:[ "InValid parameter, non existing reference image",
API_FAIL, "refImage", Capt_x, Capt_y, Capt_width, Capt_height, PERFORMANCE_TIME_TO_WAIT,
DEFAULT_WAITGAP, PIXEL_BASED_ALGORITHM, DEFAULT_STR_TOLERANCE], 1:[ "Valid parameters RMSE algoritham",
API_PASS, "refImage",  Capt_x, Capt_y, Capt_width, Capt_height, PERFORMANCE_TIME_TO_WAIT,
DEFAULT_WAITGAP, RMSE_ALGORITHM, DEFAULT_STR_TOLERANCE], 2:[ "Valid parameters, PIXEL_BASED algorithm",
API_PASS, "refImage",  Capt_x, Capt_y, Capt_width, Capt_height, PERFORMANCE_TIME_TO_WAIT,
DEFAULT_WAITGAP, PIXEL_BASED_ALGORITHM, DEFAULT_STR_TOLERANCE], 3:[ "Valid parameters, \
Test region is larger than reference image", API_FAIL, "refImage",  Capt_x, Capt_y, Capt_width + 100,
Capt_height + 200, PERFORMANCE_TIME_TO_WAIT, DEFAULT_WAITGAP, PIXEL_BASED_ALGORITHM, DEFAULT_STR_TOLERANCE],
4:[ "In Valid parameters,wrong algoritham", API_FAIL, "refImage", Capt_x, Capt_y,
Capt_width, Capt_height, PERFORMANCE_TIME_TO_WAIT, DEFAULT_WAITGAP, 3, DEFAULT_STR_TOLERANCE],
5:[ "Valid parameters, tolerance, boundary condition: 0", API_FAIL, "refImage",  Capt_x, Capt_y, Capt_width, Capt_height,
PERFORMANCE_TIME_TO_WAIT, DEFAULT_WAITGAP, PIXEL_BASED_ALGORITHM, "0"],
6:[ "InValid parameters, tolerance, out of range: '-12'",
API_FAIL, "refImage",  Capt_x, Capt_y, Capt_width, Capt_height, PERFORMANCE_TIME_TO_WAIT,
DEFAULT_WAITGAP, PIXEL_BASED_ALGORITHM, "-12"], 7:[ "InValid parameters, tolerance, \
out of range: '200'", API_FAIL, "refImage",  Capt_x, Capt_y, Capt_width, Capt_height,
PERFORMANCE_TIME_TO_WAIT, DEFAULT_WAITGAP, PIXEL_BASED_ALGORITHM, "200"],
8:[ "InValid parameters, waitGap greater than  timeToWait", API_FAIL, "refImage",
Capt_x, Capt_y, Capt_width, Capt_height, 5, 10, PIXEL_BASED_ALGORITHM, DEFAULT_STR_TOLERANCE],
9:[ "Valid parameters, whole HD frame comparison", API_PASS, "refImage",
MAX_X, MAX_Y, MAX_WIDTH, MAX_HEIGHT, PERFORMANCE_TIME_TO_WAIT, DEFAULT_WAITGAP,
PIXEL_BASED_ALGORITHM, DEFAULT_STR_TOLERANCE],10:[ "Valid parameters,ref image and test region from two different screen", API_FAIL,
"refImage", Capt_x, Capt_y, Capt_width, Capt_height, PERFORMANCE_TIME_TO_WAIT, DEFAULT_WAITGAP,
PIXEL_BASED_ALGORITHM, DEFAULT_STR_TOLERANCE],11:[ "Valid parameters, tolerance, boundary condition: 100", API_PASS, "refImage",
Capt_x, Capt_y, Capt_width, Capt_height, PERFORMANCE_TIME_TO_WAIT, DEFAULT_WAITGAP,
PIXEL_BASED_ALGORITHM, "100"] }
#-------------------------------------------------------------------------------

#validateCheckPoint
validateCheckPointTestCaseCount = 6
#inputDict = {key:[testScenario, expected, checkpointName] }
validateCheckPointInputDict = {0:[ "InValid parameter, checkpoint object \
without initializing any checkpoint", API_FAIL, SkyValidateCheckPointICrmsel], 1:[ "Valid parameter,\
 OCR checkpoint", API_PASS, SkyValidateCheckPointOCR], 2:[ "Valid parameter, Multi line OCR \
 checkpoint", API_PASS, SkyValidateCheckPointMultiOCR], 3:[ "Valid parameter, IC checkpoint, \
 pixel", API_PASS, SkyValidateCheckPointICpixel], 4:[ "Valid parameter, IC checkpoint, \
 rmse", API_PASS, SkyValidateCheckPointICrmsel], 5:[ "Valid parameter, IC checkpoint -  rmse, \
 validation on non checkpoint screen", API_FAIL, SkyValidateCheckPointICrmsel] }
#-------------------------------------------------------------------------------

#getOCRText
getOCRTextTestCaseCount = 5
#inputDict = {key:[testScenario, expected, [x_coordinate, y_coordinate, width, height], filters, language] }
getOCRTextInputDict = {0:[ "Valid parameters", API_PASS, GET_OCR_SKY_HOME_SCREEN,
DEFAULT_FILTER, DEFAULT_LANG], 1:[ "Valid parameter: language: hin", API_PASS,
GET_OCR_SKY_HOME_SCREEN, DEFAULT_FILTER, "hin"], 2:[ "Valid parameter: language: empty",
API_PASS, GET_OCR_SKY_HOME_SCREEN, DEFAULT_FILTER, ""], 3:[ "InValid parameter: \
language: wrong string", API_FAIL, GET_OCR_SKY_HOME_SCREEN, DEFAULT_FILTER, "wrong"],
4:[ "InValid parameter: filters: wrong string", API_FAIL, GET_OCR_SKY_HOME_SCREEN,
"wrong", DEFAULT_LANG] }
#-------------------------------------------------------------------------------

#ImageMatch
imageMatchTCaseCount = 9
#inputDict = {key:[testScenario, expected, refImage, testImage, algorithm, tolerance,str] }
imageMatchInputDict = {0:[ "InValid parameter, non existing reference image", API_FAIL,
"refImage", "testImage", PIXEL_BASED_ALGORITHM, DEFAULT_STR_TOLERANCE], 1:[ "InValid parameters, \
non existing test image", API_FAIL, "refImage", "testImage", PIXEL_BASED_ALGORITHM,
DEFAULT_STR_TOLERANCE], 2:[ "Valid parameters, PIXEL_BASED algorithm", API_PASS,
"refImage", "testImage", PIXEL_BASED_ALGORITHM, DEFAULT_STR_TOLERANCE], 3:[ "Valid parameters, \
RMSE algorithm", API_PASS, "refImage", "testImage", RMSE_ALGORITHM, DEFAULT_STR_TOLERANCE],
4:[ "Valid parameters,ref image and test image from two different screen", API_FAIL,
"refImage", "testImage", RMSE_ALGORITHM, DEFAULT_STR_TOLERANCE], 5:[ "InValid parameters, \
wrong algorithm", API_FAIL, "refImage", "testImage", 3, DEFAULT_STR_TOLERANCE], 6:[ "Valid parameters, \
tolerance, boundary condition: 0", API_FAIL, "refImage", "testImage", PIXEL_BASED_ALGORITHM, "0"],
7:[ "Valid parameters, tolerance, boundary condition: 100", API_PASS, "refImage",
"testImage", RMSE_ALGORITHM, "100"], 8:[ "InValid parameters, tolerance, out of range: '-12'",
API_FAIL, "refImage", "testImage", PIXEL_BASED_ALGORITHM, "-12"], 9:[ "InValid parameters, tolerance, \
out of range: '200'", API_FAIL, "refImage", "testImage", RMSE_ALGORITHM, "200"] }
#-------------------------------------------------------------------------------

#ImageSearch
#inputDict = {key:[testScenario, expected, checkpointName, regionX, regionY, regionWidth, regionHeight, algorithm, percentMatchThreshold ] }
imageSearchTestCaseCount = 9
imageSearchInputDict = { 0:[ "Valid parameters, expected region (small) and algoritham: SqdiffNormed",
API_PASS, imageSearchSingleOccurance, 255, 62, 115,71, SqdiffNormed,
DEFAULT_PERCENT_MATCH], 1:[ "Valid parameters, max region and algoritham: CcorrNormed",
API_PASS, imageSearchSingleOccurance, MAX_X, MAX_Y, MAX_WIDTH, MAX_HEIGHT, CcorrNormed,
DEFAULT_PERCENT_MATCH], 2:[ "Valid parameters, max region and algoritham: default_CcoeffNormed",
API_PASS, imageSearchSingleOccurance, MAX_X, MAX_Y, MAX_WIDTH, MAX_HEIGHT, default_CcoeffNormed,
DEFAULT_PERCENT_MATCH], 3:[ "Valid parameters, percentMatchThreshold boundary condition: 0",
API_PASS, imageSearchSingleOccurance, MAX_X, MAX_Y, MAX_WIDTH, MAX_HEIGHT, default_CcoeffNormed, 0],
4:[ "Valid parameters, region without image pattern and algoritham: SqdiffNormed",
API_FAIL, imageSearchSingleOccurance, 10, 10, 20, 30, SqdiffNormed,DEFAULT_PERCENT_MATCH],
5:[ "Valid parameters, percentMatchThreshold boundary condition: 100", API_FAIL,
imageSearchSingleOccurance, MAX_X, MAX_Y, MAX_WIDTH, MAX_HEIGHT, default_CcoeffNormed, 100],
6:[ "InValid parameters, percentMatchThreshold out of range: -12", API_FAIL, imageSearchSingleOccurance,
MAX_X, MAX_Y, MAX_WIDTH, MAX_HEIGHT, default_CcoeffNormed, -12], 7:[ "InValid parameters, \
percentMatchThreshold  out of range: 345", API_FAIL, imageSearchSingleOccurance, MAX_X,
MAX_Y, MAX_WIDTH, MAX_HEIGHT, default_CcoeffNormed, 345], 8:[ "Valid parameters, multiple \
occurance of pattern", API_PASS, imageSearchMultipleOccurance, MAX_X, MAX_Y, MAX_WIDTH,
MAX_HEIGHT, default_CcoeffNormed, DEFAULT_PERCENT_MATCH]   }
#-------------------------------------------------------------------------------

#WaitCheckPointMatch
#inputDict = {key:[testScenario, expected, checkpointName, timeToWait, waitGap] }
waitCheckPointMatchTestCaseCount = 7

waitCheckPointMatchInputDict = { 0:[ "Valid parameter, OCR checkpoint", API_PASS, SkyValidateCheckPointOCR,
PERFORMANCE_TIME_TO_WAIT, DEFAULT_WAITGAP], 1:[ "Valid parameter, Multi line OCR checkpoint",
API_PASS, SkyValidateCheckPointMultiOCR, PERFORMANCE_TIME_TO_WAIT, DEFAULT_WAITGAP],
2:[ "Valid parameter, IC checkpoint, pixel", API_PASS, SkyValidateCheckPointICpixel,
PERFORMANCE_TIME_TO_WAIT, DEFAULT_WAITGAP], 3:[ "Valid parameter, IC checkpoint, rmse",
API_PASS, SkyValidateCheckPointICrmsel, PERFORMANCE_TIME_TO_WAIT, DEFAULT_WAITGAP ],
4:[ "InValid parameters, negative time to wait, -20 sec", API_FAIL, SkyValidateCheckPointICpixel,
-20, DEFAULT_WAITGAP], 5:[ "InValid parameters, negative waitGap, -2 sec", API_FAIL,
SkyValidateCheckPointICpixel, PERFORMANCE_TIME_TO_WAIT, -2], 6:[ "InValid parameters, \
waitGap > timeToWait", API_FAIL, SkyValidateCheckPointICpixel, 5, 20] }
#-------------------------------------------------------------------------------

#WaitColorMatch
waitColorMatchTestCaseCount = 5
#inputDict = {key:[testScenario, expected, matchColor, x_coordinate, y_coordinate,
#width, height, timeToWait, waitGap, colorTolerance, flatness] }
waitColorMatchInputDict = {0:[ "Valid parameters", API_PASS, color_x_coordinate,
color_y_coordinate, color_width, color_height, PERFORMANCE_TIME_TO_WAIT, DEFAULT_WAITGAP,
DEFAULT_COLOR_TOLERANCE, DEFAULT_FLATNESS], 1:[ "Valid parameters, flatness boundary \
condition : 0", API_PASS, color_x_coordinate, color_y_coordinate, color_width, color_height,
PERFORMANCE_TIME_TO_WAIT, DEFAULT_WAITGAP, DEFAULT_COLOR_TOLERANCE, 0], 2:[ "Valid parameters, \
flatness boundary condition : 100", API_FAIL, color_x_coordinate, color_y_coordinate,
color_width, color_height, PERFORMANCE_TIME_TO_WAIT, DEFAULT_WAITGAP, DEFAULT_COLOR_TOLERANCE,
100], 3:[ "In Valid parameters, waitGap greater than timeToWait", API_FAIL, color_x_coordinate,
color_y_coordinate, color_width, color_height, 5, 20, DEFAULT_COLOR_TOLERANCE, DEFAULT_FLATNESS],
4:[ "Valid parameters, Match color check on non matching screen", API_FAIL, color_x_coordinate,
color_y_coordinate, color_width, color_height, PERFORMANCE_TIME_TO_WAIT, DEFAULT_WAITGAP,
DEFAULT_COLOR_TOLERANCE, DEFAULT_FLATNESS] }
#-------------------------------------------------------------------------------

#serverTime_QuickCaptureInputDict

serverTime_QuickCaptureTestCaseCount = 2
#inputDict = {key:[testScenario, expected, x_coordinate, y_coordinate, width, height, timeout, waitGap, tolerance] }
#need to check the behavior on key - 2
serverTime_QuickCaptureInputDict = {0:[ "QuickCapture:Valid parameters", API_PASS, CAP_IMAGE_NAME],
1:[ "QuickCapture:InValid parameter, lengthy image name", API_FAIL, LONG_NAME]}#,
#2:[ "Valid QuickCapture, after DUT power off ", API_FAIL, CAP_IMAGE_NAME] }
#-------------------------------------------------------------------------------

#ReadCustomProperty
readCustomPropertyTestCaseCount = 7
#inputDict = {key:[testScenario, expected, DUTCubeProperty] }

attributeList = ["attribute0", "attribute1", "attribute2", "attribute3", "attribute4", "attribute5"]

readCustomPropertyInputDict = { }
for i in range (0, 5):
    readCustomPropertyInputDict.update({i:[ "Defined attribute name with value , "
    + attributeList [i], API_PASS, attributeList [i]] })

readCustomPropertyInputDict.update({5:[ "Defined attribute name without value  "
 + attributeList [i], API_FAIL, attributeList [5]] })
readCustomPropertyInputDict.update({6:[ "InValid parameters, non existing attribute \
name: WrongCustomAttribute", API_FAIL, "WrongCustomAttribute"] })
#-------------------------------------------------------------------------------
