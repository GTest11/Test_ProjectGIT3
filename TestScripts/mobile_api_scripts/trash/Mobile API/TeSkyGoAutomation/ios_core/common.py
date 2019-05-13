# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Common functions and classes for scripts running in iOS devices
#
# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

import time
import MobileScriptingLibrary
from ios_core.config import IOSConfig
from ios_core.utils import detect_motion, log_screen_shot
from ios_core.exceptions import APIFailed

class TestResult(object):
    PASSED = "Passed"
    FAILED = "Failed"
    ABORTED = "Aborted"
    ERROR = "Error"

class DownloadStatus(object):
    INPROGRESS = 1
    QUEUED = 2
    DOWNLOADED = 3
    AVAILABLE = 4


def WaitForElement(dut, elm_type, elm, elm_name, wait_time, logger, interval=2):
    """
    A wrapper for checking IsElementPresent for wait_time seconds
    :param dut: MobileScriptingLibrary.MobileDUT object
    :param wait_time: wait time in secionds
    """
    MAX_WAIT_TIME = 60*60*60 # 1 hour
    start_time = time.time()
    timeout = start_time + wait_time
    max_wait = start_time + MAX_WAIT_TIME
    element_present = False
    logger.Log("Waiting for {} to become present".format(elm_name))
    while True:
        if dut.IsElementPresent(elm_type, elm):
            element_present = True
            break
        else:
            current_time = time.time()
            if (current_time > timeout):
                logger.Log("Timeout {}s reached while waiting for {}".format(timeout, elm_name))
                break
            elif (current_time > max_wait):
                logger.Log("Reached maximum wait time {}s while waiting for {}".
                           format(MAX_WAIT_TIME, elm_name))
                break
            else:
                time.sleep(interval)
    return element_present


def are_all_elements_present(dut, elements):
    """
    :param dut: MobileScriptingLibrary.MobileDUT object
    :param elements: A tuple of (element_type, element)
    """
    if not elements:
        return False
    all_present = True
    for elm_type, elm in elements:
        if not dut.IsElementPresent(elm_type, elm):
            all_present = False
            break
    return all_present


def is_present(dut, elm_type, elm, elm_name, logger, need_presence=True):
    """
    Checks if an element is present and logs the result
    :param dut: MobileScriptingLibrary.MobileDUT object
    :param elm_type: MobileScriptingLibrary element type object
    :param elm: Element name/xpath/id depending on elm_type
    :param elm_name: Friendly name of the element for logging
    :param need_presence: True if presence of element is expected
    """
    if not elm:
        return False
    result = False
    if not dut.IsElementPresent(elm_type, elm):
        logger.Log("Failed to display '{}'".format(elm_name))
    else:
        logger.Log("Displayed '{}' in the Menu Listing".format(elm_name))
        result = True
    return result

def tap(dut, elm_type, elm, elm_name, logger):
    """
    Taps on an element
    :param dut: MobileScriptingLibrary.MobileDUT object
    :param elm_type: MobileScriptingLibrary element type object
    :param elm: Element name/xpath/id depending on elm_type
    :param elm_name: Friendly name of the element for logging
    """
    if not elm:
        return False
    result = False
    if not dut.TapElement(elm_type, elm):
        logger.Log("Failed to tap on {}".format(elm_name))
    else:
        logger.Log("Tapped on '{}' Successfully".format(elm_name))
        result = True
    return result

def tap_if_present(dut, elm_type, elm, elm_name, logger):
    """
    Taps on an element if it is present
    :param dut: MobileScriptingLibrary.MobileDUT object
    :param elm_type: MobileScriptingLibrary element type object
    :param elm: Element name/xpath/id depending on elm_type
    :param elm_name: Friendly name of the element for logging
    """
    if not elm:
        return False
    result = False
    time.sleep(IOSConfig.AVG_WAIT_FOR_ELEMENT_TO_LOAD)
    # Check presence
    present = is_present(dut, elm_type, elm, elm_name, logger)
    if present:
        # Tap on the element
        tapped = tap(dut, elm_type, elm, elm_name, logger)
        if tapped:
            result = True
    return result


def navigate(dut, navigate_list, navigate_interval=2, logger=None):
    """
    Navigates to a given tuple of Element_type/Element_name
    :param dut: MobileScriptingLibrary.MobileDUT object
    :param navigate_list: A tuple of (
        Element type, element, friendly element name,
        element type to verify after navigate, verify element, verify element friendly name
    )
    :param navigate_interval: Wait time between tap and verify
    """
    if not navigate_list:
        return False
    all_done = True
    for elm_type, elm, elm_name, v_elm_type, v_elm, v_elm_name in navigate_list:
        tap_status = tap_if_present(dut, elm_type, elm, elm_name, logger)
        if not tap_status:
            all_done = False
            break

        time.sleep(IOSConfig.DEFAULT_WAIT_TIME)
        # Verify if verify_element is present
        if v_elm:
            time.sleep(navigate_interval)
            read_text = dut.GetText(v_elm_type, v_elm)
            if not (read_text == v_elm_name):
                logger.Log("Failed to display {}".format(v_elm_name))
                all_done = False
                break
            else:
                logger.Log("{} Screen displayed successfully".format(v_elm_name))
    return all_done

def verify_epg(dut, logger):
    '''
    to verify the EPG List is present
    '''
    if WaitForElement(
        dut, MobileScriptingLibrary.Constants.ElementType.Name,
        IOSConfig.DAYPICKER_TODAY, "Today Label",
        IOSConfig.DEFAULT_SLEEP_TIME, logger):
        elements_to_verify = (
            (MobileScriptingLibrary.Constants.ElementType.Name, IOSConfig.DAYPICKER_TODAY),
        )

        return are_all_elements_present(dut, elements_to_verify)
    else:
        return False

def video_player_loaded(dut, logger, check=3):
    result = False
    time.sleep(IOSConfig.DEFAULT_WAIT_TIME)

    counter = check
    while counter:
        tapped = dut.Tap(*IOSConfig.CORD_VOD_PROGRAMME)
        if tapped:
            if dut.IsElementPresent(
                MobileScriptingLibrary.Constants.ElementType.Name,
                IOSConfig.PLAYBACK_PROGRESS_BAR):
                result = True
                break
        if not result:
            counter -= 1
    if result:
        logger.Log("Video player is loaded")
    else:
        logger.Log("Video player not loaded")
    return result


def is_movie_details(dut):
    elements_to_verify = (
        (MobileScriptingLibrary.Constants.ElementType.Name, IOSConfig.PGM_DETAILS_MORE_ACTION_BTN),
        (MobileScriptingLibrary.Constants.ElementType.Name, IOSConfig.ASSET_DETAILS_PLAYBACK_BTN)
    )

    return are_all_elements_present(dut, elements_to_verify)


# ******************** get_download_status ********************

def get_download_status(dut, req_status, logger):
    '''
    get_download_status - retruns the current download status
    :param msl: library
    :param req_status: "Queued" / "Downloading" / "Downloaded" / "Interrupted"
    :param logger: logger
    :return:  True if present, else False
    '''


    dl_status = False
    logger.Log("Getting the Download Status")
    dl_message = get_download_status_details_page(dut, logger)

    for i in range(3):
        dut.Tap(*IOSConfig.CORD_ESCAPE_MORE_INFO_MENU)

    time.sleep(IOSConfig.DEFAULT_WAIT_TIME)
    if req_status == DownloadStatus.QUEUED:
        return True
    if req_status == DownloadStatus.INPROGRESS:
        return True
    if req_status == DownloadStatus.DOWNLOADED:
        return True
    return False


def wait_for_detect_motion(dut, rectangle_coords, screen_shot_count=2,
                  screen_shot_interval=0, precision=90, logger=None, iter_count = 2):
    """
        Takes screenshots and calls SkyUtils API to detect motion.
        Returns True or False
        :param dut: dut object created by MobileScriptingLibrary.MobileDUT()
        :param rectangle_coords: Coordinates in the screen
        :param screen_shot_count: Number of screenshots to be taken
        :param screen_shot_interval: Number of seconds to sleep bw screenshots
        :param precision: Percentage of precision needed in image comparison
        :param iter_count: Number of times to call the detect_motion() method
        """
    is_motion = False
    for i in range(iter_count):
        is_motion = detect_motion(dut, rectangle_coords, 2, 5, 100, logger)
        if is_motion:
            break
        else:
            time.sleep(IOSConfig.DEFAULT_WAIT_TIME)
    return is_motion

def sleep_for_max_time(dut, time_in_min, tap_needed = False):
    time_to_wait = (time_in_min * 60)/5

    for i in range (time_to_wait):
        time.sleep(IOSConfig.SLEEP_TIME)
        if tap_needed:
            dut.Tap(IOSConfig.CORD_VOD_PROGRAMME[0], IOSConfig.CORD_VOD_PROGRAMME[1])


# ******************** goto_movie ********************
def goto_movie(dut, MobileScriptingLibrary, movie_name, is_back, logger):
    if is_back:
        back_to_skycinema = tap_if_present(
            dut,
            MobileScriptingLibrary.Constants.ElementType.Name,
            IOSConfig.BACK_BTN_ON_SKYCINEMA,
            "Back Button",
            logger
        )
        if not back_to_skycinema:
            return back_to_skycinema

    time.sleep(IOSConfig.DEFAULT_WAIT_TIME)
    tapped = tap_if_present(
        dut,
        MobileScriptingLibrary.Constants.ElementType.Name,
        movie_name,
        movie_name,
        logger,
    )
    if not tapped:
        logger.Log("Tap unsuccessful")
        return tapped

    time.sleep(IOSConfig.DEFAULT_WAIT_TIME)
    is_details_screen = is_movie_details(dut)
    if not (is_details_screen):
        logger.Log("Movie Details Screen not displayed, Tapping again on the Movie")
        tapped = tap_if_present(
            dut,
            MobileScriptingLibrary.Constants.ElementType.Name,
            movie_name,
            movie_name,
            logger,
        )
        is_details_screen = is_movie_details(dut)
        if not is_details_screen:
            logger.Log("Failed to load the Details Screen")
            return  is_details_screen

    logger.Log("Displayed Sky Cinema Movie Details Screen")
    return is_details_screen


def add_movie_to_dwn_queue(dut, logger, cancel=False, delete=False):
    """
    This function shall be called from Movie Details page -
    where there is a more info button
    """
    log_screen_shot(dut)
    status = get_download_status_details_page(dut, logger)
    if (status == DownloadStatus.INPROGRESS or status == DownloadStatus.QUEUED):
        if cancel:
            tapped = dut.TapElement(
                MobileScriptingLibrary.Constants.ElementType.Name,
                IOSConfig.CANCEL_DOWNLOAD_BTN
            )
            if not tapped:
                raise APIFailed("Failed to Cancel the iPad Download")
            logger.Log("Cancelled current iPad Download")
        else:
            # tapped = dut.TapElement(
            #     MobileScriptingLibrary.Constants.ElementType.Name,
            #     IOSConfig.PGM_DETAILS_MORE_ACTION_BTN,
            # )
            tapped = dut.Tap(*IOSConfig.CORD_ESCAPE_MORE_INFO_MENU)
            time.sleep(IOSConfig.DEFAULT_WAIT_TIME)
            if not tapped:
                raise APIFailed("Failed to tap on More Actions button")
            return False
    if status == DownloadStatus.DOWNLOADED:
        if delete:
            tapped = dut.TapElement(
                MobileScriptingLibrary.Constants.ElementType.Name,
                IOSConfig.DELETE_DOWNLOAD_BTN
            )
            if not tapped:
                raise APIFailed("Failed to Delete downloaded movie")
            logger.Log("Deleted downloaded movie")
        else:
            # tapped = dut.TapElement(
            #     MobileScriptingLibrary.Constants.ElementType.Name,
            #     IOSConfig.PGM_DETAILS_MORE_ACTION_BTN,
            # )
            tapped = dut.Tap(*IOSConfig.CORD_ESCAPE_MORE_INFO_MENU)
            if not tapped:
                raise APIFailed("Failed to tap on More Actions button")
            return False
    # Now press download button
    tapped = dut.TapElement(
        MobileScriptingLibrary.Constants.ElementType.Name,
        IOSConfig.ASSET_DOWNLOAD_BTN)
    if not tapped:
        raise APIFailed("Failed to Tap on Download menu")

    # check for alerts
    # alert = WaitForElement(MobileScriptingLibrary.Constants.ElementType.Name,
    #     IOSConfig.X_ALERT_WINDOW, 10)

    wait_count = 3
    alert = False
    while wait_count:
        if dut.IsElementPresent(MobileScriptingLibrary.Constants.ElementType.XPath,
                IOSConfig.X_ALERT_WINDOW):
            alert = True
            break
        else:
            wait_count -= 1
            time.sleep(5)
    log_screen_shot(dut)
    if alert:
        logger.Log("This item has exceeded download limit")
        tapped = dut.TapElement(
            MobileScriptingLibrary.Constants.ElementType.Name,
            IOSConfig.DOWNLOAD_LIMIT_OK_BTN)
        if not tapped:
            raise APIFailed("Failed to clear Alert")
        return False
    else:
        return True

def initiate_download(dut, logger):

    tapped = tap_if_present(
        dut, MobileScriptingLibrary.Constants.ElementType.Name,
        IOSConfig.PGM_DETAILS_MORE_ACTION_BTN,
        "More Actions Button", logger)
    if not tapped:
        logger.Log("Tap unsuccessful")
        return tapped

    if not dut.IsElementPresent(
        MobileScriptingLibrary.Constants.ElementType.Name,
        IOSConfig.ASSET_DOWNLOAD_BTN
    ):
        logger.Log("Failed to find 'Download to iPad' button")
        if dut.IsElementPresent(
                MobileScriptingLibrary.Constants.ElementType.Name,
                IOSConfig.CANCEL_DOWNLOAD_BTN
        ):
            logger.Log("'Cancel iPad Download' button is available")
            tapped = dut.TapElement(
                MobileScriptingLibrary.Constants.ElementType.Name,
                IOSConfig.CANCEL_DOWNLOAD_BTN
            )
            if not tapped:
                logger.Log("Failed to Cancel the iPad Download")
                return tapped
            logger.Log("Cancelled the iPad Download")
        else:
            if dut.IsElementPresent(
                    MobileScriptingLibrary.Constants.ElementType.Name,
                    IOSConfig.DELETE_DOWNLOAD_BTN
            ):
                tapped = dut.TapElement(
                    MobileScriptingLibrary.Constants.ElementType.Name,
                    IOSConfig.DELETE_DOWNLOAD_BTN
                )
                if not tapped:
                    logger.Log("Failed to Delete the Download from iPad")
                    return tapped
                logger.Log("Deleted the Download from iPad")

        if dut.IsElementPresent(
            MobileScriptingLibrary.Constants.ElementType.Name,
            IOSConfig.PGM_DETAILS_MORE_ACTION_BTN
        ):
            if not dut.TapElement(
                    MobileScriptingLibrary.Constants.ElementType.Name,
                    IOSConfig.PGM_DETAILS_MORE_ACTION_BTN
            ):
                logger.Log("Could not tap on More Action Button after deleting/Cancelling the Download")
                return False

    # if 'Download to iPad' is present
    tapped = tap_if_present(
        dut,
        MobileScriptingLibrary.Constants.ElementType.Name,
        IOSConfig.ASSET_DOWNLOAD_BTN,
        IOSConfig.ASSET_DOWNLOAD_BTN,
        logger)
    if not tapped:
        return tapped

    #Waiting for Download Status to update
    time.sleep(IOSConfig.AVG_WAIT_FOR_ELEMENT_TO_LOAD)
    if not get_download_status(dut, DownloadStatus.INPROGRESS, logger):
        logger.Log("Downloading to iPad failed")
        if is_max_dl_limit(dut):
            logger.Log("This movie has downloaded maximum times")
            tapped = dut.TapElement(
                MobileScriptingLibrary.Constants.ElementType.Name,
                IOSConfig.DOWNLOAD_LIMIT_OK_BTN
            )
            if not tapped:
                return tapped
        else:
            return False
    return True


def is_max_dl_limit(dut):
    for i in range(5):
        if dut.IsElementPresent(
        MobileScriptingLibrary.Constants.ElementType.XPath,
        IOSConfig.X_DWN_ALERT_WINDOW
     ):
            return True

    return False


def verify_movie_details_reached(dut):
    #  Verify if movie detail screen is reached
    found = False
    trial = IOSConfig.DEFAULT_TRIAL
    elements = (
        (MobileScriptingLibrary.Constants.ElementType.Name, IOSConfig.PGM_DETAILS_MORE_ACTION_BTN),
        (MobileScriptingLibrary.Constants.ElementType.Name, IOSConfig.ASSET_DETAILS_PLAYBACK_BTN)
    )
    while trial:
        time.sleep(IOSConfig.MIN_SLEEP_TIME)
        found = are_all_elements_present(dut, elements)
        if found:
            break
        trial -= 1
    return found

def is_valid_grid(dut):
    # Check if there is a main Title
    is_valid = False
    page_name = dut.GetText(
        MobileScriptingLibrary.Constants.ElementType.Name,
        IOSConfig.MAIN_NAV_TITLE)
    if page_name:
        # Check if there is an item (First one)
        page_item = dut.GetText(
            MobileScriptingLibrary.Constants.ElementType.XPath,
            IOSConfig.X_ASSET_IN_SKYCINEMA.format(1))
        if page_item:
            is_valid = True
    return is_valid, page_name

def init_movie_download(dut, logger, cancel=False, delete=False, start_page=IOSConfig.BTN_BACK_TO_SKY_CINEMA):
    """
        This function shall be called from a category in Sky Cinema.
        It will traverse through the grid until a movie is successfully queued
        for download.
        :param dut: MobileScriptingLibrary.MobileDUT object
        :param logger: Logger object
        :param cancel: Should cancel the download if it is in progress
        :param delete: Should delete the movie if it is downloaded
    """
    index = 1
    movie_index = 1
    MAX_INDEX = 10
    MAX_MOVIE_INDEX = 25
    visited = []
    download_added = False
    movie = None
    while True:
        logger.Log("Trying to get movie name to download")
        x_movie = IOSConfig.X_ASSET_IN_SKYCINEMA.format(movie_index)
        movie = dut.GetText(
            MobileScriptingLibrary.Constants.ElementType.XPath, x_movie)
        if movie and (movie in visited):
            # This movie is already visited. Came again after swipe
            movie_index = len(visited) - visited.index(movie) + 1
            x_movie = IOSConfig.X_ASSET_IN_SKYCINEMA.format(movie_index)
            movie = dut.GetText(
                MobileScriptingLibrary.Constants.ElementType.XPath, x_movie)
        if not movie:
            logger.Log("Failed to get movie name")
            break
        visited.append(movie)
        x_grid_item = IOSConfig.X_GRID_ITEM
        if "'" in movie:
            x_grid_item = x_grid_item.replace("'", '"')
        movie_tapped = dut.TapElement(
            MobileScriptingLibrary.Constants.ElementType.XPath, x_grid_item.format(movie))
        if not movie_tapped:
            logger.Log("Failed to tap on {}".format(movie))
            break
        #  Verify if movie details page is reached
        found = verify_movie_details_reached(dut)
        if found:
            try:
                added = add_movie_to_dwn_queue(dut, logger, cancel, delete)
                logger.Log("Add movie to download queue: "+str(added))
            except Exception as e:
                logger.Log(str(e))
            if added:
                download_added = True
                break
        else: # Not in a Movie details screen
            # Check if this is a category
            valid_grid, title = is_valid_grid(dut)
            if valid_grid:
                download_added, movie = init_movie_download(
                    dut, logger, start_page=title)
                if download_added:
                    break

        # Go back to start grid page
        x_back_to_parent_grid = IOSConfig.X_BACK_TO_PARENT_GRID
        if "'" in start_page:
            x_back_to_parent_grid = x_back_to_parent_grid.replace("'", '"')
        tapped = dut.TapElement(
                MobileScriptingLibrary.Constants.ElementType.XPath,
                x_back_to_parent_grid.format(start_page))
        if not tapped:
            break

        index += 1  # For checking next item
        movie_index += 1
        if index > MAX_INDEX:
            # Swipe up and reassign index
            swiped = dut.Swipe(*IOSConfig.CORD_SWIPE_GRID_UP)
            if not swiped:
                logger.Log("Failed to swipe up")
                break
            index = 1
            movie_index = 1
        if movie_index > MAX_MOVIE_INDEX:
            movie_index = 1
    return download_added, movie


def download_movie(dut, logger, movie_index = 1):
    init_dl = False
    x_movie_path = IOSConfig.XPATH_OF_ASSET_ON_SKYCINEMA
    for movie_index in range(1,IOSConfig.TOTAL_SKY_CINEMA_MOVIES):
        x_movie = x_movie_path + "XCUIElementTypeCell[" + str(movie_index) + "]"
        movie = dut.GetText(
            MobileScriptingLibrary.Constants.ElementType.XPath,
            x_movie
        )

        movie_details = goto_movie(dut, MobileScriptingLibrary, movie, False, logger)
        if not movie_details:
            logger.Log("Failed to go to Movie Details Page")
            return movie_details
        init_dl = initiate_download(dut, logger)
        if init_dl:
            break
    return  init_dl


def cancel_download(dut, logger):
    tapped = tap_if_present(
        dut,
        MobileScriptingLibrary.Constants.ElementType.Name,
        IOSConfig.PGM_DETAILS_MORE_ACTION_BTN,
        IOSConfig.PGM_DETAILS_MORE_ACTION_BTN,
        logger)

    if not tapped:
        logger.Log("Tap unsuccessful")
        return

    time.sleep(IOSConfig.DEFAULT_WAIT_TIME)
    tapped = tap_if_present(
        dut,
        MobileScriptingLibrary.Constants.ElementType.Name,
        IOSConfig.CANCEL_DOWNLOAD_BTN,
        IOSConfig.CANCEL_DOWNLOAD_BTN,
        logger
    )
    if not tapped:
        logger.Log("Tap unsuccessful")
    return tapped

#****************** get_download_status_details_page ****************
def get_download_status_details_page(dut, logger):
    tapped = tap_if_present(
        dut, MobileScriptingLibrary.Constants.ElementType.Name,
        IOSConfig.PGM_DETAILS_MORE_ACTION_BTN,
        "More Actions Button", logger)
    if not tapped:
        logger.Log("Tap unsuccessful")
        return tapped

    if  dut.IsElementPresent(
        MobileScriptingLibrary.Constants.ElementType.Name,
        IOSConfig.ASSET_DOWNLOAD_BTN
    ):
        return DownloadStatus.AVAILABLE
    elif dut.IsElementPresent(
        MobileScriptingLibrary.Constants.ElementType.Name,
        IOSConfig.DELETE_DOWNLOAD_BTN
    ):
        return DownloadStatus.DOWNLOADED
    elif dut.IsElementPresent(
        MobileScriptingLibrary.Constants.ElementType.Name,
        IOSConfig.CANCEL_DOWNLOAD_BTN
    ):
        return DownloadStatus.QUEUED

def wait_for_download_complete(dut,logger):
    #Waiting for download to complete
    MAX_WAIT_TIME = 60*60 # 1 hour - 3 hr changed to 1hr
    start_time = time.time()
    timeout = start_time + MAX_WAIT_TIME
    while(True):
        current_time = time.time()
        if current_time > timeout:
            logger.Log("Timeout {}s reached while waiting for download".format(timeout))
            break
        if dut.IsElementPresent(
                MobileScriptingLibrary.Constants.ElementType.Name,
                IOSConfig.ASSET_DOWNLOAD_COMPLETED):
            logger.Log("Download complete")
            return True
            break
        else:
            # tapped = tap_if_present(
            #     dut, MobileScriptingLibrary.Constants.ElementType.Name,
            #     IOSConfig.PGM_DETAILS_MORE_ACTION_BTN,
            #     "More Actions Button", logger, step_no)
            # if not tapped:
            #     return False
            # if not dut.IsElementPresent(
            #     MobileScriptingLibrary.Constants.ElementType.Name,
            #     IOSConfig.ASSET_DOWNLOAD_CANCEL_BTN):
            #     return False
            # logger.Log("Cancel ipad download found")
            # # tapped = tap_if_present(
            # #     dut, MobileScriptingLibrary.Constants.ElementType.Name,
            # #     IOSConfig.PGM_DETAILS_MORE_ACTION_BTN,
            # #     "More Actions Button", logger, step_no)
            # tapped = dut.Tap(*IOSConfig.CORD_ESCAPE_MORE_INFO_MENU)
            # if not tapped:
            #     return False
            time.sleep(IOSConfig.DEFAULT_DOWNLOAD_WAITTIME)

def goto_downloads(dut, logger):
    navigate_list = (
        (
            MobileScriptingLibrary.Constants.ElementType.Name,
            IOSConfig.HOMESCREEN_DOWNLOADS, IOSConfig.HOMESCREEN_DOWNLOADS,
            MobileScriptingLibrary.Constants.ElementType.Name,
            IOSConfig.MAIN_NAV_TITLE, IOSConfig.HOMESCREEN_DOWNLOADS
        ),
    )

    is_navigated = navigate(dut, navigate_list, logger=logger)
    if not is_navigated:
        logger.Log("Failed to go to Downloads")
    return is_navigated

def clear_downloads(dut, logger, cancel=True, delete=True):
    # This function shall be called from home page
    if not (cancel or delete):
        return False
    reached_downloads = goto_downloads(dut, logger)
    if not reached_downloads:
        logger.Log("Failed to go to Downloads Page")
        return False
    all_cleared = True
    while dut.IsElementPresent( # Check if there is a More Action Btn
        MobileScriptingLibrary.Constants.ElementType.Name,
        IOSConfig.PGM_DETAILS_MORE_ACTION_BTN):
        # Tap on it
        tapped = dut.TapElement(MobileScriptingLibrary.Constants.ElementType.Name,
                       IOSConfig.PGM_DETAILS_MORE_ACTION_BTN)
        if not tapped:
            all_cleared = False
        time.sleep(IOSConfig.MD_SLEEP_TIME)

        if delete and dut.IsElementPresent( # Delete if it is downloaded
            MobileScriptingLibrary.Constants.ElementType.Name,
            IOSConfig.DELETE_DOWNLOAD_BTN):

            tapped = dut.TapElement(MobileScriptingLibrary.Constants.ElementType.Name,
                           IOSConfig.DELETE_DOWNLOAD_BTN)
            if not tapped:
                all_cleared = False
            time.sleep(IOSConfig.MD_SLEEP_TIME)
            continue

        if cancel and dut.IsElementPresent( # Cancel if it is downloading
            MobileScriptingLibrary.Constants.ElementType.Name,
            IOSConfig.CANCEL_DOWNLOAD_BTN):

            tapped = dut.TapElement(MobileScriptingLibrary.Constants.ElementType.Name,
                           IOSConfig.CANCEL_DOWNLOAD_BTN)
            if not tapped:
                all_cleared = False
            time.sleep(IOSConfig.MD_SLEEP_TIME)
            continue
    if all_cleared:
        # Go Back to Home
        if dut.IsElementPresent(MobileScriptingLibrary.Constants.ElementType.Name,
            IOSConfig.APP_HOME):

            tapped = dut.TapElement(MobileScriptingLibrary.Constants.ElementType.Name,
                           IOSConfig.APP_HOME)
            if not tapped:
                all_cleared = False
            time.sleep(IOSConfig.MD_SLEEP_TIME)
    return all_cleared


def clear_download_from_details_page(dut, logger):
    # This function shall be called from a movie's details page
    # Tap more info btn
    present = dut.IsElementPresent( # Check if there is a More Info Btn
        MobileScriptingLibrary.Constants.ElementType.Name,
        IOSConfig.MORE_INFO_BUTTON)
    if not present:
        logger.Log("Failed to find More-Action-Button")
        return False
    tapped = dut.TapElement(MobileScriptingLibrary.Constants.ElementType.Name,
                   IOSConfig.MORE_INFO_BUTTON)
    if not tapped:
        logger.Log("Failed to tap on More-Action-Button")
        return False
    time.sleep(IOSConfig.MD_SLEEP_TIME)

    if dut.IsElementPresent( # Check if there is a Cancel btn
        MobileScriptingLibrary.Constants.ElementType.Name,
        IOSConfig.CANCEL_DOWNLOAD_BTN):
        # Tap on it
        tapped = dut.TapElement(MobileScriptingLibrary.Constants.ElementType.Name,
                       IOSConfig.CANCEL_DOWNLOAD_BTN)
        if tapped:
            time.sleep(IOSConfig.MD_SLEEP_TIME)
            return True
        else:
            logger.Log("Failed to cancel asset download")
            return False

    if dut.IsElementPresent( # Check if there is a Cancel btn
        MobileScriptingLibrary.Constants.ElementType.Name,
        IOSConfig.DELETE_DOWNLOAD_BTN):
        # Tap on it
        tapped = dut.TapElement(MobileScriptingLibrary.Constants.ElementType.Name,
                       IOSConfig.DELETE_DOWNLOAD_BTN)
        if tapped:
            return True
        else:
            logger.Log("Failed to delete asset")
            return False

def tap_popup_init_dl_playback(dut, logger):

    status =  WaitForElement(
        dut,
        MobileScriptingLibrary.Constants.ElementType.Name,
        IOSConfig.CONTINUE_PLAYBACK_FIRSTTIME,
        "Asset will expire in 48 Hours",
        IOSConfig.AVG_WAIT_FOR_ELEMENT_TO_LOAD,
        logger
    )
    if status:
        logger.Log("'This asset will expire in 48 hrs' message displayed")
        continue_playback = tap_if_present(
            dut,
            MobileScriptingLibrary.Constants.ElementType.Name,
            IOSConfig.CONTINUE_PLAYBACK_FIRSTTIME,
            IOSConfig.CONTINUE_PLAYBACK_FIRSTTIME,
            logger
        )
        if not continue_playback:
            logger.Log("Failed to tap on the message")
        return (status and continue_playback)
    else:
        logger.Log("'This asset will expire in 48 hrs' message not displayed")
        return not status


def sendpin(dut, pin, logger):
    tapped = False
    for p in pin:
        tapped = dut.TapElement(MobileScriptingLibrary.Constants.ElementType.Name, p)
        if not tapped:
            break
    return tapped
