import requests

# Define the payload
payload = "04{NA,V,f25073ce9d46b0f720d00f32d8979c4efdab5346868ffac90f4412d02710f 7ef,0100002020000000,2.0,20160603104809,1,0,0,0,2.0,1f5368b4cf6d74290 33a47b8c7963329945c2bdf2690fa3685945b15d3cda2e0,96cae35ce8a9b0244178b f28e4966c2ce1b8385723a96a6b838858cdd6ca0a1e,,NA,P,50,NA,E,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA,af76e1ffcb2e308770ac5212acbbc7d93ba5693d828714a513 6b6e1a9f438fc3,NA,NA}"

# Define the HTTPS URL
url = "https://developer.uidai.gov.in/2.5/public/0/0/MCNYL7FpPgjEhx7HBp9tu59Vdm4FnYGlxuqHctfAeNNaCufVafshqzQ"  # Replace with your actual URL

# Send the POST request
response = requests.post(url, data=payload)

# Check the response
if response.status_code == 200:
    print("Request successful")
else:
    print(f"Request failed with status code: {response.status_code}")
    print(response.text)  # Print the response content for debugging purposes
