# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Base configurations for scripts running in Android devices
#
# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''


class ConfigBase(object):

    QOE_DB                      = 'stage'  # name of the db, string value : dev or prod or stage.  "prod" FOR USER ENVIRONMENT
    DEVICE_PLATFORM             = "Android"
    APP_NAME                    = "com.bskyb.nowtv.beta"

    DEFAULT_SLEEP_TIME          = 60

    APP_HOME                    = "com.bskyb.nowtv.beta:id/action_search"

    QoEMONITORING_TIME              = 300
    QoEITERATION_COUNT              = 5
    QoEMONITORING_INTERVAL          = 600
    QoE_FAILURE_MONITORING_INTERVAL = 60
    QoETUNEMAXWAIT_TIME             = 120

    NOWTV_BUFFERCHECK_COLOR_TOLERANCE = 25
    NOWTV_BUFFERCHECK_MIN_PIXALS      = 80

    # Variable declarations
    MINTIMEOUT                        = 1
    TIMEOUT                           = 2
    MAXTIMEOUT                        = 5
    MORETIMEOUT                       = 20
    HALFMINTIMEOUT                    = 30
    WAIT_GAP                          = 1
    WAIT_GAP_SCREENSAVER              = 0.5
    WAIT_GAP_DETECT_MOTION            = 0.04
    MAXCOUNT                          = 4
    MAXRANGE                          = 20
    ITERATION                         = 5
    SHORT_WAITTIME                    = 3
    WAITTIME                          = 10
    MAX_ITERATION                     = 60
    BUFFER_TIME                       = 100
    QoE_DURATION				      = 120
    NO_OF_CHANNELS                    = 10
    NO_OF_VOD                         = 12
    default_tolerance                 = '3'
    DEFAULT_JPEGQUALITY               = 90
    DEFAULT_OVERWRITEACTION           = 0


    DetectMotion_x                      = 125
    DetectMotion_y                      = 190
    DetectMotion_w                      = 225
    DetectMotion_h                      = 200

    DETECT_MOTION_CENTER_AREA_X         = 280
    DETECT_MOTION_CENTER_AREA_Y         = 160
    DETECT_MOTION_CENTER_AREA_W         = 500
    DETECT_MOTION_CENTER_AREA_H         = 280

    SWIPE_CHECK_AREA_X = 140
    SWIPE_CHECK_AREA_Y = 130
    SWIPE_CHECK_AREA_W = 430
    SWIPE_CHECK_AREA_H = 450

    Small_Swipe_Vertical_BottomToTop_x  = 350
    Small_Swipe_Vertical_BottomToTop_y1 = 625
    Small_Swipe_Vertical_BottomToTop_y2 = 120

    SCREENSHOT_BASE_DIR = 'C:\\'
    SCREENSHOT_DIRNAME = 'ScreenShots'

    MENU_ICON = "//android.widget.ImageButton[@content-desc='menu_icon']"

    SPORTS_BUTTON = "//android.widget.TextView[@text='Sports']"

    MOVIES_BUTTON = "//android.widget.TextView[@text='Movies']"

    ENTERTAINMENT_BUTTON = "//android.widget.TextView[@text='Entertainment']"

    SPORTS_WATCH_LIVE = "(//android.widget.TextView[@content-desc='sub_menu'])[1]"

    WATCH_LIVE = "(//android.widget.TextView[@content-desc='sub_menu'])[4]"

    ALL_TV_SHOWS_OPTION = "(//android.widget.TextView[@content-desc='sub_menu'])[2]"

    ALL_TV_SHOWS_TITLE = "//android.widget.TextView[@text='All TV Shows']"

    ALL_MOVIES_OPTION = "(//android.widget.TextView[@content-desc='sub_menu'])[3]"

    ALL_MOVIES_TITLE = "//android.widget.TextView[@text='All Movies']"

    ALL_MOVIES_FIRST_TILE = "//android.support.v7.widget.RecyclerView/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.ImageView"

    ALL_MOVIES_PLAYBUTTON = "com.bskyb.nowtv.beta:id/img_play_icon"

    ALL_MOVIES_ITEM_NAME = "com.bskyb.nowtv.beta:id/txt_title"

    FIRST_PLAY_BUTTON = "(//android.widget.ImageView[@content-desc='Play button'])[1]"

    FIRST_CHANNEL_PROGRAMME_NAME = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v4.widget.DrawerLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.TextView[1]"

    MOVIES_RESUME_BUTTON = "com.bskyb.nowtv.beta:id/btn_positive"

    WATCH_FROM_BEGIN_BUTTON = "com.bskyb.nowtv.beta:id/btn_negative"

    VIDEO_PLAYER = 'com.bskyb.nowtv.beta:id/videoplayer'

    LOADING_SPINNER = 'com.bskyb.nowtv.beta:id/loading_spinner'

    BUFFERING_CIRCLE = 'com.bskyb.nowtv.beta:id/progress_bar'

    OK_BUTTON = '//android.widget.Button[@text="OK"]'

    def get_all_tv_shows_tile(self, i):
        ent_tile = '//android.support.v7.widget.RecyclerView/android.widget.FrameLayout['+str(i)+']/android.widget.LinearLayout/android.widget.FrameLayout'
        return ent_tile

    TESTSCENARIO_FOLDER = 'TestScenarios/'
    TESTVECTOR_FOLDER = 'TestVectors/'

    SCENARIO_COLUMN = {
        "category": 0,
        "asset_type": 1,
        "channel_list": 2,
        "use_case": 3,
        "test_vector_file_name": 4,
        "channel_play_time": 5,
        "loop_count": 6
    }

    TESTVECTOR_COLUMN = {
        "choke_time": 0,
        "limited_bw_up": 1,
        "limited_bw_down": 2,
        "delay": 3,
        "jitter": 4,
        "packet_loss": 5
    }

    SEARCH_BUTTON = "com.bskyb.nowtv.beta:id/action_search"
    X_EDIT_BOX = '//android.widget.EditText[@content-desc="search_text_field"]'
    X_FIRST_SEARCH_RESULT = '(//android.widget.ImageView[@content-desc="search_item_image"])[1]'

    ID_NAVIGATE_UP = "Navigate up"
    ID_BACK_BUTTON = "back_button"
    #X_FIRST_PLAY_BUTTON = '(//android.widget.ImageView[@content-desc="Play button"])[1]'
    ID_ALL_KIDS_ITEM_NAME_VOD = "com.bskyb.nowtv.beta:id/kids_detail_title"
    X_KIDS_PLAY_BUTTON = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.widget.RelativeLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ImageView[2]'
    ID_KIDS_LEAVE_NOW = 'com.bskyb.nowtv.beta:id/leave_text_view'

    CATEGORY_BUTTON = "//android.widget.TextView[@text='{}']"
    CHANNEL_NAME = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v4.widget.DrawerLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.RelativeLayout[{}]'
    ON_NOW_PGM = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v4.widget.DrawerLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[{}]/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.RelativeLayout[{}]/android.widget.FrameLayout[2]'
    NEXT_PGM = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v4.widget.DrawerLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[{}]/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.RelativeLayout[{}]/android.widget.FrameLayout[2]'
    WATCH_LIVE_TITLE = "com.bskyb.nowtv.beta:id/title"
    ON_NOW_PGM_ENT = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v4.widget.DrawerLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[{}]/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.LinearLayout[{}]/android.widget.FrameLayout/android.widget.LinearLayout'
    NEXT_PGM_ENT = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v4.widget.DrawerLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[{}]/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.LinearLayout[{}]/android.widget.FrameLayout/android.widget.LinearLayout'
    KIDS_ON_NOW_PGM = '//android.support.v7.widget.RecyclerView[@content-desc="Live"]/android.widget.LinearLayout[{}]/android.widget.LinearLayout'
    KISDS_LETS_GO = '//android.widget.TextView[@content-desc="sub_menu"]'
    X_ON_NOW = '//android.widget.ImageView[@content-desc="On Now"]'