# Idea class in which will hold each idea that the ChatGPT API generates

class Idea:
    # Constructor
    def __init__(self, title='', description='', votes=0):
        self.title = title
        self.description = description
        self.votes = votes

    def __str__(self):
        return f"{self.title}\n{self.description}\n"

    # Get, Add and Reduce vote counter
    def AddVote(self):
        self.votes += 1
    def RemoveVote(self):
        if (self.votes <= 0):
            pass
        else:
            self.votes -= 1

# '''
# main to test the class' function calls
if __name__ == '__main__':

    testIdea = Idea("Title", "foo desc")   
    print("testIdea's member variables")
    print("title: " + testIdea.title)
    print("description: " + testIdea.description)
    print("votes: " + str(testIdea.votes))

    testIdea2 = Idea("Title #2", "bar desc", 3)   
    print("\ntestIdea #2 member variables")
    print("title: " + testIdea2.title)
    print("description: " + testIdea2.description)
    print("votes: " + str(testIdea2.votes))

    testIdea3 = Idea("Title #3")
    print("\ntestIdea #3 member variables")
    print("title: " + testIdea3.title)
    print("description: " + testIdea3.description)
    print("votes: " + str(testIdea3.votes))

    testIdea.AddVote()
    testIdea.AddVote()
    testIdea.AddVote()

    print("\ntestIdea's votes: " + str(testIdea.votes))

# '''

