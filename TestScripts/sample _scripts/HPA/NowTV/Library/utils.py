import clr, time, os, tempfile
clr.AddReference("SkyUtils\SkyUtils")
from SkyUtils import ImageUtils, MotionDetector
from datetime import datetime
from android_core.config import AndroidConfig

def getNowStr():
    return datetime.utcnow().strftime("%d%m%Y_%H%M%S")


def detect_motion(dut,x,y,w,h, screen_shot_count=2,
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
    ss_save_path = os.path.join(AndroidConfig.SCREENSHOT_BASE_DIR, AndroidConfig.SCREENSHOT_DIRNAME)
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

    md = MotionDetector(x,y,w,h, precision)
    motion_detected = False
    if md.DetectMotion(saved_screenshots):
        motion_detected = True

    # Remove screenshots
    # for ss in saved_screenshots:
    #     os.remove(ss)

    return motion_detected
