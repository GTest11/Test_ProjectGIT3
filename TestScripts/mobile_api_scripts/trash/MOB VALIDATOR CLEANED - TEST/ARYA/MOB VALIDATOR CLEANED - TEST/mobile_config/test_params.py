from library.common_functions import dut, get_image_resolution

# general
API_PASS = True
API_FAIL = False
NONE = None
EMPTY = ""
video_sources = ["f3b91a95", "21435", "aa455"]



# ---------------------------  CacheImageFromUrl

CACHE_VALID_URL = "http://10.47.166.48/TestImage/testImageForCacheImageFromUrl.jpg"
CACHE_VALID_URL_FOR_DYNAMIC_COMPARE = "http://10.47.166.48/TestImage/ImageForDynamicImageCompare.JPG"

IMG_NAME = "testimage"
LONG_NAME = "testimage_abcdefghijklmnopqrstuvwxyz_abcdefghijklmnopqrstuvwxyz_abc\
defghijklmnopqrstuvwxyz_abcdefghijklmnopqrstuvwxyz_abcdefghijklmnopqrstuvwxyz_ab\
cdefghijklmnopqrstuvwxyz.jpg"
INVALID_URL = "https://invalidurl1234/"

#inputDict = {key:[url,imageName, testScenario, expected] }
cache_image_from_url_params = {
    0:[ CACHE_VALID_URL, IMG_NAME, "Valid url, Valid image name", API_PASS],

}



# ---------------------------  CaptureImage

Capt_x = 89
Capt_y = 60
Capt_width = 138
Capt_height = 68
cap_im_coordinates = (89, 61, 139, 69)

CAP_IMAGE_NAME = "cap_img"
CAP_IMG_DEFAULT_QUALITY = 90

MAX_X = 0
MAX_Y = 0
# MAX_WIDTH = 768 #720#768
# MAX_HEIGHT = 1024 # 1280 #1024
MAX_WIDTH, MAX_HEIGHT = get_image_resolution()

cap_im_max_coord = (0, 0, 720, 1280)

capture_image_params =  {
    0:[
        "Valid parameters: overWriteAction: 0", API_PASS,
       (Capt_x, Capt_y, Capt_width, Capt_height, CAP_IMAGE_NAME, CAP_IMG_DEFAULT_QUALITY, 0)
       ],
    1:[
        "Valid parameters: overWriteAction: 2", API_PASS,
        (Capt_x, Capt_y, Capt_width, Capt_height, CAP_IMAGE_NAME, CAP_IMG_DEFAULT_QUALITY, 2)
    ],
    2:[
        "Valid parameters: jpegQuality: 100", API_PASS,
        (Capt_x, Capt_y, Capt_width, Capt_height, CAP_IMAGE_NAME, 100, 2)
    ],
    3:[
        "Valid parameters: jpegQuality: 0",API_PASS,
        (Capt_x, Capt_y, Capt_width, Capt_height, CAP_IMAGE_NAME, 0, 2)
    ],
    4:[
        "Valid parameters: another co ordinate", API_PASS,
        (10, 45, 50, 50, CAP_IMAGE_NAME, CAP_IMG_DEFAULT_QUALITY, 2)
    ],
    5:[
        "Valid parameters: whole frame", API_PASS,
        (MAX_X, MAX_Y, MAX_WIDTH, MAX_HEIGHT, CAP_IMAGE_NAME, CAP_IMG_DEFAULT_QUALITY, 2)
    ],

}



# ---------------------------  DetectMotion

det_x = 176
det_y = 99
det_width = 439
det_height = 250

DEFAULT_TIMEOUT = 20
DEFAULT_WAITGAP = 5
DEFAULT_STR_TOLERANCE = "8"

det_motion_param = (det_x, det_y, det_width, det_height, DEFAULT_TIMEOUT, DEFAULT_WAITGAP, DEFAULT_STR_TOLERANCE)

detect_motion_params = {
    0:[
        "Valid parameters", API_PASS,
        (det_x, det_y, det_width, det_height, DEFAULT_TIMEOUT, DEFAULT_WAITGAP, DEFAULT_STR_TOLERANCE)
    ],
    # 1:[
    # "Valid: tolerance, boundary condition [100]", API_PASS,
    #     (det_x, det_y, det_width, det_height, DEFAULT_TIMEOUT, DEFAULT_WAITGAP, "100")
    # ],
    # 2:[
    #     "Valid: tolerance, boundary condition [0]", API_PASS,
    #     (det_x, det_y, det_width, det_height, DEFAULT_TIMEOUT, DEFAULT_WAITGAP, "0")
    # ],

}



# ---------------------------  DynamicImageCompare

img_name = "dynamic_compare_img"
DEFAULT_INT_TOLERANCE = 10
dy_Capt_x = 0
dy_Capt_y = 57
dy_Capt_width = 216
dy_Capt_height = 83
dynamic_image_compare_params = {
    0:[ "Valid parameters", API_PASS,
        (img_name, dy_Capt_x, dy_Capt_y, dy_Capt_width, dy_Capt_height, DEFAULT_INT_TOLERANCE)
    ],
    1:[
        "Valid: tolerance, boundary condition [100]", API_PASS,
        (img_name, Capt_x, Capt_y, Capt_width, Capt_height, 100)
    ],

}



# ----------------------------- WaitCheckPointMatch


SkyValidateCheckPointOCR = "Mobile_YouTube"
TIME_TO_WAIT = 20
SkyValidateCheckPointMultiOCR = "youtube_MultiOcr"
SkyValidateCheckPointICpixel = "youtube_valIcPixel"
SkyValidateCheckPointICrmsel = "youtube_valIcRmse"
imageSearchSingleOccurance = "CheckpointPatternSingleOccurance"
imageSearchMultipleOccurance = "CheckpointPatternMultipleOccurance"
CheckpointScreenForTransition = "GetScreenTransitionCheck"
GET_OCR_SKY_HOME_SCREEN = "getOcrSkyHome"
CheckpointScreenToWait = "Mobile_YouTube"

wait_for_chkpt_match_params = {
    0:[
        "Valid parameter, OCR checkpoint", API_PASS, SkyValidateCheckPointOCR,
        TIME_TO_WAIT, DEFAULT_WAITGAP
    ],
    1:[
        "Valid parameter, Multi line OCR checkpoint",
        API_PASS, SkyValidateCheckPointMultiOCR, TIME_TO_WAIT, DEFAULT_WAITGAP
    ],
    2:[
        "Valid parameter, IC checkpoint, pixel", API_PASS, SkyValidateCheckPointICpixel,
        TIME_TO_WAIT, DEFAULT_WAITGAP
    ],
    3:[
        "Valid parameter, IC checkpoint, rmse",
        API_PASS, SkyValidateCheckPointICrmsel, TIME_TO_WAIT, DEFAULT_WAITGAP
    ],

}


# ----------------------- WaitColorMatch

color_x = 37
color_y = 82
color_w = 15
color_h = 24

COLOR_TOLERANCE = '[10,10,10]'
FLATNESS = 90
captureZapTime = 30
matchColor = "[254,0,3]"

wait_color_match_params = {
    0:[ 
        "Valid parameters", API_PASS, (matchColor, color_x, color_y, color_w, color_h,
        TIME_TO_WAIT, DEFAULT_WAITGAP, COLOR_TOLERANCE, FLATNESS)
    ],
    1:[
        "Valid parameters, flatness boundary condition : 0", API_PASS, (matchColor, color_x,
        color_y, color_w, color_h, TIME_TO_WAIT, DEFAULT_WAITGAP, COLOR_TOLERANCE, 0)
    ],

}


# -------------------------------- WaitImageMatch 

PIXEL_BASED_ALGORITHM = 1
RMSE_ALGORITHM = 2

img_wait_im_match = "refImage"

wait_image_match_params = {
    0:[ "Valid parameters RMSE algoritham", API_PASS, (img_wait_im_match,  Capt_x, Capt_y,
        Capt_width, Capt_height, TIME_TO_WAIT, DEFAULT_WAITGAP, RMSE_ALGORITHM, DEFAULT_STR_TOLERANCE)
    ],
    1:[ "Valid parameters, PIXEL_BASED algorithm", API_PASS, (img_wait_im_match,  Capt_x, Capt_y,
        Capt_width, Capt_height, TIME_TO_WAIT, DEFAULT_WAITGAP, PIXEL_BASED_ALGORITHM, DEFAULT_STR_TOLERANCE)
    ],

    2:[
        "Valid parameters, whole HD frame comparison", API_PASS, (img_wait_im_match, MAX_X, MAX_Y,
        MAX_WIDTH, MAX_HEIGHT, TIME_TO_WAIT, DEFAULT_WAITGAP, PIXEL_BASED_ALGORITHM, DEFAULT_STR_TOLERANCE)
    ],

    3:[ "Valid parameters, tolerance, boundary condition: 100", API_PASS, (img_wait_im_match, Capt_x, Capt_y,
         Capt_width, Capt_height, TIME_TO_WAIT, DEFAULT_WAITGAP, PIXEL_BASED_ALGORITHM, "100")
    ]
}


# ----------------------- WaitForCheckpoint

INITIAL_DELAY = 2

wait_for_chkpt_params =   {
    0:[
        "Valid parameters, screen transition to the checkpoint screen.", API_PASS,
        CheckpointScreenToWait, TIME_TO_WAIT, INITIAL_DELAY
    ],
    1:[
        "Valid parameters, very small time to wait, 3 sec.", API_PASS, CheckpointScreenToWait,
        3, INITIAL_DELAY
    ],
}


# ----------------- getOCRText

DEFAULT_FILTER = "Greyscale"
DEFAULT_LANG = "eng"

get_ocr_text_params = {
    0:[
        "Valid parameters", API_PASS, (DEFAULT_FILTER, DEFAULT_LANG),
    ],
    # 1:[
    #     "Valid parameter: language: hin", API_PASS, (DEFAULT_FILTER, "hin")
    # ],
    2:[ "Valid parameter: language: empty", API_PASS, (DEFAULT_FILTER, "")
    ],
}


#  ----------------------- ImageMatch

ref_img_0 = "ref_img_0"
test_img_0 = "test_img_0"


ref_image_param = (599, 509, 27, 37, ref_img_0, CAP_IMG_DEFAULT_QUALITY, 0)
test_image_param = (599, 1043, 27, 37, test_img_0, 100, 2)

image_match_params = {
    0:[
        "Valid parameters, PIXEL_BASED algorithm", API_PASS,
        (ref_img_0, test_img_0, PIXEL_BASED_ALGORITHM, DEFAULT_STR_TOLERANCE)
    ],
    1:[
        "Valid parameters, RMSE algorithm", API_PASS,
        (ref_img_0, test_img_0, RMSE_ALGORITHM, DEFAULT_STR_TOLERANCE)
    ],
    2:[
        "Valid parameters, tolerance, boundary condition: 100", API_PASS,
        (ref_img_0, test_img_0, RMSE_ALGORITHM, "100")
    ],
}



# ---------------------- ImageSearch

SqdiffNormed = 1
CcorrNormed  = 3
default_CcoeffNormed  = 5
DEFAULT_PERCENT_MATCH = 97

image_search_params = {
    0:[
        "Valid parameters, expected region (small) and algoritham: SqdiffNormed",
        API_PASS, (imageSearchSingleOccurance, 199, 37, 427, 139, SqdiffNormed, DEFAULT_PERCENT_MATCH)
    ],
    1:[
        "Valid parameters, max region and algoritham: CcorrNormed", API_PASS, (imageSearchSingleOccurance,
        MAX_X, MAX_Y, MAX_WIDTH, MAX_HEIGHT, CcorrNormed, DEFAULT_PERCENT_MATCH)
    ],
    2:[
        "Valid parameters, max region and algoritham: default_CcoeffNormed", API_PASS,
        (imageSearchSingleOccurance, MAX_X, MAX_Y, MAX_WIDTH, MAX_HEIGHT, default_CcoeffNormed, DEFAULT_PERCENT_MATCH)
    ],
    3:[
        "Valid parameters, percentMatchThreshold boundary condition: 0", API_PASS, (imageSearchSingleOccurance,
        MAX_X, MAX_Y, MAX_WIDTH, MAX_HEIGHT, default_CcoeffNormed, 0)
    ],
    4:[
        "Valid parameters, multiple occurance of pattern", API_PASS, (imageSearchMultipleOccurance,
        MAX_X, MAX_Y, MAX_WIDTH, MAX_HEIGHT, default_CcoeffNormed, DEFAULT_PERCENT_MATCH)
    ]
}




# ------------------------------------ GetScreenTransitionTime

# TIME_TO_WAIT = 20

chkpt_screen_elm = "CheckpointPatternSingleOccurance"

get_screen_transition_time_params = {
    # "chkpt_screen":[
    #     "Valid parameters, No screen transition from the checkpoint screen", API_FAIL,
    #     (chkpt_screen_elm, TIME_TO_WAIT, INITIAL_DELAY)
    # ],

    "not_on_chkpt_screen":[
        "Valid parameters, not on checkpoint screen", API_PASS,
        (chkpt_screen_elm, TIME_TO_WAIT, INITIAL_DELAY)
    ],

    "move_out_chkpt_screen":[
        "Valid parameters, screen transition from the checkpoint screen", API_PASS,
        (chkpt_screen_elm, TIME_TO_WAIT, INITIAL_DELAY)
    ],

}


# -------------------------------- validateCheckPoint

validate_chkpt_params = {
    0:[ "Valid parameter, OCR checkpoint", API_PASS, SkyValidateCheckPointOCR],
    1:[ "Valid parameter, Multi line OCR checkpoint", API_PASS, SkyValidateCheckPointMultiOCR],
    2:[ "Valid parameter, IC checkpoint, pixel", API_PASS, SkyValidateCheckPointICpixel],
    3:[ "Valid parameter, IC checkpoint, rmse", API_PASS, SkyValidateCheckPointICrmsel],
}

