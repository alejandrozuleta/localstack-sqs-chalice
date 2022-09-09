import json

import boto3

from config import CONFIG
from message import generate_fake_message

def main():
    sqs_client = boto3.client("sqs", endpoint_url=CONFIG.get("AWS_ENDPOINT_URL"))

    message = generate_fake_message()

    sqs_client.send_message(
        QueueUrl=CONFIG.get("QUEUE_URL"),
        MessageBody=json.dumps(message, default=str)
    )


if __name__ == "__main__":
    main()