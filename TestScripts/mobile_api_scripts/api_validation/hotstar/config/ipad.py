# ''''''''''''''''''''''''''' CONFIG FILE - IPad '''''''''''''''''''''''''''''''''''''''''
# Author            : Lincy Robert
# Date              : 02-04-2019
# Script Version    : 1.0
# Modification details:
# ''''''''''''''''''''''''''' CONFIG FILE - IPad - END '''''''''''''''''''''''''''''''''

# imports
from config.configbase import ConfigBase


class IPad(ConfigBase):
    """
        This contains config variable specific to iPhones.
        This inherits all variables in ConfigBase class
    """

    # ==================================================== COMMON
    # ================================================================================
    # zee5
    package = {
        # "youtube": "com.google.ios.youtube",
        # "skygo": "com.bskyb.skygo",
        "zee5": "com.zeeTV.DIDS4",
    }

    # zee5
    activity = {
        # "youtube": "com.google.ios.youtube.HomeActivity",
        # "skygo": "com.bskyb.uma.app.bootstrap.BootstrapActivity",
        "zee5": "xxxxxxxxxxxxxxxxxxxx",
    }

    app_name = {
        "zee5": "com.zeeTV.DIDS4",
        # "skygo": "com.bskyb.skygo",
    }

    platform = "iOS"
    # ==================================================== END COMMON =============

    # ==================================================== CHECKPOINT VARIABLES =============
    # zee5
    zee5_home_menu = "aut_zee_home_menu"
    # ==================================================== END CHECKPOINT VARIABLES =============

    # ==================================================== VARIABLES =============
    # app element data
    # App home element
    home = {
        'xpath': "//android.widget.ImageView[@content-desc='YouTube']",
        'id': 'com.google.android.youtube:id/youtube_logo',
        'name': None,
        'class': None,
        'access_id': None,
    }

    # ==================================================== COORDINATE VARIABLES =============
    # zee5
    # zee5_tap_get_ocr_text.py
    home_in_home_menu = (589, 736)  # tap coordinates
    # ==================================================== END COORDINATE VARIABLES =============

    # ==================================================== API PARAMETER VARIABLES =============
    # getOCRText params for HOME string in top left corner after selecting HOME option from the main menu
    home_launched = (62, 235, 55, 20, '', 'eng')
    # ==================================================== END API PARAMETER VARIABLES =============

    # ==================================================== STRING VARIABLES =============
    # HOME string in top left corner after selecting HOME option from the main menu
    home_string = 'HOME'
    # ==================================================== END STRING VARIABLES =============

    API_PASS = True
    API_FAIL = False
    # ==================================================== END VARIABLES =============