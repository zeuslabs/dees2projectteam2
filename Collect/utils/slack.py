from slackclient import SlackClient
from config import Config


def send_message(channel, message):
    SlackClient(Config.SLACK_TOKEN).api_call(
        "chat.postMessage",
        channel=channel,
        text=message,
        username='FCDEES2PROJECTTEAM2',
    )
    return True