# ''''''''''''''''''''''''''' CONFIG FILE - iPHONE '''''''''''''''''''''''''''''''''''''''''
# Author            : Shameena HA
# Date              :   26-11-2018
# Script Version     : 1.0
# Modification details:
#
# ''''''''''''''''''''''''''' CONFIG FILE - iPHONE - END '''''''''''''''''''''''''''''''''


from config.config_base import config_base

class iPhone(config_base):
    '''
        This contains config variable specific to iPhones.
        This inherits all variables in config_base class

    '''


    # ==================================================== COMMON
    # ================================================================================
    app_name = {
        "youtube": "com.google.ios.youtube",
        # "skygo": "com.bskyb.skygo",
    }

    platform = "iOS"
    # ==================================================== END COMMON =============


    # ==================================================== CHECKPOINT VARIABLES
    # ================================================================================
    yt_logo = "Mobile_YouTube"

    # ==================================================== END CHECKPOINT VARIABLES =============
    # ================================================================================

    # DetectMotion
    detect_motion_check = (176, 99, 439, 251, 20, 5, "10")
    C_SWIPE_WRONG = (1000, 1000, -1000, -1000)
    C_TOP_DOWN_SWIPE = (500, 0, 500, 700)
    C_BOTTOM_UP_SWIPE = (500, 700, 500, 0)
    C_LEFT_RIGHT_SWIPE = (0, 500, 500, 0)
    C_RIGHT_LEFT_SWIPE = (500, 0, 0, 500)
    C_SMALL_AREA_SWIPE = (500, 0, 500, 700)
    C_SAME_SWIPE_CORD = (500, 0, 500, 0)
    c_img_search = (498, 54, 51, 51)
    C_DYN_IMG_COMP = (1, 1, 493, 323)
    C_TAP_PLAYBACK = (260, 300)
    C_WRONG_COORDS = (5000, 5000)

    # Cordinate to tap for youtube playback
    c_tap_for_yt_playback = (285, 550)

    # dynamic image compare
    dyn_img = "dynamic_compare_img"
    CACHE_VALID_URL_FOR_DYNAMIC_COMPARE = "http://10.47.166.48/TestImage/iPhone/iphone.jpg"
    DEFAULT_DYN_TOLERANCE = 15

    # ==================================================== VARIABLES
    # ================================================================================


    home = {
        'xpath': "//XCUIElementTypeApplication[@name='YouTube']",
        'id': None,
        'name': None,
        'class': None,
        'access_id': None,
    }

    getelmcount_multi = {
        'xpath': '//XCUIElementTypeButton',
        'id': None,
        'name': None,
        'class': None,
        'access_id': None,
    }

    getelmcount_single = {
        'xpath': '//XCUIElementTypeButton[@name="id.ui.navigation.search.button"]',
        'id': None,
        'name': 'id.ui.navigation.search.button',
        'class': None,
        'access_id': 'id.ui.navigation.search.button',
    }

    getelmcount_not_exists = {
        'xpath': '//XCUIElementTypeButton[0]',  # an element which does not exist
        'id': None,
        'name': None,
        'class': None,
        'access_id': None,
    }

    # is_selected.py
    without_selected_prop = {
        'xpath': "//XCUIElementTypeApplication[@name='YouTube']",
        'id': None,
        'name': None,
        'class': None,
        'access_id': None,
    }

    with_selected_prop = {
        'xpath': '//XCUIElementTypeButton[@name="id.autoplay.toggle.button"]',
        'id': None,
        'name': 'id.autoplay.toggle.button',
        'class': None,
        'access_id': 'id.autoplay.toggle.button',
    }

    # is_enabled.py
    without_enabled_prop = {
        'xpath': "//XCUIElementTypeApplication[@name='YouTube']",
        'id': None,
        'name': None,
        'class': None,
        'access_id': None,
    }

    invalid_elem = {
        'xpath': '//XCUIElementTypeButton[0]',  # an element which does not exist
        'id': None,
        'name': None,
        'class': None,
        'access_id': None,
    }

    with_enabled_prop = {
        'xpath': '//XCUIElementTypeButton[@name="id.autoplay.toggle.button"]',
        'id': None,
        'name': 'id.autoplay.toggle.button',
        'class': None,
        'access_id': 'id.autoplay.toggle.button',
    }

    # wait_for_checkpoint.py
    navbar_home = {
        'xpath': '//XCUIElementTypeButton[@name="id.ui.pivotbar.FEwhat_to_watch.button"]',
        'id': None,
        'name': 'id.ui.pivotbar.FEwhat_to_watch.button',
        'class': None,
        'access_id': 'id.ui.pivotbar.FEwhat_to_watch.button',
    }

    trending_nav = {
        'xpath': '//XCUIElementTypeButton[@name="id.ui.pivotbar.FEtrending.button"]',
        'id': None,
        'name': 'id.ui.pivotbar.FEtrending.button',
        'class': None,
        'access_id': 'id.ui.pivotbar.FEtrending.button',
    }

    library_nav = {
        'xpath': '//XCUIElementTypeButton[@name="id.ui.pivotbar.FElibrary.button"]',
        'id': None,
        'name': 'id.ui.pivotbar.FElibrary.button',
        'class': None,
        'access_id': 'id.ui.pivotbar.FElibrary.button',
    }

    video_player = {
        'xpath': '//XCUIElementTypeOther[@name="Video Player"]',
        'id': None,
        'name': 'Video Player',
        'class': None,
        'access_id': 'Video Player',
    }

    is_elm = {
        'xpath': '//XCUIElementTypeButton[@name="id.ui.navigation.search.button"]',
        'id': None,
        'name': 'id.ui.navigation.search.button',
        'class': None,
        'access_id': 'id.ui.navigation.search.button',
    }

    autoplay_toggle = {
        'xpath': '//XCUIElementTypeButton[@name="id.autoplay.toggle.button"]',
        'id': None,
        'name': 'id.autoplay.toggle.button',
        'class': None,
        'access_id': 'id.autoplay.toggle.button',
    }

    # search image
    search_icon = {
        'xpath': '//XCUIElementTypeButton[@name="id.ui.navigation.search.button"]',
        'id': None,
        'name': 'id.ui.navigation.search.button',
        'class': None,
        'access_id': 'id.ui.navigation.search.button',
    }

    account_icon = {
        'xpath': "//XCUIElementTypeButton[@name='account_panel_button']",
        'id': None,
        'name': 'id.ui.navigation.account.button',
        'class': None,
        'access_id': 'account_panel_button',
    }

    search_txt_box = {
        'xpath': '//XCUIElementTypeSearchField[@name="id.navigation.search.text_field"]',
        'id': None,
        'name': 'id.navigation.search.text_field',
        'class': None,
        'access_id': 'id.navigation.search.text_field',
    }

    search_box_with_text = {
        'xpath': '//XCUIElementTypeSearchField[@name="id.navigation.search.text_field"]',
        'id': None,
        'name': 'id.navigation.search.text_field',
        'class': None,
        'access_id': 'id.navigation.search.text_field',
    }

    download_opt= {
        'xpath': '//XCUIElementTypeButton[@name="Download"]',
        'id': None,
        'name': None,
        'class': None,
        'access_id': None,
    }

    downloaded = {
        'xpath': '//XCUIElementTypeButton[@name="Downloaded"]',
        'id': None,
        'name': None,
        'class': None,
        'access_id': None,
    }

    elem_det = {
        'xpath': '//XCUIElementTypeButton[@name="id.ui.pivotbar.FEwhat_to_watch.button"]',
        'id': None,
        'name': 'id.ui.pivotbar.FEwhat_to_watch.button',
        'class': None,
        'access_id': 'id.ui.pivotbar.FEwhat_to_watch.button',
    }

    # getallattributes
    ytb_logo = {
        'xpath': '//XCUIElementTypeImage[@name="youtube_logo"]',
        'id': None,
        'name': None,
        'class': None,
        'access_id': None,
    }

    read_text = {
        'xpath': '//XCUIElementTypeButton[@name="id.ui.pivotbar.FEwhat_to_watch.button"]',
        'id': None,
        'name': None,
        'class': None,
        'access_id': None,
    }

    read_text_idx ={
            'xpath': '//XCUIElementTypeButton',
            'id': None,
            'name': None,
            'class': None,
            'access_id': None,
    }

    click_tap_idx = {
        'xpath': '//XCUIElementTypeButton',
        'id': None,
        'name': None,
        'class': None,
        'access_id': None,
    }

    elm_idx = {
        'xpath': '//XCUIElementTypeButton',
        'id': None,
        'name': None,
        'class': None,
        'access_id': None,
    }


    # wait_for_checkpoint.py
    navbar_trending = {
        'xpath': '//XCUIElementTypeButton[@name="id.ui.pivotbar.FEtrending.button"]',
        'id': None,
        'name': 'id.ui.pivotbar.FEwhat_to_watch.button',
        'class': None,
        'access_id': 'id.ui.pivotbar.FEwhat_to_watch.button',
    }

    # get_text.py
    ele_without_text = {
        'xpath': '//XCUIElementTypeButton[@name="account_panel_button"]',
        'id': None,
        'name': 'account_panel_button',
        'class': None,
        'access_id': 'account_panel_button',
    }

    non_exist_ele = {
        'xpath': '//XCUIElementTydfsdfOther',
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
        'xpath': '//XCUIElementTypeButton[@name="id.ui.pivotbar.FEtrending.button"]',
        'id': None,
        'name': 'id.ui.pivotbar.FEwhat_to_watch.button',
        'class': None,
        'access_id': 'id.ui.pivotbar.FEwhat_to_watch.button',
    }

    # click_index.py
    click_button = {
        'xpath': '//XCUIElementTypeButton',
        'id': None,
        'name': None,
        'class': None,
        'access_id': None,
    }
    non_clickable = {
        'xpath': '//XCUIElementTypeOther',
        'id': None,
        'name': None,
        'class': None,
        'access_id': None,
    }
    invalid_click = {
        'xpath': '//XCUIElementTydfsdfOther',
        'id': None,
        'name': None,
        'class': None,
        'access_id': None,
    }
    non_visible_click = {
        'xpath': '//XCUIElementTypeOther[@name="id.app.view"]/XCUIElementTypeOther[2]/XCUIElementTypeOther',
        'id': None,
        'name': None,
        'class': None,
        'access_id': None,
    }

    #get_text_index.py
    ele_with_text = {
        'xpath': '//XCUIElementTypeButton[@name="id.ui.pivotbar.FEtrending.button"]',
        'id': None,
        'name': 'id.ui.pivotbar.FEtrending.button',
        'class': None,
        'access_id': 'id.ui.pivotbar.FEtrending.button',
    }
    #send_keys.py
    edit_box = {
        'xpath': '//XCUIElementTypeSearchField[@name="id.navigation.search.text_field"]',
        'id': None,
        'name': 'id.navigation.search.text_field',
        'class': None,
        'access_id': 'id.navigation.search.text_field'
    }
    non_text_field = {
        'xpath': '//XCUIElementTypeButton[@name="account_panel_button"]',
        'id': None,
        'name': 'account_panel_button',
        'class': None,
        'access_id': 'account_panel_button',
    }

    # tap_percent.py cordinates of search icon as percentage
    search_icon_tap_percent = (80, 6)
    # tap_percent.py cordinates of youtube image as percentage
    youtube_img_percent = (8, 6)
    # tap_percent.py cordinates of back icon in search text as percentage
    back_icon_percent = (5, 6)

    # sanity_iselement_tapelement.py - overrides this item in respective configs
    list_iselm = (navbar_home, home, search_icon)
    search_icon_index = 3
    account_icon_index = 4
    index_not_on_page = 115  # TapElement (with index)
    # ==================================================== END VARIABLES =============


    API_PASS = True
    API_FAIL = False

    get_element_count_params = {
        0: ["Mutliple element", API_PASS, getelmcount_multi],
        1: ["Single element", API_PASS, getelmcount_single],
        3: ["No element", API_FAIL, getelmcount_not_exists],
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

    # -------------------------------- TapPercent
    tap_percent_params = {
        0: ["Parameter out of boundary", API_FAIL, config_base.percent_out_of_boundary],
        1: ["Tap on element with Clickable - False, but available on the screen", API_PASS, youtube_img_percent],
        2: ["Tap on lock screen", API_PASS, search_icon_tap_percent],
        3: ["Tap on Clickable element", API_PASS, search_icon_tap_percent],
    }

    is_element_present_params = {
        0: ["Element does not exist on the Page", API_FAIL, autoplay_toggle],
        1: ["For a visible element", API_PASS, is_elm],
        2: ["For an element with 'visible' False", API_FAIL, is_elm ],    #start playback and check for the element

        # 3: ["Element having same ID but differ in index", API_PASS], # this will pass if the element is available
    }

    is_selected_params = {
        0: ["For an element without 'Selected' property", API_FAIL, without_selected_prop],
        1: ["Element with 'Selected' property", API_PASS, with_selected_prop]
    }

    is_enabled_params = {
        0: ["For an element without 'Enabled' property", API_FAIL, without_enabled_prop],
        1: ["Element with 'Enabled' property", API_PASS, with_enabled_prop]
    }

    # -------------------------------- WaitForElement
    wait_for_element_params = {
        0: ["Invalid Params: TimeToWait=0, element available", API_FAIL,
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


    # -------------------------------- Swipe
    swipe_params = {
        0: ["Wrong coordinates", API_FAIL, C_SWIPE_WRONG],
        # 1: ["Out of boundary coordinates", API_FAIL, C_SWIPE_WRONG],
        2: ["Top-down swipe", API_PASS, C_TOP_DOWN_SWIPE],
        3: ["Bottom-up swipe", API_PASS, C_BOTTOM_UP_SWIPE],
        4: ["Right-left swipe", API_PASS, C_RIGHT_LEFT_SWIPE],
        5: ["Left-right swipe", API_PASS, C_LEFT_RIGHT_SWIPE],
        6: ["Swipe on a small area", API_PASS, C_SMALL_AREA_SWIPE],
        7: ["Both coordinates are same", API_PASS, C_SAME_SWIPE_CORD],
        8: ["Swipe until page ends", API_PASS, C_BOTTOM_UP_SWIPE],
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
            "Valid parameters, max region and algorithm: CcorrNormed", API_PASS, (config_base.imageSearchSingleOccurance,
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

    # -------------------------------- TapElement
    tap_element_params = {
        0: ["Element does not exist on the Page", API_FAIL, autoplay_toggle],
        1: ["For a visible element", API_PASS, is_elm],
        2: ["For an element with 'visible' False", API_PASS, is_elm],   # when search text box is visible
        3: ["Tap on Non-clickable element", API_PASS, account_icon],
    }

    # -------------------------------- TapElement (with index)
    tap_element_with_index_params = {
        0: ["For a visible element", API_PASS, (elm_idx, search_icon_index)],
        1: ["Valid element which does not exist on the Page", API_FAIL, (elm_idx, index_not_on_page)],
        2: ["For an element with 'visible' False", API_FAIL, (elm_idx, index_not_on_page)],  # when search text box is visible
        3: ["Tap on Non-clickable element", API_PASS, (elm_idx, account_icon_index)],
        4: ["Element with wrong index value", API_FAIL, (elm_idx, -1)]
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
        3: ["Invalid: on an element with visible property False, but available on the screen", API_FAIL, search_txt_box],
    }
    get_text_params = {
        0: ["Element without text", "", ele_without_text],
        1: ["Non existing element", "", non_exist_ele],
        2: ["Element with lengthy text", "", lengthy_text],
        3: ["Two elements with same Id but differs in index", "", ele_with_dif_ind]
    }

    click_index_params = {
        0: ["Invalid: Index outside boundary", API_FAIL, (click_button, 100)],
        1: ["Invalid: on a non click-able element", API_FAIL, (non_clickable, 1)],
        2: ["Valid: on a click-able element", API_PASS, (click_button, 1)],
        3: ["Invalid: Invalid element value", API_FAIL, (invalid_click, 1)],
        4: ["Invalid: Invalid index values", API_FAIL, (click_button, -1)],
        5: ["Invalid: on an element with visible property False, but available on the screen", API_FAIL, (non_visible_click, 1)]
    }
    get_text_index_params = {
        0: ["Invalid: Index outside boundary", "", (ele_with_text, 555)],
        1: ["Invalid: Non existing element", "", (non_exist_ele, 1)],
        2: ["Valid: Element without text", API_PASS, (ele_without_text, 1)],
        3: ["Valid: Element with lengthy text", API_PASS, (lengthy_text, 1)],
        4: ["Invalid: Negative value for index", "", (ele_with_text, -1)]
    }
    send_keys_params = {
        0: ["Valid: send to edit box", API_PASS, edit_box, config_base.search_text],
        1: ["Valid: Send lengthy string", API_PASS, edit_box, config_base.LENGTHY_NAME],
        2: ["Valid: Send spl chars & nums", API_PASS, edit_box, config_base.MSG_WITH_SPLCHARS],
        3: ["Invalid: Send to non-text field", API_FAIL, non_text_field, config_base.search_text],
    }

    tap_params = {
        0: ["Invalid: Wrong/unavailable coordinates", API_FAIL, C_WRONG_COORDS],
        # seems like click works regradless of the element property, so given PASS for the api
        1: ["Valid: Tap on anywhere on an element", API_PASS, C_TAP_PLAYBACK],
    }


    # ------------------------------------ GetScreenTransitions
    # same as detect_motion coords

    HPA_X = 176
    HPA_Y = 99
    HPA_W = 439
    HPA_H = 251
    HPA_SENS = 3
    HPA_DUR = 60