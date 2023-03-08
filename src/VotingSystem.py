from Idea import Idea

class VotingSystem:
    # Init class
    # ideas is a list of Idea objects passed in from Generator
    def __init__(self, numVotes=0, ideas=[]):
        self.numVotes = numVotes
        self.ideas = ideas

    # TODO: Determine algorithm to decide winning idea
    def GetWinningIdeas(self):
        for idea in self.ideas:
            if idea.GetNumVotes() > 3:
                print('Winning Idea Found:', idea.GetTitle())

    # Cast a vote on the selected idea
    def CastVote(self, ideaPos):
        self.ideas[ideaPos].AddVote()

    # Removes a vote from the selected idea 
    def RemoveVote(self, ideaPos):
        self.ideas[ideaPos].RemoveVote()


# Run everytime the script is called
if __name__ == '__main__':
    test = VotingSystem()