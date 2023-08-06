import requests
import json
from .helpers import *
from .subscriptions import *
from .azure_token import getAccessKey
from .constants import *

color = bcolors

class User:
	# primarySubKey expects a dictionary in the form of Azure Product Name : Primary key to use for that product subscription
	# Need to revise primarySubKey to be dictionary: ?? "primarySubKey": ["subscription name", "product"]
	def __init__(self, firstName, lastName, email, primarySubKey, userId, note):
		self.firstName = firstName
		self.lastName = lastName
		self.email = email
		self.primarySubKey = primarySubKey
		self.userId = userId
		self.note = note

def getUsers(apim):
	requestUrl = "users"
	return simpleGet(apim, requestUrl)



def checkIfUserExistsByName(apim, user):
	userFound = False

	users = getUsers(apim)

	for item in users['value']:
		if item['lastName'] == user:
			userFound = True
			print("user found")
			print(item)
			for k, v in item.items():
				if v != None:
					print(k, ": ", v)

	return userFound


def checkIfUserExistsByprimarySubKey(apim, primarySubKey):
	data = getSubscriptions(apim)
	appIds = getConfiguredAppIds(data)
	if primarySubKey in AppIdList(appIds.keys()):
		return (True, appIds[getExactValueOfKey(appIds, primarySubKey)].userId)
	else:
		return (False, None)


def createAzureUser(apim, user):
	if apim.token is None:
		apim.token = getAccessKey(apim.apimId, apim.apimKey)

	headers = basicHeader(apim)
	body = {
				"firstName": user.firstName,
				"lastName": user.lastName,
				"email": user.email,
				"note": user.note
			}

	if user.userId is None:
		user.userId = "/users/" +body["firstName"] + body["lastName"]

	requestUrl = user.userId.replace("/", "", 1)

	
	myResponse = requests.put(apim.apimBaseUrl + requestUrl, headers=headers, json=body, params=apim.apiVersion)
	return myResponse


def subscribeUserToProduct(apim, body, subscriptionId):
	headers = basicPutPatchHeader(apim)
	body = body
	requestUrl = ("subscriptions/" + subscriptionId).replace(" ", "")
	myResponse = requests.put(apim.apimBaseUrl + requestUrl, headers=headers, json=body, params=apim.apiVersion)
	
	return myResponse


def deleteAzureUser(apim, uid):
	if apim.token is None:
		apim.token = getAccessKey(apim.apimId, apim.apimKey)

	headers = basicPutPatchHeader(apim)

	params = apim.apiVersion + "&deleteSubscriptions=true"

	requestUrl = uid.replace("/", "", 1)

	#print(apim.apimBaseUrl + requestUrl)

	myResponse = requests.delete(apim.apimBaseUrl + requestUrl, headers=headers, params=params)
	#print(myResponse)

	if myResponse.status_code == 204:
			print(color.WARNING + "DELETED! " + uid + color.ENDC)


