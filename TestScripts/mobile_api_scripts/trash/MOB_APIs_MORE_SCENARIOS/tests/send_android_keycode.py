# '''''''''''''''''''''''''''TEST CASE DETAILS'''''''''''''''''''''''''''''''''''''''''
# Author            : Shameena HA
# Date              :   29-11-2018
# Script Version    : 1.0
# Modification details:
# APIs covered      :   "SendAndroidKeyCode"
# Test Scenario: "All keys",
#                 "Not existing key",

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


    def sendkeys_and_verify(self, search_text=None, compare_text=None):
        sent_and_ok = True
        try:
            keys_sent = self.lib.send_keys(self.config.search_txt_box,
                                           search_text
                                           )
            if not keys_sent:
                self.logger.Error("Failed to send the search text")
                sent_and_ok = False
                return



            sent_and_ok = self.verify_text(search_text, compare_text)
            # same = self.lib.gettext(
            #     self.config.search_box_with_text,
            #     search_text
            # ) == compare_text
            # if same:
            #     status = "PASSED"
            # else:
            #     status = "FAILED"
            #     sent_and_ok = False
            # self.lib.report("Failed to verify sent keys", status, ss_required=True)
            # if not same:
            #     return

        except Exception as e:
            self.logger.Error("Search text not found")
            sent_and_ok = False

        finally:
            return sent_and_ok


    def verify_text(self, search_text, compare_text=None):
        '''
        This compares the text in the edit box  with the given compare_text,
        and returns the comparison status

        :param search_text: the current text in the search box
        :param compare_text: the text to be compared with
        :return: True if both are same
                Else returns False
        '''


        verified = True
        try:
            same = self.gettext(
                self.config.search_box_with_text,
                search_text
            ) == compare_text
            if same:
                status = "PASSED"
            else:
                status = "FAILED"
                verified = False
            self.lib.report("Failed to verify text", status, ss_required=True)

        except Exception as e:
            self.logger.Error("Failed verify text {} ".format(compare_text) + str(e))
            verified = False

        finally:
            # return verified
            return verified


    def gettext(self, elm_name, txt=None):
        '''
        This verifies the selected property of the given element, and returns its status

        :param elm_name: name of element from which text has to be read
        :return: read string,
                else returns None
        '''


        status = "FAILED"
        text = None
        try:
            elm_type, type = self.lib.choose_elm_type(elm_name)
            if not type:
                self.logger.Error("Invalid element type")
                return False
            if type == 'xpath':
                elm = elm_name[type].format(txt)
            else:
                elm = elm_name[type]
            self.logger.Log("================  elm {}  ======================".format(elm))
            start_time = self.lib.gettimestamp()
            text = self.dut.GetText(elm_type, elm)
            end_time = self.lib.gettimestamp()

            if text:
                status = "PASSED"
            self.lib.report_api_status(start_time, end_time, "GetText", status, ss_required=True)

        except Exception as e:
            self.logger.Error("Error in searching for element" + str(e))
            text = None

        finally:
            return text


    def sendkeycode_playback(self):
        '''
        Sends and verifies the Keycodes during media playback

        :return: True if successfully sent and the expected response is obtained.
                Else returns False
        '''

        done = True
        step_fwd = False
        try:
            if not self.dut.Tap(*self.config.C_TAP_PLAYBACK):
                self.logger.Error("Failed to start playback")
                return False

            time.sleep(5)
            if not self.lib.verify_playback():
                self.logger.Error("Failed to verify the media playback")
                return False

            # pausing the playback
            start_time = self.lib.gettimestamp()
            sent = self.dut.SendAndroidKeyCode(self.config.keys['media'][0])
            end_time = self.lib.gettimestamp()
            playing =  self.lib.verify_playback()

            if sent and (not playing):
                status = "PASSED"
                step_fwd = True
            else:
                status = "FAILED"
                done = False
                step_fwd = False
            self.lib.report_api_status(start_time, end_time, self.config.keys['media'][0],status, ss_required=True)
            self.lib.report(self.config.keys['media'][0], status)

            if not step_fwd:
                return False

            # starting the playback using play/pause
            start_time = self.lib.gettimestamp()
            sent = self.dut.SendAndroidKeyCode(self.config.keys['media'][2])
            time.sleep(3) #wait before resuming playback
            end_time = self.lib.gettimestamp()
            playing = self.lib.verify_playback()
            if sent and playing:
                status = "PASSED"
                step_fwd = True
            else:
                status = "FAILED"
                done = False
                step_fwd = False
            self.lib.report_api_status(start_time, end_time, self.config.keys['media'][2],status, ss_required=True)
            self.lib.report(self.config.keys['media'][2], status)

            if not step_fwd:
                return False

            # pausing the playback using play/pause
            start_time = self.lib.gettimestamp()
            sent = self.dut.SendAndroidKeyCode(self.config.keys['media'][2])
            time.sleep(3)  # wait before resuming playback
            end_time = self.lib.gettimestamp()
            playing = self.lib.verify_playback()    # expects no playback
            if sent and (not playing):
                status = "PASSED"
                step_fwd = True
            else:
                status = "FAILED"
                done = False
                step_fwd = False
            self.lib.report_api_status(start_time, end_time, "PAUSE - " + self.config.keys['media'][2], status, ss_required=True)
            self.lib.report(self.config.keys['media'][2], status)

            if not step_fwd:
                return False

            # playback using media_play keycode
            start_time = self.lib.gettimestamp()
            sent = self.dut.SendAndroidKeyCode(self.config.keys['media'][1])
            time.sleep(3)  # wait before resuming playback
            end_time = self.lib.gettimestamp()
            playing = self.lib.verify_playback()
            if sent and playing:
                status = "PASSED"
            else:
                status = "FAILED"
                done = False
            self.lib.report_api_status(start_time, end_time, self.config.keys['media'][1], status,
                                       ss_required=True)
            self.lib.report(self.config.keys['media'][1], status)

        except Exception as e:
            self.logger.Error("Failed to verify during media playback")
            done = False
        finally:
            return done


    def playback(self):
        '''
        Playbacks next item, previous item, stops the playback

        :return: True if success, else False
        '''

        done = True
        try:

            tapped = self.lib.element_ops(self.config.bottom_nav_home_button, action='tap')
            if not tapped:
                self.logger.Error("Failed to tap on Home Button")
                return False

            if not self.dut.Tap(*self.config.C_TAP_PLAYBACK):
                self.logger.Error("Failed to start playback")
                return False

            time.sleep(5)
            if not self.lib.verify_playback():
                self.logger.Error("Failed to verify the media playback")
                return False

            start_time = self.lib.gettimestamp()
            sent = self.dut.SendAndroidKeyCode(self.config.keys['media'][4])
            end_time = self.lib.gettimestamp()
            playing = self.lib.verify_playback()
            if sent and (not playing):
                status = "PASSED"
            else:
                status = "FAILED"
                done = False

            self.lib.report_api_status(
                start_time, end_time,
                "SendAndroidKeyCode {}".format(self.config.keys['media'][4]),
                status, ss_required=True
            )
            self.lib.report(self.config.keys['media'][4], status)
            time.sleep(5)

            # next video - media_next, # previous video - media_previous
            media_keys = [self.config.keys['media'][4], self.config.keys['media'][5]]
            for key in media_keys:
                start_time = self.lib.gettimestamp()
                sent = self.dut.SendAndroidKeyCode(key)
                end_time = self.lib.gettimestamp()
                playing = self.lib.verify_playback()
                if sent and playing:
                    status = "PASSED"
                else:
                    status = "FAILED"
                    done = False

                self.lib.report_api_status(
                    start_time, end_time,
                    "SendAndroidKeyCode {}".format(key),
                    status, ss_required=True
                )
                self.lib.report(key, status)
                time.sleep(5) # sleep before next verification

            volume_keys = [self.config.keys['volume'][0],
                           self.config.keys['volume'][1],
                           self.config.keys['volume'][2],
                           ]
            for key in media_keys:
                start_time = self.lib.gettimestamp()
                sent = self.dut.SendAndroidKeyCode(key)
                end_time = self.lib.gettimestamp()

                # To get the screenshot with volume bar
                self.dut.validator.QuickCapture("volume_img")
                if sent:
                    status = "PASSED"
                else:
                    status = "FAILED"
                    done = False

                self.lib.report_api_status(
                    start_time, end_time,
                    "SendAndroidKeyCode {}".format(key),
                    status, ss_required=True
                )
                self.lib.report(key, status)
                time.sleep(3)

        except Exception as e:
            self.logger.Error("Failed to stop/playback the next/last item")
            done = False

        finally:
            return done


    def sendkeycode_text(self):

        test_result = True
        # params = self.config.get_dut_attr_params
        try:
            for i in range(0, 2):
                clicked = self.lib.element_ops(elm_name=self.config.search_icon, action='click')
                if not clicked:
                    self.logger.Error("Failed to click the Search Icon")
                    test_result = False
                    return False

                self.logger.Log("Clicked on the Search Icon")
                found = self.lib.is_present(self.config.search_txt_box)
                if not found:
                    self.logger.Error("Failed to find the Search Edit Box")
                    test_result = False
                    return False

                self.logger.Log("Search Edit Box displayed ------------- " + str(i))
                time.sleep(3) # wait before sending search text

                if i == 0:
                    send_and_check = self.sendkeys_and_verify(self.config.mid_search_text, compare_text=self.config.mid_search_text)
                    if not send_and_check:
                        self.logger.Error("Failed to send - {}".format(self.config.mid_search_text))
                        test_result = False
                        return False

                    # move_end
                    start_time = self.lib.gettimestamp()
                    sent = self.dut.SendAndroidKeyCode(self.config.keys['text'][0])
                    end_time = self.lib.gettimestamp()
                    if sent:
                        status = "PASSED"
                    else:
                        status = "FAILED"
                        self.logger.Error("Send key code MOVE_END - {}".format(sent))
                        test_result = False
                        return False
                    self.lib.report_api_status(
                        start_time, end_time,
                        "SendAndroidKeyCode {}".format(self.config.keys['text'][0]),
                        status, ss_required=True
                    )

                    # sending key again - Last word of search string
                    send_and_check = self.sendkeys_and_verify(
                        self.config.last_search_text,
                        compare_text=(self.config.mid_search_text + self.config.last_search_text)
                    )
                    if not send_and_check:
                        self.logger.Error("Failed to send - {}".format(self.config.last_search_text))
                        test_result = False
                        return False

                    # delete last char
                    start_time = self.lib.gettimestamp()
                    sent = self.dut.SendAndroidKeyCode(self.config.keys['text'][4])
                    end_time = self.lib.gettimestamp()
                    if sent:
                        status = "PASSED"
                    else:
                        status = "FAILED"
                        self.logger.Error("Send key code DEL - {}".format(sent))
                        test_result = False
                        return False
                    self.lib.report_api_status(
                        start_time, end_time,
                        "SendAndroidKeyCode {}".format(self.config.keys['text'][4]),
                        status, ss_required=True
                    )
                    comp_text = self.config.mid_search_text + self.config.last_search_text
                    verified = self.verify_text(
                        self.config.last_search_text,
                        compare_text=comp_text[:-1]
                    )
                    if not verified:
                        self.logger.Error("Failed to verify text - {}".format(comp_text[:-1]))
                        test_result = False
                        return False

                    # move to home and insert text
                    start_time = self.lib.gettimestamp()
                    sent = self.dut.SendAndroidKeyCode(self.config.keys['text'][2])
                    end_time = self.lib.gettimestamp()
                    if sent:
                        status = "PASSED"
                    else:
                        status = "FAILED"
                        self.logger.Error("Send key code MOVE_HOME - {}".format(sent))
                        test_result = False
                        return False
                    self.lib.report_api_status(
                        start_time, end_time,
                        "SendAndroidKeyCode {}".format(self.config.keys['text'][2]),
                        status, ss_required=True
                    )

                    # sending key again - First word of search string
                    send_and_check = self.sendkeys_and_verify(
                        self.config.first_search_text,
                        compare_text=self.config.first_search_text+self.config.mid_search_text+self.config.last_search_text[0:-1]
                    )
                    if not send_and_check:
                        self.logger.Error("Failed to send - {}".format(self.config.search_text[:-1]))
                        test_result = False
                        return False

                    # deleting first char and verify
                    start_time = self.lib.gettimestamp()
                    sent = self.dut.SendAndroidKeyCode(self.config.keys['text'][3])
                    end_time = self.lib.gettimestamp()
                    if sent:
                        status = "PASSED"
                    else:
                        status = "FAILED"
                        self.logger.Error("Send key code FORWARD_DEL - {}".format(sent))
                        test_result = False
                        return False
                    self.lib.report_api_status(
                        start_time, end_time,
                        "SendAndroidKeyCode {}".format(self.config.keys['text'][3]),
                        status, ss_required=True
                    )

                    verified = self.verify_text(self.config.search_text,
                                                self.config.search_text
                                                )

                    if not verified:
                        self.logger.Error("Failed to verify text - {}".format(self.config.search_text))
                        test_result = False
                        return False

                    # Navigating back to App Home
                    sent = self.dut.SendAndroidKeyCode(self.config.keys['nav'][0])
                    if not sent:
                        self.logger.Error("Send key code BACK - {}".format(sent))
                        test_result = False
                        return False

                    time.sleep(5)
                    self.logger.Log("ESCAPE")
                    sent = self.dut.SendAndroidKeyCode(self.config.ESCAPE)
                    time.sleep(5)


            sent = self.sendkeys_and_verify(self.config.search_text, self.config.search_text)
            if not sent:
                status = "FAILED"
                self.logger.Error("Send key code - {}".format(sent))
                test_result = False
            else:
                status = "PASSED"
            self.lib.report("Send search key -{}".format(self.config.search_text), status)
            if not sent:
                return False

            sent = self.dut.SendAndroidKeyCode(self.config.keys['nav'][1])
            if not sent:
                self.logger.Error("Send key code ENTER - {}".format(sent))
                test_result = False
                return False
            time.sleep(3)

            if not self.dut.Tap(*self.config.C_TAP_PLAYBACK):
                self.logger.Error("Failed to tap on the video")
                test_result = False
                return False

            time.sleep(5)
            motion = self.dut.validator.DetectMotion(*self.config.detect_motion_check)
            if not motion:
                self.logger.Error("Failed to verify media playback")
                test_result = False
                return False
            self.logger.Error("Media playback started")

        except Exception as e:
            self.logger.Error("Error in run_api_test() " + str(e))
            test_result = False

        finally:
            return test_result


    def run_api_test(self):
        self.sendkeycode_text()


def main():
    testobj = api_test()
    testobj.run_test(testobj.script_name, testobj.apis)


if __name__ == '__main__':
    main()
