# ''''''''''''''''''''''''''' CONFIG FILE - ANDROID '''''''''''''''''''''''''''''''''''''''''
# Author            : Lincy Robert
# Date              : 02-04-2019
# Script Version    : 1.0
# Modification details:
# ''''''''''''''''''''''''''' CONFIG FILE - ANDROID - END '''''''''''''''''''''''''''''''''

# imports
from config.configbase import ConfigBase


class AndroidPhone(ConfigBase):
    """
    This contains config variable specific to android phones.
    This inherits all variables in ConfigBase class
    """


    # ==================================================== COMMON
    # ================================================================================
    # zee5
    package = {
        # "youtube": "com.google.android.youtube",
        # "skygo": "com.bskyb.skygo",
        "zee5": "com.graymatrix.did",
    }

    # zee5
    activity = {
        # "youtube": "com.google.android.youtube.HomeActivity",
        # "skygo": "com.bskyb.uma.app.bootstrap.BootstrapActivity",
        "zee5": "com.graymatrix.did.splash.SplashActivity",
    }

    platform = "Android"
    # ==================================================== END COMMON =============

    # ==================================================== CHECKPOINT VARIABLES =============
    # zee5
    zee5_home_menu = "aut_zee_home_menu"
    # ==================================================== END CHECKPOINT VARIABLES =============

    # ==================================================== VARIABLES =============
    # app element data
    # App home element - zee5 logo
    home = {
        'xpath': '//android.widget.ImageView[@id="com.graymatrix.did:id/app_logo"]',
        'id' : 'com.graymatrix.did:id/app_logo',
        'name'  : None,
        'class' : None,
        'access_id': None,
    }


    home_button = {
        'xpath': '//android.widget.Button[@text="HOME"]',
        'id' : None,
        'name': None,
        'class' : None,
        'access_id' : None,

    }


    search_icon = {
    'xpath' : '//android.widget.ImageView[@id="com.graymatrix.did:id/action_bar_search"]',
    'id': 'com.graymatrix.did:id/action_bar_search',
    'name': None,
    'class': None,
    'access_id': None,

    }

    child_attr = {
        'xpath': "//android.widget.TextView[contains(@text,'Most Watched')]",
        'id': None,
        'name': None,
        'class': None,
        'access_id': None,

    }

    click_tap_idx = {
    'xpath' : '//android.widget.ImageView',
    'id': None,
    'name': None,
    'class': None,
    'access_id': None,

    }

    gettext_idx =  {
    'xpath' : '//android.widget.TextView',
    'id': None,
    'name': None,
    'class': None,
    'access_id': None,

    }


    search_box = {
        'xpath': '//android.widget.EditText[@id="com.graymatrix.did:id/action_bar_search"]',
        'id': 'com.graymatrix.did:id/text1',
        'name': None,
        'class': None,
        'access_id': None,
    }

    # need to add the below items to iphone, ipad configs
    screen_title = {
        'xpath': '//android.widget.TextView[@id="com.graymatrix.did:id/filter_view_screen_title"]',
        'id': 'com.graymatrix.did:id/filter_view_screen_title',
        'name': None,
        'class': None,
        'access_id': None,

    }

    shows_view_all = {
        'xpath': '//android.widget.TextView[@id="com.graymatrix.did:id/view_all"]',
        'id': 'com.graymatrix.did:id/view_all',
        'name': None,
        'class': None,
        'access_id': None,
    }

    elm_attr = {
        'xpath': '//android.widget.TextView[@id="com.graymatrix.did:id/view_all"]',
        'id': 'com.graymatrix.did:id/view_all',
        'name': None,
        'class': None,
        'access_id': None,
    }

    filter_icon = {
        'xpath': '//android.widget.ImageView[@id="com.graymatrix.did:id/filter_icon"]',
        'id': 'com.graymatrix.did:id/filter_icon',
        'name': None,
        'class': None,
        'access_id': None,

    }

    # filter for different movie genres
    checkbx_filter =  {
        'xpath': '//android.widget.CheckBox[@text="Animation"]',
        #use like, checkbx_filter['xpath'].format("Animation"), or checkbx_filter['xpath'].format("Action"), or checkbx_filter['xpath'].format("Comedy")
        'id': None,
        'name': None,
        'class': None,
        'access_id': None,

    }

    filter_apply_button = {
        'xpath': '//android.widget.Button[@id="com.graymatrix.did:id/applybtn"]',
        'id': 'com.graymatrix.did:id/applybtn',
        'name': None,
        'class': None,
        'access_id': None,

    }

    filter_reset_button = {
        'xpath': '//android.widget.Button[@id="com.graymatrix.did:id/resetbtn"]',
        'id': 'com.graymatrix.did:id/resetbtn',
        'name': None,
        'class': None,
        'access_id': None,

    }

    exit_from_app_no = {
        'xpath': '//android.widget.Button[contains(@text,"Next")]',
        'id': None,
        'name': None,
        'class': None,
        'access_id': None,

    }

    home_menu = {
        'xpath': "//android.widget.LinearLayout//android.widget.RelativeLayout/android.widget.TextView[contains(@text,'HOME')]",
        'id': None,
        'name': None,
        'class': None,
        'access_id': None,

    }

    list_iselm = (home_menu, home, search_icon)

    # ==================================================== COORDINATE VARIABLES =============
    c_tap_search_result = (199,489)
    # ==================================================== END COORDINATE VARIABLES =============

    # ==================================================== API PARAMETER VARIABLES =============

    # ==================================================== END API PARAMETER VARIABLES =============

    # ==================================================== STRING VARIABLES =============

    # ==================================================== END STRING VARIABLES =============

    # ==================================================== END VARIABLES =============
