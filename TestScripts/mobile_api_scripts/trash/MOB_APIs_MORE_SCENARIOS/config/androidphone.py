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



    # ==================================================== VARIABLES
    # ================================================================================

    # App home element
    home = {
        'xpath' : "//android.widget.ImageView[@content-desc='YouTube']",
        'id'    : None,
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
        'xpath': '//android.widget.ImageView[0]',  # an element which does not exist
        'id': None,
        'name': None,
        'class': None,
        'access_id': None
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
        'xpath': '//android.widget.ImageView[0]',  # an element which does not exist
        'id': None,
        'name': None,
        'class': None,
        'access_id': None
    }


    # ==================================================== END VARIABLES =============

    # class test_params(config_base):
    API_PASS = True
    API_FAIL = False

    get_element_count_params = {
        0: ["Mutliple element", API_PASS, getelmcount_multi],
        1: ["Single element", API_PASS, getelmcount_single],
        3: ["No element", API_FAIL, getelmcount_not_exists],
    }

    is_selected_params = {
        0: ["For an element without 'Selected' property", API_FAIL, without_selected_prop],
        1: ["Element with 'Selected' property", API_PASS, with_selected_prop]
    }

    is_enabled_params = {
        0: ["For an element without 'Enabled' property", API_FAIL, without_selected_prop],
        1: ["Element with 'Enabled' property", API_PASS, with_selected_prop]
    }