# ''''''''''''''''''''''''''' CONFIG FILE - iPAD '''''''''''''''''''''''''''''''''''''''''
# Author            : Shameena HA
# Date              :   26-11-2018
# Script Version     : 1.0
# Modification details:
#
# ''''''''''''''''''''''''''' CONFIG FILE - iPAD - END '''''''''''''''''''''''''''''''''


from config.config_base import config_base


class iPad(config_base):
    '''
        This contains config variable specific to iPad devices.
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



    # ==================================================== VARIABLES
    # ================================================================================
    home = {
        'xpath': "//XCUIElementTypeApplication[@name='YouTube']",
        'id': None,
        'name': None,
        'class': None,
        'access_id': None,
    }

    # ==================================================== END VARIABLES =============