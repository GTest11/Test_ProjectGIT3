# ''''''''''''''''''''''''''' CONFIG FILE - ANDROID '''''''''''''''''''''''''''''''''''''''''
# Author            : Shameena HA
# Date              :   26-11-2018
# Script Version     : 1.0
# Modification details:
#
# ''''''''''''''''''''''''''' CONFIG FILE - ANDROID - END '''''''''''''''''''''''''''''''''

# imports
from config.config_base import config_base


class androidPhone(config_base):
    '''
    This contains config variable specific to android phones.
    This inherits all variables in config_base class

    '''


    # ==================================================== COMMON
    # ================================================================================
    package = {
        "youtube": "com.google.android.youtube",
        # "skygo": "com.bskyb.skygo",
    }

    activity = {
        "youtube": "com.google.android.youtube.HomeActivity",
        # "skygo": "com.bskyb.uma.app.bootstrap.BootstrapActivity",
    }

    platform = "Android"
    # ==================================================== END COMMON =============


    # ==================================================== CHECKPOINT VARIABLES
    # ================================================================================
    yt_logo = "Mobile_YouTube"

    # ==================================================== END CHECKPOINT VARIABLES =============

    #press and move coordinates
    c_press_move = (139, 147, 431, 1259)
    C_TAP_PLAYBACK = (260, 300)
    C_WRONG_COORDS = (5000, 5000)

    # coordinates
    # C_DET_MOTION = (176, 99, 439, 251)
    # detect motion - send_android_keycode.py
    detect_motion_check = (176, 99, 439, 251, 20, 5, "10")
    c_img_search = (543, 71, 49, 51)

    # DynamicImageCompare
    C_DYN_IMG_COMP = (5, 55, 215, 88)
    dyn_img = "dynamic_compare_img"
    DEFAULT_DYN_TOLERANCE = 15

    # ==================================================== VARIABLES
    # ================================================================================

    # App home element
    home = {
        'xpath' : "//android.widget.ImageView[@content-desc='YouTube']",
        'id'    : 'com.google.android.youtube:id/youtube_logo',
        'name'  : None,
        'class' : None,
        'access_id': None,
    }

    # get_element_count.py
    getelmcount_multi = {
        'xpath' : '//android.widget.ImageView',
        'id' : None,
        'name' : None,
        'class': 'android.widget.ImageView',
        'access_id' : None
    }

    getelmcount_single = {
        'xpath': '//android.widget.ImageView[@content-desc="Video"]',
        'id': None,
        'name': None,
        'class': None,
        'access_id': None
    }

    getelmcount_not_exists = {
        'xpath': '//android.widget.ImageView[0]',   #an element which does not exist
        'id': None,
        'name': None,
        'class': None,
        'access_id': None
    }

    # is_selected.py
    without_selected_prop = {
        'xpath' : "//android.widget.ImageView[@content-desc='YouTube']",
        'id'    : 'com.google.android.youtube:id/youtube_logo',
        'name'  : None,
        'class' : None,
        'access_id': None,
    }

    with_selected_prop = {
        'xpath': '//android.widget.Switch[@content-desc="Autoplay"]',  # an element which does not exist
        'id': 'com.google.android.youtube:id/autonav_toggle',
        'name': None,
        'class': None,
        'access_id': None
    }

    # is_enabled.py
    without_enabled_prop = {
        'xpath' : "//android.widget.ImageView[@content-desc='YouTube']",
        'id'    : 'com.google.android.youtube:id/youtube_logo',
        'name'  : None,
        'class' : None,
        'access_id': None,
    }

    invalid_elem = {
        'xpath': '//android.widget.ImageView[0]',  # an element which does not exist
        'id': None,
        'name': None,
        'class': None,
        'access_id': None,
    }

    with_enabled_prop = {
        'xpath': '//android.widget.Switch[@content-desc="Autoplay"]',  # an element which does not exist
        'id': 'com.google.android.youtube:id/autonav_toggle',
        'name': None,
        'class': None,
        'access_id': None
    }

    is_elm = {
        'xpath': '//android.widget.ImageView[@content-desc="Search"]',
        'id': None,
        'name': 'id.ui.navigation.search.button',
        'class': None,
        'access_id': 'Search'
    }

    autoplay_toggle = {
        'xpath': '//android.widget.Switch[@content-desc="Autoplay"]',  # an element which does not exist
        'id': 'com.google.android.youtube:id/autonav_toggle',
        'name': None,
        'class': None,
        'access_id': None
    }

    # search image
    search_icon = {
        'xpath': '//android.widget.ImageView[@content-desc="Search"]',
        'id': None,
        'name': 'id.ui.navigation.search.button',
        'class': None,
        'access_id': 'Search'
    }

    search_txt_box = {
        'xpath': '//android.widget.EditText[@text="Search YouTube"]',
        'id': 'com.google.android.youtube:id/search_edit_text',
        'name': None,
        'class': None,
        'access_id': None,
    }

    search_box_with_text = {
        # 'xpath': '//android.widget.TextView[@text="{}"]',
        #format(config_base.search_text),
        'xpath': '// android.widget.TextView[@text="master chef australia"]',
        'id': 'com.google.android.youtube:id/search_query', #'com.google.android.youtube:id/search_query',
        'name': None,
        'class': None,
        'access_id': None,
    }

    # Bottom nav panel button - Home, Trending, etc
    bottom_nav_home_button = {
        'xpath': '//android.widget.TextView[@text="Home"]',
        'id': None,
        'name': None,
        'class': None,
        'access_id': None,
    }

    # Bottom nav panel button - Home, Trending, etc
    navbar_home = {
        'xpath': '//android.widget.TextView[@text="Home"]',
        'id': None,
        'name': None,
        'class': None,
        'access_id': None,
    }

    # to get the element height and width
    elem_det = {
        'xpath': '//android.widget.ImageView[@content-desc="Video"]',
        'id': None,
        'name': None,
        'class': None,
        'access_id': None,
    }

    ytb_logo = {
        'xpath': "//android.widget.ImageView[@content-desc='YouTube']",
        'id': None,
        'name': None,
        'class': None,
        'access_id': None,
    }

    read_text = {
        'xpath': '//android.widget.TextView[@text="Home"]',
        'id': None,
        'name': None,
        'class': None,
        'access_id': None,
    }

    read_text_idx = {
        'xpath': '//android.widget.TextView',
        'id': None,
        'name': None,
        'class': None,
        'access_id': None,
    }

    download_opt = {
        'xpath': '//android.widget.Button[@content-desc="Download"]',
        'id': None,
        'name': None,
        'class': None,
        'access_id': None,
    }

    downloaded = {
        'xpath': '//android.widget.TextView[@text="Downloaded"]',
        'id': None,
        'name': None,
        'class': None,
        'access_id': None,
    }


    click_tap_idx = {
        'xpath': '//android.widget.ImageView',
        'id': None,
        'name': 'id.ui.navigation.search.button',
        'class': None,
        'access_id': 'id.ui.navigation.search.button'
    }

    elm_idx = {
        'xpath': '//android.widget.ImageView',
        'id': None,
        'name': 'id.ui.navigation.search.button',
        'class': None,
        'access_id': 'id.ui.navigation.search.button'
    }

    element_referred_by_index = {
        'xpath': '//android.widget.ImageView',
        'id': None,  # needs to be None
        'name': None,  # needs to be None
        'class': None,  # needs to be None
        'access_id': None  # needs to be None
    }

    user_icon_identifier = {
        'xpath': '//android.widget.ImageView[@content-desc="Account"]',  # an element with clickable FALSE
        'id': None,
        'name': None,
        'class': None,
        'access_id': None
    }

    search_refered_by_index = {
        'xpath': "//XCUIElementTypeOther[@name='Top View']/XCUIElementTypeOther[1]/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeButton[2]",
        'id': None,
        'name': None,
        'class': None,
        'access_id': None
    }

    trending_nav = {

        'xpath': '//android.widget.Button[@content-desc="Trending"]',
        'id': None,
        'name': None,
        'class': None,
        'access_id': None,

    }

    library_nav = {

        'xpath': '//android.widget.Button[@content-desc="Library"]',
        'id': None,
        'name': None,
        'class': None,
        'access_id': None,

    }

    navbar_trending = {
        'xpath': '//android.widget.Button[@content-desc="Trending"]',
        'id': None,
        'name': None,
        'class': None,
        'access_id': None,
    }

    # tap_percent.py cordinates of search icon as percentage
    search_icon_tap_percent = (78, 7)
    # tap_percent.py cordinates of youtube image as percentage
    youtube_img_percent = (9, 7)
    # tap_percent.py cordinates of back icon in search text as percentage
    back_icon_percent = (4, 7)

    # sanity_iselement_tapelement.py - overrides this item in respective configs
    list_iselm = (navbar_home, home, search_icon)
    search_icon_index = 3
    wrong_index = 27
    account_icon_index = 4
    index_not_on_page = 115  # TapElement (with index)

    # Cordinate to tap for youtube playback
    c_tap_for_yt_playback = (285, 691)

    # get_text.py
    ele_without_text = {
        'xpath': '//android.widget.ImageView[@content-desc="Account"]',
        'id': "com.google.android.youtube:id/image",
        'name': None,
        'class': "android.widget.ImageView",
        'access_id': "Account",
    }
    non_exist_ele = {
        'xpath': None,
        'id': "com.google.android.youtube:id/search_edit_text",
        'name': None,
        'class': "android.widget.EditText",
        'access_id': None,
    }
    lengthy_text = {
        'xpath': None,
        'id': "com.google.android.youtube:id/title",
        'name': None,
        'class': "android.widget.Textview",
        'access_id': None,
    }
    ele_with_dif_ind = {
        'xpath': None,
        'id': "com.google.android.youtube:id/title",
        'name': None,
        'class': "android.widget.Textview",
        'access_id': None,
    }

    # click_index.py
    click_button = {
        'xpath': '//android.widget.ImageView[@content-desc="Account"]',
        'id': "com.google.android.youtube:id/image",
        'name': None,
        'class': "android.widget.ImageView",
        'access_id': "Account",
    }
    non_clickable = {
        'xpath': '//android.widget.ImageView',
        'id': None,
        'name': None,
        'class': None,
        'access_id': None,
    }

    invalid_click = {
         'xpath': '//android.widget.Butsdton[@content-desc="Home"]/android.widget.ImageView',
        'id': 'com.google.android.yousdtube:id/image',
        'name': None,
        'class': 'android.widgsdet.ImageView',
        'access_id': None,
    }
    non_visible_click = {
        'xpath': '//android.widget.ImageView[@content-desc="Search"]',
        'id': None,
        'name': None,
        'class': "android.widget.ImageView",
        'access_id': None,
    }

    # get_text_index.py
    ele_with_text = {
        'xpath': '//android.widget.Button[@content-desc="Trending]/android.widget.TextView"',
        'id': 'com.google.android.youtube:id/text',
        'name': None,
        'class': "android.widget.TextView",
        'access_id': None,
    }
    #send_keys.py
    edit_box = {
        'xpath': '//android.widget.EditText[@text="Search YouTube"]',
        'id': 'com.google.android.youtube:id/search_edit_text',
        'name': None,
        'class': None,
        'access_id': None,
    }
    non_text_field = {
        'xpath': '/hierarchy/android.widget.FrameLayout/android.view.View',
        'id': 'android:id/statusBarBackground',
        'name': 'account_panel_button',
        'class': 'android.view.View',
        'access_id': None,
    }

    account_icon = {
        'xpath': '//android.widget.ImageView[@content-desc="Account"]',
        'id': None,
        'name': None,
        'class': None,
        'access_id': 'Account'
    }

    # ==================================================== END VARIABLES =============

    # class test_params(config_base):
    API_PASS = True
    API_FAIL = False

    # -------------------------------- TapPercent
    tap_percent_params = {
        0: ["Parameter out of boundary", API_FAIL, config_base.percent_out_of_boundary],
        1: ["Tap on element with Clickable - False, but available on the screen", API_PASS, youtube_img_percent],
        2: ["Tap on lock screen", API_PASS, search_icon_tap_percent],
        3: ["Tap on Clickable element", API_PASS, search_icon_tap_percent],
    }

    get_element_count_params = {
        0: ["Mutliple element", API_PASS, getelmcount_multi],
        1: ["Single element", API_PASS, getelmcount_single],
        2: ["No element", API_FAIL, getelmcount_not_exists],
    }

    # -------------------------------- GetHeight, GetWidth, GetLocation
    get_height_width_params = {
        0: ["Mutliple element", API_PASS, getelmcount_multi],
        1: ["Single element", API_PASS, getelmcount_single],
        2: ["No element", API_FAIL, getelmcount_not_exists],
    }

    # -------------------------------- GetAttribute, GetAllAttributeValues
    get_all_attribute_value_params = {
        0: ["An Element which exists", API_PASS, getelmcount_single, config_base.attr_list],
        1: ["An Element which does not exist", API_FAIL, getelmcount_not_exists, config_base.attr_list],
        2: ["With invalid attribute name ", API_FAIL, getelmcount_single, config_base.invalid_attr_list],
    }

    # -------------------------------- GetAllChildAttributeValues
    get_all_child_attribute_values_params = {
        0: ["No previous element interaction", API_FAIL, getelmcount_single, config_base.attr_list],
        1: ["With invalid attribute name", API_FAIL, getelmcount_single, config_base.invalid_attr_list],
        2: ["An Element which does not exist", API_FAIL, getelmcount_not_exists, config_base.attr_list],
        3: ["With previous element interaction", API_PASS, getelmcount_single, config_base.attr_list],
    }

    is_selected_params = {
        0: ["For an element without 'Selected' property", API_FAIL, without_selected_prop],
        1: ["Element with 'Selected' property", API_PASS, with_selected_prop]
    }

    is_enabled_params = {
        0: ["For an element without 'Enabled' property", API_FAIL, without_enabled_prop],
        1: ["Element with 'Enabled' property", API_PASS, with_enabled_prop]
    }

    is_element_present_params = {
        0: ["Element does not exist on the Page", API_FAIL, autoplay_toggle],
        1: ["For a visible element", API_PASS, is_elm],
        2: ["For an element with 'visible' False", API_FAIL, is_elm],  # start playback and check for the element
        # 3: ["Element having same ID but differ in index", API_PASS], # this will pass if the element is available
    }

    # -------------------------------- WaitForElement
    wait_for_element_params = {
        0: ["Invalid Parameters: TimeToWait=0, element available", API_FAIL,
            (home, config_base.T_NO_WAIT)
            ],
        1: ["Valid Parameters: Wait till WD timeout time, element not available", API_FAIL,
            (search_txt_box, config_base.T_WD_TIMEOUT)
            ],
        2: ["Valid Parameters: Min wait time, element not available", API_FAIL,
            (search_txt_box, config_base.T_MIN_WAIT)
            ],
        3: ["Valid Parameters: Min wait time, element available", API_PASS,
            (home, config_base.T_MIN_WAIT)
            ],
        4: ["Valid Parameters: Element already available", API_PASS,
            (search_icon, config_base.T_MD_WAIT)
            ],
        5: ["Invalid Parameters: Negative TimeToWait", API_FAIL,
            (home, config_base.T_NEG_TIME_TO_WAIT)
            ],
        6: ["Valid Parameters: Wait till WD timeout time, element available", API_PASS,
            (search_txt_box, config_base.T_WD_TIMEOUT)
            ],
        7: ["Invalid Params: Element which does not exist", API_FAIL,
            (invalid_elem, config_base.T_MD_WAIT)
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
            (config_base.IMG_NAME_SPL, C_DYN_IMG_COMP[0], C_DYN_IMG_COMP[1], C_DYN_IMG_COMP[2], C_DYN_IMG_COMP[3],
             DEFAULT_DYN_TOLERANCE)
        ],
        4: ["Invalid parameter, coordinate out of boundary", API_FAIL,
            (dyn_img, config_base.MAX_X, config_base.MAX_Y, config_base.MAX_WIDTH,
             config_base.MAX_HEIGHT, DEFAULT_DYN_TOLERANCE)],
        5: ["Invalid case, Use image from CaptureImage API as refImage", API_FAIL,
            (dyn_img, C_DYN_IMG_COMP[0], C_DYN_IMG_COMP[1], C_DYN_IMG_COMP[2], C_DYN_IMG_COMP[3],
             DEFAULT_DYN_TOLERANCE)]
    }

    # ---------------------- ImageSearch

    # moved to respective configs
    sanity_image_search_params = (0, 1,)
    image_search_params = {
        0: [
            "Valid parameters, expected region (small) and algorithm: SqdiffNormed",
            API_PASS, (config_base.imageSearchSingleOccurance, c_img_search[0], c_img_search[1],
                       c_img_search[2], c_img_search[3], config_base.SqdiffNormed, config_base.DEFAULT_PERCENT_MATCH)
        ],
        1: [
            "Valid parameters, max region and algorithm: CcorrNormed", API_PASS,
            (config_base.imageSearchSingleOccurance,
             config_base.MAX_X, config_base.MAX_Y, config_base.MAX_WIDTH, config_base.MAX_HEIGHT,
             config_base.CcorrNormed, config_base.DEFAULT_PERCENT_MATCH
             )
        ],
        2: [
            "Valid parameters, max region and algorithm: default_CcoeffNormed", API_PASS,
            (
                config_base.imageSearchSingleOccurance,
                config_base.MAX_X, config_base.MAX_Y,
                config_base.MAX_WIDTH, config_base.MAX_HEIGHT,
                config_base.default_CcoeffNormed, config_base.DEFAULT_PERCENT_MATCH
            )
        ],
        3: [
            "Valid parameters, percentMatchThreshold boundary condition: 0", API_PASS,
            (
                config_base.imageSearchSingleOccurance, config_base.MAX_X,
                config_base.MAX_Y, config_base.MAX_WIDTH, config_base.MAX_HEIGHT,
                config_base.default_CcoeffNormed, 0
            )
        ],
        4: [
            "Valid parameters, multiple occurance of pattern", API_PASS,
            (
                config_base.imageSearchMultipleOccurance, config_base.MAX_X,
                config_base.MAX_Y, config_base.MAX_WIDTH, config_base.MAX_HEIGHT,
                config_base.default_CcoeffNormed, config_base.DEFAULT_PERCENT_MATCH
            )
        ],
        5: [
            "Invalid parameters, Checkpoint does not exist", API_FAIL,
            (
                "checkpoint_not_exists", config_base.MAX_X, config_base.MAX_Y,
                config_base.MAX_WIDTH, config_base.MAX_HEIGHT,
                config_base.default_CcoeffNormed, config_base.DEFAULT_PERCENT_MATCH
            )
        ],
        6: [
            "Valid parameters, OCR Checkpoint", API_PASS,
            (
                config_base.ocr_image_search_chkpt, config_base.MAX_X, config_base.MAX_Y,
                config_base.MAX_WIDTH, config_base.MAX_HEIGHT, config_base.default_CcoeffNormed,
                config_base.DEFAULT_PERCENT_MATCH
            )
        ],

    }

    # -------------------------------- TapElement
    tap_element_params = {
        0: ["Element does not exist on the Page", API_FAIL, autoplay_toggle],
        1: ["For a visible element", API_PASS, is_elm],
        2: ["For an element with 'visible' False", API_FAIL, is_elm],   # when search text box is visible
        3: ["Tap on Non-clickable element", API_PASS, user_icon_identifier],
    }

    # -------------------------------- TapElement (with index)
    tap_element_with_index_params = {
        0: ["For a visible element", API_PASS, (element_referred_by_index, search_icon_index)],
        1: ["Valid element which does not exist on the Page", API_FAIL, (element_referred_by_index, index_not_on_page)],
        2: ["For an element with 'visible' False", API_FAIL, (element_referred_by_index, index_not_on_page)],  # when search text box is visible
        3: ["Tap on Non-clickable element", API_PASS, (element_referred_by_index, account_icon_index)],
        4: ["Element with wrong index value", API_FAIL, (element_referred_by_index, -1)]
    }

    # -------------------------------- DoubleTapElement, DoubleTapElement with Index
    doubletap_params = {
        0: ["Invalid, non-visible element", API_FAIL, search_icon],
        1: ["Invalid, non-existing element", API_FAIL, invalid_elem],
    }

    doubletap_idx_params = {
        0: ["Invalid, non-visible element", API_FAIL, (elm_idx, search_icon_index)],
        1: ["Invalid, non-existing element", API_FAIL, (elm_idx, -1)],
    }


    click_params = {
        0: ["Element does not exist on the Page", API_FAIL, autoplay_toggle],
        # seems like click works regradless of the element property, so given PASS for the api
        1: ["Invalid: on a non-clickable element", API_PASS, home],
        2: ["Valid: on a clickable element", API_PASS, search_icon],
        3: ["Invalid: on an element with visible property False, but available on the screen", API_FAIL, search_icon]
    }

    tap_params = {
        0: ["Invalid: Wrong/unavailable coordinates", API_FAIL, C_WRONG_COORDS],
        # seems like click works regradless of the element property, so given PASS for the api
        1: ["Valid: Tap on anywhere on an element", API_PASS, C_TAP_PLAYBACK],
    }

    get_text_params = {
        0: ["Element without text", "", ele_without_text],
        1: ["Non existing element", "", non_exist_ele],
        2: ["Element with lengthy text", "", lengthy_text],
        3: ["Two elements with same Id but differs in index", "", ele_with_dif_ind]
    }

    click_index_params = {
        0: ["Invalid: Index outside boundary", API_FAIL, (click_button, 100)],
        1: ["Invalid: on a non click-able element", API_PASS, (non_clickable, 3)],
        2: ["Valid: on a click-able element", API_PASS, (non_clickable, 2)],
        3: ["Invalid: Invalid element value", API_FAIL, (invalid_click, 1)],
        4: ["Invalid: Invalid index values", API_FAIL, (click_button, -1)],
        5: ["Invalid: on an element with visible property False, but available on the screen", API_FAIL, (non_visible_click, 1)]
    }

    get_text_index_params = {
        0: ["Invalid: Index outside boundary", "", (ele_with_text, 555)],
        1: ["Invalid: Non existing element", "", (non_exist_ele, 1)],
        2: ["Valid: Element without text", "", (ele_without_text, 1)],
        3: ["Valid: Element with lengthy text", "", (lengthy_text, 1)],
        4: ["Invalid: Negative value for index", "", (ele_with_text, -1)]
    }
    send_keys_params = {
        0: ["Valid: send to edit box", API_PASS, edit_box, config_base.search_text],
        1: ["Valid: Send lengthy string", API_PASS, edit_box, config_base.LENGTHY_NAME],
        2: ["Valid: Send spl chars & nums", API_PASS, edit_box, config_base.MSG_WITH_SPLCHARS],
        3: ["Invalid: Send to non-text field", API_FAIL, non_text_field, config_base.search_text],
        4: ["Send numbers to the edit box", API_PASS, edit_box, config_base.MSG_WITH_NUMBERS],
    }
    # ------------------------------------ GetScreenTransitions
    # same as detect_motion coords
    HPA_X = 176
    HPA_Y = 99
    HPA_W = 439
    HPA_H = 251
    HPA_SENS = 3
    HPA_DUR = 60
