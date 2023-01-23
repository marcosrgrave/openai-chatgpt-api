from http import HTTPStatus
from unittest import TestCase

from source.open_ai import OpenAI
from source.config import API_KEY


class TestOpenAIChatGPT(TestCase):
    """
    Basic tests following the 'Given, When, Then' methodology.
    """

    valid_text: str = "How is the weather in Florianópolis tomorrow?"

    def test_with_invalid_open_ai_api_key_then_unauthorized_response(self):
        OpenAI.api_key = "invalid.key"
        expected_message: str = "Incorrect API key provided: invalid.key. You can find your API key at https://beta.openai.com."
        expected_status_code: int = HTTPStatus.UNAUTHORIZED

        response_message, response_status_code = OpenAI.chatgpt(self.valid_text)

        self.assertEqual(expected_message, response_message)
        self.assertEqual(expected_status_code, response_status_code)

    def test_with_promt_not_a_string_then_bad_request_response(self):
        OpenAI.api_key = API_KEY
        int_text: int = 1
        expected_message: str = f"{int_text} is not valid under any of the given schemas - 'prompt'"
        expected_status_code: int = HTTPStatus.BAD_REQUEST

        response_message, response_status_code = OpenAI.chatgpt(int_text)

        self.assertEqual(expected_message, response_message)
        self.assertEqual(expected_status_code, response_status_code)

    def test_with_valid_key_and_text_then_ok_response(self):
        OpenAI.api_key = API_KEY
        expected_status: int = HTTPStatus.OK

        response_message, response_status_code = OpenAI.chatgpt(self.valid_text)

        self.assertEqual(expected_status, response_status_code)
