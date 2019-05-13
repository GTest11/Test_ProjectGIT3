#cubeModule  module - Wrapper module for module_FCPE
# module_FCPE: module initiating the interaction between FCPE-CUBE and FCPE-DBS
#*******************************************************************************
# Copyright (c) TataElxsi.
# All rights reserved.
#*******************************************************************************

#imports
import clr
import sys
import os
import time
#import module_FCPE as netlib

#importing module_FCPE
try:
    import cubeModule
except ImportError:
    print("Failed to import cubeModule common library")
#*******************************************************************************
#Methods


def InitializeCube(dut_obj, lgr_obj, input_database_name):
    '''
    Initializes dut and logger objects, checking and getting required cube parameters.
    '''
    return cubeModule.initialize_cube(dut_obj, lgr_obj, input_database_name)
#*******************************************************************************


def CubeEnableNetworkdataPush(custom_attributs_dict = None):
    '''
    API to enable_networkdata_push for the target device.
    '''
    return cubeModule.cube_enable_networkdata_push(custom_attributs_dict)

#*******************************************************************************


def CubeChokeNetwork(limited_bandwidth_up = 2048, limited_bandwidth_down=1024, delay= 0, jitter=0, packetloss=0.0):
    '''
    attenuate network parameters of the target device through CUBE.
    '''
    return cubeModule.cube_choke_network(limited_bandwidth_up, limited_bandwidth_down, delay, jitter, packetloss )
#*******************************************************************************


def CubeGetCurrentNetworkparams(user_client_ip = "empty"):
    '''
    API to get current network parameter of the target device or all the device registered under the target device's cube controller.
    '''
    return cubeModule.cube_get_current_networkparams(user_client_ip )
#*******************************************************************************


def CubeDisableNetworkdataPush():
    '''
    API to disable_networkdata_push of the target device.
    '''
    return cubeModule.cube_disable_networkdata_push()
#*******************************************************************************


def CubeDeleteNetworkParams(network_params ="all"):
    '''
    API to delete network_params.
    '''
    return cubeModule.cube_delete_network_params(network_params)
#*******************************************************************************


def QoePush( qoe_params, date_time, params_value, category_type, asset_name, capped_bw, custom_attributs_dict = None):
    '''
    Push to DBs
    '''
    return cubeModule.qoe_push( qoe_params, date_time, params_value, category_type, asset_name, capped_bw, custom_attributs_dict)
#*******************************************************************************


#*******************************EOF*********************************************
