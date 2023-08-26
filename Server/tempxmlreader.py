import xml.etree.ElementTree as ET

xml_data = '''
<Auth uid="999941057058" rc="Y" tid="" ac="public" sa="ac" ver="2.5" txn="CHETAN123456789" lk="MAvSQG0jKTW4XxQc2cI-oXZYxYH-zi7IWmsQY1q3JNLlC8VOWOHYGj8">
    <Uses pi="" pa="" pfa="" bio="" bt="" pin="n" otp="n"/>
    <Device rdsId="" rdsVer="" dpId="" dc="" mi="" mc=""/>
    <Skey ci="">encrypted and encoded session key</Skey>
    <Hmac>SHA-256 Hash of Pid block, encrypted and then encoded</Hmac>
    <Data type="X">encrypted PID block</Data>
    <Signature>Digital signature of AUA</Signature>
</Auth>
'''

root = ET.fromstring(xml_data)

# Access attributes of the root element
uid = root.get("uid")
rc = root.get("rc")
ver = root.get("ver")
txn = root.get("txn")

print(f"UID: {uid}")
print(f"RC: {rc}")
print(f"Version: {ver}")
print(f"Transaction: {txn}")

# Access child elements
uses_element = root.find("Uses")
pin = uses_element.get("pin")
otp = uses_element.get("otp")

print(f"PIN: {pin}")
print(f"OTP: {otp}")
