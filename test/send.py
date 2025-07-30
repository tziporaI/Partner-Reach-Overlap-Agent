# # send_correct_request.py
# import requests
# import uuid

# payload = {
#     "id": str(uuid.uuid4()),
#     "jsonrpc": "2.0",
#     "method": "message/send",
#     "params": {
#         "message": {
#             "message_id": str(uuid.uuid4()),
#             "role": "user",
#             "parts": [
#                 {
#                     "text": """
# Please analyze the data per media source and return which ones provide the best value for investment, based on metrics like unique users, overlap rate, and incrementality score.format ans send the data to slack

# Parameters:

# app_id: ad_1  
# date_range: 2025-06-26 to 2025-06-30  
# campaign_name: adnet_adrevenue_raw_all_on  
# media_sources:
#     1. advprivacy_int  
#     2. reengage_int  
#     3. adrevenueqa_int
# """
#                 }
#             ]
#         }
#     }
# }

# response = requests.post("http://localhost:8001", json=payload)
# print(response.status_code)
# print(response.json())
import requests
import uuid

def send_to_agent(url, text):
    payload = {
        "id": str(uuid.uuid4()),
        "jsonrpc": "2.0",
        "method": "message/send",
        "params": {
            "message": {
                "message_id": str(uuid.uuid4()),
                "role": "user",
                "parts": [{"text": text}]
            }
        }
    }
    response = requests.post(url, json=payload)
    print(f"\n📡 Response from {url}")
    print("Status code:", response.status_code)
    try:
        print("Response:", response.json())
    except Exception as e:
        print("⚠️ Failed to parse response:", e)

# שליחה לאיגנט הראשי
send_to_agent("http://localhost:8001", "חשב חפיפה בין פייסבוק לגוגל")

# שליחה לאיגנט HelloWorld
send_to_agent("http://localhost:8002", "מה שלומך?")
