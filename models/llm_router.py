import openai

class IlmRouter:
    def __init__(self, api_key, name_gsd):
        self.api_key = api_key
        self.name_gsd = name_gsd
        openai.api_key = self.api_key

    def call_router(self, message):
        """Call the LLM Router API using OpenAI's API."""
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=message,
                max_tokens=None,
                stop=None,
                temperature=0.7
            )
            result = response["choices"][0]["message"]["content"]
            return {"request_source": self.name_gsd, "response": result}
        except openai.OpenAIError as e:
            print(f"Error calling OpenAI API: {e}")
            return None
