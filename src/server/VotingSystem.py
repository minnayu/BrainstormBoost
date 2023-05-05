from Group import Group
from Member import Member
from Generator import Generator

class VotingSystem:
    # Init class
    # ideas is a list of Idea objects passed in from Generator
    def __init__(self, generator):
        self.generator = generator
        self.votes = [0] * len(generator.ideas)

    def DisplayIdeas(self):
        for index, idea in enumerate(self.generator.ideas, start=1):
            print(f"{index}. {idea.title}")
            print(idea.description)
            print()

    def CastVote(self, first_choice, second_choice, third_choice):
        choices = [first_choice, second_choice, third_choice]
        for index, choice in enumerate(choices, start=1):
            if 1 <= choice <= len(self.votes):
                self.votes[choice - 1] += (4 - index)  # Assign 3 points for 1st choice, 2 points for 2nd choice, 1 point for 3rd choice
            else:
                print(f"Invalid idea index for choice {index}. Please try again.")

    def DisplayResults(self):
        print("\nVoting Results:")
        for index, idea in enumerate(self.generator.ideas, start=1):
            print(f"{index}. {idea.title} - {self.votes[index - 1]} votes")

    def DisplayWinner(self):
        winner_index = self.votes.index(max(self.votes))
        winning_idea = self.generator.ideas[winner_index]
        print("\nWinning Idea:")
        print(f"{winner_index + 1}. {winning_idea}")
        return(f"{winner_index + 1}. {winning_idea}")



# Run everytime the script is called
if __name__ == '__main__':

    testGroup = Group("Data Science Project")
    testGroup.projectDesc = "Find a dataset and create a technical report on a subject"
    testGroup.AddMember(Member("Gilberto Arellano", ["C++", "Data Structures"], ["Video Games", "Soccer"]))
    testGroup.AddMember(Member("Minna Yu", ["Web Design"], ["Data Science"]))
    testGroup.AddMember(Member("Luis Rivas", ["C++", "Tableau", "R", "Data Structures"], ["Overwatch", "Data Science"]))

    fooGenerator = Generator(testGroup)

    fooGenerator.CreatePrompt()
    print(fooGenerator.prompt)

    '''
    fooGenerator.response = ''
        1. Video Game Industry Analysis: Using a dataset of video game sales, create a technical report analyzing the trends in the video game industry. Gilberto can use his C++ and data structure skills to analyze the data, while Minna can use her web design skills to create a visually appealing report.

        2. Soccer Performance Analysis: Using a dataset of soccer match results, create a technical report analyzing the performance of teams and players. Gilberto can use his C++ and data structure skills to analyze the data, while Minna can use her web design skills to create a visually appealing report.

        3. Data Science Project: Using a dataset of your choice, create a technical report analyzing the data. Gilberto can use his C++ and data structure skills to analyze the data, while Minna can use her web design skills to create a visually appealing report.

        4. Social Media Analysis: Using a dataset of social media posts, create a technical report analyzing the trends in social media usage. Gilberto can use his C++ and data structure skills to analyze the data, while Minna can use her web design skills to create a visually appealing report.

        5. Online Shopping Analysis: Using a dataset of online shopping transactions, create a technical report analyzing the trends in online shopping. Gilberto can use his C++ and data structure skills to analyze the data, while Minna can use her web design skills to create a visually appealing report.
    ''
    '''

    fooGenerator.Generate()
    fooGenerator.ParseIdeas()

    # Create an instance of the IdeaVotingSystem class
    voting_system = VotingSystem(fooGenerator)

    # Display the ideas
    voting_system.DisplayIdeas()

    # Determine the number of voters based on the number of group members
    num_voters = len(fooGenerator.group.members)

    print("\nPlease cast your votes for your top three ideas by entering the corresponding idea numbers:")

    for i in range(num_voters):
        member_name = fooGenerator.group.members[i].name
        print(f"\n{member_name} votes:")
        first_choice = int(input("First choice: "))
        second_choice = int(input("Second choice: "))
        third_choice = int(input("Third choice: "))
        voting_system.CastVote(first_choice, second_choice, third_choice)

    # Display the voting results
    voting_system.DisplayResults()
    voting_system.DisplayWinner()
