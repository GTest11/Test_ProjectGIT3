

class config_base(object):
    '''
    # Update the value of 'element_type_to_test' as required
    # By default, it is set to XPath
    # eg:
        'xpath'
        'id'
        'name'
        'class'
        'access_id'
    '''

    element_type_to_test = 'id'



    # ==================================================== CONSTANTS
    # ================================================================================
    T_MIN_WAIT = 3
    T_WAIT_FOR_HOME = 50
    T_MD_WAIT = 20
    T_WD_TIMEOUT = 120  # StartCaptureZapFrames

    # StartCaptureZapFrames
    T_NEGETIVE_ZAP_FRM = -30
    T_VALID_ZAP_FRM = 30

    # ==================================================== END CONSTANTS =============



    # ==================================================== COORDINATES
    # ================================================================================
    C_TAP_PLAYBACK = (260, 300) # is_selected.py

    # ==================================================== END COORDINATES =============


    # **************************************  TEST PARAMETERS

    # ==================================================== general
    # ================================================================================
    API_PASS = True
    API_FAIL = False
    NONE = None
    EMPTY = ""
    IMG_NAME = "testimage"
    LONG_IMG_NAME = "testimage_abcdefghijklmnopqrstuvwxyz_abcdefghijklmnopqrstuvwxyz_abc\
    defghijklmnopqrstuvwxyz_abcdefghijklmnopqrstuvwxyz_abcdefghijklmnopqrstuvwxyz_ab\
    cdefghijklmnopqrstuvwxyz.jpg"

    CAP_IMAGE_NAME = "cap_img"
    CAP_IMG_DEFAULT_QUALITY = 90
    MAX_X = 0
    MAX_Y = 0
    MAX_WIDTH, MAX_HEIGHT = 768, 1024  # get_image_resolution()

    # detect motion
    DEFAULT_TIMEOUT = 20
    DEFAULT_WAITGAP = 5
    DEFAULT_STR_TOLERANCE = "8"

    # dynamic image compare
    dyn_img = "dynamic_compare_img"
    DEFAULT_DYN_TOLERANCE = 8
    # T_MD_WAIT = 20

    # WAITCOLORMATCH
    COLOR_TOLERANCE = '[10,10,10]'
    FLATNESS = 90
    captureZapTime = 30
    matchColor = "[254,0,3]"

    # WAIT IMAGE MATCH
    PIXEL_BASED_ALGORITHM = 1
    RMSE_ALGORITHM = 2

    # WAIT FOR CHECKPOINT
    INITIAL_DELAY = 2

    # GETOCRTEXT
    DEFAULT_FILTER = "Greyscale"
    DEFAULT_LANG = "eng"

    # IMAGE SEARCH
    SqdiffNormed = 1
    CcorrNormed = 3
    default_CcoeffNormed = 5
    DEFAULT_PERCENT_MATCH = 97

    # StartCaptureZapFrames
    zap_frame_iter_count = 3

    # ==================================================== CHECKPOINT VARIABLES
    # ================================================================================
    yt_logo = "Mobile_YouTube"
    SkyValidateCheckPointOCR = "Mobile_YouTube"
    SkyValidateCheckPointMultiOCR = "youtube_MultiOcr"
    SkyValidateCheckPointICpixel = "youtube_valIcPixel"
    SkyValidateCheckPointICrmsel = "youtube_valIcRmse"
    imageSearchSingleOccurance = "CheckpointPatternSingleOccurance"
    imageSearchMultipleOccurance = "CheckpointPatternMultipleOccurance"
    CheckpointScreenForTransition = "GetScreenTransitionCheck"
    GET_OCR_SKY_HOME_SCREEN = "getOcrSkyHome"
    CheckpointScreenToWait = "Mobile_YouTube"
    chkpt_screen_elm = "CheckpointPatternSingleOccurance"

    # ==================================================== URLS
    # ================================================================================
    CACHE_VALID_URL = "https://wallpapers.pub/web/wallpapers/birds-water-spray-wallpaper/3840x2160.jpg"
    INVALID_URL = "https://invalidurl1234/"

    # ==================================================== COORDINATES
    # ================================================================================
    C_CAP_IMAGE = (89, 60, 139, 69)
    C_DET_MOTION = (176, 99, 439, 251)
    C_DYN_IMG_COMP = (89, 60, 139, 69)
    C_COLOR_MATCH = (37, 81, 15, 23)
    C_WAIT_IMG_MATCH = (89, 60, 139, 69)

    # ---------------------------  CacheImageFromUrl


    # inputDict = {key:[url,imageName, testScenario, expected] }
    cache_image_from_url_params = {
        0: [CACHE_VALID_URL, IMG_NAME, "Valid url, Valid image name", API_PASS],
        1: [INVALID_URL, IMG_NAME, "Invalid url, Valid image name", API_FAIL],
        2: [INVALID_URL, IMG_NAME, "Invalid url, Valid image name", API_FAIL],
        3: [CACHE_VALID_URL, LONG_IMG_NAME, "Valid url, Lengthy image name", API_FAIL]
    }

    # ---------------------------  CaptureImage

    capture_image_params = {
        0: [
            "Valid parameters: overWriteAction: 0", API_PASS,
            (C_CAP_IMAGE[0], C_CAP_IMAGE[1], C_CAP_IMAGE[2], C_CAP_IMAGE[3], CAP_IMAGE_NAME, CAP_IMG_DEFAULT_QUALITY, 0)
        ],
        1: [
            "Valid parameters: overWriteAction: 1", API_FAIL,
            (C_CAP_IMAGE[0], C_CAP_IMAGE[1], C_CAP_IMAGE[2], C_CAP_IMAGE[3], CAP_IMAGE_NAME, CAP_IMG_DEFAULT_QUALITY, 1)
        ],
        2: [
            "Valid parameters: overWriteAction: 2", API_PASS,
            (C_CAP_IMAGE[0], C_CAP_IMAGE[1], C_CAP_IMAGE[2], C_CAP_IMAGE[3], CAP_IMAGE_NAME, CAP_IMG_DEFAULT_QUALITY, 2)
        ],
        3: [
            "InValid parameters: overWriteAction: 5", API_FAIL,
            (C_CAP_IMAGE[0], C_CAP_IMAGE[1], C_CAP_IMAGE[2], C_CAP_IMAGE[3], CAP_IMAGE_NAME, CAP_IMG_DEFAULT_QUALITY, 5)
        ],
        4: [
            "Valid parameters: jpegQuality: 100", API_PASS,
            (C_CAP_IMAGE[0], C_CAP_IMAGE[1], C_CAP_IMAGE[2], C_CAP_IMAGE[3], CAP_IMAGE_NAME, 100, 2)
        ],
        5: [
            "Valid parameters: jpegQuality: 0", API_PASS,
            (C_CAP_IMAGE[0], C_CAP_IMAGE[1], C_CAP_IMAGE[2], C_CAP_IMAGE[3], CAP_IMAGE_NAME, 0, 2)
        ],
        6: [
            "InValid parameters: jpegQuality: -10", API_FAIL,
            (C_CAP_IMAGE[0], C_CAP_IMAGE[1], C_CAP_IMAGE[2], C_CAP_IMAGE[3], CAP_IMAGE_NAME, -10, 2)
        ],
        7: [
            "InValid parameters: jpegQuality: 200", API_FAIL,
            (C_CAP_IMAGE[0], C_CAP_IMAGE[1], C_CAP_IMAGE[2], C_CAP_IMAGE[3], CAP_IMAGE_NAME, 200, 2)
        ],
        8: [
            "InValid parameters: lengthy image name", API_FAIL,
            (C_CAP_IMAGE[0], C_CAP_IMAGE[1], C_CAP_IMAGE[2], C_CAP_IMAGE[3], LONG_IMG_NAME, CAP_IMG_DEFAULT_QUALITY, 2)
        ],
        9: [
            "Valid parameters: another co ordinate", API_PASS,
            (10, 45, 50, 50, CAP_IMAGE_NAME, CAP_IMG_DEFAULT_QUALITY, 2)
        ],
        10: [
            "Valid parameters: whole frame", API_PASS,
            (MAX_X, MAX_Y, MAX_WIDTH, MAX_HEIGHT, CAP_IMAGE_NAME, CAP_IMG_DEFAULT_QUALITY, 2)
        ],
        11: [
            "Invalid parameters: overWriteAction: -1", API_FAIL,
            (C_CAP_IMAGE[0], C_CAP_IMAGE[1], C_CAP_IMAGE[2], C_CAP_IMAGE[3], CAP_IMAGE_NAME, CAP_IMG_DEFAULT_QUALITY, -1)
        ]
    }

    # ---------------------------  DetectMotion

    detect_motion_params = {
        0: [
            "Valid parameters", API_PASS,
            (C_DET_MOTION[0], C_DET_MOTION[1], C_DET_MOTION[2], C_DET_MOTION[3], DEFAULT_TIMEOUT, DEFAULT_WAITGAP, DEFAULT_STR_TOLERANCE)
        ],
        1: [
            "Valid: tolerance, boundary condition [100]", API_PASS,
            (C_DET_MOTION[0], C_DET_MOTION[1], C_DET_MOTION[2], C_DET_MOTION[3], DEFAULT_TIMEOUT, DEFAULT_WAITGAP, "100")
        ],
        2: [
            "Valid: tolerance, boundary condition [0]", API_PASS,
            (C_DET_MOTION[0], C_DET_MOTION[1], C_DET_MOTION[2], C_DET_MOTION[3], DEFAULT_TIMEOUT, DEFAULT_WAITGAP, "0")
        ],
        3: [
            "InValid: wait gap greater than timeout", API_FAIL,
            (C_DET_MOTION[0], C_DET_MOTION[1], C_DET_MOTION[2], C_DET_MOTION[3], 5, 10, "0")
        ]
    }

    # ---------------------------  DynamicImageCompare

    dynamic_image_compare_params = {
        0: ["Valid parameters", API_PASS,
            (dyn_img, C_DYN_IMG_COMP[0], C_DYN_IMG_COMP[1], C_DYN_IMG_COMP[2], C_DYN_IMG_COMP[3], DEFAULT_DYN_TOLERANCE)
            ],
        1: [
            "Valid: tolerance, boundary condition [100]", API_PASS,
            (dyn_img, C_DYN_IMG_COMP[0], C_DYN_IMG_COMP[1], C_DYN_IMG_COMP[2], C_DYN_IMG_COMP[3], 100)
        ],
        2: [
            "Valid: tolerance, boundary condition [0]", API_FAIL,
            (dyn_img, C_DYN_IMG_COMP[0], C_DYN_IMG_COMP[1], C_DYN_IMG_COMP[2], C_DYN_IMG_COMP[3], 0)
        ],
        3: [
            "InValid referenceImageName", API_FAIL,
            (dyn_img, C_DYN_IMG_COMP[0], C_DYN_IMG_COMP[1], C_DYN_IMG_COMP[2], C_DYN_IMG_COMP[3], DEFAULT_DYN_TOLERANCE)
        ]
    }

    # ----------------------------- WaitCheckPointMatch

    wait_for_chkpt_match_params = {
        0: [
            "Valid parameter, OCR checkpoint", API_PASS, SkyValidateCheckPointOCR,
            T_MD_WAIT, DEFAULT_WAITGAP
        ],
        1: [
            "Valid parameter, Multi line OCR checkpoint",
            API_PASS, SkyValidateCheckPointMultiOCR, T_MD_WAIT, DEFAULT_WAITGAP
        ],
        2: [
            "Valid parameter, IC checkpoint, pixel", API_PASS, SkyValidateCheckPointICpixel,
            T_MD_WAIT, DEFAULT_WAITGAP
        ],
        3: [
            "Valid parameter, IC checkpoint, rmse",
            API_PASS, SkyValidateCheckPointICrmsel, T_MD_WAIT, DEFAULT_WAITGAP
        ],
        4: [
            "InValid parameters, negative time to wait, -20 sec", API_FAIL, SkyValidateCheckPointICpixel,
            -20, DEFAULT_WAITGAP
        ],
        5: [
            "InValid parameters, negative waitGap, -2 sec", API_FAIL,
            SkyValidateCheckPointICpixel, T_MD_WAIT, -2
        ],
        6: [
            "InValid parameters, waitGap > timeToWait", API_FAIL,
            SkyValidateCheckPointICpixel, 5, 20
        ]
    }

    # ----------------------- WaitColorMatch

    wait_color_match_params = {
        0: [
            "Valid parameters", API_PASS, (matchColor, C_COLOR_MATCH[0], C_COLOR_MATCH[1], C_COLOR_MATCH[2], C_COLOR_MATCH[3],
                                           T_MD_WAIT, DEFAULT_WAITGAP, COLOR_TOLERANCE, FLATNESS)
        ],
        1: [
            "Valid parameters, flatness boundary condition : 0", API_PASS, (matchColor, C_COLOR_MATCH[0], C_COLOR_MATCH[1],
                                                                            C_COLOR_MATCH[2], C_COLOR_MATCH[3], T_MD_WAIT,
                                                                            DEFAULT_WAITGAP, COLOR_TOLERANCE, 0)
        ],
        2: ["Valid parameters, flatness boundary condition : 100", API_FAIL, (matchColor, C_COLOR_MATCH[0],
                                                                              C_COLOR_MATCH[1], C_COLOR_MATCH[2], C_COLOR_MATCH[3],
                                                                              T_MD_WAIT, DEFAULT_WAITGAP,
                                                                              COLOR_TOLERANCE, 100)
            ],
        3: [
            "In Valid parameters, waitGap greater than timeToWait", API_FAIL, (matchColor, C_COLOR_MATCH[0],
                                                                               C_COLOR_MATCH[1], C_COLOR_MATCH[2], C_COLOR_MATCH[3], 5, 20,
                                                                               COLOR_TOLERANCE, FLATNESS)
        ],
        4: [
            "Valid parameters, Match color check on non matching screen", API_FAIL, (matchColor, C_COLOR_MATCH[0],
                                                                                     C_COLOR_MATCH[1], C_COLOR_MATCH[2], C_COLOR_MATCH[3],
                                                                                     T_MD_WAIT, DEFAULT_WAITGAP,
                                                                                     COLOR_TOLERANCE, FLATNESS)
        ]
    }

    # -------------------------------- WaitImageMatch

    img_wait_im_match = "refImage"

    wait_image_match_params = {
        0: [
            "InValid parameter, non existing reference image", API_FAIL, (img_wait_im_match,
                                                                          C_WAIT_IMG_MATCH[0], C_WAIT_IMG_MATCH[1],
                                                                          C_WAIT_IMG_MATCH[2], C_WAIT_IMG_MATCH[3],
                                                                          T_MD_WAIT, DEFAULT_WAITGAP,
                                                                          PIXEL_BASED_ALGORITHM,
                                                                          DEFAULT_STR_TOLERANCE)
        ],
        1: ["Valid parameters RMSE algoritham", API_PASS, (img_wait_im_match, C_WAIT_IMG_MATCH[0], C_WAIT_IMG_MATCH[1],
                                                                          C_WAIT_IMG_MATCH[2], C_WAIT_IMG_MATCH[3],
                                                                          T_MD_WAIT, DEFAULT_WAITGAP,
                                                           RMSE_ALGORITHM, DEFAULT_STR_TOLERANCE)
            ],
        2: ["Valid parameters, PIXEL_BASED algorithm", API_PASS, (img_wait_im_match, C_WAIT_IMG_MATCH[0], C_WAIT_IMG_MATCH[1],
                                                                          C_WAIT_IMG_MATCH[2], C_WAIT_IMG_MATCH[3],
                                                                          T_MD_WAIT,
                                                                  DEFAULT_WAITGAP, PIXEL_BASED_ALGORITHM,
                                                                  DEFAULT_STR_TOLERANCE)
            ],
        3: ["Valid parameters, Test region is larger than reference image", API_FAIL, (img_wait_im_match,
                                                                                       C_WAIT_IMG_MATCH[0],
                                                                                       C_WAIT_IMG_MATCH[1],
                                                                                       C_WAIT_IMG_MATCH[2] + 100,
                                                                                       C_WAIT_IMG_MATCH[3] + 200,
                                                                                       T_MD_WAIT,
                                                                                       DEFAULT_WAITGAP,
                                                                                       PIXEL_BASED_ALGORITHM,
                                                                                       DEFAULT_STR_TOLERANCE)
            ],
        4: [
            "In Valid parameters,wrong algoritham", API_FAIL, (img_wait_im_match, C_WAIT_IMG_MATCH[0], C_WAIT_IMG_MATCH[1],
                                                                          C_WAIT_IMG_MATCH[2], C_WAIT_IMG_MATCH[3],
                                                                          T_MD_WAIT,
                                                               DEFAULT_WAITGAP, 3, DEFAULT_STR_TOLERANCE)
        ],
        5: ["Valid parameters, tolerance, boundary condition: 0", API_FAIL, (img_wait_im_match, C_WAIT_IMG_MATCH[0], C_WAIT_IMG_MATCH[1],
                                                                          C_WAIT_IMG_MATCH[2], C_WAIT_IMG_MATCH[3],
                                                                          T_MD_WAIT, DEFAULT_WAITGAP,
                                                                             PIXEL_BASED_ALGORITHM, "0")
            ],
        6: ["InValid parameters, tolerance, out of range: '-12'", API_FAIL, (img_wait_im_match, C_WAIT_IMG_MATCH[0], C_WAIT_IMG_MATCH[1],
                                                                          C_WAIT_IMG_MATCH[2], C_WAIT_IMG_MATCH[3],
                                                                          T_MD_WAIT, DEFAULT_WAITGAP,
                                                                             PIXEL_BASED_ALGORITHM, "-12")
            ],
        7: ["InValid parameters, tolerance, out of range: '200'", API_FAIL, (img_wait_im_match, C_WAIT_IMG_MATCH[0], C_WAIT_IMG_MATCH[1],
                                                                          C_WAIT_IMG_MATCH[2], C_WAIT_IMG_MATCH[3],
                                                                          T_MD_WAIT, DEFAULT_WAITGAP,
                                                                             PIXEL_BASED_ALGORITHM, "200")
            ],
        8: ["InValid parameters, waitGap greater than  timeToWait", API_FAIL, (img_wait_im_match, C_WAIT_IMG_MATCH[0], C_WAIT_IMG_MATCH[1],
                                                                          C_WAIT_IMG_MATCH[2], C_WAIT_IMG_MATCH[3],
                                                                          T_MD_WAIT, 5, 10,
                                                                               PIXEL_BASED_ALGORITHM,
                                                                               DEFAULT_STR_TOLERANCE)
            ],
        9: [
            "Valid parameters, whole HD frame comparison", API_PASS, (img_wait_im_match, MAX_X, MAX_Y,
                                                                      MAX_WIDTH, MAX_HEIGHT, T_MD_WAIT,
                                                                      DEFAULT_WAITGAP, PIXEL_BASED_ALGORITHM,
                                                                      DEFAULT_STR_TOLERANCE)
        ],
        10: [
            "Valid parameters,ref image and test region from two different screen", API_FAIL, (img_wait_im_match,
                                                                                               C_WAIT_IMG_MATCH[0],
                                                                                               C_WAIT_IMG_MATCH[1],
                                                                                               C_WAIT_IMG_MATCH[2],
                                                                                               C_WAIT_IMG_MATCH[3],
                                                                                               T_MD_WAIT,
                                                                                               DEFAULT_WAITGAP,
                                                                                               PIXEL_BASED_ALGORITHM,
                                                                                               DEFAULT_STR_TOLERANCE)
        ],
        11: ["Valid parameters, tolerance, boundary condition: 100", API_PASS, (img_wait_im_match, C_WAIT_IMG_MATCH[0], C_WAIT_IMG_MATCH[1],
                                                                          C_WAIT_IMG_MATCH[2], C_WAIT_IMG_MATCH[3],
                                                                          T_MD_WAIT, DEFAULT_WAITGAP,
                                                                                PIXEL_BASED_ALGORITHM, "100")
             ]
    }

    # ----------------------- WaitForCheckpoint

    wait_for_chkpt_params = {
        0: [
            "Valid parameters, DUT already in checkpoint screen", API_FAIL,
            CheckpointScreenToWait, T_MD_WAIT, INITIAL_DELAY
        ],
        1: [
            "Valid parameters, No screen transition to the checkpoint screen.", API_FAIL,
            CheckpointScreenToWait, T_MD_WAIT, INITIAL_DELAY
        ],
        2: [
            "Valid parameters, screen transition to the checkpoint screen.", API_PASS,
            CheckpointScreenToWait, T_MD_WAIT, INITIAL_DELAY
        ],
        3: [
            "Valid parameters, very small time to wait, 2 sec.", API_FAIL, CheckpointScreenToWait,
            2, INITIAL_DELAY
        ],
        4: [
            "InValid parameters, non existing checkpoint name", API_FAIL, "nonExisting",
            T_MD_WAIT, INITIAL_DELAY
        ],
        5: [
            "InValid parameters, negative time to wait, -20 sec", API_FAIL, CheckpointScreenToWait,
            -20, INITIAL_DELAY
        ],
        6: [
            "InValid parameters, negative initial delay, -2 sec", API_FAIL,
            CheckpointScreenToWait, T_MD_WAIT, -2
        ]
    }

    # ----------------- getOCRText

    get_ocr_text_params = {
        0: [
            "Valid parameters", API_PASS, (DEFAULT_FILTER, DEFAULT_LANG),
        ],
        1:[
            "Valid parameter: language: hin", API_PASS, (DEFAULT_FILTER, "hin")
        ],
        2: ["Valid parameter: language: empty", API_PASS, (DEFAULT_FILTER, "")
            ],
    }

    #  ----------------------- ImageMatch

    ref_img_0 = "ref_img_0"
    test_img_0 = "test_img_0"

    ref_image_param = (599, 509, 27, 37, ref_img_0, CAP_IMG_DEFAULT_QUALITY, 0)
    test_image_param = (599, 1043, 27, 37, test_img_0, 100, 2)

    image_match_params = {
        0: [
            "Valid parameters, PIXEL_BASED algorithm", API_PASS,
            (ref_img_0, test_img_0, PIXEL_BASED_ALGORITHM, DEFAULT_STR_TOLERANCE)
        ],
        1: [
            "Valid parameters, RMSE algorithm", API_PASS,
            (ref_img_0, test_img_0, RMSE_ALGORITHM, DEFAULT_STR_TOLERANCE)
        ],
        2: [
            "Valid parameters, tolerance, boundary condition: 100", API_PASS,
            (ref_img_0, test_img_0, RMSE_ALGORITHM, "100")
        ],
    }

    # ---------------------- ImageSearch

    image_search_params = {
        0: [
            "Valid parameters, expected region (small) and algoritham: SqdiffNormed",
            API_PASS, (imageSearchSingleOccurance, 199, 37, 427, 139, SqdiffNormed, DEFAULT_PERCENT_MATCH)
        ],
        1: [
            "Valid parameters, max region and algoritham: CcorrNormed", API_PASS, (imageSearchSingleOccurance,
                                                                                   MAX_X, MAX_Y, MAX_WIDTH,
                                                                                   MAX_HEIGHT, CcorrNormed,
                                                                                   DEFAULT_PERCENT_MATCH)
        ],
        2: [
            "Valid parameters, max region and algoritham: default_CcoeffNormed", API_PASS,
            (imageSearchSingleOccurance, MAX_X, MAX_Y, MAX_WIDTH, MAX_HEIGHT, default_CcoeffNormed,
             DEFAULT_PERCENT_MATCH)
        ],
        3: [
            "Valid parameters, percentMatchThreshold boundary condition: 0", API_PASS, (imageSearchSingleOccurance,
                                                                                        MAX_X, MAX_Y, MAX_WIDTH,
                                                                                        MAX_HEIGHT,
                                                                                        default_CcoeffNormed, 0)
        ],
        4: [
            "Valid parameters, multiple occurance of pattern", API_PASS, (imageSearchMultipleOccurance,
                                                                          MAX_X, MAX_Y, MAX_WIDTH, MAX_HEIGHT,
                                                                          default_CcoeffNormed,
                                                                          DEFAULT_PERCENT_MATCH)
        ]
    }

    # ------------------------------------ GetScreenTransitionTime

    get_screen_transition_time_params = {
        "chkpt_screen": [
            "Valid parameters, No screen transition from the checkpoint screen", API_FAIL,
            (chkpt_screen_elm, T_MD_WAIT, INITIAL_DELAY)
        ],

        "not_on_chkpt_screen": [
            "Valid parameters, not on checkpoint screen", API_PASS,
            (chkpt_screen_elm, T_MD_WAIT, INITIAL_DELAY)
        ],

        "move_out_chkpt_screen": [
            "Valid parameters, screen transition from the checkpoint screen", API_PASS,
            (chkpt_screen_elm, T_MD_WAIT, INITIAL_DELAY)
        ],

    }

    # -------------------------------- validateCheckPoint

    validate_chkpt_params = {
        0: ["Valid parameter, OCR checkpoint", API_PASS, SkyValidateCheckPointOCR],
        1: ["Valid parameter, Multi line OCR checkpoint", API_PASS, SkyValidateCheckPointMultiOCR],
        2: ["Valid parameter, IC checkpoint, pixel", API_PASS, SkyValidateCheckPointICpixel],
        3: ["Valid parameter, IC checkpoint, rmse", API_PASS, SkyValidateCheckPointICrmsel],
    }

    # -------------------------------- LaunchApp
    launch_app_params = {
        0: ["Valid Scenario, App is closed", API_PASS],
        1: ["Invalid Scenario, App is open already", API_FAIL],
        2: ["Invalid Scenario, App is backgrounded", API_FAIL],
    }

    # -------------------------------- GetElementCount
    element_count = 2
    get_element_count_params = {
        0: ["Mutliple element", API_PASS, element_count],
        1: ["Single element", API_PASS, 1],
        2: ["No element", API_FAIL, 0],
    }

    # -------------------------------- StartCaptureZapFrames
    start_capture_zap_frame_params = {
        0: ["Duration equal to WD timeout or greater", API_PASS, T_WD_TIMEOUT],
        1: ["Negative value for duration", API_FAIL, T_NEGETIVE_ZAP_FRM],
        2: ["Call multiple times without calling StopCaptureZapFrames", API_FAIL, T_VALID_ZAP_FRM]
    }

    # -------------------------------- IsSelected
    is_selected_params = {
        0: ["For an element without 'Selected' property", API_FAIL],
        1: ["Element with 'Selected' property", API_PASS]
    }

    # -------------------------------- IsEnabled
    is_enabled_params = {
        0: ["For an element without 'Enabled' property", API_FAIL],
        1: ["Element with 'Enabled' property", API_PASS]
    }
