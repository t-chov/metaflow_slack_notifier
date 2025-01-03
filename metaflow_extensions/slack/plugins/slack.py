import requests

POST_MESSAGE_URL = "https://slack.com/api/chat.postMessage"


def send_message(
    token: str,
    channel: str,
    message: str,
) -> None:
    """Sends a message to a Slack channel using the Slack Web API.

    Args:
        token: Slack API token for authentication.
        channel: Target Slack channel ID or name.
        message: Content of the message to be sent.
    """
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "channel": channel,
        "text": message,
    }
    requests.post(POST_MESSAGE_URL, headers=headers, data=data)
