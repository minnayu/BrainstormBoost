
class Group:
    # Init class
    def __init__(self):
        self.projectDesc = ''
        self.members = []
        self.numMembers = len(self.members)

    # Sets the project description given a description
    def setProjectDesc(self, projDesc):
        self.projectDesc = projDesc

    # Returns the project description
    def getProjectDesc(self):
        return self.projectDesc

    # Adds member to the member array
    def addMember(self, newMember):
        self.members.append(newMember)

    # Returns a member given the index
    def getMember(self, memberPos):
        return self.members[memberPos]

# Run everytime the script is called
if __name__ == '__main__':
    test = Group()