from crewai.flow.flow import Flow, start, listen
from dotenv import load_dotenv
from litellm import acompletion  # async version

load_dotenv()


class JokeFlow(Flow):
    model = "gpt-4o-mini"

    @start()
    async def draft_joke(self):
        message = self.state["message"]
        response = await acompletion(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": f"Write a short joke in response to: '{message}'",
                },
            ],
        )

        joke_draft = response["choices"][0]["message"]["content"]
        self.state["joke_draft"] = joke_draft
        return joke_draft

    @listen(draft_joke)
    async def polish_joke(self, joke_draft: str):
        response = await acompletion(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": f"Polish this joke so it’s funnier but still short: {joke_draft}",
                },
            ],
        )

        final_joke = response["choices"][0]["message"]["content"]
        self.state["final_joke"] = final_joke
        return final_joke
