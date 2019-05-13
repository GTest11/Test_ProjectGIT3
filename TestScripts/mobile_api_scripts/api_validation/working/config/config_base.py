

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

    element_type_to_test = 'xpath'



    # ==================================================== CONSTANTS
    # ================================================================================
    T_MIN_WAIT = 3
    T_WAIT_FOR_HOME = 50
    T_MD_WAIT = 20
    T_WD_TIMEOUT = 160  # StartCaptureZapFrames, send_app_background.py

    # StartCaptureZapFrames
    T_NEGETIVE_ZAP_FRM = -30
    T_VALID_ZAP_FRM = 30
    RETURN_FAIL_VAL = -1
    RETURN_PASS_VAL = 1
    T_NEG_TIME_TO_WAIT = -20    #waitforcheckpoint.py, send_app_background.py
    T_NO_WAIT = 0   #waitforcheckpoint.py, send_app_background.py
    TAP_PERCENTAGE = (30, 50) #(1990, 82)

    DEVICE_DETAILS = [
        ("DUT_NAME", 1), ("DUT_UDID", 6), ("DUT_PLATFORMNAME", 3), ("DUT_PLATFORMVERSION", 4),
        ("DUT_RACKNO", 9), ("DUT_SLOTNO", 10),
    ]

    video_sources = ["camera0", "camera1", "f3b91a95", "21435", "aa455", "camera_ipad"]
    non_existing_source = "non-existing-source"
    available_video_source = "camera1"  # video source configured for all DUTs
    min_swipe_duration = 550
    yt_default_text = 'Search YouTube'

    # constants for ADB, GetDeviceHeight and GetDeviceWidth APIs as dicts for different devices

    # 1. ADB and Device details of Samsung_21435
    dict_21435 = {
        'GetAdbAPIVersion': '24',
        'GetAdbVersion': '7.0',
        'GetApkVersion': '7.0',
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
        0 : "933",
        1 : "SamsungGalaxyJ7_21435_7_0",
        2 : "Samsung_21435",
        3 : "Android",
        4 : "7.0",
        5 : "",
        6 : "52036efdeac21435",
        7 : "manufacturer",
        8 : "",
        9 : "115",
        10 : "2",
        12 : "ScheduledExecution",  # ManualTesting (for local execution)
    }

    # 2. MobileDUTProperty details of iphone8plus
    dict_property_i8plus = {
        0 : "932",
        1 : "iPhone8 Plus_11",
        2 : "iPhone",
        3 : "iOS",
        4 : "11.0",
        5 : "apple",
        6 : "50f1975ffa0d7bde86a70da88f752b8435542e1b",
        7 : "manufacturer",
        8 : "",
        9 : "115",
        10 : "1",
        12 : "ScheduledExecution",  # ManualTesting (for local execution)
    }

    # 3. MobileDUTProperty details of iphone7
    dict_property_i7 = {
        0 : "934",
        1 : "iPhone7_11_0_3",
        2 : "apple",
        3 : "iOS",
        4 : "10.3.1",
        5 : "",
        6 : "a357b3dd0060713d39c63c42537bfedb305dae91",
        7 : "apple",
        8 : "iPhone8",
        9 : "115",
        10 : "3",
        12 : "ScheduledExecution",  # ManualTesting (for local execution)
    }

    # 4. MobileDUTProperty details of iphone12_1
    dict_property_iphone_12_1 = {
        0 : "935",
        1 : "Iphone_12_1",
        2 : "iPhone",
        3 : "iOS",
        4 : "12.1",
        5 : "",
        6 : "2d05f50798febdb805a4786a51792542e09ae22f",
        7 : "manufacturer",
        8 : "",
        9 : "115",
        10 : "4",
        12 : "ScheduledExecution",  # ManualTesting (for local execution)
    }

    # 5. MobileDUTProperty details of Redmi
    dict_property_MIA1 = {
        0 : "940",
        1 : "MiA1712",
        2 : "Redmi",
        3 : "Android",
        4 : "7.1.2",
        5 : "",
        6 : "006abf510704",
        7 : "falconeye_api1234567890*^%$#%$^",
        8 : "",
        9 : "115",
        10 : "10",
        12 : "ScheduledExecution",  # ManualTesting (for local execution)
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
                     'OnePlus5T': dict_5T, 'MiA1712': dict_MIA1, 'iPhone8Plus_11_0': dict_i8plus, 'IpadFE': dict_ipad,
                     'iPhone7_11_0_3': dict_i7, 'iPhone 6': dict_i6, 'iPhone6sPlus': dict_i6plus,
                     'iPhone8 Plus_11': dict_i8plus, 'OnePlus2': dict_oneplus2
                     }

    # Dictionary of DUT property mapping
    dut_property_dict_map = {'SamsungGalaxyJ7_21435_7_0': dict_property_21435, 'iPhone8 Plus_11': dict_property_i8plus,
                             'iPhone7_11_0_3': dict_property_i7, 'Iphone_12_1': dict_property_iphone_12_1,
                             'MiA1712': dict_property_MIA1, 'iPhone 6': dict_property_iphone_6,
                             'Samsung_galaxyJ7_a445_7_0': dict_property_a445, 'IpadFE': dict_property_ipad,
                             'OnePlus2': dict_property_oneplus2, 'NewOnePlus_5T': dict_property_newoneplus5T,
                             }

    #'Samsung_galaxyJ7_a445_7_0': dict_property_aa455,
    #                     'OnePlus5T': dict_property_5T, 'MiA1712': dict_property_MIA1, 'iPhone8Plus_11_0': dict_property_i8plus, 'IpadFE': dict_property_ipad,
    #                     'iPhone7_11_0_3': dict_i7, 'iPhone6': dict_i6, 'iPhone6sPlus': dict_i6plus,
    #                     'iPhone8 Plus_11': dict_property_i8plus, 'OnePlus2': dict_property_oneplus2


    # ==================================================== END CONSTANTS =============



    # ==================================================== COORDINATES
    # ================================================================================
    C_TAP_PLAYBACK = (260, 300) # is_selected.py
    C_SWIPE_WRONG = (1000, 1000, -1000, -1000)
    C_TOP_DOWN_SWIPE = (0, 0, 0, 700)
    C_BOTTOM_UP_SWIPE = (700, 1000, 700, 0)
    C_LEFT_RIGHT_SWIPE = (0, 500, 500, 0)
    C_RIGHT_LEFT_SWIPE = (500, 0, 0, 500)
    C_SMALL_AREA_SWIPE = (500, 0, 500, 700)
    C_SAME_SWIPE_CORD = (500, 0, 500, 0)

    # vertical_swipe.py
    C_V_SWIPE_WRONG = (1000, 1000, -1000, -1000)
    C_TOP_DOWN_V_SWIPE = (100, 700, 50, 600)
    C_V_SWIPE_WD_DUR = (100, 700, 50, (T_WD_TIMEOUT * 60 * 1000))
    C_V_SWIPE_LEAST_DUR = (100, 700, 50, min_swipe_duration-100)
    C_V_SWIPE_MAX_DUR = (100, 700, 50, (T_WD_TIMEOUT * 60 * 1000) + 100)
    C_BOTTOM_UP_V_SWIPE = (1000, 0, 0, min_swipe_duration)

    # horizontal_swipe.py
    C_H_SWIPE_WRONG = (1000, 1000, -1000, -1000)
    C_RIGHT_LEFT_H_SWIPE = (200, 0, 300, 600)
    C_H_SWIPE_WD_DUR = (200, 0, 300, (T_WD_TIMEOUT * 60 * 1000))
    C_H_SWIPE_LEAST_DUR = (200, 0, 300, min_swipe_duration - 100)
    C_H_SWIPE_MAX_DUR = (200, 0, 300, (T_WD_TIMEOUT * 60 * 1000) + 100)

    # press_and_move.py
    C_MOVE_WRONG = (0, 0, -1000, -1000)
    C_MOVE_OUTBOUND = (0, 1000, 5000, 7000)
    C_SMALL_MOVE_DIST = (0, 10, 0, 100)
    C_SAME_MOVE_LOC = (0, 10, 0, 10)
    c_press_move = (0, 10, 0, 700)



    # DetectMotion, send_android_keycode.py, verify_playback() function
    detect_motion_check = (176, 99, 439, 251, 20, 5, "10")
    c_getocrtext = {"SamsungGalaxyJ7_21435_7_0": (38, 1243, 71, 33),
                    "Samsung_galaxyJ7_a445_7_0": (38, 1243, 71, 33),
                    "OnePlus5T": (31, 1179, 72, 20),
                    "MiA1712": (38, 1243, 71, 33),
                    "iPhone8Plus_11_0": (61, 1949, 95, 43),
                    "IpadFE": (569, 1501, 69, 29),
                    "iPhone7_11_0_3": (38, 1243, 71, 33),
                    "iPhone 6": (38, 1243, 71, 33),
                    "iPhone6sPlus": (38, 1243, 71, 33),
                    "iPhone8 Plus_11": (33, 1243, 67, 31),
                    "OnePlus2": (31, 1179, 72, 20),
                    "NewOnePlus_5T": (31, 1179, 72, 20),
                    }

    c_color_match = {
        "SamsungGalaxyJ7_21435_7_0": (33, 75, 56, 40),
        "Samsung_galaxyJ7_a445_7_0": (33, 75, 56, 40),
        "OnePlus5T": (33, 75, 56, 40),
        "MiA1712": (33, 75, 56, 40),
        "iPhone8Plus_11_0": (33, 75, 56, 40),
        "IpadFE": (569, 1501, 69, 29),
        "iPhone7_11_0_3": (38, 1243, 71, 33),
        "iPhone 6": (38, 1243, 71, 33),
        "iPhone6sPlus": (38, 1243, 71, 33),
        "iPhone8 Plus_11": (61, 1949, 95, 43),
        "OnePlus2": (33, 75, 56, 40),
        "NewOnePlus_5T": (33, 75, 56, 40),
    }

    c_hide_kbd = {
        "SamsungGalaxyJ7_21435_7_0": (9, 1025, 200, 700),
        "Samsung_galaxyJ7_a445_7_0": (9, 1025, 200, 700),
        "OnePlus5T": (9, 1025, 200, 700),
        "MiA1712": (129, 995, 500, 251),
        "iPhone8Plus_11_0": (9, 1025, 200, 700),
        "IpadFE": (9, 1025, 200, 700),
        "iPhone7_11_0_3": (9, 1025, 200, 700),
        "iPhone 6": (9, 1025, 200, 700),
        "iPhone6sPlus": (9, 1025, 200, 700),
        "iPhone8 Plus_11": (9, 1025, 200, 700),
        "OnePlus2": (9, 1025, 200, 700),
        "NewOnePlus_5T": (9, 1025, 200, 700),
    }

    c_capture_image = {
        "SamsungGalaxyJ7_21435_7_0": (127, 571, 540, 263),
        "Samsung_galaxyJ7_a445_7_0": (127, 571, 540, 263),
        "OnePlus5T": (127, 571, 540, 263),
        "MiA1712": (129, 995, 500, 251),
        "iPhone8Plus_11_0": (9, 1025, 200, 700),
        "IpadFE": (9, 1025, 200, 700),
        "iPhone7_11_0_3": (9, 1025, 200, 700),
        "iPhone 6": (9, 1025, 200, 700),
        "iPhone6sPlus": (9, 1025, 200, 700),
        "iPhone8 Plus_11": (9, 1025, 200, 700),
        "OnePlus2": (127, 571, 540, 263),
        "NewOnePlus_5T": (127, 571, 540, 263),
    }

    c_capture_image_non_playback_region = {
        "SamsungGalaxyJ7_21435_7_0": (7, 553, 705, 243),
        "Samsung_galaxyJ7_a445_7_0": (7, 553, 705, 243),
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

    c_img_search = (199, 37, 427, 139)
    TAP_PERCENT_FIRST_SEARCH_RESULT = (30,16)
    TAP_PERCENT_VIDEO_TO_PLAY = (30, 47)
    alert_accept_upper = "ACCEPT"
    alert_accept_lower = "accept"
    alert_accept_camel = "Accept"
    alert_dismiss_upper = "DISMISS"
    alert_dismiss_lower = "dismiss"
    alert_dismiss_camel = "Dismiss"
    alert_wrong_action = "wrong_action"


    # ==================================================== END COORDINATES =============


    # **************************************  TEST PARAMETERS

    # ==================================================== general
    # ================================================================================
    API_PASS = True
    API_FAIL = False
    NONE = None
    EMPTY = ""
    IMG_NAME_SPL = "test@#$%^&*"
    IMG_NAME = "testimage"
    IMAGE_NAME_NUMBER = "test987654"
    LONG_IMG_NAME = "testimage_abcdefghijklmnopqrstuvwxyz_abcdefghijklmnopqrstuvwxyz_abc\
    defghijklmnopqrstuvwxyz_abcdefghijklmnopqrstuvwxyz_abcdefghijklmnopqrstuvwxyz_ab\
    cdefghijklmnopqrstuvwxyz.jpg"
    CACHE_VALID_URL_FOR_DYNAMIC_COMPARE = "http://10.47.166.48/TestImage/ImageForDynamicImageCompare.JPG"
    EMPTY_MSG = ''
    LONG_MSG = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%~^&*()_++{}:<>?|\/.,;[]=-09"
    MSG_WITH_NUMBERS = '1234567890123456789012345678901234567890'
    MSG_WITH_SPLCHARS = '!@#$%^&*()~:;,.<>?/'
    ERROR_MSG = "Scenario not Passed"
    LOG_MSG = "Scenario not Passed"
    WARN_MSG = "this scenarios is not successful"
    INVALID_IMAGE_FORMAT = "xyz"
    VALID_IMAGE_FORMAT = "jpg"
    VALID_IMG_FORMAT_WRONG_CASE = "JPG"
    LENGTHY_NAME = "qwertypoiuyasdfghlkjhgzxcvbmnbbvaaqwertypoiuyasdfghlkjhgzxcvbmnbbvaaaqwertypoiuyasdfghlk" \
                   "jhgzxcvbmnbbvaaaqwertypoiuyasdfghlkjhgzxcvbmnbbvaaaqwertypoiuyasdfghlkjhgzxcvbmnbbvaaaqw" \
                   "ertypoiuyasdfghlkjhgzxcvbmnbbvaaaqwertypoiuyasdfghlkjhgzxcvbmnbbvaaaqwertypoiuyasdfghlkj" \
                   "hgzxcvbmnbbvaaaqwertypoiuyasdfghlkjhgzxcvbmnbbvaaaqwertypoiuyasdfghlkjhgzxcvbmnbbvaaaqwe" \
                   "rtypoiuyasdfghlkjhgzxcvbmnbbvaaaqwertypoiuyasdfghlkjhgzxcvbmnbbvaaaqwertypoiuyasdfghlkjh" \
                   "gzxcvbmnbbvaaaqwertypoiuyasdfghlkjhgzxcvbmnbbvaaaqwertypoiuyasdfghlkjhgzxcvbmnbbvaaaa"

    # status
    PASSED = "PASSED"
    FAILED = "FAILED"
    UNKNOWN = "UNKNOWN"
    ABORTED = "ABORTED"
    ERROR = "ERROR"
    INVALID_STATUS = "INVALID_STATUS"
    SPL_CHR_STATUS = "!@#$%^&"
    CAPTURE_IMAGE_RETURN = "captured_image"
    GET_SCREENSHOT_RETURN = "obtained_screenshot"
    commit_apis_valid_status = [PASSED, FAILED, UNKNOWN, ABORTED, ERROR]

    CAP_IMAGE_NAME = "cap_img"
    CAP_IMG_OVERWRITE = "cap_img_unique"
    CAP_IMG_DEFAULT_QUALITY = 90
    overwrite_file = 0

    MAX_X = 0
    MAX_Y = 0
    
    MAX_WIDTH, MAX_HEIGHT = "max_width", "max_height"

    # detect motion
    DEFAULT_TIMEOUT = 20
    DEFAULT_WAITGAP = 5
    DEFAULT_STR_TOLERANCE = "8"

    # dynamic image compare
    dyn_img = "dynamic_compare_img"
    DEFAULT_DYN_TOLERANCE = 15
    c_capture_image_for_dyn_im = (dyn_img, 5, 39, 166, 71, 90, 0)

    # T_MD_WAIT = 20

    # WAITCOLORMATCH
    COLOR_TOLERANCE = '[10,10,10]'
    FLATNESS = 90
    captureZapTime = 30
    matchColor = "[231, 5, 5]"

    # WAIT IMAGE MATCH
    PIXEL_BASED_ALGORITHM = 1
    RMSE_ALGORITHM = 2

    # WAIT FOR CHECKPOINT
    INITIAL_DELAY = 2
    TIME_TO_WAIT = 10

    # GETOCRTEXT
    DEFAULT_FILTER = "Greyscale"
    DEFAULT_LANG = "eng"
    MULTIPLE_FILTER = "Contrast:25;Resize:2"
    INVALID_LANG = "invalid_language"
    NON_SUPPORTED_LANG = "kor"
    INVALID_FILTER = "invalid_filter"
    OUT_OF_BOUND_FILTER = "Contrast:101;Resize:5;"

    # IMAGE SEARCH
    SqdiffNormed = 1
    CcorrNormed = 3
    default_CcoeffNormed = 5
    DEFAULT_PERCENT_MATCH = 97

    # READPROPERTY
    READ_PROPERTY_LOWEST_BOUNDARY = 0
    READ_PROPERTY_HIGHEST_BOUNDARY = 12
    READ_PROPERTY_INVALID = 19

    # StartCaptureZapFrames
    zap_frame_iter_count = 3

    # SetDutAttribute
    used_attr_name = "manufacturer"

    # set_dut_attribute.py
    valid_attr_value = "manufacturer"
    empty_attr_value = ""
    long_attr_value = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz123"
    splchar_attr_value = "*()^%~!@#$%^&**()_.^%~!@#$%^&**"
    number_attr_value = "0123456789"
    comb_attr_value = "falconeye_api1234567890*^%$#%$^"
    non_existing_attr = "manufacturer123"
    txt_getocrtext = "Home"
    home_index = 14
    # get_dut_attribute.py
    valid_attr = "manufacturer"
    empty_attr = ""

    # handlealertmessage
    accept_alert = "ACCEPT"
    dismiss_alert = "DISMISS"

    # VolumeUp # VolumeDown
    VALID_MAX_VOL = VALID_MIN_VOL = 14
    INVALID_VOL_LEVEL_MIN = 0
    INVALID_VOL_LEVEL_MAX = 15
    INVALID_VOL_NEGATIVE = -1
    VOLUME_UNIT = 1

    # GetScreenTransitionTime
    SCREEN_TRANSITION_FAIL_VAL = -1

    # init.py
    non_existing_chkpt = "non_existing_checkpoint"
    lengthy_name_chkpt = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
    not_created = "auto_chkpt"
    not_initialized = "not_initialized"
    time_to_wait = 10
    wait_gap = 5
    volume_levels = 5
    search_icon_index = 4

    # sanity_iselement_tapelement.py - overrides this item in respective configs
    list_iselm = ()
    unique_attr = "unique_attr"
    unique_val = "unique_val"
    long_val = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz123"
    long_val_attr = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz12345678"
    splchar_attr_val = "*()^%~!@#$%^&**()_.^%~!@#$%^&**()^%~!@#$%^&*"
    empty_val = ""
    attr_name = "attr_{}"
    number_attr_val = "123456789012345678901"
    comb_attr_val = "abcd1234567890&*%#@!"

    # SendAndroidKeyCode
    DEL = "Keycode_DEL" # Backspace key
    BACK = "Keycode_BACK" # Back key
    FORWARD = "Keycode_FORWARD" # Navigates forward in the history stack. Complement of KEYCODE_BACK
    VOLUME_DOWN = "Keycode_VOLUME_DOWN"
    VOLUME_UP = "Keycode_VOLUME_UP"
    ENTER = "Keycode_ENTER" # Enter key
    DVR = "Keycode_DVR" # Key code constant: DVR key. On some TV remotes, switches to a DVR mode for recorded shows
    ENDCALL = "Keycode_ENDCALL" # End Call key - Can not test
    ESCAPE = "Keycode_ESCAPE" # Escape key
    EXPLORER = "Keycode_EXPLORER" # Explorer special function key. Used to launch a browser application
    FORWARD_DEL = "Keycode_FORWARD_DEL" # Forward Delete key. Deletes characters ahead of the insertion point, unlike KEYCODE_DEL
    HOME = "Keycode_HOME" # This key is handled by the framework and is never delivered to applications
    INSERT = "Keycode_INSERT" # Toggles insert / overwrite edit mode
    MEDIA_FAST_FORWARD = "Keycode_MEDIA_FAST_FORWARD" # Fast Forward media key
    MEDIA_NEXT = "Keycode_MEDIA_NEXT" # Play Next media key
    MEDIA_PAUSE = "Keycode_MEDIA_PAUSE" # Pause media key
    MEDIA_PLAY = "Keycode_MEDIA_PLAY" # Play media key
    MEDIA_PLAY_PAUSE = "Keycode_MEDIA_PLAY_PAUSE" # Play/Pause media key
    MEDIA_PREVIOUS = "Keycode_MEDIA_PREVIOUS" # Play Previous media key
    MEDIA_REWIND = "Keycode_MEDIA_REWIND" # Rewind media key
    MEDIA_STOP = "Keycode_MEDIA_STOP" # Stop media key
    MENU = "Keycode_MENU" # Menu key
    MOVE_END = "Keycode_MOVE_END" # End Movement key.
    WRONG_KEYCODE = "Keycode_WRONG"
    # Used for scrolling or moving the cursor around to the end of a line or to the bottom of a list.
    MOVE_HOME = "Keycode_MOVE_HOME" # Home Movement key.
    # Used for scrolling or moving the cursor around to the start of a line or to the top of a list.
    MUTE = "Keycode_MUTE" # Mute key. Mutes the microphone, unlike KEYCODE_VOLUME_MUTE
    CALL = "Keycode_CALL" # Call key
    DPAD_RIGHT = "Keycode_DPAD_RIGHT" # Directional Pad Right key. May also be synthesized from trackball motions
    VALID_STEP_NAME = "VALID STEP"
    STEP_NAME_WITH_SPL_CHAR = "abc!@#$abc)(*&^123"

    keys_media = {
        'pause': MEDIA_PAUSE,
        'play': MEDIA_PLAY,
        'play_pause' : MEDIA_PLAY_PAUSE,
        'rewind' : MEDIA_REWIND,
        'fast_forward': MEDIA_FAST_FORWARD,
        'stop' : MEDIA_STOP,
        'next' : MEDIA_NEXT,
        'previous': MEDIA_PREVIOUS,

        }


    keys_volume = {
        'down' : VOLUME_DOWN,
        'mute' : MUTE,
        'up' : VOLUME_UP,

    }

    keys_nav = {
        'back': BACK,
        'enter': ENTER,
    }

    key_text = {
        'end': MOVE_END,
        'insert': INSERT,
        'home': MOVE_HOME,
        'f_del': FORWARD_DEL,
        'del': DEL,
        'enter': ENTER,
    }

    search_text = 'master chef australia'
    first_search_text = 'mmaster '
    mid_search_text = 'chef'
    last_search_text = ' australiaa'

    attr_list = "enabled,checked,clickable,checkable,focusable,focused,scrollable,password,selected"
    invalid_attr_list = "invalid_attr_1,invalid_attr_2"
    percent_out_of_boundary = (110, 110)


    # ==================================================== CHECKPOINT VARIABLES
    # ================================================================================
    yt_logo = "Mobile_YouTube"
    SkyValidateCheckPointOCR = "Mobile_YouTube"
    SkyValidateCheckPointMultiOCR = "youtube_MultiOcr"
    SkyValidateCheckPointICpixel = "youtube_valIcPixel"
    SkyValidateCheckPointICrmsel = "youtube_valIcRmse"
    ParentCheckPoint = "Parent_checkpoint_Mobile"
    OCRCheckpointMultipleFilters = "ocr_checkpoint_multiple_filters"
    LengthyCheckpoint = "LengthyCheckpoint1234567890longnamelongnamelongnamelongnamelongnamelongnamelongnamelongnamelongnamel"
    CheckpointWithoutInitialize = "chkpt_without_initialize"
    NotExistingCheckpoint = "stb_checkpoint"
    imageSearchSingleOccurance = "CheckpointPatternSingleOccurance"
    imageSearchMultipleOccurance = "CheckpointPatternMultipleOccurance"
    CheckpointScreenForTransition = "GetScreenTransitionCheck"
    GET_OCR_SKY_HOME_SCREEN = "getOcrSkyHome"
    CheckpointScreenToWait = "Mobile_YouTube"
    chkpt_screen_elm = "CheckpointPatternSingleOccurance"
    img_unlike_symbol = "ic_dislike_video_yt"  # tap on a video and get to this screen
    ocr_image_search_chkpt = 'ocr_image_search'

    # ==================================================== URLS
    # ================================================================================
    CACHE_VALID_URL = 'http://10.47.166.48/TestImage/ImageForDynamicImageCompare.JPG'
    #"https://wallpapers.pub/web/wallpapers/birds-water-spray-wallpaper/3840x2160.jpg"
    INVALID_URL = "https://invalidurl1234/"
    URL_WITHOUT_EXT = "https://www.google.com/imgres?imgurl=https://images.homedepot-static.com/productImages" \
                      "/e350ef76-f7ff-46ee-83d2-606aab23453c/svn/mea-nursery-rose-bushes-62014-64_1000.jpg&imgr" \
                      "efurl=https://www.homedepot.com/p/Mea-Nursery-FRAGRANT-Red-Mister-Lincoln-Rose-62014/30493" \
                      "7447&h=1000&w=1000&tbnid=2U5BtPSy_ReQXM:&q=rose&tbnh=186&tbnw=186&usg=AI4_-kT353MLm_-eQBPAs" \
                      "PnRer5dx4CGUQ&vet=12ahUKEwiEsZfttpXgAhUBKY8KHcWsBPAQ_B0wG3oECAUQBg..i&docid=5s9yfLJzUad" \
                      "2ZM&itg=1&sa=X&ved=2ahUKEwiEsZfttpXgAhUBKY8KHcWsBPAQ_B0wG3oECAUQBg"

    # ==================================================== COORDINATES
    # ================================================================================
    C_CAP_IMAGE = (89, 60, 139, 69)
    C_DET_MOTION = (176, 99, 439, 251)
    C_DYN_IMG_COMP = (89, 60, 139, 69)
    C_COLOR_MATCH = (37, 81, 15, 23)
    C_WAIT_IMG_MATCH = (89, 60, 139, 69)

    # ---------------------------  CacheImageFromUrl


    # inputDict = {key:[url,imageName, testScenario, expected] }
    sanity_cache_image_from_url_params = (0, )
    cache_image_from_url_params = {
        0: ["Valid url, Valid image name", CACHE_VALID_URL, IMG_NAME, API_PASS],
        1: ["Invalid url, Valid image name", INVALID_URL, IMG_NAME, API_FAIL],
        2: ["Valid url, Lengthy image name", CACHE_VALID_URL, LONG_IMG_NAME, API_FAIL],
        3: ["Invalid parameter' Empty string as image name", CACHE_VALID_URL, EMPTY, API_FAIL],
        4: ["Invalid parameter' image name with special character", CACHE_VALID_URL, IMG_NAME_SPL, API_FAIL],
        5: ["Invalid parameter' URL without file extension", URL_WITHOUT_EXT, IMG_NAME, API_FAIL],
        6: ["Invalid parameter' Empty string as URL", EMPTY, IMG_NAME, API_FAIL],
    }

    # indices of parameters considered in sanity test script to cover positive scenarios
    sanity_wait_chkpt_match_params = (0,1,2,3,)

    # ---------------------------  WaitCheckPointMatch

    wait_chkpt_match_params = {
        0:[
            "Valid parameter, OCR checkpoint", API_PASS, SkyValidateCheckPointOCR,
            TIME_TO_WAIT, DEFAULT_WAITGAP
        ],
        1:[
            "Valid parameter, IC checkpoint, pixel", API_PASS, SkyValidateCheckPointICpixel,
            TIME_TO_WAIT, DEFAULT_WAITGAP
        ],
        2:[
            "Valid parameter, IC checkpoint, rmse",
            API_PASS, SkyValidateCheckPointICrmsel, TIME_TO_WAIT, DEFAULT_WAITGAP
        ],
        3: [
            "Valid parameter, already on checkpoint screen", API_PASS, SkyValidateCheckPointOCR,
            TIME_TO_WAIT, DEFAULT_WAITGAP
        ],
        4: [
            "Valid parameter, Max wait equal to WD timeout", API_PASS, SkyValidateCheckPointOCR,
            T_WD_TIMEOUT, DEFAULT_WAITGAP
        ],
        5: [
            "Valid parameter, Negative values for timeToWait and waitGap", API_FAIL, SkyValidateCheckPointOCR,
            T_NEG_TIME_TO_WAIT, DEFAULT_WAITGAP
        ],

        6: [
            "Invalid parameter, timeToWait < waitGap", API_FAIL, SkyValidateCheckPointOCR,
            TIME_TO_WAIT, DEFAULT_WAITGAP
        ],
        7: [
            "Valid parameter, Multi line OCR checkpoint",
            API_PASS, SkyValidateCheckPointMultiOCR, TIME_TO_WAIT, DEFAULT_WAITGAP
        ],
        8: [
            "Valid parameter, Max wait equal to WD timeout, Checkpoint not available", API_FAIL, SkyValidateCheckPointOCR,
            T_WD_TIMEOUT, DEFAULT_WAITGAP
        ],
        # The below scenario is being commented since FAL-3610 is open
        # FAL - 3610 - [WaitCheckPointMatch API]: throws exception if checkpoint does not exist
        # 9: [
        #     "Invalid parameter, Checkpoint does not exist", API_FAIL, not_created,
        #     TIME_TO_WAIT, DEFAULT_WAITGAP
        # ],


    }

    # ---------------------------  CaptureImage
    # the parametrs till key-3 are being used in sanity scripts, so for any modifications, please dont
    # change the parameters till key-3 (0, 1, 2, 3)

    sanity_capture_image_params = (0, 1, 2, 3,)
    capture_image_params = {
        0: [
            "Valid parameters: overWriteAction: 1 (OverWrite action set to Error)", API_FAIL,
            (C_CAP_IMAGE[0], C_CAP_IMAGE[1], C_CAP_IMAGE[2], C_CAP_IMAGE[3], CAP_IMG_OVERWRITE, CAP_IMG_DEFAULT_QUALITY, 1)
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
            "Valid parameters: another coordinates", API_PASS,
            (10, 45, 50, 50, CAP_IMAGE_NAME, CAP_IMG_DEFAULT_QUALITY, 2)
        ],
        10: [
            "Valid parameters: whole frame", API_PASS,
            (MAX_X, MAX_Y, MAX_WIDTH, MAX_HEIGHT, CAP_IMAGE_NAME, CAP_IMG_DEFAULT_QUALITY, 2)
        ],
        11: [
            "Invalid parameters: overWriteAction: -1", API_FAIL,
            (C_CAP_IMAGE[0], C_CAP_IMAGE[1], C_CAP_IMAGE[2], C_CAP_IMAGE[3], CAP_IMAGE_NAME, CAP_IMG_DEFAULT_QUALITY, -1)
        ],
        12: [
            "Invalid parameters: Empty string as image name", API_FAIL,
            (C_CAP_IMAGE[0], C_CAP_IMAGE[1], C_CAP_IMAGE[2], C_CAP_IMAGE[3], EMPTY, CAP_IMG_DEFAULT_QUALITY, 2)
        ],
        13: [
            "Invalid parameters: Negative value for parameters", API_FAIL, (-12, -12, -12, -12, CAP_IMAGE_NAME,
                                                                            CAP_IMG_DEFAULT_QUALITY, 0)
        ],
        14: ["Invalid parameters: Image name with special characters", API_FAIL,
             (C_CAP_IMAGE[0], C_CAP_IMAGE[1], C_CAP_IMAGE[2], C_CAP_IMAGE[3], IMG_NAME_SPL, CAP_IMG_DEFAULT_QUALITY, 2)]
    }

    # ---------------------------  DetectMotion
    sanity_detect_motion_params = (0, 2,)
    detect_motion_params = {
        0: [
            "Valid parameters", API_PASS,
            (C_DET_MOTION[0], C_DET_MOTION[1], C_DET_MOTION[2], C_DET_MOTION[3], DEFAULT_TIMEOUT, DEFAULT_WAITGAP, DEFAULT_STR_TOLERANCE)
        ],
        1: [
            "Valid: tolerance, boundary condition [100]", API_FAIL,
            (C_DET_MOTION[0], C_DET_MOTION[1], C_DET_MOTION[2], C_DET_MOTION[3], DEFAULT_TIMEOUT, DEFAULT_WAITGAP, "100")
        ],
        2: [
            "Valid: tolerance, boundary condition [0]", API_PASS,
            (C_DET_MOTION[0], C_DET_MOTION[1], C_DET_MOTION[2], C_DET_MOTION[3], DEFAULT_TIMEOUT, DEFAULT_WAITGAP, "0")
        ],
        3: [
            "InValid: wait gap greater than timeout", API_FAIL,
            (C_DET_MOTION[0], C_DET_MOTION[1], C_DET_MOTION[2], C_DET_MOTION[3], 5, 10, DEFAULT_STR_TOLERANCE)
        ],
        4: [
            "Valid: wait gap & timeout are equal", API_PASS,
            (C_DET_MOTION[0], C_DET_MOTION[1], C_DET_MOTION[2], C_DET_MOTION[3], 5, 5, DEFAULT_STR_TOLERANCE)
        ],
        5: [
            "Valid: max timeout", API_PASS,
            (C_DET_MOTION[0], C_DET_MOTION[1], C_DET_MOTION[2], C_DET_MOTION[3], 500, DEFAULT_WAITGAP, DEFAULT_STR_TOLERANCE)
        ],
        6: [
            "Valid parameters, whole HD frame comparison", API_PASS,
            (MAX_X, MAX_Y, MAX_WIDTH, MAX_HEIGHT, DEFAULT_TIMEOUT, DEFAULT_WAITGAP, DEFAULT_STR_TOLERANCE)
        ],
        7: [
            "InValid parameter, negative tolerance", API_FAIL,
            (C_DET_MOTION[0], C_DET_MOTION[1], C_DET_MOTION[2], C_DET_MOTION[3], DEFAULT_TIMEOUT, DEFAULT_WAITGAP, "-10")
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
        3: [
            "InValid referenceImageName", API_FAIL,
            (IMG_NAME_SPL, C_DYN_IMG_COMP[0], C_DYN_IMG_COMP[1], C_DYN_IMG_COMP[2], C_DYN_IMG_COMP[3], DEFAULT_DYN_TOLERANCE)
        ],
        4: ["Invalid parameter, coordinate out of boundary", API_FAIL, (dyn_img, MAX_X, MAX_Y, MAX_WIDTH,
                                                                        MAX_HEIGHT, DEFAULT_DYN_TOLERANCE)],
        5: ["Invalid case, Use image from CaptureImage API as refImage", API_FAIL,
            (dyn_img, C_DYN_IMG_COMP[0], C_DYN_IMG_COMP[1], C_DYN_IMG_COMP[2], C_DYN_IMG_COMP[3],
             DEFAULT_DYN_TOLERANCE)]
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
    
    # indices of parameters considered in sanity test script to cover positive scenarios
    sanity_wait_color_match_params = (0,1,2,4,)

    # ----------------------- WaitColorMatch

    wait_color_match_params = {
        0: [
            "Valid parameters", API_PASS, [matchColor, C_COLOR_MATCH[0], C_COLOR_MATCH[1], C_COLOR_MATCH[2], C_COLOR_MATCH[3],
                                           T_MD_WAIT, DEFAULT_WAITGAP, COLOR_TOLERANCE, FLATNESS],
        ],
        1: [
            "Valid parameters, flatness boundary condition : 0", API_PASS, [matchColor, C_COLOR_MATCH[0], C_COLOR_MATCH[1],
                                                                            C_COLOR_MATCH[2], C_COLOR_MATCH[3], T_MD_WAIT,
                                                                            DEFAULT_WAITGAP, COLOR_TOLERANCE, 0],
        ],
        2: ["Valid parameters, flatness boundary condition : 100", API_FAIL, [matchColor, C_COLOR_MATCH[0],
                                                                              C_COLOR_MATCH[1], C_COLOR_MATCH[2], C_COLOR_MATCH[3],
                                                                              T_MD_WAIT, DEFAULT_WAITGAP,
                                                                              COLOR_TOLERANCE, 100],
            ],
        3: [
            "Invalid parameters, waitGap greater than timeToWait", API_FAIL, [matchColor, C_COLOR_MATCH[0],
                                                                               C_COLOR_MATCH[1], C_COLOR_MATCH[2], C_COLOR_MATCH[3], 5, 20,
                                                                               COLOR_TOLERANCE, FLATNESS],
        ],
        4: [
            "Valid parameters, Multiple occurrences of Match color", API_PASS, [matchColor, MAX_X, MAX_Y,
                                                                               MAX_WIDTH, MAX_HEIGHT,
                                                                               T_MD_WAIT, DEFAULT_WAITGAP,
                                                                               COLOR_TOLERANCE, FLATNESS],
        ],

        5: [
            "Valid parameters, Match color check on non matching screen", API_FAIL, [matchColor, C_COLOR_MATCH[0],
                                                                                     C_COLOR_MATCH[1], C_COLOR_MATCH[2], C_COLOR_MATCH[3],
                                                                                     T_MD_WAIT, DEFAULT_WAITGAP,
                                                                                     COLOR_TOLERANCE, FLATNESS],
        ],


    }

    # indices of parameters considered in sanity test script to cover positive scenarios
    sanity_wait_image_match_params = (1,2,9,11)

    # -------------------------------- WaitImageMatch

    img_wait_im_match = "refImage"
    pixel_tolerance = "15;10"
    #sanity_wait_image_match_params = (1, 2, 3)
    wait_image_match_params = {
        0: [
            "InValid parameter, non existing reference image", API_FAIL,
            ("nonExist", C_WAIT_IMG_MATCH[0], C_WAIT_IMG_MATCH[1], C_WAIT_IMG_MATCH[2], C_WAIT_IMG_MATCH[3],
             T_MD_WAIT, DEFAULT_WAITGAP, PIXEL_BASED_ALGORITHM, DEFAULT_STR_TOLERANCE),
        ],
        1: ["Valid parameters RMSE algorithm", API_PASS,
            (img_wait_im_match, C_WAIT_IMG_MATCH[0], C_WAIT_IMG_MATCH[1], C_WAIT_IMG_MATCH[2], C_WAIT_IMG_MATCH[3],
             T_MD_WAIT, DEFAULT_WAITGAP, RMSE_ALGORITHM, DEFAULT_STR_TOLERANCE),
        ],
        2: ["Valid parameters, PIXEL_BASED algorithm", API_PASS,
            (img_wait_im_match, C_WAIT_IMG_MATCH[0], C_WAIT_IMG_MATCH[1], C_WAIT_IMG_MATCH[2], C_WAIT_IMG_MATCH[3],
             T_MD_WAIT, DEFAULT_WAITGAP, PIXEL_BASED_ALGORITHM, pixel_tolerance),
            ],
        3: ["Valid parameters, Test region is larger than reference image", API_FAIL,
            (img_wait_im_match, C_WAIT_IMG_MATCH[0],C_WAIT_IMG_MATCH[1], C_WAIT_IMG_MATCH[2] + 100,
             C_WAIT_IMG_MATCH[3] + 200, T_MD_WAIT, DEFAULT_WAITGAP, PIXEL_BASED_ALGORITHM, pixel_tolerance)
            ],
        4: [
            "In Valid parameters, wrong algorithm", API_FAIL,
            (img_wait_im_match, C_WAIT_IMG_MATCH[0], C_WAIT_IMG_MATCH[1], C_WAIT_IMG_MATCH[2], C_WAIT_IMG_MATCH[3],
             T_MD_WAIT, DEFAULT_WAITGAP, 3, DEFAULT_STR_TOLERANCE)
        ],
        5: ["Valid parameters, tolerance, boundary condition: 0", API_FAIL,
            (img_wait_im_match, C_WAIT_IMG_MATCH[0], C_WAIT_IMG_MATCH[1], C_WAIT_IMG_MATCH[2], C_WAIT_IMG_MATCH[3],
             T_MD_WAIT, DEFAULT_WAITGAP, PIXEL_BASED_ALGORITHM, "0")
            ],
        6: ["InValid parameters, tolerance, invalid value: '-12'", API_FAIL,
            (img_wait_im_match, C_WAIT_IMG_MATCH[0], C_WAIT_IMG_MATCH[1], C_WAIT_IMG_MATCH[2], C_WAIT_IMG_MATCH[3],
             T_MD_WAIT, DEFAULT_WAITGAP, PIXEL_BASED_ALGORITHM, "-12")
            ],
        7: ["InValid parameters, tolerance, out of range: '200'", API_FAIL,
            (img_wait_im_match, C_WAIT_IMG_MATCH[0], C_WAIT_IMG_MATCH[1], C_WAIT_IMG_MATCH[2], C_WAIT_IMG_MATCH[3],
             T_MD_WAIT, DEFAULT_WAITGAP, PIXEL_BASED_ALGORITHM, "200")
            ],
        8: ["InValid parameters, waitGap greater than timeToWait", API_FAIL,
            (img_wait_im_match, C_WAIT_IMG_MATCH[0], C_WAIT_IMG_MATCH[1], C_WAIT_IMG_MATCH[2], C_WAIT_IMG_MATCH[3],
             T_MD_WAIT, 25, PIXEL_BASED_ALGORITHM, pixel_tolerance)
            ],
        9: [
            "Valid parameters, whole HD frame comparison", API_PASS,
            (img_wait_im_match, MAX_X, MAX_Y, MAX_WIDTH, MAX_HEIGHT, T_MD_WAIT, DEFAULT_WAITGAP, PIXEL_BASED_ALGORITHM,
             DEFAULT_STR_TOLERANCE)
        ],
        10: [
            "Valid parameters,ref image and test region from two different screen", API_FAIL,
            (img_wait_im_match, C_WAIT_IMG_MATCH[0], C_WAIT_IMG_MATCH[1], C_WAIT_IMG_MATCH[2], C_WAIT_IMG_MATCH[3],
             T_MD_WAIT, DEFAULT_WAITGAP, PIXEL_BASED_ALGORITHM, DEFAULT_STR_TOLERANCE)
        ],
        11: ["Valid parameters, tolerance, boundary condition: 100", API_PASS,
             (img_wait_im_match, C_WAIT_IMG_MATCH[0], C_WAIT_IMG_MATCH[1], C_WAIT_IMG_MATCH[2], C_WAIT_IMG_MATCH[3],
              T_MD_WAIT, DEFAULT_WAITGAP, PIXEL_BASED_ALGORITHM, "100")
        ],
        12: ["Valid parameters, timeToWait, large value", API_PASS,
             (img_wait_im_match, C_WAIT_IMG_MATCH[0], C_WAIT_IMG_MATCH[1], C_WAIT_IMG_MATCH[2], C_WAIT_IMG_MATCH[3],
              100, DEFAULT_WAITGAP, PIXEL_BASED_ALGORITHM, "100")]
    }

    # indices of parameters considered in sanity test script to cover positive scenarios
    sanity_wait_for_chkpt_params = (0,1,2,3,)

    # ----------------------- WaitForCheckpoint

    wait_for_chkpt_params = {
        0: [
            "Valid parameters, DUT already on checkpoint screen", RETURN_PASS_VAL,
            (CheckpointScreenToWait, T_MD_WAIT, INITIAL_DELAY)
        ],
        1: [
            "Valid parameters, No screen transition to the checkpoint screen", RETURN_FAIL_VAL,
            (img_unlike_symbol, T_MD_WAIT, INITIAL_DELAY)
        ],
        2: [
            "Valid parameters, Maximum TimeToWait = WD Timeout", RETURN_PASS_VAL,
            (CheckpointScreenToWait, T_MD_WAIT, 5)
        ],

        3: [
            "Valid parameters, screen transition to the checkpoint screen", RETURN_PASS_VAL,
            (img_unlike_symbol, T_MD_WAIT, INITIAL_DELAY)
        ],
        4: [
            "Valid parameters, very small time to wait, 2 sec", RETURN_PASS_VAL,
            (img_unlike_symbol, 2, INITIAL_DELAY)
        ],
        5: [
            "InValid parameters, Checkpoint does not exist for the device", RETURN_FAIL_VAL,
            ("nonExisting", T_MD_WAIT, INITIAL_DELAY)
        ],
        6: [
            "InValid parameters, negative time to wait, -20 sec", RETURN_FAIL_VAL,
            (img_unlike_symbol, -20, INITIAL_DELAY)
        ],
        7: [
            "InValid parameters, negative initial delay, -2 sec", RETURN_FAIL_VAL,
            (img_unlike_symbol, T_MD_WAIT, -2)
        ],
        8: [
            "InValid parameters, Initial delay greater than TimeToWait", RETURN_FAIL_VAL,
            (img_unlike_symbol, T_MD_WAIT, 25)
        ],


    }


    # ----------------- getOCRText
    get_ocr_text_valid_param = [
        "Valid parameters", API_PASS, (DEFAULT_FILTER, DEFAULT_LANG),
    ] # expects the text - 'Home'

    # ----------------- getOCRText
    get_ocr_text_params = {
        0: [
            "Valid parameters", API_PASS, (DEFAULT_FILTER, DEFAULT_LANG),
        ],
        1: [
            "Valid parameter: language: hin", API_PASS, (DEFAULT_FILTER, "hin")
        ],
        2: ["Valid parameter: language: empty", API_PASS, (DEFAULT_FILTER, "")
        ],
        3: [
            "Out of boundary coordinates", API_FAIL, (DEFAULT_FILTER, DEFAULT_LANG)
        ],
        4: [
            "Multiple filters", API_PASS, (MULTIPLE_FILTER, DEFAULT_LANG)
        ],
        5: [
            "Invalid language", API_PASS, (DEFAULT_FILTER, INVALID_LANG)
        ],
        6: [
            "Non-supported language", API_PASS, (DEFAULT_FILTER, NON_SUPPORTED_LANG)
        ],
        7: [
            "Invalid filter", API_PASS, (INVALID_FILTER, DEFAULT_LANG)
        ],
        8: [
            "Filters with out-of boundary values", API_FAIL, (OUT_OF_BOUND_FILTER, DEFAULT_LANG)
        ],
    }

    #  ----------------------- ImageMatch

    ref_img_0 = "ref_img_0"
    test_img_0 = "test_img_0"

    ref_image_param = (599, 509, 27, 37, ref_img_0, CAP_IMG_DEFAULT_QUALITY, 0)
    test_image_param = (599, 509, 27, 37, test_img_0, 90, 0)

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
            "Valid parameters, tolerance, boundary condition: 100", API_PASS,
            (ref_img_0, test_img_0, RMSE_ALGORITHM, "100")
        ],
        3: [
            "Invalid parameter, image doesn't exist", API_FAIL,
            ("ref_#%$#^%", "cap_#@$%23", PIXEL_BASED_ALGORITHM, DEFAULT_STR_TOLERANCE)
        ],
        4: [
            "Invalid parameters, tolerance: -12", API_FAIL, (ref_img_0, test_img_0, RMSE_ALGORITHM, "-12")
        ],
        5: [
            "Invalid Parameters, tolerance invalid", API_FAIL, (ref_img_0, test_img_0, RMSE_ALGORITHM, "a")
        ],
        6: [
            "Valid parameters, tolerance boundary condition: 0", API_FAIL, (ref_img_0, test_img_0, RMSE_ALGORITHM, "0")
        ],
        7: [
            "Invalid parameters, wrong algorithm", API_FAIL, (ref_img_0, test_img_0, 3, DEFAULT_STR_TOLERANCE)
        ],
        8: [
            "Invalid parameters, negative algorithm", API_FAIL, (ref_img_0, test_img_0, -3, DEFAULT_STR_TOLERANCE)
        ],
    }

    # ---------------------- ImageSearch
    # moved to respective configs; so update the device config file any change required

    sanity_image_search_params = (0, 1, 6)
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
        ],
        5: [
            "Valid parameters, OCR Checkpoint", API_PASS, (ocr_image_search_chkpt,
                                                           MAX_X, MAX_Y, MAX_WIDTH, MAX_HEIGHT,
                                                           default_CcoeffNormed,
                                                           DEFAULT_PERCENT_MATCH)
        ],

        6: [
            "Valid parameters, Checkpoint not available on the screen",
            API_FAIL, (imageSearchSingleOccurance, c_img_search[0], c_img_search[1],
                       c_img_search[2], c_img_search[3], SqdiffNormed, DEFAULT_PERCENT_MATCH)
        ],

        7: [
            "Invalid parameters, Checkpoint does not exist", API_FAIL, ("checkpoint_not_exists",
                                                                          MAX_X, MAX_Y, MAX_WIDTH, MAX_HEIGHT,
                                                                          default_CcoeffNormed,
                                                                          DEFAULT_PERCENT_MATCH)
        ],


    }

    # ------------------------------------ GetScreenTransitionTime

    sanity_get_screen_transition_time_params = ('not_on_chkpt_screen', 'move_out_chkpt_screen')

    get_screen_transition_time_params = {
        "chkpt_screen": [
            "Valid parameters, No screen transition from the checkpoint screen", SCREEN_TRANSITION_FAIL_VAL,
            (chkpt_screen_elm, T_MD_WAIT, INITIAL_DELAY)
        ],

        "not_on_chkpt_screen": [
            "Valid parameters, not on checkpoint screen", SCREEN_TRANSITION_FAIL_VAL,
            (img_unlike_symbol, T_MD_WAIT, INITIAL_DELAY)
        ],

        "move_out_chkpt_screen": [
            "Valid parameters, screen transition from the checkpoint screen", SCREEN_TRANSITION_FAIL_VAL,
            (chkpt_screen_elm, T_MD_WAIT, INITIAL_DELAY)
        ],
        0: [
            "Invalid parameters, Non existing checkpoint", SCREEN_TRANSITION_FAIL_VAL, ("nonExistingCheckpoint", T_MD_WAIT, INITIAL_DELAY)
        ],
        1: [
            "Invalid parameters, large timeToWait & initial delay", SCREEN_TRANSITION_FAIL_VAL, (chkpt_screen_elm, 500, 500)
        ],
        2: [
            "Invalid parameters, initial delay greater than time out", SCREEN_TRANSITION_FAIL_VAL, (chkpt_screen_elm, T_MD_WAIT, 25)
        ],
        3: [
            "Invalid parameters, negative timeToWait", SCREEN_TRANSITION_FAIL_VAL, (chkpt_screen_elm, -5, INITIAL_DELAY)
        ],
    }

    # indices of parameters considered in sanity test script to cover positive scenarios
    sanity_validate_chkpt_params = (0,1,2,3,)

    # -------------------------------- validateCheckPoint

    validate_chkpt_params = {
        0: ["Invalid scenario, checkpoint object without initializing", API_FAIL, not_initialized],
        1: ["Valid parameter, IC checkpoint, pixel", API_PASS, SkyValidateCheckPointICpixel],
        2: ["Valid parameter, IC checkpoint, rmse", API_PASS, SkyValidateCheckPointICrmsel],
        3: ["Valid parameter, Checkpoint created for parent DUT", API_PASS, ParentCheckPoint],
        4: ["Valid parameter, OCR checkpoint with multiple filters", API_PASS, OCRCheckpointMultipleFilters],
        5: ["Valid parameter, lengthy name for checkpoint", API_PASS, LengthyCheckpoint],
        6: ["Invalid scenario, checkpoint not created for target device", API_FAIL, not_created],
        7: ["Valid parameter, OCR checkpoint", API_PASS, SkyValidateCheckPointOCR],
        8: ["Valid parameter, Multiline OCR checkpoint", API_PASS, SkyValidateCheckPointMultiOCR],
    }

    # -------------------------------- QuickCaptureEx
    quick_capture_ex_params = {
        0: ["Lengthy image name", API_FAIL, (LONG_IMG_NAME, VALID_IMAGE_FORMAT)],
        1: ["Invalid image format", API_PASS, (IMG_NAME, INVALID_IMAGE_FORMAT)],
        2: ["Case sensitivity of valid image formats", API_PASS, (IMG_NAME, VALID_IMG_FORMAT_WRONG_CASE)],
        3: ["Valid image name, valid image format", API_PASS, (IMG_NAME, VALID_IMAGE_FORMAT)],
        4: ["Valid image name (containing numbers), valid image format", API_PASS, (IMAGE_NAME_NUMBER, VALID_IMAGE_FORMAT)],
        5: ["Invalid image name (containing special characters), valid image format", API_FAIL, (IMG_NAME_SPL, VALID_IMAGE_FORMAT)],
    }

    # -------------------------------- Reboot
    reboot_params = {
        0: ["Reboot while media playback", API_PASS],
        1: ["Reboot after reboot", API_FAIL],
        2: ["Reboot during locked state", API_PASS],
    }

    # -------------------------------- ReadProperty
    read_property_params = {
        0: ["Invalid property number", API_FAIL, READ_PROPERTY_INVALID],
        1: ["Lowest boundary value of property", API_PASS, READ_PROPERTY_LOWEST_BOUNDARY],
        2: ["Highest boundary value of property", API_PASS, READ_PROPERTY_HIGHEST_BOUNDARY],
    }

    # -------------------------------- Lock, Shake
    lock_params = {
        0: ["while device is not Locked", API_PASS],
        1: ["while device is already Locked", API_FAIL],
    }

    # -------------------------------- Unlock
    unlock_params = {
        0: ["while device is Locked", API_PASS],
        1: ["while device is already Unlocked", API_FAIL],
    }

    # -------------------------------- LaunchApp InitApp
    launch_app_params = {
        0: ["Valid Scenario, App is closed", API_PASS],
        1: ["Invalid Scenario, App is open already", API_PASS],
        2: ["Invalid Scenario, App is backgrounded", API_PASS],
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
        0: ["For an element without 'Selected' property", API_FAIL], # could not find an element without selected property
        1: ["Element with 'Selected' property", API_PASS]
    }

    # -------------------------------- IsEnabled
    is_enabled_params = {
        0: ["For an element without 'Enabled' property", API_FAIL],
        1: ["Element with 'Enabled' property", API_PASS]
    }

    # -------------------------------- StopCaptureZapFrames
    stop_capture_frame_params = {
        0: ["Without using StartCaptureZapFrames API", API_FAIL,],
        1: ["Multiple times without caliing StartCaptureZapFrames", API_FAIL,],
    }

    # -------------------------------- IsElementPresent
    is_element_present_params = {
        0: ["Element does not exist on the Page", API_FAIL,],
        1: ["For a visible element", API_PASS,],
        2: ["For an element with 'visible' False", API_FAIL,],  # start playback and check for the element,
        # need to confirm on the expected result
        # 3: ["Element having same ID but differ in index", API_PASS], # this will pass if the element is available
    }

    # -------------------------------- SetDUTAttribute
    # selected attribute is 'Manufacturer'
    set_dut_attr_params = {
        0: ["Valid attribute", API_PASS, (used_attr_name, valid_attr_value)],
        1: ["Empty attribute value", API_FAIL, (used_attr_name, empty_attr_value)],
        2: ["Long attribute value", API_FAIL, (used_attr_name, long_attr_value)],
        3: ["Attribute value with special characters", API_PASS, (used_attr_name, splchar_attr_value)],
        4: ["Attribute value with numbers alone", API_PASS, (used_attr_name, number_attr_value)],
        5: ["Attribute value with combination of spl chars, numbers", API_PASS, (used_attr_name, comb_attr_value)],
        6: ["Non existing attribute", API_FAIL, (non_existing_attr, valid_attr_value)],
    }


    # -------------------------------- GetDUTAttribute
    get_dut_attr_params = {
        0: ["Valid attribute", API_PASS, valid_attr],
        1: ["Empty attribute", API_FAIL, empty_attr],
        2: ["Not existing attribute", API_FAIL, non_existing_attr],
    }

    # -------------------------------- ReadCustomProperty
    # 1. Valid property number, property name
    # 2. Empty parameter
    # 3. Defined attribute but value not assigned for the target device
    # 4. Accessing attribute values with special character attribute name

    read_custom_prop_params = {
        0: ["Valid property name", API_PASS,],
        1: ["Valid property number", API_PASS, ],

    }

    # -------------------------------- Init
    init_params = {
        0: ["Non Existing checkpoint", API_FAIL, non_existing_chkpt, (time_to_wait, wait_gap)],
        1: ["Checkpoint with lengthy name", API_FAIL, lengthy_name_chkpt, (time_to_wait, wait_gap)], # Need to confirm about the status
        2: ["Checkpoint which is not created for the target device", API_FAIL, not_created, (time_to_wait, wait_gap)],
        3: ["Checkpoint which is not created for the target device", API_FAIL, not_created, (time_to_wait, wait_gap)],
    }


    # -------------------------------- SendAndroidKeyCode
    # key name or scenario, expected, key_code
    send_keycode_params = {
        0: []
    }

    # -------------------------------- WaitForElement
    wait_for_element_params = {
        0: ["Valid Parameters: Wait till WD timeout time, element available", API_PASS],
        1: ["Valid Parameters: Wait till WD timeout time, element not available", API_FAIL],
        2: ["Valid Parameters: Min wait time, element not available", API_FAIL],
        3: ["Valid Parameters: Min wait time, element available", API_PASS],
        4: ["Valid Parameters: Element already available", API_PASS],
        5: ["Invalid Parameters: Negative TimeToWait", API_FAIL],
        6: ["Invalid Parameters: TimeToWait=0, element available", API_PASS],
        7: ["Invalid Params: Non clickable element", API_FAIL,],

    }


    # -------------------------------- Swipe
    swipe_params = {
        0: ["Wrong coordinates", API_FAIL, C_SWIPE_WRONG],
        1: ["Out of boundary coordinates", API_FAIL, C_SWIPE_WRONG],
        2: ["Bottom-up swipe", API_PASS, C_BOTTOM_UP_SWIPE],
        3: ["Top-down swipe", API_PASS, C_TOP_DOWN_SWIPE],
        4: ["Right-left swipe", API_PASS, C_RIGHT_LEFT_SWIPE],
        5: ["Left-right swipe", API_PASS, C_LEFT_RIGHT_SWIPE],
        6: ["Swipe on a small area", API_PASS, C_SMALL_AREA_SWIPE],
        7: ["Both coordinates are same", API_PASS, C_SAME_SWIPE_CORD],
        8: ["Swipe until page ends", API_PASS, C_BOTTOM_UP_SWIPE],
        9: ["Swipe with an invalid argument", API_FAIL, ("700", "1000", "700", "0")],  # Invalid argument - FAL-3996
    }


    # -------------------------------- VerticalSwipe
    v_swipe_params = {
        0: ["Wrong coordinates", API_FAIL, C_V_SWIPE_WRONG],
        1: ["Swipe with max duration > WD timeout", API_FAIL, C_V_SWIPE_MAX_DUR],
        2: ["Vertical swipe on a horizontally scrolling area", API_PASS, C_TOP_DOWN_V_SWIPE],
        3: ["Swipe duration less than minimum expected = {}ms".format(min_swipe_duration), API_PASS, C_V_SWIPE_LEAST_DUR],
        4: ["Swipe with max duration = WD timeout", API_PASS, C_V_SWIPE_WD_DUR],
        5: ["Swipe till page ends", API_PASS, C_BOTTOM_UP_V_SWIPE],
    }

    # -------------------------------- HorizontalSwipe
    h_swipe_params = {
        0: ["Wrong coordinates", API_FAIL, C_H_SWIPE_WRONG],
        1: ["Swipe with max duration > WD timeout", API_FAIL, C_H_SWIPE_MAX_DUR],
        2: ["Out of boundary coordinates", API_FAIL, C_H_SWIPE_WRONG],
        3: ["Horizontal swipe on a vertically scrolling area", API_PASS, C_RIGHT_LEFT_H_SWIPE],
        4: ["Swipe duration less than minimum expected = {}ms".format(min_swipe_duration), API_PASS,
            C_H_SWIPE_LEAST_DUR],
        5: ["Swipe with max duration = WD timeout", API_PASS, C_H_SWIPE_WD_DUR],
    }

    # -------------------------------- PressAndMove
    press_and_move_params = {
        0: ["Wrong coordinates", API_FAIL, C_MOVE_WRONG],
        1: ["Out of boundary coordinates", API_FAIL, C_MOVE_OUTBOUND],
        2: ["Move to a small distance", API_PASS, C_SMALL_MOVE_DIST],
        3: ["Both locations are same", API_PASS, C_SAME_MOVE_LOC],
    }



    # -------------------------------- Error
    logger_error_params = {
        0: ["Invalid: Empty/No message", EMPTY_MSG],
        1: ["Invalid: Max length", LONG_MSG],
        2: ["Invalid: Message with number alone", MSG_WITH_NUMBERS],
        3: ["Invalid: Message with spl char alone", MSG_WITH_SPLCHARS],
        4: ["Invalid: Message with Positive words", ERROR_MSG],

    }

    # -------------------------------- Log
    logger_log_params = {
        0: ["Invalid: Empty/No message", EMPTY_MSG],
        1: ["Invalid: Max length", LONG_MSG],
        2: ["Invalid: Message with number alone", MSG_WITH_NUMBERS],
        3: ["Invalid: Message with spl char alone", MSG_WITH_SPLCHARS],
        4: ["Invalid: Message with Positive words", LOG_MSG],
    }

    # -------------------------------- Warn
    logger_warn_params = {
        0: ["Invalid: Empty/No message", EMPTY_MSG],
        1: ["Invalid: Max length", LONG_MSG],
        2: ["Invalid: Message with number alone", MSG_WITH_NUMBERS],
        3: ["Invalid: Message with spl char alone", MSG_WITH_SPLCHARS],
        4: ["Invalid: Message with Positive words", WARN_MSG],
    }


    # -------------------------------- CommitStepResult
    commit_step_params = {
        0: ["Long step name", (LONG_MSG, PASSED)],
        1: ["Long step name", (LONG_MSG, FAILED)],
        2: ["Valid step name, Status - PASSED", (VALID_STEP_NAME, PASSED)],
        3: ["Valid step name, Status - FAILED", (VALID_STEP_NAME, FAILED)],
        4: ["Valid step name, Status - UNKNOWN", (VALID_STEP_NAME, UNKNOWN)],
        5: ["Valid step name, Status - ERROR", (VALID_STEP_NAME, ERROR)],
        6: ["Valid step name, Status - ABORTED", (VALID_STEP_NAME, ABORTED)],
        7: ["Valid step name", (VALID_STEP_NAME, UNKNOWN)],
        8: ["Step name with special chars", (STEP_NAME_WITH_SPL_CHAR, FAILED)],
        9: ["Valid step name, Invalid status ", (VALID_STEP_NAME, INVALID_STATUS)],
        10: ["Valid step name, Status with special chars", (VALID_STEP_NAME, STEP_NAME_WITH_SPL_CHAR)],

    }

    # -------------------------------- CommitTestResult
    commit_test_params = {
        0: ["Valid Status - PASSED", PASSED],
        1: ["Valid Status - FAILED", FAILED],
        2: ["Valid Status - UNKNOWN", UNKNOWN],
        3: ["Valid Status - ERROR", ERROR],
        4: ["Valid Status - ABORTED", ABORTED],
        5: ["Invalid Status", INVALID_STATUS],
        6: ["Invalid Status: Special Chars", SPL_CHR_STATUS],
    }


    # ----------------- UploadScreenshot

    upload_screenshot_params = {
        0: [
            "Valid parameters", API_PASS, (IMG_NAME, GET_SCREENSHOT_RETURN)
        ],
        1: [
            "Invalid parameters: Invalid Screenshot", API_FAIL, (IMG_NAME, IMG_NAME)
        ],
        2: ["Invalid parameters: Lengthy image name", API_FAIL, (LONG_IMG_NAME, GET_SCREENSHOT_RETURN)
            ],
        3: [
            "Invalid parameters: Non base64ImageString as Screenshot", API_FAIL, (IMG_NAME, CAPTURE_IMAGE_RETURN)
        ],
    }

    # ----------------- AddCustomDUTAttribute

    add_custom_dut_attribute_params = {
        0: [
            "Valid parameters", API_PASS, unique_attr
        ],
        1: [
            "Invalid parameters: Empty attribute", API_FAIL, empty_attr_value
        ],
        2: ["Invalid parameters: Long name", API_FAIL, long_attr_value
            ],
        3: [
            "Invalid parameters: Name with special characters", API_PASS, splchar_attr_value
        ],
    }

    # ----------------- SetCustomDUTAttribute

    set_custom_dut_attribute_params = {
        0: [
            "Valid parameters", API_PASS, unique_val,
        ],
        # As per the current implementaion, to clear the param value, api accepts empty val
        1: [
            "Invalid: Empty value", API_PASS, empty_val,
        ],
        2: ["Invalid: Long value", API_FAIL, long_val,
            ],
        3: [
            "Invalid: Value with special characters", API_PASS, splchar_attr_val,
        ],
        4: [
            "Invalid: Value with digits alone", API_PASS, number_attr_val,
        ],
        5: [
            "Invalid: Value with combination of splchar, numbers, alphabets", API_PASS, comb_attr_val,
        ],
    }

    # ----------------- GetCustomDUTAttribute, ReadCustomProperty

    get_custom_dut_attribute_params = {
        # this is being verified along with set_custom_dut_attribute

        # 0: [
        #     "Valid parameters", API_PASS, unique_val,
        # ],
        1: [
            "Invalid: Empty attribute", API_FAIL, empty_val,
        ],
        2: ["Invalid: Long name", API_FAIL, long_val,
            ],
        3: [
            "Invalid: Name with special characters", API_PASS, splchar_attr_val,
        ],
    }


    # -------------------------------- SendAppToBackground
    send_app_bg_duration = 30
    send_app_bg_params = {

        # resume from background after given wait time and goes off again to bg > seems like this scenario is invalid
        1: ["Invalid Scenario, App is backgrounded already", API_PASS, send_app_bg_duration],
        2: ["Valid Scenario, with duration equal to timeout time of webdriver", API_PASS, T_WD_TIMEOUT],
        3: ["Valid Scenario, with duration equal to WD timeout+1", API_FAIL, T_WD_TIMEOUT+1],
        4: ["Invalid Scenario, with negative value for duration", API_FAIL, T_NEG_TIME_TO_WAIT],
        5: ["Invalid Scenario, with duration set to 0", API_FAIL, T_NO_WAIT],
        6: ["Valid Scenario, App is closed", API_FAIL, send_app_bg_duration],
    }

    # -------------------------------- CloseApp
    close_app_params = {
        # once app is backgrounded, the control will not be transferred to other dut calls until SendAppBackground API finished
        # so this scenario is euivalent to the CloseApp call when application is open
        0: ["Valid Scenario, App is backgrounded", API_PASS, ],
        1: ["Invalid Scenario, when launch app/initapp failed (calls CloseApp)", API_FAIL],

    }

    # -------------------------------- DoubleTapElement, DoubleTapElement with Index
    doubletap_params = {
        0: ["Invalid, non-existing element", API_FAIL, ],
        1: ["Invalid, non-visible element", API_FAIL,],
    }

    # -------------------------------- HideKeyboard
    hide_kbd_params = {
        0: ["Invalid: Keyboard not available, no text field", API_FAIL],    # call api when on app home screen
        1: ["Valid: Keyboard visible", API_PASS],
        2: ["Invalid: Focused on text field, but keyboard not visible", API_FAIL],
    }

    # -------------------------------- ClearText
    clear_text_params = {
        0: ["Invalid: with a non-text field", API_FAIL],
        1: ["Invalid: on an empty text field", API_FAIL],
        2: ["Valid: on a text field with data", API_PASS],
        # 3: ["Invalid: with search results", API_FAIL],
        4: ["Invalid: Wrong element Id", API_FAIL],
    }

    # -------------------------------- HandleAlertMessage
    handle_alert_params = {
        0: ["Invalid: Alert not present", API_FAIL, alert_accept_upper],
        1: ["Invalid: During media playback", API_FAIL, alert_accept_upper],
        2: ["Invalid: Popup present, Empty action", API_FAIL, empty_attr],
        3: ["Invalid: Popup present, Wrong action", API_FAIL, alert_wrong_action],
        4: ["Valid: Action - ACCEPT - uppercase", API_PASS, alert_accept_upper],
        5: ["Valid: Action - accept - lowercase", API_PASS, alert_accept_lower],
        6: ["Valid: Action - Accept - Camel case", API_PASS, alert_accept_camel],
        7: ["Valid: Action - DISMISS - uppercase", API_PASS, alert_dismiss_upper],
        8: ["Valid: Action - dismiss - lowercase", API_PASS, alert_dismiss_lower],
        9: ["Valid: Action - Dismiss - Camel case", API_PASS, alert_dismiss_camel],

    }

    # ------------------------------------ GetScreenTransitions
    HPA_X = 90
    HPA_Y = 90
    HPA_W = 90
    HPA_H = 90
    HPA_SENS = 3
    HPA_DUR = 60

    # ------------------------------------ VolumeUp
    volume_up_params = {
        0: ["Valid: maximum volume", VALID_MAX_VOL, API_PASS],
        1: ["Valid: volume up when max volume", VOLUME_UNIT, API_PASS],
        2: ["Invalid: numberOfLevels boundary - min", INVALID_VOL_LEVEL_MIN, API_FAIL],
        3: ["Invalid: numberOfLevels boundary - max", INVALID_VOL_LEVEL_MAX, API_FAIL],
        4: ["Invalid: numberOfLevels negative value", INVALID_VOL_NEGATIVE, API_FAIL]
    }

    # ------------------------------------ VolumeDown
    volume_down_params = {
        0: ["Valid: minimum volume", VALID_MIN_VOL, API_PASS],
        1: ["Valid: volume down when min volume", VOLUME_UNIT, API_PASS],
        2: ["Invalid: numberOfLevels boundary - min", INVALID_VOL_LEVEL_MIN, API_FAIL],
        3: ["Invalid: numberOfLevels boundary - max", INVALID_VOL_LEVEL_MAX, API_FAIL],
        4: ["Invalid: numberOfLevels negative value", INVALID_VOL_NEGATIVE, API_FAIL]
    }

    # --------------------------------- GetScreenTransitions
    get_screen_transitions = {
        0: ["Invalid: Tap coordinate outside boundary", 'coordinates', (1000000, 1000000), HPA_DUR,
            (HPA_X, HPA_Y, HPA_W, HPA_H, HPA_SENS)],
        1: ["Invalid: Non Existing Tap Element", 'element', ("test",), HPA_DUR,
            (HPA_X, HPA_Y, HPA_W, HPA_H, HPA_SENS)],
        2: ["Invalid: Duration Out of boundary", 'coordinates', (C_TAP_PLAYBACK[0], C_TAP_PLAYBACK[1]), 150,
            (HPA_X, HPA_Y, HPA_W, HPA_H, HPA_SENS)],
        3: ["Invalid: Negative sensitivity", 'coordinates', (C_TAP_PLAYBACK[0], C_TAP_PLAYBACK[1]), HPA_DUR,
            (HPA_X, HPA_Y, HPA_W, HPA_H, -4)],
        4: ["Invalid: Param out of boundary", 'coordinates', (C_TAP_PLAYBACK[0], C_TAP_PLAYBACK[1]), HPA_DUR,
            (22222, 2222, 2222, 2222, 2222, HPA_SENS)]
    }
