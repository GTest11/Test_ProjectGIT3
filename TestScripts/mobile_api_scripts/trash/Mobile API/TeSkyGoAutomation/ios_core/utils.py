import clr, time, os, tempfile
clr.AddReference("SkyUtils")
from SkyUtils import ImageUtils, MotionDetector
from System.Drawing import Rectangle
from datetime import datetime
from ios_core.config import IOSConfig

def getNowStr():
    return datetime.utcnow().strftime("%d%m%Y_%H%M%S")


def log_screen_shot(dut, img_str=None):
    if not img_str:
        img_str = dut.GetScreenshot()
    dut.validator.UploadScreenshot("SkyGo", img_str)


def take_screen_shot(dut):
    try:
        img_str = dut.GetScreenshot()
        ss_filename = os.path.join(IOSConfig.SCREENSHOT_BASE_DIR,
                                   IOSConfig.SCREENSHOT_DIRNAME,
                                   getNowStr()+".png")
        ImageUtils.SaveImage(img_str, ss_filename)
        return ss_filename
    except Exception as e:
        return False

def detect_change(rectangle_coords, saved_screenshots, precision):
    try:
        roi = Rectangle(*rectangle_coords) #  Set Region of Interest
        md = MotionDetector(roi, precision)
        motion_detected = False
        if md.DetectMotion(saved_screenshots):
            motion_detected = True
        return motion_detected
    except Exception as e:
        return False

def detect_motion(dut, rectangle_coords, screen_shot_count=2,
                  screen_shot_interval=0, precision=90, logger=None):
    """
    Takes screenshots and calls SkyUtils API to detect motion.
    Returns True or False
    :param dut: dut object created by MobileScriptingLibrary.MobileDUT()
    :param rectangle_coords: Coordinates in the screen
    :param screen_shot_count: Number of screenshots to be taken
    :param screen_shot_interval: Number of seconds to sleep bw screenshots
    :param precision: Percentage of precision needed in image comparison
    """

    screenshots = []
    last_index = screen_shot_count - 1
    ss_save_path = os.path.join(IOSConfig.SCREENSHOT_BASE_DIR, IOSConfig.SCREENSHOT_DIRNAME)
    if not os.path.exists(ss_save_path):
        os.makedirs(ss_save_path)
    for index in range(screen_shot_count):
        img_str = dut.GetScreenshot()
        screenshots.append( (img_str, getNowStr()) )
        if screen_shot_interval and index < last_index:
            logger.Log("Sleeping for "+str(screen_shot_interval)+" seconds" )
            time.sleep(screen_shot_interval)
    saved_screenshots = []
    for ss, ts in screenshots:
        ss_filename = os.path.join(ss_save_path, ts+".png")
        ImageUtils.SaveImage(ss, ss_filename)
        if logger:
            logger.Log("Screenshot saved : "+ ss_filename )
        saved_screenshots.append(ss_filename)

    roi = Rectangle(*rectangle_coords) #  Set Region of Interest
    md = MotionDetector(roi, precision)
    motion_detected = False
    if md.DetectMotion(saved_screenshots):
        motion_detected = True

    # Log Screenshots
    for ss, ts in screenshots:
        log_screen_shot(dut, ss)

    # Remove screenshots
    # for ss in saved_screenshots:
    #     os.remove(ss)

    return motion_detected
