# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Configuration - SamsungTabA
# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

from System.Drawing import Color
from android_core.config import ConfigBase

class Config(ConfigBase):

    DEVICE_TYPE = 'SamsungTabA'
    DEVICE_VERSION = '7.1.1'

    DETECT_BLACKSCREEN_X        = 115
    DETECT_BLACKSCREEN_Y        = 105
    DETECT_BLACKSCREEN_W        = 564
    DETECT_BLACKSCREEN_H        = 225


    NOWTV_BUFFERING_AREA_X      = 525
    NOWTV_BUFFERING_AREA_Y      = 280
    NOWTV_BUFFERING_AREA_W      = 100
    NOWTV_BUFFERING_AREA_H      = 90

    VOD_ASSET_COUNT_IN_ONE_ROW  = 3
    TV_SHOWS_COUNT_IN_ONE_ROW = 2

    Swipe_Vertical_BottomToTop_x1 = 333
    Swipe_Vertical_BottomToTop_y1 = 930
    Swipe_Vertical_BottomToTop_x2 = 333
    Swipe_Vertical_BottomToTop_y2 = 415

    AllTVShows_Swipe_Vertical_BottomToTop_y1 = 425
    AllTVShows_Swipe_Vertical_BottomToTop_x2 = 150
    AllTVShows_Swipe_Vertical_BottomToTop_y2 = 150

    AllMovie_Swipe_Vertical_BottomToTop_y1 = 827
    AllMovie_Swipe_Vertical_BottomToTop_x2 = 333
    AllMovie_Swipe_Vertical_BottomToTop_y2 = 400

    MOVIES_LIVE_SWIPE_TIME = 2500
    MOVIES_VOD_SWIPE_TIME = 2500
    SPORTS_LIVE_SWIPE_TIME = 2500
    KIDS_LIVE_SWIPE_TIME = 2300
    KIDS_HORIZONTAL_LIVE_SWIPE_TIME = 2500

    Kids_Swipe_Vertical_BottomToTop_x1 = 376
    Kids_Swipe_Vertical_BottomToTop_y1 = 482
    Kids_Swipe_Vertical_BottomToTop_x2 = 376
    Kids_Swipe_Vertical_BottomToTop_y2 = 26

    Kids_Swipe_Horizontal_BottomToTop_x1 = 565
    Kids_Swipe_Horizontal_BottomToTop_y1 = 643
    Kids_Swipe_Horizontal_BottomToTop_x2 = 229
    Kids_Swipe_Horizontal_BottomToTop_y2 = 643

    Kids_Generic_Swipe_Horizontal_BottomToTop_x1 = 430
    Kids_Generic_Swipe_Horizontal_BottomToTop_y1 = 643
    Kids_Generic_Swipe_Horizontal_BottomToTop_x2 = 229
    Kids_Generic_Swipe_Horizontal_BottomToTop_y2 = 643

    KIDSVOD_Swipe_Vertical_BottomToTop_x1 = 209
    KIDSVOD_Swipe_Vertical_BottomToTop_y1 = 435
    KIDSVOD_Swipe_Vertical_BottomToTop_x2 = 209
    KIDSVOD_Swipe_Vertical_BottomToTop_y2 = 250

    NOWTV_BUFFERING_COLORS      =  [Color.FromArgb(241, 102, 39),
                                    Color.FromArgb(52, 172, 64),
                                    Color.FromArgb(102, 55, 147),
                                    Color.FromArgb(33, 96, 180)]

    def get_all_tv_shows_tile(self, i):
        ent_tile = '//android.support.v7.widget.RecyclerView/android.widget.LinearLayout['+ str(i) +']/android.widget.FrameLayout'
        return ent_tile

###################### Added by the koustubha for Kids live###########################################

    KIDS_BUTTON = "//android.widget.TextView[@text='Kids']"

    LETS_GO = '//android.widget.TextView[@content-desc="sub_menu"]'

    ON_NOW = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v4.view.ViewPager/android.widget.ViewSwitcher/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[4]/android.widget.LinearLayout/android.widget.TextView"

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
