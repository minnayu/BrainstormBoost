# import openai
#
# openai.ChatCompletion.create(
#   model="gpt-3.5-turbo",
#   messages=[
#         {"role": "system", "content": "You are a very kind helpdesk agent."},
#         {"role": "user", "content": "How can I fix my computer if it is not turning on?"},
#         {"role": "assistant", "content": "Did you try to turn it off and on again?"},
#         {"role": "user", "content": "Yes, I did. What can be the problem?"}
#     ]
# )

import os
import openai
openai.organization = "org-sOZGOhaWYNTrQ6u683TleyYE"
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.Model.list()


# Class Generator
class Generator:
    # initializes Member's attributes (name, skills, interests)
    def __init__(self):
        self.prompt = ""
        self.ideas = []
        self.group = Group()

    def getPrompt(self):
        return self.prompt

    def getIdeas(self):
        return self.ideas

    def createPrompt(self, skills, interests, ):
        prompt += "" #fix prompt creation later

    def generate(self):
        # send to chatGPT here
        pass
