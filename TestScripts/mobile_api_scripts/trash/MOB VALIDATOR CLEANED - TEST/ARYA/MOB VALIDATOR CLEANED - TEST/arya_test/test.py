__author__ = 'arya'

class test():

    def CloseApp(self):
        print("Close")


    def LaunchApp(self):
        print("LaunchApp")



    def send_app_to_background(self):
        print("send_app_to_background")

apis = ("CloseApp", "LaunchApp",
                "SendAppToBackground",
       )

dut = test()
apis_call = {
    "CloseApp": dut.CloseApp,
    "LaunchApp": dut.LaunchApp,
    "SendAppToBackground": dut.send_app_to_background,
}

for api in apis:
    apis_call[api]()
#33333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
from collections import OrderedDict


def aa(a):
    #a = 3
    print "a - {}".format(a)

def bb():
    b = 4
    print "b - {}".format(b)


dict_val = {
    "one" : (1),
    "b" : (),
}

dict_test = {
    "one" : aa,
    "b" : bb}

for api  in dict_test:
    if dict_val[api]:
        dict_test[api](dict_val[api])
    else:
        dict_test[api]()



for api  in apis_call:
    if apis_params[api]:
        apis_call[api](apis_params[api])
    else:
        apis_call[api]()

##########################################################################################
###########################################################################################


# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Author            :
# Date              :   01-10-2018, 17-10-2018
#Script Version     : 1.1
#Modification details: 17 Oct 2018, fixed review comments - Arya
# APIs covered      :   "LaunchApp", "SendAppToBackground",
#                       "CloseApp"
#Test Scenario:
#init to Youtube
#close youtube by CloseApp
#LaunchApp again and calling SendAppToBackground
# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''



#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#@Function Name	  	: main()
#@Description		: main function
#@Input arguments	: None
#@Output values		: None
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#@Function Name	  	: test_api()
#@Description		: Positive scenario testing of following APIs:
#                     "CloseApp", "LaunchApp","SendAppToBackground"
#@Input arguments	: None
#@Output values		: None
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#@Function Name	  	: log_script_info()
#@Description		: logs file name and APIs covered
#@Input arguments	: None
#@Output values		: None
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''



#importing python modules
import sys
import os
import time

#importing user defined functions
sys.path.append('../')
try:
    # Import library file
    import library.common_functions as lib
except ImportError:
    print("Failed to import common_functions file")
    sys.exit()



#Variables


lib.log_script_info(os.path.basename(__file__), apis_in_the_script)