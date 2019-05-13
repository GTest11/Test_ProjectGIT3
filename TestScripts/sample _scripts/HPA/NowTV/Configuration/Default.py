# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Configuration - Default
# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

from System.Drawing import Color
from android_core.config import ConfigBase

class Config(ConfigBase):

    DEVICE_TYPE = 'Default'
    DEVICE_VERSION = 'x.x'

    DETECT_BLACKSCREEN_X = 170
    DETECT_BLACKSCREEN_Y = 80
    DETECT_BLACKSCREEN_W = 290
    DETECT_BLACKSCREEN_H = 185

    NOWTV_BUFFERING_AREA_X      = 586
    NOWTV_BUFFERING_AREA_Y      = 283
    NOWTV_BUFFERING_AREA_W      = 109
    NOWTV_BUFFERING_AREA_H      = 116

    VOD_ASSET_COUNT_IN_ONE_ROW  = 2
    TV_SHOWS_COUNT_IN_ONE_ROW = 1

    AllMovie_Swipe_Vertical_BottomToTop_y1 = 1100
    AllMovie_Swipe_Vertical_BottomToTop_x2 = 333
    AllMovie_Swipe_Vertical_BottomToTop_y2 = 300

    AllTVShows_Swipe_Vertical_BottomToTop_y1 = 762
    AllTVShows_Swipe_Vertical_BottomToTop_x2 = 300
    AllTVShows_Swipe_Vertical_BottomToTop_y2 = 400

    Swipe_Vertical_BottomToTop_x1 = 363
    Swipe_Vertical_BottomToTop_y1 = 775
    Swipe_Vertical_BottomToTop_x2 = 363
    Swipe_Vertical_BottomToTop_y2 = 350

    MOVIES_LIVE_SWIPE_TIME = 2500
    MOVIES_VOD_SWIPE_TIME = 2500
    SPORTS_LIVE_SWIPE_TIME = 2500


    KIDS_LIVE_SWIPE_TIME = 2300
    KIDS_HORIZONTAL_LIVE_SWIPE_TIME = 2500

    Kids_Swipe_Vertical_BottomToTop_x1 = 836
    Kids_Swipe_Vertical_BottomToTop_y1 = 750
    Kids_Swipe_Vertical_BottomToTop_x2 = 836
    Kids_Swipe_Vertical_BottomToTop_y2 = 33

    Kids_Swipe_Horizontal_BottomToTop_x1 = 945
    Kids_Swipe_Horizontal_BottomToTop_y1 = 755
    Kids_Swipe_Horizontal_BottomToTop_x2 = 470
    Kids_Swipe_Horizontal_BottomToTop_y2 = 755

    Kids_Generic_Swipe_Horizontal_BottomToTop_x1 = 700
    Kids_Generic_Swipe_Horizontal_BottomToTop_y1 = 755
    Kids_Generic_Swipe_Horizontal_BottomToTop_x2 = 470
    Kids_Generic_Swipe_Horizontal_BottomToTop_y2 = 755

    NOWTV_BUFFERING_COLORS      =  [Color.FromArgb(248, 97, 52),
                                    Color.FromArgb(47, 165, 64),
                                    Color.FromArgb(101, 56, 151),
                                    Color.FromArgb(39, 92, 184)]

    KIDSVOD_Swipe_Vertical_BottomToTop_x1 = 389
    KIDSVOD_Swipe_Vertical_BottomToTop_y1 = 531
    KIDSVOD_Swipe_Vertical_BottomToTop_x2 = 389
    KIDSVOD_Swipe_Vertical_BottomToTop_y2 = 130


####################### Added by the koustubha for kids Live###########################################

    KIDS_BUTTON = "//android.widget.TextView[@text='Kids']"

    LETS_GO = '//android.widget.TextView[@content-desc="sub_menu"]'

    ON_NOW = "On Now"

    ALL_KIDS_ITEM_NAME = '//android.support.v7.widget.RecyclerView[@content-desc="Live"]/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ImageView'

    OK = "com.bskyb.nowtv.beta:id/onboarding_ok"

    TOP_SHOWS_CHANNEL = '//android.support.v7.widget.RecyclerView[@content-desc="TopShows"]/android.widget.LinearLayout[1]/android.widget.LinearLayout'

    KIDS_ITERATION = 12

    BACK_KIDS = "com.bskyb.nowtv.beta:id/kids_rails_back_button"

    LEAVE_NOW = "com.bskyb.nowtv.beta:id/leave_text_view"

    NOW_TV = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v4.view.ViewPager/android.widget.ViewSwitcher/android.support.v7.widget.RecyclerView/android.widget.FrameLayout/android.widget.ImageView'

    #########################Added by koustubha for kids VOD #######################################

    ALL_KIDS_ITEM_NAME_VOD = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.TextView'

    BACK_BUTTON = "com.bskyb.nowtv.beta:id/kids_details_back_button"

    KIDS_PLAY_BUTTON='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.widget.RelativeLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ImageView[2]'
