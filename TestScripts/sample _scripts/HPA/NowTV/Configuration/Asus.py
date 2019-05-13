# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Configuration - ZenPad8_0
# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

from System.Drawing import Color
from android_core.config import ConfigBase

class Config(ConfigBase):

    DEVICE_TYPE = 'ZenPad8_0'
    DEVICE_VERSION = '6'

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

    Kids_Generic_Swipe_Horizontal_BottomToTop_x1 = 700
    Kids_Generic_Swipe_Horizontal_BottomToTop_y1 = 755
    Kids_Generic_Swipe_Horizontal_BottomToTop_x2 = 470
    Kids_Generic_Swipe_Horizontal_BottomToTop_y2 = 755

    MOVIES_LIVE_SWIPE_TIME = 2500
    MOVIES_VOD_SWIPE_TIME = 2500
    SPORTS_LIVE_SWIPE_TIME = 2500

    NOWTV_BUFFERING_COLORS      =  [Color.FromArgb(241, 102, 39),
                                    Color.FromArgb(52, 172, 64),
                                    Color.FromArgb(102, 55, 147),
                                    Color.FromArgb(33, 96, 180)]

    def get_all_tv_shows_tile(self, i):
        ent_tile = '//android.support.v7.widget.RecyclerView/android.widget.LinearLayout['+ str(i) +']/android.widget.FrameLayout'
        return ent_tile
