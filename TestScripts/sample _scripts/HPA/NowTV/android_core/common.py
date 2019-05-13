# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Common functions and classes for scripts running in Android devices
#
# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
import time, clr
clr.AddReference("MobileScriptingLibrary")
import MobileScriptingLibrary
logger = MobileScriptingLibrary.Logger()

from android_core.config import ConfigBase as ConfFile


class TestResult(object):
    PASSED = "Passed"
    FAILED = "Failed"
    ABORTED = "Aborted"
    ERROR = "Error"


class QoEParams(object):
    START_UP_TIME = "startup_time"
    START_UP_FAILURE = "startup_failure"
    BUFFERING_TIME = "buffering_time"
    BUFFERING_RATIO = "buffering_ratio"
    PLAYBACK_FAILURE = "playback_failure"
    STATUS = "Status"


def Click(dut_object, elementType, elementId, retryCount = 3):
    for i in range(retryCount):
        if(dut_object.Click(elementType,elementId)):
            return True
        else:
            time.sleep(1)
    return False

def GetText(dut_object, elementType, elementId, retryCount = 3):
    value = ''
    for i in range(retryCount):
        value = dut_object.GetText(elementType,elementId)
        if(value != ''):
            return value
        else:
            time.sleep(1)
    return value


def ClickWithIndex(dut_object, elementType, elementId, index, retryCount = 3):
    for i in range(retryCount):
        if(dut_object.Click(elementType,elementId, index)):
            return True
        else:
            time.sleep(1)
    return False


def get_movies_tile(i):
        MOVIES_TILE = "//android.support.v7.widget.RecyclerView/android.widget.FrameLayout[" + str(i) + "]/android.widget.LinearLayout/android.widget.ImageView"
        return MOVIES_TILE


def get_movies_live_tile(i):
        movies_tile = '//android.widget.LinearLayout['+ str(i) +']/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.RelativeLayout[1]'
        return movies_tile


def get_ent_live_tile(i):
    ent_tile = '//android.widget.LinearLayout['+ str(i) +']/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.FrameLayout/android.widget.LinearLayout'
    return ent_tile

def get_kids_live_tile(i):
    kids_tile='//android.support.v7.widget.RecyclerView[@content-desc="Live"]/android.widget.LinearLayout['+ str(i) +']/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ImageView[1]'
    return kids_tile

def get_text_kids_item(i):
    kids_text='//android.support.v7.widget.RecyclerView[@content-desc="Live"]/android.widget.LinearLayout[' + str(i) + ']/android.widget.TextView'
    return kids_text

def get_kids_channel(i):
    kids_channel='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v4.view.ViewPager/android.widget.ViewSwitcher/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[' + str(i) + ']/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]'
    return kids_channel

def send_back_key(dut_object, maxcount=ConfFile.TIMEOUT):
    back_play_count = 0
    while not dut_object.SendAndroidKeyCode(
            "Keycode_BACK") and back_play_count < maxcount:
        back_play_count += 1
        logger.Log("Sending Back key failed...trying again")
        if back_play_count == maxcount:
            return False
    else:
        return True

class QoEScenario(object):
    CATEGORY_NAME = ""
    ASSET_TYPE = ""
    CHANNEL_LIST = []
    TEST_VECTOR_NAME = []
    USECASE = 0
    CHANNEL_PLAY_TIME = 0
    LOOP_COUNT = 0
    TEST_VECTOR_OBJLIST = []


class TestVector(object):
    def __init__(self, number):
        self.number = number
        self.CHOKE_TIME = 0
        self.LIMITED_BW_UP = 0
        self.LIMITED_BW_DOWN = 0
        self.DELAY = 0
        self.JITTER = 0
        self.PACKET_LOSS = 0


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
    time.sleep(ConfFile.MAXTIMEOUT)
    # Check presence
    present = is_present(dut, elm_type, elm, elm_name, logger)
    if present:
        # Tap on the element
        tapped = tap(dut, elm_type, elm, elm_name, logger)
        if tapped:
            result = True
    return result

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
    for i in range(0, 2):
        if not dut.IsElementPresent(elm_type, elm):
            logger.Log("'{}' not found".format(elm_name))
        else:
            logger.Log("'{}' found".format(elm_name))
            result = True
            break
        time.sleep(ConfFile.TIMEOUT)
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

def WaitForElement(dut, elm_type, elm, elm_name, wait_time, interval=2):
    """
    A wrapper for checking IsElementPresent for wait_time seconds
    :param dut: MobileScriptingLibrary.MobileDUT object
    :param wait_time: wait time in seconds
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