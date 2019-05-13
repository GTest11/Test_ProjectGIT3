#***FalconEyeCUBE - Module for initiating the interaction between FCPE-CUBE and FCPE-DBS
#*************************************************************************************************************************************************
#@author: Rithumol R S, Stephanie Cherian
#@Version: FalconEyeCUBE version 5.0
#@Date  : 03-05-2018
#*************************************************************************************************************************************************


#Importing required python modules

# coding=utf-8
import requests
import json
import sys,os
import re
import socket
from Logger import *

#Configuring the path for import
sys.path.append('../')
try:
	#Import config file
	import Configuration.Config_File as config
except ImportError:
	logger.Log("Failed to import config file.")
	sys.exit()




class FcpeInteraction(object):

	global host_db,port_db,keys_list_qoe,response_dict,keys_list_device,keys_list_network

	keys_list_qoe = ["client_ip","qoe_params","date_time","params_value","category_type","device_type","device_version","asset_name","platform","batch_id","slot_no","rack_no","device_name","capped_bw"]
	keys_list_network = ["client_ip","limited_bandwidth_up","limited_bandwidth_down","delay","packetloss","jitter","device_type","device_version","platform","database_name","batch_id","slot_no","rack_no","device_name"]
	keys_list_device = ["client_ip","device_type","device_version","platform","database_name","batch_id","slot_no","rack_no","device_name"]

	response_dict = {}
	host_db = config.RestServerDB_host
	port_db = config.RestServerDB_port


	###   Method for generating the response and logging   ###
	@classmethod
	def response_return_log(cls,dict_response,status,response,httpcode,httpreason):
		dict_response['Status'] = status
		dict_response['Response'] = response
		dict_response['HTTPCode'] = httpcode
		dict_response['HTTPReason'] = httpreason
		log.info(dict_response)
		log.error(response)


	###   Method to check for the required keys-values in input json data   ###
	@classmethod
	def check_input(cls,dict,keys_list):
		success = 0
		fail = 0

		length = len(dict)
		if length >= 1:
			for key in keys_list:
				if key not in dict:
					fail += 1
					log.error('Key "%s" not found' % key)
				elif key in dict and dict[key] == None:
					if key == "asset_name":
						success = 0
					else:
						fail += 1
						log.error('No valid value found for Key "%s"' % key)

				else:
					success = 0
		else:
			fail += 1
			log.error('Invalid!!! Missing key-value data')

		proceed = success + fail
		return proceed



	###   Method to initiate the POST call to attenuate network parameters through CUBE   ###
	@classmethod
	def network_choke(cls, host, port, argdict=None):

		response_dict = {}
		failure = cls.check_input(argdict,keys_list_network)

		if failure == 0:
			url = "http://" + host + ":" + port + "/falconeyecube/rest/networkParams"

			log.info('Network Choke : %s' % url)

			#Request payload
			payload = argdict

			#Payload json data passed
			payloadData = json.dumps(payload)
			log.info('Network Choke inputs : %s' % payloadData)

			#Request headers
			requestHeaders = {'content-type': 'application/json'}

			try:
				request_response = requests.post(url, data=payloadData, headers=requestHeaders)

				requestResponse = request_response.status_code
				responseReason = request_response.reason

				#That will raise an HTTPError, if the response was an http error.
				request_response.raise_for_status()

				response=str(request_response.text)
				response_dict = json.loads(response)
				response_dict['HTTPCode'] = requestResponse
				response_dict['HTTPReason'] = responseReason

				log.info(response_dict)

				if response_dict['Status'] == True:
					log.info("Succesfully choked network parameters")
				else:
					log.info("Failed to choke network parameters")


			#Exception handler for connection errors
			except requests.exceptions.ConnectionError as connectionError:
				cls.response_return_log(response_dict,False,"Connection Error","Nil","Nil")
				return response_dict


			#Exception handler for HTTP errors
			except requests.exceptions.HTTPError as httpError:
				status_code = httpError.response.status_code
				status_reason = httpError.response.reason
				cls.response_return_log(response_dict,False,"HTTP Error",status_code,status_reason)
				return response_dict


			#Exception handler for Timeout errors
			except requests.exceptions.Timeout as timeoutError:
				cls.response_return_log(response_dict,False,"Timeout Error","Nil","Nil")
				return response_dict


			#Exception handler for all sort of Request errors - base-class exception
			except requests.exceptions.RequestException as requestError:
				cls.response_return_log(response_dict,False,"Request Error","Nil","Nil")
				log.error(requestError)
				return response_dict


		else:
			log.info("Failed to choke network parameters - Missing required key-value data")
			cls.response_return_log(response_dict,False,"Unsupported request format",400,"BAD REQUEST")


		return response_dict




	###   Method to initiate the POST call for enabling CUBE network data push services for a client device  ###
	@classmethod
	def enable_networkdata_push(cls, host, port, argdict=None):

		response_dict = {}
		failure = cls.check_input(argdict,keys_list_device)

		if failure == 0:
			url = "http://" + host + ":" + port + "/falconeyecube/rest/addDevInfo"

			log.info('Enable network data push services for device : %s' % url)

			#Request payload
			payload = argdict

			#Payload json data passed
			payloadData = json.dumps(payload)
			log.info('Device info inputs : %s' % payloadData)

			#Request headers
			requestHeaders = {'content-type': 'application/json'}

			try:
				request_response = requests.post(url, data=payloadData, headers=requestHeaders)
				requestResponse = request_response.status_code
				responseReason = request_response.reason

				#That will raise an HTTPError, if the response was an http error.
				request_response.raise_for_status()

				response=str(request_response.text)
				response_dict = json.loads(response)
				response_dict['HTTPCode'] = requestResponse
				response_dict['HTTPReason'] = responseReason

				log.info(response_dict)

				if response_dict['Status'] == True:
					log.info("Succesfully enabled network data push services")
				else:
					log.info("Failed to enable network data push services")


			#Exception handler for connection errors
			except requests.exceptions.ConnectionError as connectionError:
				cls.response_return_log(response_dict,False,"Connection Error","Nil","Nil")
				return response_dict


			#Exception handler for HTTP errors
			except requests.exceptions.HTTPError as httpError:
				status_code = httpError.response.status_code
				status_reason = httpError.response.reason
				cls.response_return_log(response_dict,False,"HTTP Error",status_code,status_reason)
				return response_dict


			#Exception handler for Timeout errors
			except requests.exceptions.Timeout as timeoutError:
				cls.response_return_log(response_dict,False,"Timeout Error","Nil","Nil")
				return response_dict


			#Exception handler for all sort of Request errors - base-class exception
			except requests.exceptions.RequestException as requestError:
				cls.response_return_log(response_dict,False,"Request Error","Nil","Nil")
				log.error(requestError)
				return response_dict


		else:
			log.info("Failed to enable network data push services - Missing required key-value data")
			cls.response_return_log(response_dict,False,"Unsupported request format",400,"BAD REQUEST")


		return response_dict



	###   Method to initiate the POST call to insert the QoE parameters into QoE_player table   ###
	@classmethod
	def qoe_params_push(cls,argdict=None,dbname=None):

		response_dict = {}
		failure = cls.check_input(argdict,keys_list_qoe)
		database_names=['dev','stage','prod']


		if failure == 0 and dbname in database_names:
			url = "http://" + host_db + ":" + port_db + "/" + dbname + "/QoE_player"

			log.info('QoE_player push : %s' % url)

			#Request payload
			payload = argdict

			#Payload json data passed
			payloadData = json.dumps(payload)
			log.info('QoE push inputs : %s' % payloadData)

			#Request headers
			requestHeaders = {'content-type': 'application/json'}


			#To validate the client_ip
			if ( not re.match('^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$', payload['client_ip'])) :
				cls.response_return_log(response_dict,False,"Invalid client IP address",400,"BAD REQUEST")
				log.info("Failed to push QoE data. Reason : Invalid client IP address ")

			#To check non-string values as qoe_params
			elif (re.search(r'\d', payload['qoe_params'])) :
				cls.response_return_log(response_dict,False,"Invalid QoE parameter",400,"BAD REQUEST")
				log.info("Failed to push QoE data. Reason : Invalid QoE parameter ")

			#To check negative values for qoe_params
			elif (payload['params_value'] < 0) :
				cls.response_return_log(response_dict,False,"Invalid negative values for QoE parameters",400,"BAD REQUEST")
				log.info("Failed to push QoE data. Reason : Negative values are not applicable for QoE parameters ")

			#To check values other than 1 / 0 for startup_failure and video_playback_failure
			elif (payload['qoe_params'] in ('startup_failure','video_playback_failure')) and (payload['params_value'] not in ('1','0')) :
				cls.response_return_log(response_dict,False,"Invalid values for startup_failure/video_playback_failure",400,"BAD REQUEST")
				log.info("Failed to push QoE data. Reason : Values other than '1/0' are not applicable for 'startup_failure' and 'video_playback_failure' ")

			else :
				try:
					request_response = requests.post(url, data=payloadData, headers=requestHeaders)
					requestResponse = request_response.status_code
					responseReason = request_response.reason

					#That will raise an HTTPError, if the response was an http error.
					request_response.raise_for_status()

					response=str(request_response.text)

					if response == "True":
						response_dict['Status'] = True
						response_dict['Response'] = "Pushed QoE data"
					else:
						response_dict['Status'] = False
						response_dict['Response'] = "Failed to push QoE data"

					response_dict['HTTPCode'] = requestResponse
					response_dict['HTTPReason'] = responseReason

					log.info(response_dict)

					if response_dict['Status'] == True:
						log.info("Succesfully pushed QoE data")
					else:
						log.info("Failed to push QoE data")



				#Exception handler for connection errors
				except requests.exceptions.ConnectionError as connectionError:
					cls.response_return_log(response_dict,False,"Connection Error","Nil","Nil")
					return response_dict


				#Exception handler for HTTP errors
				except requests.exceptions.HTTPError as httpError:
					status_code = httpError.response.status_code
					status_reason = httpError.response.reason
					cls.response_return_log(response_dict,False,"HTTP Error",status_code,status_reason)
					return response_dict


				#Exception handler for Timeout errors
				except requests.exceptions.Timeout as timeoutError:
					cls.response_return_log(response_dict,False,"Timeout Error","Nil","Nil")
					return response_dict


				#Exception handler for all sort of Request errors - base-class exception
				except requests.exceptions.RequestException as requestError:
					cls.response_return_log(response_dict,False,"Request Error","Nil","Nil")
					log.error(requestError)
					return response_dict


		else:
			log.info("Failed to push QoE data - Missing required key-value data / Invalid database name")
			cls.response_return_log(response_dict,False,"Unsupported request format",400,"BAD REQUEST")


		return response_dict




	###   Method to initiate the GET call to get controlled network-parameters of a client IP or all client IPs   ###
	###   Set "client_ip" argument to "all" (string) for getting the network-parameters of all client devices   ###
	@classmethod
	def get_current_networkparams(cls,host, port,client_ip=None):

		response_dict = {}
		url = "http://" + host + ":" + port + "/falconeyecube/rest/networkParams"

		log.info('Get current network parameters : %s' % url)

		#Request payload
		payload = client_ip

		#Payload - data passed
		payloadData = dict(clientIP=client_ip)


		log.info('Input client_ip : %s' % payloadData)


		try:
			request_response = requests.get(url, params=payloadData)

			log.info('Get network parameters url : %s' % request_response.url)

			requestResponse = request_response.status_code
			responseReason = request_response.reason

			#That will raise an HTTPError, if the response was an http error.
			request_response.raise_for_status()

			response=str(request_response.text)
			response_dict = json.loads(response)
			response_dict['HTTPCode'] = requestResponse
			response_dict['HTTPReason'] = responseReason

			log.info(response_dict)

			if response_dict['Status'] == True:
				log.info("Succesfully fetched the current network parameters")
			else:
				log.info("Failed to fetch the current network parameters")


		#Exception handler for connection errors
		except requests.exceptions.ConnectionError as connectionError:
			cls.response_return_log(response_dict,False,"Connection Error","Nil","Nil")
			return response_dict


		#Exception handler for HTTP errors
		except requests.exceptions.HTTPError as httpError:
			status_code = httpError.response.status_code
			status_reason = httpError.response.reason
			cls.response_return_log(response_dict,False,"HTTP Error",status_code,status_reason)
			return response_dict


		#Exception handler for Timeout errors
		except requests.exceptions.Timeout as timeoutError:
			cls.response_return_log(response_dict,False,"Timeout Error","Nil","Nil")
			return response_dict


		#Exception handler for all sort of Request errors - base-class exception
		except requests.exceptions.RequestException as requestError:
			cls.response_return_log(response_dict,False,"Request Error","Nil","Nil")
			log.error(requestError)
			return response_dict



		return response_dict




	###   Method to initiate the DELETE call to disable the CUBE network data push services for a device  ###
	###   Set "client_ip" argument to "all" (string) for disabling the CUBE network data push services of all client devices  ###
	@classmethod
	def disable_networkdata_push(cls,host, port,client_ip=None):

		response_dict = {}
		url = "http://" + host + ":" + port + "/falconeyecube/rest/deleteDevInfo"

		log.info('Disable network data push services for device : %s' % url)

		#Request payload
		payload = client_ip

		#Payload json data passed
		payloadData = dict(clientIP=client_ip)

		log.info('Input client_ip : %s' % payloadData)

		#Request headers
		requestHeaders = {'content-type': 'application/json'}


		try:
			request_response = requests.delete(url,params=payloadData, headers=requestHeaders)

			log.info('Disable network data push services for device url : %s' % request_response.url)

			requestResponse = request_response.status_code
			responseReason = request_response.reason

			#That will raise an HTTPError, if the response was an http error.
			request_response.raise_for_status()

			response=str(request_response.text)
			response_dict = json.loads(response)
			response_dict['HTTPCode'] = requestResponse
			response_dict['HTTPReason'] = responseReason

			log.info(response_dict)

			if response_dict['Status'] == True:
				log.info("Succesfully disabled network data push services")
			else:
				log.info("Failed to disable network data push services")


		#Exception handler for connection errors
		except requests.exceptions.ConnectionError as connectionError:
			cls.response_return_log(response_dict,False,"Connection Error","Nil","Nil")
			return response_dict


		#Exception handler for HTTP errors
		except requests.exceptions.HTTPError as httpError:
			status_code = httpError.response.status_code
			status_reason = httpError.response.reason
			cls.response_return_log(response_dict,False,"HTTP Error",status_code,status_reason)
			return response_dict


		#Exception handler for Timeout errors
		except requests.exceptions.Timeout as timeoutError:
			cls.response_return_log(response_dict,False,"Timeout Error","Nil","Nil")
			return response_dict


		#Exception handler for all sort of Request errors - base-class exception
		except requests.exceptions.RequestException as requestError:
			cls.response_return_log(response_dict,False,"Request Error","Nil","Nil")
			log.error(requestError)
			return response_dict



		return response_dict



	###   Method to initiate the DELETE call to delete specific/all network-parameters of a client IP  ###
	###   Set "network_params" argument to "all" for deleting all network-parameters for a client IP  ###
	@classmethod
	def delete_network_params(cls, host, port , client_ip=None , network_params=None):

		response_dict = {}
		url = "http://" + host + ":" + port + "/falconeyecube/rest/networkParams"

		log.info('Delete the network parameters : %s' % url)

		#Payload json data passed
		payload_params = ["clientIP","nwparam"]
		params_value = [client_ip,network_params]
		payloadData = dict(zip(payload_params, params_value))

		log.info('Input client_ip and network_param: %s' % payloadData )

		#Request headers
		requestHeaders = {'content-type': 'application/json'}


		try:
			request_response = requests.delete(url,params=payloadData, headers=requestHeaders)

			log.info('Delete network parameters url : %s' % request_response.url)

			requestResponse = request_response.status_code
			responseReason = request_response.reason

			#That will raise an HTTPError, if the response was an http error.
			request_response.raise_for_status()

			response=str(request_response.text)
			response_dict = json.loads(response)
			response_dict['HTTPCode'] = requestResponse
			response_dict['HTTPReason'] = responseReason

			log.info(response_dict)

			if response_dict['Status'] == True:
				log.info("Succesfully deleted the network parameters")
			else:
				log.info("Failed to delete the network parameters")


		#Exception handler for connection errors
		except requests.exceptions.ConnectionError as connectionError:
			cls.response_return_log(response_dict,False,"Connection Error","Nil","Nil")
			return response_dict


		#Exception handler for HTTP errors
		except requests.exceptions.HTTPError as httpError:
			status_code = httpError.response.status_code
			status_reason = httpError.response.reason
			cls.response_return_log(response_dict,False,"HTTP Error",status_code,status_reason)
			return response_dict


		#Exception handler for Timeout errors
		except requests.exceptions.Timeout as timeoutError:
			cls.response_return_log(response_dict,False,"Timeout Error","Nil","Nil")
			return response_dict


		#Exception handler for all sort of Request errors - base-class exception
		except requests.exceptions.RequestException as requestError:
			cls.response_return_log(response_dict,False,"Request Error","Nil","Nil")
			log.error(requestError)
			return response_dict


		return response_dict
