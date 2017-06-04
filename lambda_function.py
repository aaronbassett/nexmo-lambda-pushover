import os
import json
import requests

def lambda_handler(event, context):
    if 'text' in event:
        response = requests.post(
            'https://api.pushover.net/1/messages.json',
            data={
                "token": os.environ['PUSHOVER_TOKEN'],
                "user": os.environ['PUSHOVER_USER_KEY'],
                "message": event['text']
            }
        )

        return response.text
    else:
        return 'No SMS text to forward'
