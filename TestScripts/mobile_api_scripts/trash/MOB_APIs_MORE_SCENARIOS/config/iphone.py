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
        'xpath': '//android.widget.ImageView',
        'id': None,
        'name': None,
        'class': 'android.widget.ImageView',
        'access_id': None
    }

    getelmcount_single = {
        'xpath': '//android.widget.ImageView[@content-desc="Video"]',
        'id': None,
        'name': None,
        'class': None,
        'access_id': None
    }

    getelmcount_not_exists = {
        'xpath': '//android.widget.ImageView[0]',  # an element which does not exist
        'id': None,
        'name': None,
        'class': None,
        'access_id': None
    }

    # ==================================================== END VARIABLES =============


    API_PASS = True
    API_FAIL = False

    get_element_count_params = {
        0: ["Mutliple element", API_PASS, getelmcount_multi],
        1: ["Single element", API_PASS, getelmcount_single],
        3: ["No element", API_FAIL, getelmcount_not_exists],
    }