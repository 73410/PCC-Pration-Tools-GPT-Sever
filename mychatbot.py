import requests
import tiktoken

ENCODER = tiktoken.get_encoding("gpt2")


class MyChatbot:
    """
    Official ChatGPT API
    """

    def __init__(
            self,
            api_key: str,
            engine: str = "gpt-3.5-turbo",
            proxy: str = None,
            max_tokens: int = 3000,
            system_prompt: str = " 你要记住这些设定，并严格按照此设定角色扮演； 你是一个名为pcc的minecraft的服务器的问答机器人，你需要解答玩家们的问题",
    ) -> None:
        """
        Initialize Chatbot with API key (from https://platform.openai.com/account/api-keys)
        """
        self.engine = engine
        self.session = requests.Session()
        self.api_key = api_key
        self.proxy = proxy
        self.max_tokens = max_tokens
        self.system_prompt = system_prompt

    def __truncate_conversation(self, messages: list):
        """
        Truncate the conversation
        """
        while True:
            full_conversation = "\n".join([x["content"] for x in messages])
            if (
                    len(ENCODER.encode(full_conversation)) > self.max_tokens
                    and len(self.conversation) > 1
            ):
                # Don't remove the first message
                messages.pop(1)
            else:
                break

    def ask(self, messages: list) -> dict:
        """
        Ask a question
        """
        self.__truncate_conversation(messages)
        # Get response
        response = self.session.post(
            "https://api.openai.com/v1/chat/completions",
            headers={"Authorization": "Bearer " + self.api_key},
            json={
                "model": self.engine,
                "messages": messages,
                "user": "user",
            },
        )
        if response.status_code != 200:
            raise Exception(
                f"Error: {response.status_code} {response.reason} {response.text}",
            )
        message = response.json()["choices"][0]["message"]
        return message
