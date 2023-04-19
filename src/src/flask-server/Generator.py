from Member import Member
from Group import Group
from Idea import Idea
import re
import openai
import os

# Class Generator
class Generator:
    # initializes Member's attributes (name, skills, interests)
    def __init__(self, group = Group()):
        self.group = group # FIX USAGE OF GROUP IN THIS CLASS
        self.prompt = ""
        self.response = ""
        self.ideas = []

    def CreatePrompt(self):
        header = ("Please generate 5 group project ideas in a numbered list. "
              "For each idea, provide a title and a brief description. "
              "Consider the unique skills and interests of each group member "
              "to ensure the projects are engaging and relevant. "
              "Below are the project description and details of each group member:\n\n")

        project_description = f"Project Description: {self.group.projectDesc}\n\n"

        members_string = ""
        for i, member in enumerate(self.group.members, start=1):
            skills = ', '.join(member.skills)
            interests = ', '.join(member.interests)
            members_string += f"Member {i}, {member.name}:\nSkills: {skills}\nInterests: {interests}\n\n"

        self.prompt = header + project_description + members_string

    
    def Generate(self):
        openai.api_key = "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"
        response = openai.Completion.create(
            model= "text-davinci-003",
            max_tokens= 2048,
            prompt= self.prompt,
            temperature= 0.0,
        )
        self.response = response.choices[0].text
    

    def ParseIdeas(self):
        idea_pattern = re.compile(r'(\d+)\.\s(.*?):\s(.*?)(?=\n\n\d+\.|\n?$)', re.DOTALL)
        matches = idea_pattern.findall(self.response)

        ideas = []
        for match in matches:
            idea_number, idea_title, idea_content = match
            ideas.append(Idea(idea_title, idea_content.strip()))

        self.ideas = ideas


# Run everytime the script is called
if __name__ == '__main__':

    testGroup = Group("Data Science Project")
    testGroup.projectDesc = "Find a dataset and create a technical report on a subject"
    testGroup.AddMember(Member("Gilberto Arellano", ["C++", "Data Structures"], ["Video Games", "Soccer"]))
    testGroup.AddMember(Member("Minna Yu", ["Web Design"], ["Data Science"]))

    fooGenerator = Generator(testGroup)

    fooGenerator.CreatePrompt()
    print(fooGenerator.prompt)

    fooGenerator.response = '''
1. Video Game Industry Analysis: Using a dataset of video game sales, create a technical report analyzing the trends in the video game industry. Gilberto can use his C++ and data structure skills to analyze the data, while Minna can use her web design skills to create a visually appealing report.

2. Soccer Performance Analysis: Using a dataset of soccer match results, create a technical report analyzing the performance of teams and players. Gilberto can use his C++ and data structure skills to analyze the data, while Minna can use her web design skills to create a visually appealing report.

3. Data Science Project: Using a dataset of your choice, create a technical report analyzing the data. Gilberto can use his C++ and data structure skills to analyze the data, while Minna can use her web design skills to create a visually appealing report.

4. Social Media Analysis: Using a dataset of social media posts, create a technical report analyzing the trends in social media usage. Gilberto can use his C++ and data structure skills to analyze the data, while Minna can use her web design skills to create a visually appealing report.

5. Online Shopping Analysis: Using a dataset of online shopping transactions, create a technical report analyzing the trends in online shopping. Gilberto can use his C++ and data structure skills to analyze the data, while Minna can use her web design skills to create a visually appealing report.
    '''
    fooGenerator.ParseIdeas()

    for idea in fooGenerator.ideas:
        print(idea)

#    fooGenerator.Generate()
#    print(fooGenerator.response)