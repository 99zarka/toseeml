import requests
import json
import time
print("staring the script to Update location every 20 seconds...")

while True:
    api_url = "https://api.tosee.live/api/Users/update-location"
    token = "eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJuYW1laWQiOiI3IiwidW5pcXVlX25hbWUiOiJ6YXJrYTIwMzAiLCJyb2xlIjoiTWVtYmVyIiwibmJmIjoxNjg2NjUwMDgwLCJleHAiOjE2ODkyNDIwODAsImlhdCI6MTY4NjY1MDA4MH0.gfQgM8YZlr_mFOXogWnGkaUlQAWw5DfAVicHFiCn-7iibIiQ8cyXG1UgrUaqm3qk0CKePtYgNhJfkiOJBEPQiA"

    data = {
        "location": "30.900664,29.875518"
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }

    try:
        response = requests.put(api_url, data=json.dumps(data), headers=headers)
    except:
        print("can't update location, No internet connection")
    if response.ok:
        print("Updated location successfully")
    else:
        print("Error in PUT request:", response.text)
    time.sleep(20)