"""
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Author          :     Arathy P S
# Date            :     14-03-2018
# Script Version  :     01
# Description     :     This is a Library of constants values used in script execution
''''''''''''''''''''AUTO GENERATED CODE - DO NOT MODIFY''''''''''''''''''''
"""

BUILD_NO = '5.1.0.4'

TAP_X = 241
TAP_Y = 370
ios_expected_str = "masterchef australia"
android_expected_str = "masterchef australia"
android_expected_str_index = "Search YouTube"
ios_expected_str_index = "Trending"
android_expected_str_gettext = "Inbox"
ios_expected_str_gettext = "Trending"
TAP_Y_PERCENT = 24
TAP_X_PERCENT = 37
Motion_AREA_x = 10
Motion_AREA_y = 80
Motion_AREA_w = 500
Motion_AREA_h = 200

# Timeout in seconds until which the function has to wait before returning
WAIT_TIME = 15

# Time in seconds to wait before frame comparison starts.
# This value is used to skip the initial comparison if the expected time is too high.
INIT_DELAY = 1

# duration for frame capture in seconds
FRAME_DURATION = 20

# Time in seconds to wait between comparisons
WAIT_GAP = 1

# In PIXEL_BASED comparison pixel tolerance and RGB tolerance separated by a semicolon.
# For example, if pixel tolerance is 15 and RGB tolerance is 10, use 15;10.
TOLERANCE = "15"

#Algorithm for image comparison. Possible values are 1 and 2 PIXEL_BASED = 1 and RMSE = 2
ALGORITHM = 2

"Jpeg quality for capture image API"
jpegQuality = 90

# Whether to overwrite existing image in the same name or not
over_write_action = 0

app_home_checkpoint = "Mobile_YouTube_Home"
app_close_checkpoint = "app_close_YouTube"

app_double_tap_screen = "checkpoint name"

propertyName = ["cube_controller_ip", "cube_controller_port","cube_client_ip","cube_device_type",
                "cube_device_version", "cube_device_platform"]

youtube_search_index = 0
nowtv_search_index = ''

# attribute count
COUNT = 15

#constants for CaptureImage API
JPEGQUALITY = 100 #1-100
OVERWRITEACTION = 2

#constants for ImageMatch API
ALGORITHM=2 #PIXEL_BASED = 1 and RMSE = 2
TOLERANCE=13

#constant for Click API Script
ELEMENT_ID_CLICK="com.google.android.youtube:id/mobile_topbar_avatar"
CHKPNT_CLICK="CHKPNT_CLICK"


#constants for Click API with index Script
ELEMENT_CLASSNAME_CLICK_INDEX="android.widget.ImageView"

CLICK_INDEX=0
CLICK_INDEX_DELAY=5
CLICK_DELAY =5
CHKPNT_CLICK_INDEX="CHKPNT_CLICK_INDEX"
CHKPNT_CLICK_INDEX_SENDKEYS="CHKPNT_CLICK_INDEX_SENDKEYS"
CHKPNT_CLICK_INDEX_SENDANDROIDKEYCODE="CHKPNT_CLICK_INDEX_SENDANDROIDKEYCODE"

#constant for SendAndroidKeyCode API Script
KEYCODE_HOME="Keycode_HOME"
KEYCODE_ENTER="Keycode_ENTER"
CHKPNT_SENDANDROIDKEYCODE_ENTER="CHKPNT_SENDANDROIDKEYCODE_ENTER"

#constant for SendKeys API Script
ELEMENT_ID_SENDKEYS="com.google.android.youtube:id/search_edit_text"
KEYS="Master Chef Australia"


#constant for Install API Script
APP_PATH="/Users/falconeyemac/Documents/Apk/WhatsApp.apk"
APP_PACKAGE_NAME="com.whatsapp"#enter the app package name of the installing app here
INVALID_APP_PATH="/Users/falconeyemac/Documents/FCPE/WhatsApp1.apk"
INVALID_APP_PACKAGE_NAME="app package name"#enter an invalid app package name here
CHKPNT_INSTALL="checkpoint name"
CHKPNT_CLICK_INSTALL="CHKPNT_CLICK_INSTALL"
ELEMENT_CLASSNAME_CLICK_INSTALL="android.view.ViewGroup"#"android.widget.ImageView"
CHKPNT_INSTALL_WHATSAPP="CHKPNT_INSTALL_WHATSAPP"

#constant for Lock_Unlock API Script
CHKPNT_LOCK="CHKPNT_LOCK"
CHKPNT_UNLOCK="CHKPNT_UNLOCK"
TIME_TO_WAIT_LOCK_UNLOCK=15 #wait_for_checkpoint function for Lock and Unlock
INITIAL_DELAY_LOCK_UNLOCK=0 #wait_for_checkpoint function for Lock and Unlock
LOCK_DELAY=12

#constants for ElementCount, Height, Width API Script
ELEMENT_CLASSNAME_ELEMENTCOUNT_HEIGHT_WIDTH_ANDROID="android.widget.ImageView"#for android
ELEMENT_XPATH__ELEMENTCOUNT_HEIGHT_WIDTH_IOS="//XCUIElementTypeImage[@name='youtube_logo']"#for iOS

#constant for HideKeyboard API Script
CHKPNT_HIDEKEYBOARD="CHKPNT_HIDEKEYBOARD"

#constants for VolumeUp, VolumeDown API Script
CHKPNT_VOLUMEUP="CHKPNT_VOLUMEUP"
CHKPNT_VOLUMEDOWN="CHKPNT_VOLUMEDOWN"
VOLUMEUP_LEVEL=1
VOLUMEDOWN_LEVEL=1
INITIAL_DELAY_VOLUME=0
TIME_TO_WAIT_VOLUME=10

#constants for Reboot API Script
CHKPNT_UNLOCK="CHKPNT_UNLOCK"
INITIAL_DELAY_REBOOT=1
TIME_TO_WAIT_REBOOT=30

#constants for ClearText API
CHKPNT_CLEARTEXT="CHKPNT_CLEARTEXT"
INITIAL_DELAY_CLEARTEXT=0
TIME_TO_WAIT_CLEARTEXT=10
ELEMENT_ID_CLEARTEXT="com.google.android.youtube:id/search_edit_text"

#constants for IsEnabled and IsSelected APIs
ELEMENT_CLASSNAME_ISSELECTED="android.widget.Button"
CLICK_INDEX_ISSELECTED=1
CLICK_ISSELECTED_DELAY=10
ELEMENT_CLASSNAME_ISENABLED="android.view.View" #/ android.widget.ImageView/"
CHKPNT_CLICK_ISSELECTED="CHKPNT_CLICK_ISSELECTED"
INITIAL_DELAY_ISSELECTED=0
TIME_TO_WAIT_ISSELECTED=10

#constants for GetDeviceHeight and GetDeviceWidth APIs
HEIGHT_21435=1920#Device height for DUT 21435
WIDTH_21435=1080#Device width for DUT 21435
HEIGHT_ios = 667
WIDTH_ios = 375


'''
#constants for PressAndMove API Script
ELEMENT_CLASSNAME_CLICK_INDEX="android.widget.ImageView"
CLICK_INDEX=2
CLICK_INDEX_DELAY=5
KEYCODE_PRESSANDMOVE="Keycode_ENTER"
KEYS_PRESSANDMOVE="Master Chef Australia"
CHKPNT_CLICK_INDEX="CHKPNT_CLICK_INDEX"
CHKPNT_CLICK_INDEX_SENDKEYS_PRESSANDMOVE="CHKPNT_CLICK_INDEX_SENDKEYS_PRESSANDMOVE"
CHKPNT_TAP_SENDANDROIDKEYCODE_PRESSANDMOVE="CHKPNT_TAP_SENDANDROIDKEYCODE_PRESSANDMOVE"
TAP_X_PRESSANDMOVE=241
TAP_Y_PRESSANDMOVE=370
X1_PRESSANDMOVE=241
Y1_PRESSANDMOVE=370
X2_PRESSANDMOVE=800
Y2_PRESSANDMOVE=1500
'''
#constants for Swipe API Script
X1_SWIPE=241
Y1_SWIPE=1500
X2_SWIPE=241
Y2_SWIPE=370
VIDEO_X_SWIPE=241
VIDEO_Y_SWIPE=370
VIDEO_W_SWIPE=50
VIDEO_H_SWIPE=50
TIMEOUT_SWIPE = 10
WAITGAP_SWIPE = 2
TOLERANCE_SWIPE = "10"
DELAY_BEFORE_SWIPE=10
DELAY_AFTER_SWIPE=5
CHKPNT_SWIPE="CHKPNT_CLICK_INDEX"

#constants for VerticalSwipe API Script
Y_START_VERTICALSWIPE=300
Y_END_VERTICALSWIPE=1500
X_VERTICALSWIPE=800
TIMEOUT_VERTICALSWIPE=10
CHKPNT_CLICK_INDEX="CHKPNT_CLICK_INDEX"

#constants for HorizontalSwipe API Script
X_START_HORIZONTALSWIPE=800
X_END_HORIZONTALSWIPE=100
Y_HORIZONTALSWIPE=1500
TIMEOUT_HORIZONTALSWIPE=10
CHKPNT_TAP_SENDANDROIDKEYCODE_PRESSANDMOVE="CHKPNT_TAP_SENDANDROIDKEYCODE_PRESSANDMOVE"
#constants for GetAllAttributeValues API Script
ELEMENT_ID_GETALLATTRIBUTEVALUES="com.google.android.youtube:id/mobile_topbar_avatar"
ATTRIBUTE_LIST_GETALLATTRIBUTEVALUES= 'checkable,checked,clickable,enabled,focusable,focused,scrollable,password,selected'#index,package,

#constants for GetAttribute API Script
ELEMENT_CLASSNAME_GETATTRIBUTE="com.google.android.youtube:id/mobile_topbar_avatar"
ATTRIBUTE_LIST_GETATTRIBUTE= ["text","index","class","package","checkable","checked","clickable","enabled","focusable","focused",
            "scrollable","password","selected"]
#ATTRIBUTE_LIST_GETATTRIBUTE= ["focusable"]

#constants for Reset API Script
CHKPNT_RESET="CHKPNT_RESET"
INITIAL_DELAY_RESET=0
TIME_TO_WAIT_RESET=10

#constant for SetDefaultWaitTime  API Script
ELEMENT_ID_CLICK="com.google.android.youtube:id/mobile_topbar_avatar"
TIMEOUT_SETDEFAULTWAITTIME=10

#constant for Shake  API Script
SHAKE_DELAY=12
CHKPNT_UNLOCK="CHKPNT_UNLOCK"
INITIAL_DELAY_SHAKE=1
TIME_TO_WAIT_SHAKE=30


#constant for HandleAlertMessage  API Script
PLATFORM_PROPERTY = 3
CHKPNT_IOS_YOU_TUBE_DOWNLOAD_BUTTON = "ios_youTubeDownloadOptionOCR"#"ios_youTubeDownloadOption"
CHKPNT_IOS_YOU_TUBE_DOWNLOAD_POP_UP = "ios_youTubeDownloadPopUpOCR"
 
HANDLE_ALERT_DISMISS = "dismiss"
HANDLE_ALERT_ACCEPT = "aCCept"
HANDLE_ALERT_INVALID = "invalid"