# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Base configurations for scripts running in iOS devices
#
# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''


class IOSConfig(object):

    DEVICE_TYPE = "iOS"
    APP_NAME = "com.bskyb.skygo"

    SCREENSHOT_DIRNAME = "skygo_screenshots"
    SCREENSHOT_BASE_DIR = "C:\\"

    DEFAULT_SLEEP_TIME = 10
    MIN_SLEEP_TIME = 3
    MD_SLEEP_TIME = 6
    MX_SLEEP_TIME = 20
    DEFAULT_TRIAL = 3

    APP_HOME = "Home"

    HOMESCREEN_SETTINGS = "Settings"
    HOMESCREEN_CATCHUP_TV = "Catch Up TV"
    HOMESCREEN_ON_NOW = "On Now"
    HOMESCREEN_SPORTS = "Sports"

    SPORTS_LIVE_SPORTS = "Live Sport"
    MAIN_NAV_TITLE = "MainNav.Title"
    CATCHUPSCREEN_MAIN_NAV_TITLE = "Catch Up"
    CATCHUPSCREEN_SKY_ONE = "Sky One"
    SKYONE_SERIES = "Series"

    DAYPICKER_TODAY = "All Channels" #"Today"
    EPG_PGM_DETAILS_ACTION_BTN = "Actions"

    ONNOW_ALL_CHANNELS = "All Channels"
    HOMESCREEN_MAIN_NAV_TITLE = "MainNav.Home"

    ONNOW_NEWS = "News"
    ONNOW_MOVIES = "Movies"

    HOME_CAROUSEL_COORDS = (10, 80, 200, 200)
    HOME_CAROUSEL_DISPLAY_TIME = 6
    WAIT_FOR_CAROUSEL = 6   # in seconds > wait for auto scroll to happen

    NAME_SEARCH_ICON = "search icon"
    NAME_ON_DEMAND = "On Demand"
    X_FIRST_SEARCH_RESULT = "//XCUIElementTypeWindow[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther[3]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeTable[1]/XCUIElementTypeCell[1]"

    INITIAL_PLAYBACK_TIME = 60

    XPATH_ASSETNAME_CAROUSEL = "//XCUIElementTypeApplication[@name='Sky Go']/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeCollectionView/XCUIElementTypeOther[2]/XCUIElementTypeTextView"
    XPATH_CHANNEL_CAROUSEL = "//XCUIElementTypeApplication[@name='Sky Go']/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeCollectionView/XCUIElementTypeOther[2]/XCUIElementTypeImage"
    XPATH_EPG_PROGRAMME_TITLE = "//XCUIElementTypeStaticText[@name='programme_title']"
    XPATH_FIRST_ELEMENT_ON_HOME = "//XCUIElementTypeApplication[@name='Sky Go']/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeCollectionView/XCUIElementTypeCell[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeCollectionView/XCUIElementTypeCell[1]"

    XPATH_SKYCINEMA_COLLECTION = "//XCUIElementTypeApplication[@name='Sky Go']/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeCollectionView"
    XPATH_SKYCINEMA_COLLECTION_ITEM = "//XCUIElementTypeApplication[@name='Sky Go']/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeCollectionView/XCUIElementTypeCell"

    CORD_SWIPE_CAROUSEL = [10, 256, 363, 33]
    CORD_SWIPE_EPG = [28, 149, 50, 77]

    TIME_MID_NIGHT = "11.30pm"

    CATCHUP_CATEGORY = {
        'category_level1'   : 'Catch Up TV',
        'category_level2'   : 'Channel 5',
        'category_level3'   : ['Featured', 'Most Popular', 'By Day']
    }

    CORD_EPG_FIRST_PROGRAMME = [356,165]

    COUNT_WAIT_PLAYBACK = 60

    PLAYBACK_PROGRESS_BAR = "Progress"
    PLAYBACK_FF_BTN = "customMP fastforward"
    PLAYBACK_DONE_BTN = "Done"
    PLAYBACK_PLAY_BTN = "customMP play"

    PGM_DETAILS_MORE_ACTION_BTN = "MoreInfoButton"

    # ***************** Download *****************
    HOMESCREEN_DOWNLOADS = "Downloads"
    CONTENT_DOWNLOADED = "Downloaded"
    CONTENT_DOWNLOADING = "Downloading"
    XPATH_FIRST_DOWNLOAD = "//XCUIElementTypeTable[1]/XCUIElementTypeCell[1]/XCUIElementTypeButton[@name='PlaybackButton']"
    X_DWN_FIRST_ITEM_DURATION = "//XCUIElementTypeTable/XCUIElementTypeCell[1]/XCUIElementTypeStaticText[8]"
    X_MDA_PLAYER_DONE_BTN = "//XCUIElementTypeButton[@name='Done']"
    X_MDA_PLAYER_PLAY_TIME = "//XCUIElementTypeButton[@name='Done']/following::XCUIElementTypeStaticText[1]"
    X_MDA_PLAYER_REMAINING_TIME = "//XCUIElementTypeButton[@name='Done']/following::XCUIElementTypeStaticText[2]"

    NAME_SEARCH_FIELD = "Search for TV shows, movies, actors or events..."

    # Swipes
    CORD_SWIPE_UP = [425, 80, 425, 20]
    CORD_SWIPE_UP_FAQ_LEFT = [460, 800, 460, 300]
    CORD_SWIPE_UP_FAQ_RIGHT = [2000, 800, 2000, 300]
    CORD_SWIPE_GRID_UP = [425, 120, 425, 30]

    # Buttons
    BTN_BACK_TO_SKY_CINEMA = "Sky Cinema"

    #**** Streaming_Watch_Live_Channel_15_Minutes
    CORD_ASSET_PLAYBACK = [356,20]
    ST_NEWS_CHANNEL = "Sky News HD 501"
    ST_DOC_CHANNEL = "Discovery HD 520"
    ST_ENTRTNMNT_CHANNEL = "Sky One HD 106"

    #********  Streaming_Watch_Encrypted_Channel
    ENCRYPTED_CHANNEL = 507
    CORD_SWIPE_UP_EPG = [425, 20, 475, 20]


    # ********  Streaming_Watch_Unencrypted_Channel
    UNENCRYPTED_CHANNEL = 507

    # ********  Streaming_Watch_Unencrypted_Channel
    WAIT_SLEEP_TIME = 900

    # ******* Streaming PIN check ************
    PIN_REQUIRED_CHANNEL = "Sky Premiere 301"
    PIN_WINDOW = "Sky device PIN"

    BACK_BTN_ON_PGMDETAILS = "Home"

    # ********  FAQs_No_External_Links
    SETTINGS_FAQS = "FAQs"
    XPATH_FAQS = "//XCUIElementTypeApplication[@name='Sky Go']/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeStaticText[@name='FAQs']"

    XPATH_FAQ_QUESTION_1 = "/XCUIElementTypeOther[@name='FAQs.content']/XCUIElementTypeWebView/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]"
    X_FAQ_TXT = "//XCUIElementTypeWebView[0]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[{}]"
    X_FAQ_TXT_ITEM = "/XCUIElementTypeStaticText"

    FAQ_QUESTION_1 = "What is Sky Go?"


    HOMESCREEN_SKY_CINEMA = "Sky Cinema"
    SKYCINEMA_NEW_PREMIERES = "New Premieres"
    XPATH_VOD_PROGRAMME = "//XCUIElementTypeApplication[@name='Sky Go']/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeCollectionView/XCUIElementTypeCell"
    XPATH_ASSET = "//XCUIElementTypeApplication[@name='Sky Go']/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeCollectionView/XCUIElementTypeOther[1]"
    MORE_INFO_BUTTON = "MoreInfoButton"
    CORD_VOD_PROGRAMME = [356,165]
    CORD_ESCAPE_MORE_INFO_MENU = [356,165]

    SKYCINEMA_MOST_POPULAR = "Most Popular"

    # ********  Streaming_Watch_Encrypted_Channel

    DEFAULT_WAIT_TIME = 10
    PLAYBACK_WAIT_TIME = 30
    SWIPE_COUNT = 20
    ITER_COUNT = 20

    ASSET_DETAILS_PLAYBACK_BTN = "PlaybackButton"
    ONNOW_DOCUMENTARIES = "Documentaries"
    CORD_PLAYBACK = [800, 120, 200, 200]
    MOVIE_PLAYBACK = [700,400,600,400]
    #*** EPG Screen
    XPATH_FIRST_CHANNEL_GRID = "//XCUIElementTypeApplication[@name='Sky Go']/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeCollectionView/XCUIElementTypeCell[6]"
    DOCUMENTARIES_EPG_CHANNEL = "Sky Living HD 107"

    #***** StreamingPin_No_Pin_NonMovie_Linear_Channel
    ONNOW_ENTERTAINMENT = "Entertainment"
    PARENTAL_PIN_WINDOW = "Sky device PIN"
    XPATH_PIN_WINDOW = "//XCUIElementTypeOther[@name='Sky device PIN']"
    ENTERTAINMENT_EPG_CHANNEL = "Sky Living HD 107"

    # Download traverse
    X_BACK_TO_PARENT_GRID = "//XCUIElementTypeButton[@name='{}']"
    X_GRID_ITEM = "//XCUIElementTypeCell[@name='{}']"

    # ***** InitDownload_No_Pin_Window_When_Booking_Download
    XPATH_FIRST_ASSET_ON_SKYCINEMA1 = "//XCUIElementTypeApplication[@name='Sky Go']/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeCollectionView/XCUIElementTypeCell[6]"
    ASSET_TITLE = "programme_title"
    ASSET_SYNOPSIS = "programme_synopsis"
    ASSET_DURATION = "programme_duration"
    ASSET_DOWNLOAD_BTN = "Download to iPad"
    ASSET_DOWNLOAD_QUEUE_STATUS = "Queued on iPad"
    ASSET_DOWNLOAD_COMPLETED = "Downloaded to iPad"
    ASSET_DOWNLOAD_CANCEL_BTN = "Cancel iPad download"

    DEFAULT_DOWNLOAD_WAITTIME = 60
    VOD_ASSET_DOWNLOAD_TIME = 2700

    # Append XCUIElementTypeCell[index]
    XPATH_OF_ASSET_ON_SKYCINEMA = "//XCUIElementTypeApplication[@name='Sky Go']/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeCollectionView"
    XPATH_DOWNLOADING_STATUS = "//XCUIElementTypeApplication[@name='Sky Go']/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeAny/XCUIElementTypeStaticText[6]"
    CANCEL_DOWNLOAD_BTN = "Cancel iPad download"
    BACK_BTN_ON_SKYCINEMA = "Sky Cinema"
    DELETE_DOWNLOAD_BTN = "Delete from iPad"

    #******InitDownload_Download_Resume_Close_Relaunch_App
    X_ASSET_IN_SKYCINEMA = "//XCUIElementTypeApplication[@name='Sky Go']/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeCollectionView/XCUIElementTypeCell[{}]"
    X_ASSET_SKYCINEMA_MIN = "//XCUIElementTypeCollectionView/XCUIElementTypeCell[{}]"
    XPATH_FIRST_ASSET_ON_SKYCINEMA = "//XCUIElementTypeApplication[@name='Sky Go']/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeCollectionView/XCUIElementTypeCell[1]"
    XPATH_N_ASSET_ON_SKYCINEMA = "//XCUIElementTypeApplication[@name='Sky Go']/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeCollectionView/XCUIElementTypeCell[6]"
    MAX_COUNT = 36

    X_ALERT_WINDOW = "//XCUIElementTypeAlert"
    X_DWN_ALERT_WINDOW = "//XCUIElementTypeApplication[@name='Sky Go']/XCUIElementTypeWindow[4]/XCUIElementTypeOther[2]/XCUIElementTypeAlert"
    DOWNLOAD_LIMIT_MESSAGE = "This item has already been downloaded the maximum number of times."
    DOWNLOAD_LIMIT_OK_BTN = "OK"

    # *** Please do not modify this. Used in sleep_for_max_time() ***
    SLEEP_TIME = 5
    DOWNLOAD_STATUS_WAIT = 20
    AVG_WAIT_FOR_ELEMENT_TO_LOAD = 20
    MAX_WAIT_FOR_ELEMENT_TO_LOAD = 120
    TOTAL_SKY_CINEMA_MOVIES = 15
    TOTAL_DOWNLOADED_MOVIES = 10
    XPATH_DL_ASSET_MOREINFO_BTN = "//XCUIElementTypeTable[1]/XCUIElementTypeCell[1]/XCUIElementTypeButton[@name='MoreInfoButton']"
    WATERSHED_TIME = "21" # 9.00pm
    UK_TIMEZONE = "Europe/London"

    BACK_BTN_ON_DOWNLOADS = "Home"
    BACK_TO_HOME = "Home"
    CONTINUE_PLAYBACK_FIRSTTIME = "Continue"
    XPATH_DL_STATUS_RESUME = "//XCUIElementTypeApplication[@name='Sky Go']/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeAny[2]/XCUIElementTypeStaticText[7]"

    CANCEL_PLAYBACK_FIRSTTIME = "Cancel"
    WAITITME = 60

    PC_PIN = "8832"

    X_ALERT_SAME_HOUSEHOLD = "//XCUIElementTypeApplication[@name='Sky Go']/XCUIElementTypeWindow[4]/XCUIElementTypeOther[2]/XCUIElementTypeAlert/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeOther"
    X_ALERT_SAME_HOUSEHOLD_OK = "//XCUIElementTypeApplication[@name='Sky Go']/XCUIElementTypeWindow[4]/XCUIElementTypeOther[2]/XCUIElementTypeAlert/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther"

    HOME_ICON="home icon"
    XPATH_DOWNLOADS_MOREINFO = "//XCUIElementTypeTable[1]/XCUIElementTypeCell[1]/XCUIElementTypeButton[@name='MoreInfoButton']"
    CORD_DISMISS_MORE_INFO = [2010, 278]

    SKYCINEMA_DISNEY = "All Time Greats"

    DETECT_MOTION = [64,212,1191,1109]
