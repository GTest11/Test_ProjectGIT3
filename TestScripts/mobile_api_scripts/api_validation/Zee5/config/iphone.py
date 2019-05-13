# ''''''''''''''''''''''''''' CONFIG FILE - IPhone '''''''''''''''''''''''''''''''''''''''''
# Author            : Lincy Robert
# Date              : 02-04-2019
# Script Version    : 1.0
# Modification details:
# ''''''''''''''''''''''''''' CONFIG FILE - IPhone - END '''''''''''''''''''''''''''''''''

# imports
from config.configbase import ConfigBase


class IPhone(ConfigBase):
    """
        This contains config variable specific to iPhones.
        This inherits all variables in ConfigBase class
    """

    # ==================================================== COMMON
    # ================================================================================
    # zee5

    app_name = {
        "zee5": "com.zeeTV.DIDS4",
        # "skygo": "com.bskyb.skygo",
    }

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

    platform = "iOS"
    # ==================================================== END COMMON =============

    # ==================================================== CHECKPOINT VARIABLES =============
    # zee5
    zee5_home_menu = "aut_zee_home_menu"
    # ==================================================== END CHECKPOINT VARIABLES =============

    # ==================================================== VARIABLES =============
    # app element data
    # App home element
    home = {    # currently updating with Search icon info
        'xpath': "//XCUIElementTypeNavigationBar/XCUIElementTypeButton",
        'id': None,
        'name': None,
        'class': None,
        'access_id': None,
    }

    login_via_mobile_number = {
        'xpath': '//XCUIElementTypeStaticText[@name="Login via Mobile Number"]',
        'id': None,
        'class': None,
        'access_id': None,

    }

    login_button = {
        'xpath': '//XCUIElementTypeButton[@name="LOGIN"]',
        'id': None,
        'name' : 'LOGIN',
        'class': None,
        'access_id': 'LOGIN',

    }

    search_icon = {
        'xpath': "//XCUIElementTypeNavigationBar/XCUIElementTypeButton",
        'id': None,
        'class': None,
        'access_id': None,

    }

    search_box = {
        'xpath': '//android.widget.EditText[@id="com.graymatrix.did:id/action_bar_search"]',
        'id': 'com.graymatrix.did:id/text1',
        'class': None,
        'access_id': None,
    }

    home_button = {
        'xpath': '//XCUIElementTypeButton[@name="TV SHOWS"]',
        'id': None,
        'name' : 'TV SHOWS',
        'class': None,
        'access_id': 'TV SHOWS',

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