#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Author          :   Arathy P S
# Date            :   14-03-2018
# FE Version      :   5.0.9.4
# Description     :   This is a Library for config parameters
#''''''''''''''''''''AUTO GENERATED CODE - DO NOT MODIFY''''''''''''''''''''

adb_info = {
            "GetAdbAPIVersion": 26,
            "GetAdbVersion": 8.0,
            "GetApkVersion": 8.0,
}

platform_name = "Android"

package = {
    "youtube" : "com.google.android.youtube",
    "skygo" : "com.bskyb.skygo",
}

activity = {
    "youtube" : "com.google.android.youtube.HomeActivity",
    "skygo" : "com.bskyb.uma.app.bootstrap.BootstrapActivity",
}


app_package = "com.google.android.youtube"
app_activity = "com.google.android.youtube.HomeActivity"
app_home = "//android.widget.ImageView[@content-desc='YouTube']"#"com.google.android.youtube:id/youtube_logo"

APP_TAP_ID = "//android.widget.ImageView[@content-desc='Account']"#"com.google.android.youtube:id/thumbnail"

android_APP_TAP_INDEX = 0
'get text for Home button'
APP_GETTEXT = "//android.widget.TextView[@text='Trending']"

GETTEXT_index = 0
android_APP_IS_PRESENT = "//android.widget.ImageView[@content-desc='Account']"#"com.google.android.youtube:id/image"#
app_click = "//android.widget.ImageView[@content-desc='Search']"#"android.widget.ImageView"
app_sendkeys = "//android.widget.EditText[@text='Search YouTube']"#"com.google.android.youtube:id/search_edit_text"
GETTEXT_XPath="//android.widget.EditText[@text='Search YouTube']"
#GetText_Click
click_gettext="//android.widget.ImageView[@content-desc='Search']"

ELEMENT_COUNT_ID = "//android.widget.ImageView[@package='com.google.android.youtube']"#"android.widget.ImageView"

#constant for Click API Script
ELEMENT_ID_CLICK="com.google.android.youtube:id/mobile_topbar_avatar"
ELEMENT_XPATH_CLICK="//android.widget.ImageView[@content-desc='Account']"

#constants for Click API with index Script
ELEMENT_CLASSNAME_CLICK_INDEX="android.widget.ImageView"
X_CLICK_INDEX="//android.widget.ImageView[@content-desc='Search']"

#constant for SendKeys API Script
ELEMENT_ID_SENDKEYS="com.google.android.youtube:id/search_edit_text"
X_SENDKEYS_EDIT_BOX="//android.widget.EditText[@text='Search YouTube']"

#constants for ElementCount, Height, Width API Script
ELEMENT_CLASSNAME_ELEMENTCOUNT_HEIGHT_WIDTH_ANDROID="android.widget.ImageView"#for android
ELEMENT_XPATH_COUNT_HEIGHT_WIDTH="//android.widget.ImageView[@content-desc='Video']"

#constants for ClearText API
ID_CLEARTEXT="com.google.android.youtube:id/search_edit_text"
X_CLEARTEXT="//android.widget.EditText[@text='Master Chef Australia']"

#constants for IsEnabled and IsSelected APIs
ELEMENT_CLASSNAME_ISSELECTED="android.widget.Button"
ELEMENT_CLASSNAME_ISENABLED="android.view.View" #/ android.widget.ImageView/"
ELEMENT_XPATH_ISSELECTED="//android.widget.Button[@content-desc='Trending']"
ELEMENT_XPATH_ISENABLED="//android.widget.ImageView[@content-desc='Search']"

#constants for PressAndMove API Script
ELEMENT_CLASSNAME_CLICK_INDEX="android.widget.ImageView"
search_button_index = 2

#constants for GetAllAttributeValues API Script
ELEMENT_ID_GETALLATTRIBUTEVALUES="com.google.android.youtube:id/mobile_topbar_avatar"
ELEMENT_XPATH_GETALLATTRIBUTEVALUES="//android.widget.ImageView[@content-desc='YouTube']"

#constants for GetAttribute API Script
ELEMENT_CLASSNAME_GETATTRIBUTE="com.google.android.youtube:id/mobile_topbar_avatar"
ELEMENT_XPATH_GETATTRIBUTE="//android.widget.ImageView[@content-desc='YouTube']"

#constant for SetDefaultWaitTime  API Script
ELEMENT_ID_CLICK="com.google.android.youtube:id/mobile_topbar_avatar"

HOME_TEXT_BOTTOM_NAV = "//android.widget.TextView[@text='Home']"

# ***************   to share    *********************

BUTTON_WITH_INDEX = "//android.widget.ImageView[@content-desc='Search']"
# GetAllChildAttributeValues
GET_ALL_CHILD_ELM = "//android.widget.ImageView[@content-desc='Search']"

youTube_download_option = "//android.widget.Button[@name='Download']"

ACCOUNT_BUTTON = "//android.widget.ImageView[@content-desc='Account']"
CAPTUREIMG_INFO = (50,50,15,5,"CAP_IMG", 90, 0)


# capture_image > whole frame capture
cap_im_max_coord = (0, 0, 720, 1280)

c_get_ocr_text = (149, 1175, 91, 29)

c_tap_for_yt_playback = (285, 691)


# -------   skygo   elements

hamburger = "com.bskyb.skygo:id/nav_panel_drawer_icon"
settings = "//android.widget.TextView[@text='Settings']"
id_allow_streaming = "com.bskyb.skygo:id/allowStreamingOverMobileDataCheckbox"
id_notify_streaming = "com.bskyb.skygo:id/notifyStreamingOverMobileDataCheckbox"
x_settings_network_pref = "//android.widget.TextView[@text='Network Preferences']"

skygo_home = "com.bskyb.skygo:id/nav_panel_drawer_icon"

# swipe coordinates
c_v_swipe = (700, 10, 100, 600)
c_h_swipe = (0, 591, 281, 600)
c_press_move = (0, 10, 0, 700)

# -------   getOCRText for different devices

get_ocr_text_coordinates_dict = {"SamsungGalaxyJ7_21435_7_0":(38, 1243, 71, 33), "Samsung_galaxyJ7_a445_7_0":(38, 1243, 71, 33), "OnePlus5T":(31, 1179, 72, 20), "MiA1712":(38, 1243, 71, 33), "iPhone8Plus_11_0":(43, 1184, 65, 26), "IpadFE":(38, 1243, 71, 33),
                                 "iPhone7_11_0_3":(38, 1243, 71, 33), "iPhone6":(38, 1243, 71, 33), "iPhone6sPlus":(38, 1243, 71, 33)}