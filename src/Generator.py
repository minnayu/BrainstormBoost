from Member import Member
from Group import Group
from Idea import Idea
import openai
import os

# Class Generator
class Generator:
    # initializes Member's attributes (name, skills, interests)
    def __init__(self, group = Group()):
        self.group = group # FIX USAGE OF GROUP IN THIS CLASS
        self.prompt = "Crate a list of project ideas. " #improve prompt later
        self.ideas = []

    def GetPrompt(self):
        return self.prompt

    def GetIdeas(self):
        return self.ideas

    def CreatePrompt(self, skills, interests):
        self.prompt = '''
        Generate 5 group project ideas in a numbered list. Take in consideration each group member's skills and their interests.
        Project Description: {}
        '''

        i = 0
        for member in self.group.members:
            self.prompt += ("Member ", i, "")
            self.prompt += member.skills
            self.prompt += member.interests
            i += 1

        return self.prompt

    def Generate(self):
        # send to chatGPT here
        pass

# Run everytime the script is called
if __name__ == '__main__':

    userPrompt = '''
    Generate 5 group project ideas in a numbered list. Take in consideration each group member's skills and their interests.
    Project Description: Data Science
    Member 1:
    Skills: C++, Python, Pandas, Machine Learning
    Interests: Videogames, Soccer
    Member 2:
    Skills: C++, C#, Python, Pandas, Machine Learning
    Interests: Education, League of Legends
    '''
    # openai.api_key = 
    response = openai.Completion.create(
        model="text-davinci-003",
        max_tokens=2048,
        prompt=userPrompt,
        temperature=0.0,
    )
    print(response.choices[0].text)
    #openai.api_key = os.getenv("OPENAI_API_KEY")
    print(os.getenv("OPENAI_API_KEY"))

    '''
    testGroup = Group("Data Science Project")
    testGroup.AddMember(Member("Gilberto Arellano", ["C++", "Data Structures"], ["Video Games", "Soccer"]))
    testGroup.AddMember(Member("Minna Yu", ["Web Design"], ["Data Science"]))
    '''