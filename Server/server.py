import json
import requests
from uuid import uuid4

uuidno = str(uuid4())

def getcaptcha():
    params = {
        "langCode": "en",
        "captchaLength": "3",
        "captchaType": "2"
    }
    myUri = "https://stage1.uidai.gov.in/unifiedAppAuthService/api/v2/get/captcha"

    response = requests.post(myUri, json=params, headers={'Content-type': 'application/json'})
    print('Called')
    responsebody = response.json()
    return responsebody

def getotp(aadharno, captcha, captchatxnid):
    params = {
        "uidNumber": aadharno,
        "captchaTxnId": captchatxnid,
        "captchaValue": captcha,
        "transactionId": f"MYAADHAAR:{uuidno}"
    }
    myUri = "https://stage1.uidai.gov.in/unifiedAppAuthService/api/v2/generate/aadhaar/otp"
    
    headers = {
        'x-request-id': uuidno,
        'appid': 'MYAADHAAR',
        'Accept-Language': 'en_in',
        'Content-Type': 'application/json'
    }
    
    response = requests.post(myUri, json=params, headers=headers)
    responsebody = response.json()
    return responsebody

def validateOTP(aadharno, otp, txnid):
    params = {
        'txnId': txnid,
        'otp': otp,
        'uid': aadharno
    }
    
    myUri = 'https://stage1.uidai.gov.in/onlineekyc/getAuth/'
    
    response = requests.post(myUri, json=params, headers={'Content-Type': 'application/json'})
    responsebody = response.json()
    print(responsebody)
    
    if responsebody['status'] == 'y':
        return True
    else:
        return False

# Example usage
captcha_data = getcaptcha()
captcha_value = captcha_data['captcha']

otp_data = getotp('123456789012', captcha_value, captcha_data['captchaTxnId'])
otp_value = otp_data['aadhaar-otp']

validation_result = validateOTP('123456789012', otp_value, otp_data['txnId'])
print(validation_result)
