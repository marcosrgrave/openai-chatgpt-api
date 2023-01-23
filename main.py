from source.open_ai import OpenAI


def run() -> str:
    text: str = input("What would you like to know about? ")
    open_ai_response_text, open_ai_response_status_code = OpenAI.chatgpt(text, 250)

    return open_ai_response_text


if __name__ == "__main__":
    print(run())
