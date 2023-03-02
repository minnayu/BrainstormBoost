# Idea class in which will hold each idea that the ChatGPT API generates

class Idea:
    # Constructor
    def __init__(self, title='', description='', numVotes=0):
        self.title = title
        self.description = description
        self.numVotes = numVotes

    # Sets the project description given a description
    def GetTitle(self):
        return self.title
    def SetTitle(self, title):
        self.title = title

    # Sets the project description given a description
    def GetDescription(self):
        return self.description
    def SetDescription(self, description):
        self.description = description

    # Get, Add and Reduce vote counter
    def GetNumVotes(self):
        return self.numVotes
    def AddVote(self):
        self.numVotes += 1
    def RemoveVote(self):
        if (self.numVotes <= 0):
            pass
        else:
            self.numVotes -= 1


# '''
# main to test the class' function calls
if __name__ == '__main__':

    testIdea = Idea("Title", "foo desc")   
    print("testIdea's member variables")
    print("title: " + testIdea.GetTitle())
    print("description: " + testIdea.GetDescription())
    print("numVotes: " + str(testIdea.GetNumVotes()))

    testIdea2 = Idea("Title #2", "bar desc", 3)   
    print("\ntestIdea #2 member variables")
    print("title: " + testIdea2.GetTitle())
    print("description: " + testIdea2.GetDescription())
    print("numVotes: " + str(testIdea2.GetNumVotes()))

    testIdea3 = Idea("Title #3")
    print("\ntestIdea #3 member variables")
    print("title: " + testIdea3.GetTitle())
    print("description: " + testIdea3.GetDescription())
    print("numVotes: " + str(testIdea3.GetNumVotes()))

    testIdea.AddVote()
    testIdea.AddVote()
    testIdea.AddVote()

    testIdea.RemoveVote()
    testIdea.RemoveVote()
    testIdea.RemoveVote()
    testIdea.RemoveVote()
    testIdea.RemoveVote()
    testIdea.RemoveVote()
    testIdea.RemoveVote()
    testIdea.RemoveVote()

    print("\ntestIdea's numVotes: " + str(testIdea.numVotes))

# '''

