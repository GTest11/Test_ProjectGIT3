#cubeModule  module - Wrapper module for module_FCPE
# module_FCPE: module initiating the interaction between FCPE-CUBE and FCPE-DBS
#*******************************************************************************
#@author: Arya L
#*******************************************************************************

#imports
import clr
import sys
import os
import time
#import module_FCPE as netlib

#importing module_FCPE
try:
    import module_FCPE as netlib
except ImportError:
    print("Failed to import module_FCPE common library")
#*******************************************************************************
args = sys.argv
#global variables

#logger and dut variables
dut_object, logger_object = -1,-1

#Cube attribute identifiers
dut_rack_no = 9
dut_slot_no = 10
dut_name = 1

#Cube parameter values
input_controller_ip = " "
input_controller_port = " "
input_client_ip = " "
input_device_type = " "
input_device_version = " "
input_device_platform = " "
input_device_name = ''
input_device_slot = ''
input_device_rack = ''
input_batch_id = ''
database_name = " "
#*******************************************************************************
#Methods


def initialize_cube(dut_obj, lgr_obj, input_database_name = 'dev'):
    '''
    Initializes dut and logger objects, checking and getting required cube parameters.
    '''

    initialize_status = False
    global database_name,dut_object, logger_object, input_controller_ip, input_controller_port, input_client_ip, input_device_type, input_device_version, input_device_platform,input_device_name, input_device_slot, input_device_rack
    dut_object = dut_obj
    logger_object = lgr_obj
    database_name = input_database_name
    try:
        logger_object.Log("*** initialize_cube: START  ****")
        logger_object.Log("Initializing cube.")

        #getting required cube parameters from dut details using ReadCustomProperty API
        global input_controller_ip, input_controller_port, input_client_ip, input_device_type, input_device_version, input_device_platform, input_batch_id
        logger_object.Log("Getting required cube parameters from dut details.....")
        input_controller_ip = dut_object.ReadCustomProperty("cube_controller_ip")
        input_controller_port = dut_object.ReadCustomProperty("cube_controller_port")
        input_client_ip = dut_object.ReadCustomProperty("cube_client_ip")#7
        input_device_type = dut_object.ReadCustomProperty("cube_device_type") #2 DUT_TYPE
        input_device_version = dut_object.ReadCustomProperty("cube_device_version") # 8 DUT_SOFTWARE_VERSION
        input_device_platform = dut_object.ReadCustomProperty("cube_device_platform") # 5 DUT_MANUFACTURER
        input_device_name = dut_object.ReadProperty(dut_name) #2 DUT_Name
        input_device_slot = dut_object.ReadProperty(dut_slot_no) # 8 slot number
        input_device_rack = dut_object.ReadProperty(dut_rack_no) # 5 Rack No
        input_batch_id = args[1]
        logger_object.Log("Execution id :{}".format(input_batch_id))

        #Checking the availability of cube parameters
        if input_client_ip == " " or input_device_type == " " or input_device_version == " " or input_device_platform == " ":
            logger_object.Error("Improper Cube configuration, please verify cube_controller_ip, cube_controller_port, cube_client_ip, cube_device_type, cube_device_version and cube_device_platform values.")
            dut_object.CommitStepResult("initialize_cube", "FAILED")
        else:
            logger_object.Log("Obtained the required cube parameters.")
            initialize_status = True
            dut_object.CommitStepResult("initialize_cube", "PASSED")
    except Exception as e:
        initialize_status = False
        logger_object.Log('Exception raised in initialize_cube ' + str(e))
        dut_object.CommitStepResult("initialize_cube", "FAILED")

    logger_object.Log("*** initialize_cube: END  ****")
    return initialize_status

#*******************************************************************************


def update_status(func_name, status_return_dict):
    '''
    Updates test results
    '''
    if status_return_dict['Status'] == True:
        api_status = "PASSED"
    else:
        api_status = "FAILED"

    logger_object.Log('Status: ' + str(status_return_dict['Status']))
    logger_object.Log('Response: ' + str(status_return_dict['Response']))
    dut_object.CommitStepResult(str(func_name), api_status)
    logger_object.Log("*** " + str(func_name) +": END  ****")

#*******************************************************************************


def cube_enable_networkdata_push(custom_attributs_dict = None):
    '''
    API to enable_networkdata_push for the target device.
    '''
    status_return = {}
    try:
        logger_object.Log("*** enable_networkdata_push: START  ****")

        logger_object.Log("Client IP : " + str(input_client_ip))
        key_list = ["client_ip","device_type","device_version","platform", "database_name", "device_name","slot_no","rack_no", "batch_id"]
        value_list = [str(input_client_ip), str(input_device_type), str(input_device_version), str(input_device_platform), str(database_name),
                    input_device_name, input_device_slot, input_device_rack, input_batch_id]
        register_device_dict = dict(zip(key_list, value_list))
        logger_object.Log("Data passed are : ")
        logger_object.Log(str(register_device_dict))

        if custom_attributs_dict != None:
            register_device_dict.update(custom_attributs_dict)

        logger_object.Log("enabling networkdata push...")
        status_return = netlib.FcpeInteraction.enable_networkdata_push(str(input_controller_ip), str(input_controller_port), register_device_dict)

#Exception handler
    except Exception as e:
        logger_object.Log('Exception raised in cube_enable_networkdata_push')
        status_return = {'Status':'False', 'Response': 'Exception raised', 'HTTPReason':'Nil','HTTPCode':'Nil'}
        update_status("enable_networkdata_push", status_return)
        return status_return

    update_status("enable_networkdata_push", status_return)
    return status_return

#*******************************************************************************


def cube_choke_network(limited_bandwidth_up=2048, limited_bandwidth_down=1024, delay=0, jitter=0, packetloss=0.0):
    '''
    attenuate network parameters of the target device through CUBE.
    '''
    status_return = {}
    try:
        logger_object.Log("*** choke_network: START  ****")
        logger_object.Log("Client IP : " + str(input_client_ip))
        logger_object.Log("bandwidth_up received: " + str(limited_bandwidth_up))
        logger_object.Log("bandwidth_down received: " + str(limited_bandwidth_down))
        key_list = ["client_ip","limited_bandwidth_up","limited_bandwidth_down","delay","packetloss","jitter", "device_type","device_version","platform","database_name", "device_name","slot_no","rack_no", "batch_id"]
        value_list = [str(input_client_ip), int(limited_bandwidth_up), int(limited_bandwidth_down), int(delay), float(packetloss), int(jitter), str(input_device_type), str(input_device_version), str(input_device_platform), str(database_name),
                    input_device_name, input_device_slot, input_device_rack, input_batch_id]
        choke_network_dict = dict(zip(key_list, value_list))
        logger_object.Log("Data passed are : ")
        logger_object.Log(str(choke_network_dict))
        logger_object.Log("Network  choking initialized...")
        status_return = netlib.FcpeInteraction.network_choke(str(input_controller_ip), str(input_controller_port), choke_network_dict)

#Exception handler
    except Exception as e:
        logger_object.Log('Exception raised in cube_choke_network')
        status_return = {'Status':'False', 'Response': 'Exception raised', 'HTTPReason':'Nil','HTTPCode':'Nil'}
        update_status("choke_network", status_return)
        return status_return

    update_status("choke_network", status_return)
    return status_return
#*******************************************************************************


def cube_get_current_networkparams(user_client_ip = "empty"):
    '''
    API to get current network parameter of the target device or all the device registered under the target device's cube controller.
    '''
    status_return = {}
    try:
        if "empty" == user_client_ip:
            user_client_ip = input_client_ip
        logger_object.Log("*** cube_get_current_networkparams: START  ****")
        logger_object.Log("Getting current network params...")
        status_return = netlib.FcpeInteraction.get_current_networkparams(str(input_controller_ip), str(input_controller_port), str(user_client_ip))

#Exception handler
    except Exception as e:
        logger_object.Log('Exception raised in cube_get_current_networkparams')
        status_return = {'Status':'False', 'Response': 'Exception raised', 'HTTPReason':'Nil','HTTPCode':'Nil'}
        update_status("qoe_push", status_return)
        return status_return

    update_status("cube_get_current_networkparams", status_return)
    return status_return

#*******************************************************************************


def cube_disable_networkdata_push():
    '''
    API to disable_networkdata_push of the target device.
    '''
    status_return = {}
    try:
        logger_object.Log("*** disable_networkdata_push: START  ****")

        logger_object.Log("Disabling networkdata_push...")
        logger_object.Log("Client IP : " + str(input_client_ip))
        status_return = netlib.FcpeInteraction.disable_networkdata_push(str(input_controller_ip), str(input_controller_port), str(input_client_ip))

#Exception handler
    except Exception as e:
        logger_object.Log('Exception raised in cube_disable_networkdata_push')
        status_return = {'Status':'False', 'Response': 'Exception raised', 'HTTPReason':'Nil','HTTPCode':'Nil'}
        update_status("disable_networkdata_push", status_return)
        return status_return

    update_status("disable_networkdata_push", status_return)
    return status_return

#*******************************************************************************


def cube_delete_network_params(network_params ="all"):
    '''
    API to delete network_params.
    '''
    status_return = {}
    try:
        logger_object.Log("*** cube_delete_network_params: START  ****")

        logger_object.Log("Deleting network parameters ...")
        logger_object.Log("Network parameter : " + str(network_params))
        logger_object.Log("Client IP : " + str(input_client_ip))
        status_return = netlib.FcpeInteraction.delete_network_params(str(input_controller_ip), str(input_controller_port), str(input_client_ip), str(network_params))

#Exception handler
    except Exception as e:
        logger_object.Log('Exception raised in cube_delete_network_params')
        status_return = {'Status':'False', 'Response': 'Exception raised', 'HTTPReason':'Nil','HTTPCode':'Nil'}
        update_status("cube_delete_network_params", status_return)
        return status_return

    update_status("cube_delete_network_params", status_return)
    return status_return

#*******************************************************************************


def qoe_push( qoe_params, date_time, params_value, category_type, asset_name,capped_bw, custom_attributs_dict = None):
    '''
    Push to DBs
    '''
    status_return = {}
    try:
        logger_object.Log("*** qoe_push: START  ****")

        logger_object.Log("Client IP : " + str(input_client_ip))
        key_list = ["client_ip","qoe_params","date_time","params_value","category_type","device_type","device_version","asset_name","platform", "device_name","slot_no","rack_no", "capped_bw", "batch_id"]
        value_list = [str(input_client_ip), str(qoe_params), str(date_time), str(params_value), str(category_type), str(input_device_type), str(input_device_version), str(asset_name), str(input_device_platform),
                    input_device_name, input_device_slot, input_device_rack, capped_bw, input_batch_id]
        qoe_params_push_dict = dict(zip(key_list, value_list))
        logger_object.Log(str(qoe_params_push_dict))
        if custom_attributs_dict != None:
            qoe_params_push_dict.update(custom_attributs_dict)

        logger_object.Log("Data passed are : ")
        logger_object.Log(str(qoe_params_push_dict))
        logger_object.Log("qoe data pushing to DB...")
        status_return = netlib.FcpeInteraction.qoe_params_push(qoe_params_push_dict, str(database_name))

#Exception handler
    except Exception as e:
        logger_object.Log('Exception raised in qoe_push')
        status_return = {'Status':'False', 'Response': 'Exception raised', 'HTTPReason':'Nil','HTTPCode':'Nil'}
        update_status("qoe_push", status_return)
        return status_return

    update_status("qoe_push", status_return)
    return status_return

#*******************************************************************************


#*******************************EOF*********************************************
