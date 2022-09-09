import os

CONFIG = {
    "QUEUE_URL": os.getenv("QUEUE_URL"),
    "AWS_ENDPOINT_URL": os.getenv("AWS_ENDPOINT_URL"),
}