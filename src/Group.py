from Member import Member

class Group:
    # Init class
    def __init__(self, projectDesc="", members=[Member()], numMembers=0):
        self.projectDesc = projectDesc
        self.members = members
        self.numMembers = numMembers

    # Sets the project description given a description
    def SetProjectDesc(self, projDesc):
        self.projectDesc = projDesc

    # Returns the project description
    def GetProjectDesc(self):
        return self.projectDesc

    # Adds member to the member array
    def AddMember(self, newMember):
        # Checks if the first member is null to replace it with an actual member object
        if self.members[0] == Member(): 
            self.members[0] = newMember
            self.numMembers += 1
        else:
            self.members.append(newMember)
            self.numMembers += 1
    
    def RemoveMember(self, memberPos):
        try:
            if self.numMembers >= 1:
                del self.members[memberPos]
                self.numMembers -= 1
            else:
                return -1
        except IndexError:
            return -1

    # Returns a member given the index
    '''
    def GetMember(self, memberPos):
        try:
            
            return self.members[memberPos]
        except IndexError:
            print("Member does not exist")
            return -1
    '''



# Run everytime the script is called
if __name__ == '__main__':
    testGroup = Group()

    print("Test Group's Project:", testGroup.GetProjectDesc())
    print("Test Group's Members:", testGroup.members[0]) # Null member object

    member1 = Member("Gilberto Arellano", ["C++", "Data Structures"], ["Video Games", "Soccer"])
    member2 = Member("Minna Yu", ["Web Design"], ["Data Science"])
    testGroup.AddMember(member1)
    testGroup.AddMember(member2)
    
    # Iterate through each member and its values
    for member in testGroup.members:
        print("Name: ", member.name)
        print("Skills: ", member.skills)
        print("Interests: ", member.interests)
        print()





