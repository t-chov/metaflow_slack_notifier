import pytest
import requests
from pytest_mock import MockerFixture

from metaflow_extensions.slack.plugins import send_message

# Test data
TEST_TOKEN = "xoxb-test-token-123"
TEST_CHANNEL = "test-channel"
TEST_MESSAGE = "Hello, World!"
EXPECTED_URL = "https://slack.com/api/chat.postMessage"


@pytest.fixture
def mock_response(mocker: MockerFixture):
    """Fixture to create a mock response object."""
    response = mocker.Mock()
    response.status_code = 200
    response.json.return_value = {"ok": True}
    return response


def test_send_message_success(mocker: MockerFixture, mock_response):
    """Test successful message sending with correct parameters."""
    mock_post = mocker.patch("requests.post", return_value=mock_response)

    # Call the function
    send_message(TEST_TOKEN, TEST_CHANNEL, TEST_MESSAGE)

    # Verify the POST request was made with correct parameters
    mock_post.assert_called_once_with(
        EXPECTED_URL,
        headers={"Authorization": f"Bearer {TEST_TOKEN}"},
        data={
            "channel": TEST_CHANNEL,
            "text": TEST_MESSAGE,
        },
    )


def test_send_message_network_error(mocker: MockerFixture):
    """Test handling of network errors."""
    mocker.patch("requests.post", side_effect=requests.exceptions.RequestException("Network Error"))

    with pytest.raises(requests.exceptions.RequestException):
        send_message(TEST_TOKEN, TEST_CHANNEL, TEST_MESSAGE)


def test_send_message_invalid_token(mocker):
    """Test sending message with invalid token format."""
    mock_response = mocker.Mock()
    mock_response.status_code = 401
    mock_response.json.return_value = {"ok": False, "error": "invalid_token"}

    mock_post = mocker.patch("requests.post", return_value=mock_response)

    send_message("invalid-token", TEST_CHANNEL, TEST_MESSAGE)
    mock_post.assert_called_with(
        EXPECTED_URL,
        headers={"Authorization": "Bearer invalid-token"},
        data={
            "channel": TEST_CHANNEL,
            "text": TEST_MESSAGE,
        },
    )
