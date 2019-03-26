import requests
from flask import Flask

#app = Flask(__name__)

url = 'https://erpuat.ltfs.com:446/LTFSPerfiosApp/api/twhlLogin'
headers = {'content-type' : 'application/json'}
data = {
	"registrationToken": "dDkU_gCL_u4:APA91bGGtCdVvOlX1fVMrI-y5h_D_Xv4kdWjWQgvs5Vh03m-G7FYfmSnZafeedOa5UHFOqhClkJYExFowDJNl6bLh4m0fDlCdg-tL1lOG4q1am4tocreeBDdSy7IM78ztcudODhyubqc",
	"passWord": "welcome@1234",
	"username": "USERHL11",
	"imei": "869737024563196",
	"partnerFlag": "false",
	"product": "TW",
	"version": "12.1.5"
}

#@app.route('/some-url')
def get_data():
    #return requests.get("https://www.google.com").content
    requests.post(url, data, headers)
print(get_data())