# ''''''''''''''''''''''''''' CONFIG FILE - Generic '''''''''''''''''''''''''''''''''''''''''
# Author            :
# Date              : 252-04-2019
# Script Version    : 1.0
# ''''''''''''''''''''''''''' CONFIG FILE - Generic - END '''''''''''''''''''''''''''''''''


class ConfigBase(object):
    """
    This contains config variables generic to all devices.
    """
    element_type_to_test = 'id'

    # ==================================================== CONSTANTS/CHECKPOINTS
    # ================================================================================
    imageSearchSingleOccurance = "CheckpointPatternSingleOccurance_hotstar"
    not_initialized = "not_initialized"
    HotstarValidateCheckPointICpixel = "hotstar_valIcPixel"
    HotstarValidateCheckPointICrmsel = "hotstar_valIcRmse"
    HotstarValidateCheckPointOCR = "hotstar_Home_OCR"
    ParentCheckPoint = "Parent_checkpoint_hotstar"
    CheckpointScreenToWait = "hotstar_valIcPixel"
    Multiline_Ocr = "hotstar_Multiline_Ocr"
    hotstar_home_menu = "hotstar_Multiline_Ocr"
    hotstar_back_to_home = 'hotstar_back_to_home_frm_search'

    # ==================================================== COORDINATES =============
    # zee5
    # zee5_tap_get_ocr_text.py
    home_in_home_menu = {
        "SamsungGalaxyJ7_21435_7_0": (589, 736),
        "Samsung_galaxyJ7_a445_7_0": (589, 736),
        "Galaxy_J7_6.0.1": (589, 736),
        "OnePlus5T": (),
        "MiA1712": (589, 736),
        "iPhone8Plus_11_0": (193, 413),
        "IpadFE": (),
        "iPhone7_11_0_3": (),
        "iPhone_6": (193, 413),
        "iPhone6sPlus": (),
        "iPhone8 Plus_11": (),
        "OnePlus2": (),
        "NewOnePlus_5T": (139, 223),

        }
    # swipe coordinates
    c_swipe = {
        "SamsungGalaxyJ7_21435_7_0": [200, 500, 200, 100, 600],
        "Samsung_galaxyJ7_a445_7_0": [200, 500, 200, 100, 600],
        "Galaxy_J7_6.0.1": [200, 500, 200, 100, 600],
        "OnePlus5T": (),
        "MiA1712": [200, 500, 200, 100, 600],
        "iPhone8Plus_11_0": (),
        "IpadFE": (),
        "iPhone7_11_0_3": (),
        "iPhone_6": [200, 500, 200, 100, 600], #(427*0.577, 1227*0.521, 427*0.577, 259*0.521, 1000),
        "iPhone6sPlus": (),
        "iPhone8 Plus_11": (),
        "OnePlus2": (),
        "NewOnePlus_5T": [200, 500, 200, 100, 600],
    }

    # tappercent coordinates
    c_tap_percent = {
        "SamsungGalaxyJ7_21435_7_0": [588, 718],
        "Samsung_galaxyJ7_a445_7_0": [588, 718],
        "Galaxy_J7_6.0.1": [588, 718],
        "OnePlus5T": (),
        "MiA1712": [588, 718],
        "iPhone8Plus_11_0": (),
        "IpadFE": (),
        "iPhone7_11_0_3": (),
        "iPhone_6": [588, 718],
        "iPhone6sPlus": (),
        "iPhone8 Plus_11": (),
        "OnePlus2": (),
        "NewOnePlus_5T": [588, 718],
    }

    # swipe coordinates
    c_capture_image = {
        "SamsungGalaxyJ7_21435_7_0": (20, 20, 600, 600, "ref_image", 90, 0),
        "Samsung_galaxyJ7_a445_7_0": (20, 20, 600, 600, "ref_image", 90, 0),
        "Galaxy_J7_6.0.1": (20, 20, 600, 600, "ref_image", 90, 0),
        "OnePlus5T": (),
        "MiA1712": (20, 20, 600, 600, "ref_image", 90, 0),
        "iPhone8Plus_11_0": (),
        "IpadFE": (),
        "iPhone7_11_0_3": (),
        "iPhone_6": (20, 20, 600, 600, "ref_image", 90, 0),
        "iPhone6sPlus": (),
        "iPhone8 Plus_11": (),
        "OnePlus2": (),
        "NewOnePlus_5T": (20, 20, 600, 600, "ref_image", 90, 0),
    }

    c_capture_image_non_playback_region = {
        "SamsungGalaxyJ7_21435_7_0": (7, 753, 705, 243),
        "Samsung_galaxyJ7_a445_7_0": (7, 753, 705, 243),
        "Galaxy_J7_6.0.1": (7, 753, 705, 243),
        "OnePlus5T": (13, 413, 617, 219),
        "MiA1712": (11, 567, 685, 323),
        "iPhone8Plus_11_0": (7, 553, 705, 243),
        "IpadFE": (9, 550, 200, 80),
        "iPhone7_11_0_3": (7, 553, 705, 243),
        "iPhone 6": (7, 553, 630, 243),
        "iPhone6sPlus": (9, 1025, 200, 700),
        "iPhone8 Plus_11": (11, 567, 580, 323),
        "OnePlus2": (127, 571, 540, 263),
        "NewOnePlus_5T": (127, 571, 540, 263),
    }


    # ==================================================== END COORDINATES =============

    # =================================================== API PARAMETERS ===============
    # getOCRText params for HOME string in top left corner after selecting HOME option from the main menu
    home_launched = {
        "SamsungGalaxyJ7_21435_7_0": (62, 235, 55, 20, '', 'eng'),
        "Samsung_galaxyJ7_a445_7_0": (62, 235, 55, 20, '', 'eng'),
        "Galaxy_J7_6.0.1": (62, 235, 55, 20, '', 'eng'),
        "OnePlus5T": (),
        "MiA1712": (62, 235, 55, 20, '', 'eng'),
        "iPhone8Plus_11_0": (62, 235, 55, 20, '', 'eng'),
        "IpadFE": (),
        "iPhone7_11_0_3": (),
        "iPhone_6": (62, 235, 55, 20, '', 'eng'),
        "iPhone6sPlus": (),
        "iPhone8 Plus_11": (),
        "OnePlus2": (),
        "NewOnePlus_5T": (62, 235, 55, 20, '', 'eng'),
         }

    # area to check for motion
    c_detect_motion = {
        "SamsungGalaxyJ7_21435_7_0": (69, 127, 566, 261, 30, 5, '10'),
        "Samsung_galaxyJ7_a445_7_0": (69, 127, 566, 261, 30, 5, '10'),
        "Galaxy_J7_6.0.1": (69, 127, 566, 261, 30, 5, '10'),
        "OnePlus5T": (),
        "MiA1712": (69, 127, 566, 261, 30, 5, '10'),
        "iPhone8Plus_11_0": (69, 127, 566, 261, 30, 5, '10'),
        "IpadFE": (),
        "iPhone7_11_0_3": (),
        "iPhone_6": (69, 127, 566, 261, 30, 5, '10'),
        "iPhone6sPlus": (),
        "iPhone8 Plus_11": (),
        "OnePlus2": (),
        "NewOnePlus_5T": (69, 127, 566, 261, 30, 5, '10'),
         }

    c_getocrtext = {
        "SamsungGalaxyJ7_21435_7_0": (91, 37, 417, 139),
        "Samsung_galaxyJ7_a445_7_0": (91, 37, 417, 139),
        "Galaxy_J7_6.0.1": (91, 37, 417, 139),
        "OnePlus5T": (91, 37, 417, 139),
        "MiA1712": (13, 1243, 71, 33),
        "iPhone8Plus_11_0": (41, 1949, 95, 43),
        "IpadFE": (531, 1501, 69, 29),
        "iPhone7_11_0_3": (18, 1243, 71, 33),
        "iPhone 6": (33, 1243, 71, 33),
        "iPhone6sPlus": (33, 1243, 71, 33),
        "iPhone8 Plus_11": (33, 1243, 67, 31),
        "OnePlus2": (31, 1179, 72, 20),
        "NewOnePlus_5T": (91, 37, 417, 139),

        }

    c_colour_match = {
        "SamsungGalaxyJ7_21435_7_0": (119, 37, 427, 139),
        "Samsung_galaxyJ7_a445_7_0": (119, 37, 427, 139),
        "Galaxy_J7_6.0.1": (119, 37, 427, 139),
        "OnePlus5T": (119, 37, 427, 139),
        "MiA1712": (38, 1243, 71, 33),
        "iPhone8Plus_11_0": (61, 1949, 95, 43),
        "IpadFE": (569, 1501, 69, 29),
        "iPhone7_11_0_3": (38, 1243, 71, 33),
        "iPhone 6": (38, 1243, 71, 33),
        "iPhone6sPlus": (38, 1243, 71, 33),
        "iPhone8 Plus_11": (33, 1243, 67, 31),
        "OnePlus2": (31, 1179, 72, 20),
        "NewOnePlus_5T": (119, 37, 427, 139),
    }

    c_img_search = (21, 81, 53, 47)
    c_img_search_wrong = (179, 37, 427, 139) # to give other area where checkpoint does not exist


    # constants for ADB, GetDeviceHeight and GetDeviceWidth APIs as dicts for different devices

    # 1. ADB and Device details of Samsung_21435
    dict_21435 = {
        'GetAdbAPIVersion': '24',
        'GetAdbVersion': '7.0',
        'GetApkVersion': '7.0',
        'GetDeviceHeight': 1920,
        'GetDeviceWidth': 1080,
    }

    dict_samsung = {
        'GetAdbAPIVersion': '23',
        'GetAdbVersion': '6.0.1',
        'GetApkVersion': '6.0.1',
        'GetDeviceHeight': 1920,
        'GetDeviceWidth': 1080,
    }

    # 2. ADB and Device details of Samsung_aa455
    dict_aa455 = {
        'GetAdbAPIVersion': '24',
        'GetAdbVersion': '7.0',
        'GetApkVersion': '7.0',
        'GetDeviceHeight': 1920,
        'GetDeviceWidth': 1080,
    }

    # 3. ADB and Device details of MIA1
    dict_MIA1 = {
        'GetAdbAPIVersion': '25',
        'GetAdbVersion': '7.1.2',
        'GetApkVersion': '7.1.2',
        'GetDeviceHeight': 1920,
        'GetDeviceWidth': 1080,
    }

    # 4. ADB and Device details of OnePlus5T
    dict_5T = {
        'GetAdbAPIVersion': '26',
        'GetAdbVersion': '8.0.0',
        'GetApkVersion': '8.0.0',
        'GetDeviceHeight': 2034,
        'GetDeviceWidth': 1080,
    }

    dict_oneplus2 = {
        'GetAdbAPIVersion': '26',
        'GetAdbVersion': '8.0.0',
        'GetApkVersion': '8.0.0',
        'GetDeviceHeight': 2034,
        'GetDeviceWidth': 1080,
    }

    dict_NewOnePlus_5T = {
        'GetAdbAPIVersion': '26',
        'GetAdbVersion': '8.0.0',
        'GetApkVersion': '8.0.0',
        'GetDeviceHeight': 2034,
        'GetDeviceWidth': 1080,
    }

    # 5. Device details of iPhone8plus
    dict_i8plus = {
        'GetAdbAPIVersion': '',
        'GetAdbVersion': '',
        'GetApkVersion': '11.0',
        'GetDeviceHeight': 667,
        'GetDeviceWidth': 375,
    }

    # 6. Device details of iPhone8
    dict_i7 = {
        'GetAdbAPIVersion': '',
        'GetAdbVersion': '',
        'GetDeviceHeight': 2034,
        'GetDeviceWidth': 1080,
    }

    # 7. Device details of iPhone6plus
    dict_i6plus = {
        'GetAdbAPIVersion': '',
        'GetAdbVersion': '',
        'GetDeviceHeight': 2034,
        'GetDeviceWidth': 1080,
    }

    # 8. Device details of iPhone6
    dict_i6 = {
        'GetAdbAPIVersion': '',
        'GetAdbVersion': '',
        'GetApkVersion': '12.1',
        'GetDeviceHeight': 667,
        'GetDeviceWidth': 375,
    }

    # 9. Device details of ipad
    dict_ipad = {
        'GetAdbAPIVersion': '',
        'GetAdbVersion': '',
        'GetApkVersion': '10.3.3',
        'GetDeviceHeight': 768,
        'GetDeviceWidth': 1024,
    }

    # 1. MobileDUTProperty details of Samsung_21435
    dict_property_21435 = {
        0: "933",
        1: "SamsungGalaxyJ7_21435_7_0",
        2: "Samsung_21435",
        3: "Android",
        4: "7.0",
        5: "",
        6: "52036efdeac21435",
        7: "manufacturer",
        8: "",
        9: "115",
        10: "2",
        12: "ScheduledExecution",  # ManualTesting (for local execution)
    }

    dict_property_samsung = {
        0: "939",
        1: "Galaxy_J7_6.0.1",
        2: "SamSung",
        3: "Android",
        4: "6.0.1",
        5: "none",
        6: "520396d95b40c377",
        7: "falconeyetest",
        8: "",
        9: "115",
        10: "9",
        12: "ScheduledExecution",  # ManualTesting (for local execution)
    }

    # 2. MobileDUTProperty details of iphone8plus
    dict_property_i8plus = {
        0: "932",
        1: "iPhone8 Plus_11",
        2: "iPhone",
        3: "iOS",
        4: "11.0",
        5: "apple",
        6: "50f1975ffa0d7bde86a70da88f752b8435542e1b",
        7: "manufacturer",
        8: "",
        9: "115",
        10: "1",
        12: "ScheduledExecution",  # ManualTesting (for local execution)
    }

    # 3. MobileDUTProperty details of iphone7
    dict_property_i7 = {
        0: "934",
        1: "iPhone7_11_0_3",
        2: "apple",
        3: "iOS",
        4: "10.3.1",
        5: "",
        6: "a357b3dd0060713d39c63c42537bfedb305dae91",
        7: "apple",
        8: "iPhone8",
        9: "115",
        10: "3",
        12: "ScheduledExecution",  # ManualTesting (for local execution)
    }

    # 4. MobileDUTProperty details of iphone12_1
    dict_property_iphone_12_1 = {
        0: "935",
        1: "Iphone_12_1",
        2: "iPhone",
        3: "iOS",
        4: "12.1",
        5: "",
        6: "2d05f50798febdb805a4786a51792542e09ae22f",
        7: "manufacturer",
        8: "",
        9: "115",
        10: "4",
        12: "ScheduledExecution",  # ManualTesting (for local execution)
    }

    # 5. MobileDUTProperty details of Redmi
    dict_property_MIA1 = {
        0: "940",
        1: "MiA1712",
        2: "Redmi",
        3: "Android",
        4: "7.1.2",
        5: "",
        6: "006abf510704",
        7: "falconeye_api1234567890*^%$#%$^",
        8: "",
        9: "115",
        10: "10",
        12: "ScheduledExecution",  # ManualTesting (for local execution)
    }

    # 6. MobileDUTProperty details of iPhone 6
    dict_property_iphone_6 = {
        0: "936",
        1: "iPhone 6",
        2: "iPhone",
        3: "iOS",
        4: "12.1.2",
        5: "",
        6: "724b568ddb5c4850535bc549a3f2296e4fc4a912",
        7: "falconeye_api1234567890*^%$#%$^",
        8: "",
        9: "115",
        10: "5",
        12: "ScheduledExecution",  # ManualTesting (for local execution)
    }

    # 7. MobileDUTProperty details of Samsung Galaxy a445
    dict_property_a445 = {
        0: "938",
        1: "Samsung_galaxyJ7_a445_7_0",
        2: "Samsung_a445",
        3: "Android",
        4: "7.0",
        5: "sp%ecial",
        6: "330018c873caa455",
        7: "falconeye_api1234567890*^%$#%$^",
        8: "",
        9: "115",
        10: "8",
        12: "ScheduledExecution",  # ManualTesting (for local execution)
    }

    # 8. MobileDUTProperty details of Ipad
    dict_property_ipad = {
        0: "937",
        1: "IpadFE",
        2: "iPad",
        3: "iOS",
        4: "10.3.3",
        5: "123*",
        6: "84926c63e2a43ab15d764dadc15514c0075f3a8a",
        7: "falconeye_api1234567890*^%$#%$^",
        8: "",
        9: "115",
        10: "6",
        12: "ScheduledExecution",  # ManualTesting (for local execution)
    }

    # 8. MobileDUTProperty details of OnePlus2
    dict_property_oneplus2 = {
        0: "939",
        1: "OnePlus2",
        2: "OnePlus",
        3: "Android",
        4: "8.0.0",
        5: "",
        6: "f3b91a95",
        7: "falconeye_api1234567890*^%$#%$^",
        8: "",
        9: "115",
        10: "9",
        12: "ScheduledExecution",  # ManualTesting (for local execution)
    }

    # 8. MobileDUTProperty details of New OnePlus5T
    dict_property_newoneplus5T = {
        0: "939",
        1: "NewOnePlus_5T",
        2: "OnePlus",
        3: "Android",
        4: "8.0.0",
        5: "",
        6: "2128f43",
        7: "falconeye",
        8: "",
        9: "115",
        10: "9",
        12: "ScheduledExecution",  # ManualTesting (for local execution)
    }

    # Dictionary of DUT names
    dict_dut_name = {'SamsungGalaxyJ7_21435_7_0': dict_21435, 'Samsung_galaxyJ7_a445_7_0': dict_aa455,
                     'Galaxy_J7_6.0.1': dict_samsung,
                     'OnePlus5T': dict_5T, 'MiA1712': dict_MIA1, 'iPhone8Plus_11_0': dict_i8plus, 'IpadFE': dict_ipad,
                     'iPhone7_11_0_3': dict_i7, 'iPhone 6': dict_i6, 'iPhone6sPlus': dict_i6plus,
                     'iPhone8 Plus_11': dict_i8plus, 'OnePlus2': dict_oneplus2, 'NewOnePlus_5T': dict_NewOnePlus_5T
                     }

    # Dictionary of DUT property mapping
    dut_property_dict_map = {'SamsungGalaxyJ7_21435_7_0': dict_property_21435, 'iPhone8 Plus_11': dict_property_i8plus,
                             'iPhone7_11_0_3': dict_property_i7, 'Iphone_12_1': dict_property_iphone_12_1,
                             'Galaxy_J7_6.0.1': dict_property_samsung,
                             'MiA1712': dict_property_MIA1, 'iPhone 6': dict_property_iphone_6,
                             'Samsung_galaxyJ7_a445_7_0': dict_property_a445, 'IpadFE': dict_property_ipad,
                             'OnePlus2': dict_property_oneplus2, 'NewOnePlus_5T': dict_property_newoneplus5T,
                             }

    # =================================================== END API PARAMETERS ===============

    # ==================================================== STRING VARIABLES =============
    # HOME string in top left corner after selecting HOME option from the main menu
    home_string = 'HOME'
    search_text = "Bal Hanuman"
    txt_gettext = 'Home'
    txt_getocrtext = "hotstar"
    gettext_index = 8
    txt_menu = {
        1 : 'HOME',
        2 : 'PREMIUM',
        3 : 'SHOWS',
    }

    searchbox_default_text = 'Search'
    tv_shows_view_all_page_title = "All TV Shows"

    CACHE_VALID_URL = 'http://10.47.166.48/TestImage/ImageForDynamicImageCompare.JPG'
    INVALID_URL = "https://invalidurl1234/"
    IMG_NAME = "testimage"
    LONG_IMG_NAME = "testimage_abcdefghijklmnopqrstuvwxyz_abcdefghijklmnopqrstuvwxyz_abc\
        defghijklmnopqrstuvwxyz_abcdefghijklmnopqrstuvwxyz_abcdefghijklmnopqrstuvwxyz_ab\
        cdefghijklmnopqrstuvwxyz.jpg"
    IMG_NAME_SPL = "test@#$%^&*"
    URL_WITHOUT_EXT = 'http://10.47.166.48/TestImage/ImageForDynamicImageCompare'
    EMPTY = ""
    attr_list = "enabled,checked,clickable,checkable,focusable,focused,scrollable,password,selected"

    # SendAndroidKeyCode
    DEL = "Keycode_DEL"  # Backspace key
    BACK = "Keycode_BACK"  # Back key

    search_icon_index = 3
    volume_levels = 5
    overwrite_file = 0

    # ------------------------------------ GetScreenTransitions
    HPA_X = 69
    HPA_Y = 127
    HPA_W = 566
    HPA_H = 261
    HPA_SENS = 3
    HPA_DUR = 60

    # WAIT FOR CHECKPOINT
    INITIAL_DELAY = 2
    TIME_TO_WAIT = 10

    RETURN_FAIL_VAL = -1
    RETURN_PASS_VAL = 1
    T_MD_WAIT = 20
    captureZapTime = 30

    # dynamic image compare
    dyn_img = "dynamic_compare_img"
    cap_img = "cap_dynamic_comp_img"
    CACHE_VALID_URL_FOR_DYNAMIC_COMPARE = "http://10.47.166.48/TestImage/ImageForDynamicImageCompare.JPG"
    DEFAULT_DYN_TOLERANCE = 15
    c_capture_image_for_dyn_im = (5, 39, 166, 71,cap_img,90, 0)

    # GetScreenTransitionTime
    SCREEN_TRANSITION_FAIL_VAL = -1.0

    TAP_PERCENTAGE = (30, 30)

    c_home = [88, 74, 192, 54]
    c_mline = [505, 1065, 122, 61]

    # ==================================================== END STRING VARIABLES =============

    # ==================================================== coordinates
    # ================================================================================
    C_CAP_IMAGE = (89, 60, 139, 69)
    C_TAP_PLAYBACK = (150, 355)
    C_DET_MOTION = (176, 99, 439, 251)
    C_DYN_IMG_COMP = (5, 39, 166, 71)
    C_WAIT_IMG_MATCH = (5, 39, 166, 71)
    c_press_move = (3, 405, 311, 0)

    # ==================================================== general
    # ================================================================================
    API_PASS = True
    API_FAIL = False


    WAIT_FOR_HOME = 30
    CAP_IMAGE_NAME = "cap_img"
    CAP_IMG_OVERWRITE = "cap_img_unique"
    CAP_IMG_DEFAULT_QUALITY = 90

    # detect motion
    DEFAULT_TIMEOUT = 20
    DEFAULT_WAITGAP = 5
    DEFAULT_STR_TOLERANCE = "8"

    # WAIT IMAGE MATCH
    PIXEL_BASED_ALGORITHM = 1
    RMSE_ALGORITHM = 2

    # status
    PASSED = "PASSED"
    FAILED = "FAILED"
    UNKNOWN = "UNKNOWN"
    ABORTED = "ABORTED"
    ERROR = "ERROR"
    VALID_STEP_NAME = "VALID STEP"
    STEP_NAME_WITH_SPL_CHAR = "abc!@#$abc)(*&^123"
    commit_apis_valid_status = [PASSED, FAILED, UNKNOWN, ABORTED, ERROR]

    # IMAGE SEARCH
    SqdiffNormed = 1
    CcorrNormed = 3
    default_CcoeffNormed = 5
    DEFAULT_PERCENT_MATCH = 97

    MAX_X = 0
    MAX_Y = 0
    MAX_WIDTH, MAX_HEIGHT = "max_width", "max_height"

    video_sources = ["camera0", "galaxy_j7_dev", "camera1", "21435", "aa455", "camera_ipad"]

    # GETOCRTEXT
    DEFAULT_FILTER = "Greyscale"
    DEFAULT_LANG = "eng"

    # WaitImageMatch
    img_wait_im_match = "refImage"
    pixel_tolerance = "15;10"

    # WaitOCRMatch
    home_text = 'hotstar'
    mline_text = 'hotstar\
                PREMIUM'

    # colormatch
    matchColor = "[231, 5, 5]"
    COLOR_TOLERANCE = '[10,10,10]'
    FLATNESS = 90

    DEF_COMP_TYPE = 1
    ACCURACY = 90

    ALERT_DISMISS = 'Dismiss'
    TAP_PERCENT_FIRST_SEARCH_RESULT = (30, 16)
    TAP_PERCENT_VIDEO_TO_PLAY = (30, 47)

    C_COLOR_MATCH = (37, 81, 15, 23)

    # ================================================== Scenarios
    sanity_cache_image_from_url_params = (0,)
    cache_image_from_url_params = {
        0: ["Valid url, Valid image name", CACHE_VALID_URL, IMG_NAME, API_PASS],
        1: ["Invalid url, Valid image name", INVALID_URL, IMG_NAME, API_FAIL],
        2: ["Valid url, Lengthy image name", CACHE_VALID_URL, LONG_IMG_NAME, API_FAIL],
        3: ["Invalid parameter' Empty string as image name", CACHE_VALID_URL, EMPTY, API_FAIL],
        4: ["Invalid parameter' image name with special character", CACHE_VALID_URL, IMG_NAME_SPL, API_FAIL],
        5: ["Invalid parameter' URL without file extension", URL_WITHOUT_EXT, IMG_NAME, API_FAIL],
        6: ["Invalid parameter' Empty string as URL", EMPTY, IMG_NAME, API_FAIL],
    }

    # ---------------------------  CaptureImage
    # the parametrs till key-3 are being used in sanity scripts, so for any modifications, please dont
    # change the parameters till key-3 (0, 1, 2, 3)

    sanity_capture_image_params = (0, 1, 2, 3,)
    capture_image_params = {
        0: [
            "Valid parameters: overWriteAction: 1 (OverWrite action set to Error)", API_FAIL,
            (C_CAP_IMAGE[0], C_CAP_IMAGE[1], C_CAP_IMAGE[2], C_CAP_IMAGE[3], CAP_IMG_OVERWRITE, CAP_IMG_DEFAULT_QUALITY,
             1)
        ],
        1: [
            "Valid parameters: overWriteAction: 0 (overwrites the existing file)", API_PASS,
            (C_CAP_IMAGE[0], C_CAP_IMAGE[1], C_CAP_IMAGE[2], C_CAP_IMAGE[3], CAP_IMAGE_NAME, CAP_IMG_DEFAULT_QUALITY, 0)
        ],
        2: [
            "Valid parameters: overWriteAction: 2 (creates a new file)", API_PASS,
            (C_CAP_IMAGE[0], C_CAP_IMAGE[1], C_CAP_IMAGE[2], C_CAP_IMAGE[3], CAP_IMAGE_NAME, CAP_IMG_DEFAULT_QUALITY, 2)
        ],
        3: [
            "InValid parameters: overWriteAction: 5", API_FAIL,
            (C_CAP_IMAGE[0], C_CAP_IMAGE[1], C_CAP_IMAGE[2], C_CAP_IMAGE[3], CAP_IMAGE_NAME, CAP_IMG_DEFAULT_QUALITY, 5)
        ],
    }

    # ---------------------------  DetectMotion
    sanity_detect_motion_params = (0, 2,)
    detect_motion_params = {
        0: [
            "Valid parameters", API_PASS,
            (C_DET_MOTION[0], C_DET_MOTION[1], C_DET_MOTION[2], C_DET_MOTION[3], DEFAULT_TIMEOUT, DEFAULT_WAITGAP,
             DEFAULT_STR_TOLERANCE)
        ],
        1: [
            "Valid: tolerance, boundary condition [100]", API_FAIL,
            (
            C_DET_MOTION[0], C_DET_MOTION[1], C_DET_MOTION[2], C_DET_MOTION[3], DEFAULT_TIMEOUT, DEFAULT_WAITGAP, "100")
        ],
        2: [
            "Valid: tolerance, boundary condition [0]", API_PASS,
            (C_DET_MOTION[0], C_DET_MOTION[1], C_DET_MOTION[2], C_DET_MOTION[3], DEFAULT_TIMEOUT, DEFAULT_WAITGAP, "0")
        ],

    }

    # ---------------------------  DynamicImageCompare
    sanity_dynamic_image_compare_params = (0, 2)
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

    }

    #  ----------------------- ImageMatch

    ref_img_0 = "ref_img_0"
    test_img_0 = "test_img_0"

    ref_image_param = (21, 81, 53, 47, ref_img_0, CAP_IMG_DEFAULT_QUALITY, 0)
    test_image_param = (21, 81, 53, 47, test_img_0, 90, 0)

    sanity_image_match_params = (0, 1, 2,)
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
            "Valid parameters, tolerance > boundary condition: 100", API_PASS,
            (ref_img_0, test_img_0, RMSE_ALGORITHM, "100")
        ],

    }

    # ---------------------- ImageSearch
    # moved to respective configs; so update the device config file any change required

    sanity_image_search_params = (0, 1, 2)
    image_search_params = {
        0: [
            "Valid parameters, expected region (small) and algoritham: SqdiffNormed",
            API_PASS, (imageSearchSingleOccurance, c_img_search[0], c_img_search[1],
                       c_img_search[2], c_img_search[3], SqdiffNormed, DEFAULT_PERCENT_MATCH)
        ],
        1: [
            "Valid parameters, max region and algoritham: CcorrNormed", API_PASS, (imageSearchSingleOccurance,
                                                                                   MAX_X, MAX_Y, MAX_WIDTH,
                                                                                   MAX_HEIGHT, CcorrNormed,
                                                                                   DEFAULT_PERCENT_MATCH)
        ],
        2: [
            "Valid parameters, Checkpoint not available on the screen",
            API_FAIL, (imageSearchSingleOccurance, c_img_search_wrong[0], c_img_search_wrong[1],
                       c_img_search_wrong[2], c_img_search_wrong[3], SqdiffNormed, DEFAULT_PERCENT_MATCH)
        ],

    }

    # indices of parameters considered in sanity test script to cover positive scenarios
    sanity_validate_chkpt_params = (0, 1, 2, 3, 4,)

    # -------------------------------- validateCheckPoint

    validate_chkpt_params = {
        0: ["Invalid scenario, checkpoint object without initializing", API_FAIL, not_initialized],
        1: ["Valid parameter, IC checkpoint, pixel", API_PASS, HotstarValidateCheckPointICpixel],
        2: ["Valid parameter, IC checkpoint, rmse", API_PASS, HotstarValidateCheckPointICrmsel],
        3: ["Valid parameter, Checkpoint created for parent DUT", API_PASS, ParentCheckPoint],
        4: ["Valid parameter, Multiline OCR Checkpoint", API_PASS, Multiline_Ocr],

    }

    # ----------------- getOCRText
    get_ocr_text_valid_param = [
        "Valid parameters", API_PASS, (DEFAULT_FILTER, DEFAULT_LANG),
    ]  # expects the text - 'ZEE5'


    # indices of parameters considered in sanity test script to cover positive scenarios
    sanity_wait_chkpt_match_params = (0, 1, 2, 3,)

    # ---------------------------  WaitCheckPointMatch

    wait_chkpt_match_params = {
        0: [
            "Valid parameter, OCR checkpoint", API_PASS, HotstarValidateCheckPointOCR,
            TIME_TO_WAIT, DEFAULT_WAITGAP
        ],
        1: [
            "Valid parameter, IC checkpoint, pixel", API_PASS, HotstarValidateCheckPointICpixel,
            TIME_TO_WAIT, DEFAULT_WAITGAP
        ],
        2: [
            "Valid parameter, IC checkpoint, rmse",
            API_PASS, HotstarValidateCheckPointICrmsel, TIME_TO_WAIT, DEFAULT_WAITGAP
        ],
        3: [
            "Valid parameter, already on checkpoint screen", API_PASS, HotstarValidateCheckPointOCR,
            TIME_TO_WAIT, DEFAULT_WAITGAP
        ],

    }

    # indices of parameters considered in sanity test script to cover positive scenarios
    sanity_wait_for_chkpt_params = (0, 1, 2, 3,)

    # ----------------------- WaitForCheckpoint
    wait_for_chkpt_params = {
        0: [
            "Valid parameters, DUT already on checkpoint screen", RETURN_PASS_VAL,
            (CheckpointScreenToWait, T_MD_WAIT, INITIAL_DELAY)
        ],
        1: [
            "Valid parameters, No screen transition to the checkpoint screen", RETURN_FAIL_VAL,
            (Multiline_Ocr, T_MD_WAIT, INITIAL_DELAY)
        ],
        2: [
            "Valid parameters, Maximum TimeToWait = WD Timeout", RETURN_PASS_VAL,
            (CheckpointScreenToWait, T_MD_WAIT, 5)
        ],

        3: [
            "Valid parameters, screen transition to the checkpoint screen", RETURN_PASS_VAL,
            (hotstar_back_to_home, T_MD_WAIT, INITIAL_DELAY)
        ],

    }


    # -------------------------------- WaitImageMatch

    sanity_wait_image_match_params = (0, 1, 2, 3)
    wait_image_match_params = {

        0: ["Valid parameters RMSE algorithm", API_PASS,
            (img_wait_im_match, C_WAIT_IMG_MATCH[0], C_WAIT_IMG_MATCH[1], C_WAIT_IMG_MATCH[2], C_WAIT_IMG_MATCH[3],
             T_MD_WAIT, DEFAULT_WAITGAP, RMSE_ALGORITHM, DEFAULT_STR_TOLERANCE),
            ],
        1: ["Valid parameters, PIXEL_BASED algorithm", API_PASS,
            (img_wait_im_match, C_WAIT_IMG_MATCH[0], C_WAIT_IMG_MATCH[1], C_WAIT_IMG_MATCH[2], C_WAIT_IMG_MATCH[3],
             T_MD_WAIT, DEFAULT_WAITGAP, PIXEL_BASED_ALGORITHM, pixel_tolerance),
            ],
        2: [
            "Valid parameters, whole HD frame comparison", API_PASS,
            (img_wait_im_match, MAX_X, MAX_Y, MAX_WIDTH, MAX_HEIGHT, T_MD_WAIT, DEFAULT_WAITGAP, PIXEL_BASED_ALGORITHM,
             DEFAULT_STR_TOLERANCE)
            ],
        3: ["Valid parameters, tolerance, boundary condition: 100", API_PASS,
             (img_wait_im_match, C_WAIT_IMG_MATCH[0], C_WAIT_IMG_MATCH[1], C_WAIT_IMG_MATCH[2], C_WAIT_IMG_MATCH[3],
              T_MD_WAIT, DEFAULT_WAITGAP, PIXEL_BASED_ALGORITHM, "100")
             ],

    }

    # -------------------------------- WaitOCRMatch


    sanity_wait_ocr_match_params = (0, 1,)
    wait_ocr_match_params = {
        0: ("Valid parameters", API_PASS, [home_text, c_home[0], c_home[1], c_home[2], c_home[3], T_MD_WAIT,
                DEFAULT_WAITGAP, DEFAULT_LANG, DEFAULT_FILTER, DEF_COMP_TYPE, ACCURACY]),

        1: ("Valid parameters, Multiline OCR", API_PASS, [mline_text, c_mline[0], c_mline[1], c_mline[2], c_mline[3], T_MD_WAIT,
            DEFAULT_WAITGAP, DEFAULT_LANG, DEFAULT_FILTER, DEF_COMP_TYPE, ACCURACY]),


    }

    # ------------------------------------ GetScreenTransitionTime

    sanity_get_screen_transition_time_params = ('chkpt_screen', 'not_on_chkpt_screen', 'move_out_chkpt_screen')

    get_screen_transition_time_params = {
        "chkpt_screen": [
            "Valid parameters, No screen transition from the checkpoint screen", SCREEN_TRANSITION_FAIL_VAL,
            (imageSearchSingleOccurance, T_MD_WAIT, INITIAL_DELAY)
        ],

        "not_on_chkpt_screen": [
            "Valid parameters, not on checkpoint screen", SCREEN_TRANSITION_FAIL_VAL,
            (hotstar_home_menu, T_MD_WAIT, INITIAL_DELAY)
        ],

        "move_out_chkpt_screen": [
            "Valid parameters, screen transition from the checkpoint screen", SCREEN_TRANSITION_FAIL_VAL,
            (imageSearchSingleOccurance, T_MD_WAIT, INITIAL_DELAY)
        ],

    }

    # ----------------------- WaitColorMatch
    sanity_wait_color_match_params = (0, 1, 2, 3,)

    wait_color_match_params = {
        0: [
            "Valid parameters", API_PASS,
            [matchColor, C_COLOR_MATCH[0], C_COLOR_MATCH[1], C_COLOR_MATCH[2], C_COLOR_MATCH[3],
             T_MD_WAIT, DEFAULT_WAITGAP, COLOR_TOLERANCE, FLATNESS],
        ],
        1: [
            "Valid parameters, flatness boundary condition : 0", API_PASS,
            [matchColor, C_COLOR_MATCH[0], C_COLOR_MATCH[1],
             C_COLOR_MATCH[2], C_COLOR_MATCH[3], T_MD_WAIT,
             DEFAULT_WAITGAP, COLOR_TOLERANCE, 0],
        ],
        2: ["Valid parameters, flatness boundary condition : 100", API_FAIL, [matchColor, C_COLOR_MATCH[0],
                                                                              C_COLOR_MATCH[1], C_COLOR_MATCH[2],
                                                                              C_COLOR_MATCH[3],
                                                                              T_MD_WAIT, DEFAULT_WAITGAP,
                                                                              COLOR_TOLERANCE, 100],
            ],
        3: [
            "Valid parameters, Multiple occurrences of Match color", API_PASS, [matchColor, MAX_X, MAX_Y,
                                                                                MAX_WIDTH, MAX_HEIGHT,
                                                                                T_MD_WAIT, DEFAULT_WAITGAP,
                                                                                COLOR_TOLERANCE, FLATNESS],
        ],

    }