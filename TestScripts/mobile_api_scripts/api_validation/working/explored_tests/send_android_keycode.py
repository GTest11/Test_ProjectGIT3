# '''''''''''''''''''''''''''TEST CASE DETAILS'''''''''''''''''''''''''''''''''''''''''
# Author            : Shameena HA
# Date              :   29-11-2018
# Script Version    : 1.0
# APIs covered      :   SendAndroidKeyCode - Keycode_MEDIA_PAUSE,
#                           Keycode_MEDIA_PLAY_PAUSE,
#                           Keycode_MEDIA_FAST_FORWARD,
#                           Keycode_MEDIA_PLAY,
#                           Keycode_MEDIA_REWIND,
#                           Keycode_MEDIA_STOP
# Test Scenario: A few available KeyCodes, wrong KeyCode
#

# '''''''''''''''''''''''''''TEST CASE DETAILS' - END '''''''''''''''''''''''''''''''''

import os
import sys
import time
sys.path.append('../')

from library.api_test_base import apiTestBase

class api_test(apiTestBase):

    # the class which handles the script intention.
    # this overrides base class run_api_test()

    # class variables
    apis = ('SendAndroidKeyCode',)
    script_name = os.path.basename(__file__)


    def playback(self):
        motion = True
        if not self.dut.Tap(*self.config.C_TAP_PLAYBACK):
            self.logger.Error("Failed to start playback")
            motion =  False
            return motion

        motion = self.lib.verify_playback()
        if not motion:
            self.logger.Error("No motion")
        else:
            self.logger.Log("Media playback started")
        return motion


    def run_api_test(self):
        '''
        Calls media Keycodes one by one
        :return:
        '''

        test_result = True
        motion = False

        try:
            platform = self.lib.get_dut_name()
            if platform == "iOS":
                self.lib.report("SendAndroidKeyCode API does not support iOS platform", "FAILED", ss_required=True)
                test_result = False
                return

            if not self.playback():
                self.lib.report("Video playback is not started, hence skipping the test", "FAILED", ss_required=True)
                test_result = False
                return
            playback_keys = self.config.keys_media

            # Pause
            sent  = self.lib.send_keycode(playback_keys['pause'])
            motion = self.lib.verify_playback()
            if sent and not motion:
                status = "PASSED"
            else:
                status = "FAILED"
                test_result = False
            self.lib.report(
                "SendAndroidKeyCode: Keycode_MEDIA_PAUSE", status, ss_required=True
            )
            time.sleep(3)

            # Play_pause - play starts
            sent = self.lib.send_keycode(playback_keys['play_pause'])
            motion = self.lib.verify_playback()
            if sent and motion:
                status = "PASSED"
            else:
                status = "FAILED"
                test_result = False
            self.lib.report(
                "SendAndroidKeyCode: Keycode_MEDIA_PLAY_PAUSE", status, ss_required=True
            )
            time.sleep(3)

            # Fast Forward
            sent = self.lib.send_keycode(playback_keys['fast_forward'])
            motion = self.lib.verify_playback()
            if sent and motion:
                status = "PASSED"
            else:
                status = "FAILED"
                test_result = False
            self.lib.report(
                "SendAndroidKeyCode: Keycode_MEDIA_FAST_FORWARD", status, ss_required=True
            )
            time.sleep(3)

            # Play_pause - expects media to be paused
            sent = self.lib.send_keycode(playback_keys['play_pause'])
            motion = self.lib.verify_playback()
            if sent and not motion:
                status = "PASSED"
            else:
                status = "FAILED"
                test_result = False
            self.lib.report(
                "SendAndroidKeyCode: Keycode_MEDIA_PLAY_PAUSE", status, ss_required=True
            )
            time.sleep(3)

            # Play
            sent = self.lib.send_keycode(playback_keys['play'])
            motion = self.lib.verify_playback()
            if sent and motion:
                status = "PASSED"
            else:
                status = "FAILED"
                test_result = False
            self.lib.report(
                "SendAndroidKeyCode: Keycode_MEDIA_PLAY", status, ss_required=True
            )
            time.sleep(3)

            # Rewind
            sent = self.lib.send_keycode(playback_keys['rewind'])
            motion = self.lib.verify_playback()
            if sent and motion:
                status = "PASSED"
            else:
                status = "FAILED"
                test_result = False
            self.lib.report(
                "SendAndroidKeyCode: Keycode_MEDIA_REWIND", status, ss_required=True
            )
            time.sleep(3)

            # Stop
            sent = self.lib.send_keycode(playback_keys['stop'])
            motion = self.lib.verify_playback()
            if sent and not motion:
                status = "PASSED"
            else:
                status = "FAILED"
                test_result = False
            self.lib.report(
                "SendAndroidKeyCode: Keycode_MEDIA_STOP", status, ss_required=True
            )

            # Wrong Keycode
            sent = self.lib.send_keycode(self.config.WRONG_KEYCODE)
            if not sent:
                status = "PASSED"
            else:
                status = "FAILED"
                test_result = False
            self.lib.report(
                "SendAndroidKeyCode: {}".format(self.config.WRONG_KEYCODE), status, ss_required=True
            )


        except Exception as e:
            self.logger.Log("Exception in run_api_test() " + str(e))
            test_result = False

        finally:
            self.test_result = test_result


def main():
    testobj = api_test()
    testobj.run_test(testobj.script_name, testobj.apis)


if __name__ == '__main__':
    main()
