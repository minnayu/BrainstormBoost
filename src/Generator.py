from Member import Member
from Group import Group
from Idea import Idea
import openai

openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "system", "content": "You are a very kind helpdesk agent."},
        {"role": "user", "content": "How can I fix my computer if it is not turning on?"},
        {"role": "assistant", "content": "Did you try to turn it off and on again?"},
        {"role": "user", "content": "Yes, I did. What can be the problem?"}
    ]
)

# import os
# import openai
# openai.organization = "org-sOZGOhaWYNTrQ6u683TleyYE"
# openai.api_key = os.getenv("OPENAI_API_KEY")
# openai.Model.list()


# Class Generator
class Generator:
    # initializes Member's attributes (name, skills, interests)
    def __init__(self, group = Group()):
        self.group = group # FIX USAGE OF GROUP IN THIS CLASS
        self.prompt = "Crate a list of project ideas. " #improve prompt later
        self.ideas = []

    def getPrompt(self):
        return self.prompt

    def getIdeas(self):
        return self.ideas

    def createPrompt(self, skills, interests):
        prompt += "Here is a list of skills the project members have: "
        for skill in skills:
            prompt += skill
        prompt += "Here is a list of interests the project members have: "
        for interest in interests:
            prompt += interest

    def generate(self):
        # send to chatGPT here
        pass

# Run everytime the script is called
if __name__ == '__main__':
    '''
    testGroup = Group("Data Science Project")
    testGroup.AddMember(Member("Gilberto Arellano", ["C++", "Data Structures"], ["Video Games", "Soccer"]))
    testGroup.AddMember(Member("Minna Yu", ["Web Design"], ["Data Science"]))
    '''

    testGenerator = Generator()