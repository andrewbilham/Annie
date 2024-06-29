import requests
import json
import random
from datetime import datetime, timedelta

# Constants
num_records = 100
referral_id_range = range(22, 48)  # 22 to 47 inclusive
supplier_id_choices = [26, 27] + list(range(53, 58))  # 26, 27, 53, 54, 55, 56, 57
statuses = ["pending", "accepted", "rejected"]
yesterday = datetime.now() - timedelta(days=1)

# Function to generate a single record
def generate_record():
    referral_id = random.choice(referral_id_range)
    supplier_id = random.choice(supplier_id_choices)
    sentdate = yesterday.isoformat()
    status = random.choice(statuses)
    responsedate = (yesterday + timedelta(days=random.randint(2, 3))).isoformat()

    return {
        "supplier_id": supplier_id,
        "referral_id": referral_id,
        "sentdate": sentdate,
        "status": status,
        "responsedate": responsedate
    }

# Generate the records
records = [generate_record() for _ in range(num_records)]

# The API endpoint and authorization token
url = "http://localhost/api/v1/referrals_allocations/"
headers = {
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MjAxMDg3ODAsInN1YiI6IjEifQ.KOXSFwOpyxeavuFn8pqym6WbrmxVfEUOxBhmpZ60L-E",
    "Content-Type": "application/json"
}

# Loop through each dictionary in the list and send it as a POST request
for entry in records:
    response = requests.post(url, json=entry, headers=headers)
    print(f"Status Code: {response.status_code}, Response: {response.json()}")