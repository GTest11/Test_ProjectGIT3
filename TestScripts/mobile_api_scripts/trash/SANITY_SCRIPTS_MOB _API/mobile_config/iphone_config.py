

platform_name = "iOS"

app_name = {
    "youtube" : "com.google.ios.youtube",
    "skygo" : "com.bskyb.skygo",
}

dut_type = "iPhone"

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
GETTEXT_XPath="//XCUIElementTypeOther[@name='Top View']/XCUIElementTypeOther[1]/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeButton"
GETTEXT_index = 2
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


# back to home youtube
x_back_to_home = "//XCUIElementTypeButton[@name='id.ui.browse.back.button']"

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
HOME_TEXT_BOTTOM_NAV = "//XCUIElementTypeButton[@name='id.ui.pivotbar.FEhome.button']"



CAPTUREIMG_INFO = (50,50,15,5,"CAP_IMG", 90, 1)

# capture_image > whole frame capture
cap_im_max_coord = (0, 0, 768, 1024)

# update the coordinate for getOCRText for iOS device
c_get_ocr_text = (149, 1175, 91, 29)

ELEMENT_CLASSNAME_CLICK_INDEX = "//XCUIElementTypeOther[@name='Top View']/XCUIElementTypeOther[1]/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeButton"
search_button_index = 2

c_tap_for_yt_playback = (285, 313)



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

skygo_home = "Home"

# -------   getOCRText for different devices

get_ocr_text_coordinates_dict = {"SamsungGalaxyJ7_21435_7_0":(38, 1243, 71, 33), "Samsung_galaxyJ7_a445_7_0":(38, 1243, 71, 33), "OnePlus5T":(31, 1179, 72, 20), "MiA1712":(38, 1243, 71, 33), "iPhone8Plus_11_0":(43, 1184, 65, 26), "IpadFE":(312, 611, 50, 15),
                                 "iPhone7_11_0_3":(38, 1243, 71, 33), "iPhone6":(38, 1243, 71, 33), "iPhone6sPlus":(38, 1243, 71, 33)}