import Member

class Group:
    # Init class
    def __init__(self):
        self.projectDesc = ''
        self.members = []
        self.numMembers = len(self.members)

    # Sets the project description given a description
    def SetProjectDesc(self, projDesc):
        self.projectDesc = projDesc

    # Returns the project description
    def GetProjectDesc(self):
        return self.projectDesc

    # Adds member to the member array
    def AddMember(self, newMember):
        self.members.append(newMember)

    # Returns a member given the index
    def GetMember(self, memberPos):
        return self.members[memberPos]

# Run everytime the script is called
if __name__ == '__main__':
    test = Group()