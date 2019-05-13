#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Author          :   Arathy P S
# Date            :   14-03-2018
# FE Version      :   5.0.9.4
# Description     :   This is a Library for config parameters
#''''''''''''''''''''AUTO GENERATED CODE - DO NOT MODIFY''''''''''''''''''''

platform_name = "iOS"

app_name = {
    "youtube" : "com.google.ios.youtube",
    "skygo" : "com.bskyb.skygo",
}

# package = {
#     "youtube" : "com.google.android.youtube",
#     "skygo" : "com.bskyb.skygo",
# }

activity = {
    "youtube" : "com.google.android.youtube.HomeActivity",
    "skygo" : "com.bskyb.uma.app.bootstrap.BootstrapActivity",
}


# app_name = "com.google.ios.youtube"#"com.bskyb.nowtv.intl.internal.gb"
app_package = "com.bskyb.nowtv.beta"
app_activity = "com.bskyb.nowtv.ui.activities.LaunchActivity"
app_home = "//XCUIElementTypeApplication[@name='YouTube']"
APP_TAP_ID = "//XCUIElementTypeButton[@name='id.ui.navigation.search.button']"#"element details to TAP"
APP_TAP_INDEX = 1
APP_GETTEXT = "//XCUIElementTypeButton[@name='id.ui.pivotbar.FEtrending.button']"#"gettext"
APP_IS_PRESENT = "//XCUIElementTypeButton[@name='account_panel_button']"#"isElementPresent index"
app_click = "//XCUIElementTypeButton[@name='id.ui.navigation.search.button']"
app_sendkeys = "//XCUIElementTypeOther[@name='Top View']/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]"
GETTEXT_XPath="//XCUIElementTypeOther[@name='Top View']/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]"
GETTEXT_index = 2#"gettext index"
#GETTEXT CLICK
click_gettext="//XCUIElementTypeButton[@name='id.ui.pivotbar.FEtrending.button']"
ELEMENT_COUNT_ID = "//XCUIElementTypeButton[@name='account_panel_button']"



# ios_app_name = "com.google.ios.youtube"#"com.bskyb.nowtv.intl.internal.gb"
# ios_app_package = "com.bskyb.nowtv.beta"
# ios_app_activity = "com.bskyb.nowtv.ui.activities.LaunchActivity"
# ios_APP_HOME = "//XCUIElementTypeApplication[@name='YouTube']"
# ios_APP_TAP_ID = "//XCUIElementTypeButton[@name='id.ui.navigation.search.button']"#"element details to TAP"
# ios_APP_TAP_INDEX = 1
# ios_APP_GETTEXT = "//XCUIElementTypeButton[@name='id.ui.pivotbar.FEtrending.button']"#"gettext"
# ios_APP_IS_PRESENT = "//XCUIElementTypeButton[@name='account_panel_button']"#"isElementPresent index"
# ios_app_click = "//XCUIElementTypeButton[@name='id.ui.navigation.search.button']"
# ios_app_sendkeys = "//XCUIElementTypeOther[@name='Top View']/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]"
# ios_APP_GETTEXT_XPath="//XCUIElementTypeOther[@name='Top View']/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]"
# ios_APP_GETTEXT_index = 2#"gettext index"
# #GETTEXT CLICK
# ios_app_click_gettext="//XCUIElementTypeButton[@name='id.ui.pivotbar.FEtrending.button']"
# ios_ELEMENT_COUNT_ID = "//XCUIElementTypeButton[@name='account_panel_button']"

#XPath for ElementCount, Height, Width API Script
ELEMENT_XPATH_COUNT_HEIGHT_WIDTH="//XCUIElementTypeButton[@name='45']"

#XPath for Click API Script
ELEMENT_XPATH_CLICK="//XCUIElementTypeButton[@name='account_panel_button']"

#XPath for Click API with index Script
X_CLICK_INDEX="//XCUIElementTypeButton[@name='id.ui.navigation.search.button']"

#XPath for SendKeys API Script
X_SENDKEYS_EDIT_BOX="//XCUIElementTypeSearchField[@name='id.navigation.search.text_field']"#"//XCUIElementTypeSearchField[@name='id.navigation.search.text_field']/XCUIElementTypeSearchField"

#XPath for IsEnabled and IsSelected APIs
ELEMENT_XPATH_ISSELECTED="//XCUIElementTypeButton[@name='id.ui.pivotbar.FEtrending.button']"
ELEMENT_XPATH_ISENABLED="//XCUIElementTypeButton[@name='id.ui.navigation.search.button']"

#XPath for youtube_launch_video function
ELEMENT_XPATH_CLICK_ENTER="//XCUIElementTypeButton[@name='Search']"

#XPath for GetAttribute API Script
ELEMENT_XPATH_GETATTRIBUTE="//XCUIElementTypeImage[@name='youtube_logo']"

#XPath for GetAllAttributeValues API Script
ELEMENT_XPATH_GETALLATTRIBUTEVALUES="//XCUIElementTypeImage[@name='youtube_logo']"

#XPath for ClearText API
X_CLEARTEXT="//XCUIElementTypeSearchField[@name='id.navigation.search.text_field']"#"//XCUIElementTypeSearchField[@name='id.navigation.search.text_field']/XCUIElementTypeSearchField"

#for HandleAlertMessage API
ios_app_name_youTube = "com.google.ios.youtube"
ios_youTube_home = "//XCUIElementTypeApplication[@name='YouTube']"
youTube_download_option = "//XCUIElementTypeButton[@name='Download']"

# ***************   to share    *********************

BUTTON_WITH_INDEX = "//XCUIElementTypeOther[@name='Top View']/XCUIElementTypeOther[1]/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeButton[{}]"
# GetAllChildAttributeValues
GET_ALL_CHILD_ELM = "XCUIElementTypeButton"
ACCOUNT_BUTTON = "//XCUIElementTypeButton[@name='id.ui.navigation.search.button']"

CAPTUREIMG_INFO = (50,50,15,5,"CAP_IMG", 90, 1)

# capture_image > whole frame capture
cap_im_max_coord = (0, 0, 768, 1024)

# update the coordinate for getOCRText for iOS device
c_get_ocr_text = (149, 1175, 91, 29)

ELEMENT_CLASSNAME_CLICK_INDEX = "//XCUIElementTypeOther[@name='Top View']/XCUIElementTypeOther[1]/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeButton"
search_button_index = 2

#c_tap_for_yt_playback = (285, 691)
c_tap_for_yt_playback = (300, 1000)

# -------   skygo   elements
# update for iphone

hamburger = "hamburger"
settings = "Settings"
id_allow_streaming = "com.bskyb.skygo:id/allowStreamingOverMobileDataCheckbox"
id_notify_streaming = "com.bskyb.skygo:id/notifyStreamingOverMobileDataCheckbox"
x_settings_network_pref = "//android.widget.TextView[@text='Network Preferences']"

# swipe coordinates
c_v_swipe = (700, 10, 100, 600)
c_h_swipe = (1029, 479, 20, 479)
c_press_move = (0, 10, 0, 700)