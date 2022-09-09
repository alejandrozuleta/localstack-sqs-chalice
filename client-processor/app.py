import os
import json

from chalice import Chalice
from chalicelib.log import logger
from chalicelib.client_constants import ClientStatuses

app = Chalice(app_name='client-processor')

@app.on_sqs_message(os.getenv("QUEUE_NAME"))
def process_client_signup_event(event):
    for sqs_event in event:
        message = json.loads(sqs_event.body)

        if message.get("status") == ClientStatuses.ACTIVE:
            logger.info(f"Status Active event processed: {message}")

        if message.get("status") == ClientStatuses.PENDING:
            logger.info(f"Status Pending event processed: {message}")

        if message.get("status") == ClientStatuses.DISABLED:
            logger.info(f"Status Disabled event processed: {message}")
