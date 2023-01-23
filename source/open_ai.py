from http import HTTPStatus
from typing import Generator

import requests

import openai
from openai import InvalidRequestError
from openai.error import AuthenticationError

from source.config import API_KEY


class OpenAI:
    api_key: str = API_KEY
    model: str = "text-davinci-003"
    temperature: int = 0

    @classmethod
    def chatgpt(cls, text: str = 'Say this is a test', max_tokens: int = 20) -> tuple[str, int]:

        try:
            openai.api_key = cls.api_key
            response: Generator = openai.Completion.create(model=cls.model,
                                                           prompt=text,
                                                           temperature=cls.temperature,
                                                           max_tokens=max_tokens)

        except openai.error.AuthenticationError as unauthorized_error:
            return str(unauthorized_error), HTTPStatus.UNAUTHORIZED

        except openai.error.InvalidRequestError as bad_request_error:
            return str(bad_request_error), HTTPStatus.BAD_REQUEST

        response_text: str = response.get("choices")[0].get("text")

        return response_text, HTTPStatus.OK

    @classmethod
    def chatgpt_request(cls, text: str = 'Say this is a test', max_tokens: int = 20) -> requests.Response:

        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {API_KEY}',
        }

        json_data = {
            'model': cls.model,
            'prompt': text,
            'max_tokens': max_tokens,
            'temperature': cls.temperature,
        }

        response: requests.Response = requests.post(url='https://api.openai.com/v1/completions',
                                                    headers=headers,
                                                    json=json_data)

        return response


OpenAI.chatgpt_request()
