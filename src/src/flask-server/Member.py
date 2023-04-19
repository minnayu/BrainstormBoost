# Member Class
# Holds each members' interests and skills to later create a custom prompt

class Member:
    # Constructor
    def __init__(self, name="", skills=[""], interests=[""]):
        self.name = name
        self.skills = skills
        self.interests = interests

#    def __call__(self):
#        return print(self.name)
    def __eq__(self, Member2):
        if (self.name == Member2.name):
            return True
        else:
            return False

    # Gets the Member's interests
    def AddInterest(self, interest): 
        self.interests += [str(interest)]

    def AddSkill(self, skill):
        self.skills += [str(skill)]

#'''
# Testing Member class
if __name__ == '__main__':


    print("member1's attributes")
    member1 = Member("Luis Rivas", ["Skill1", "Skill2"], ["Interest1", "Interest2"])
    print("Name: ", member1.name)
    print("Interests: ", member1.interests)
    print("Skills: ", member1.skills)

    member1.AddInterest("Data Science")
    member1.AddInterest("Computer Science")
    member1.AddInterest("Fitness")
    member1.AddSkill("C++")
    member1.AddSkill("Python")
    member1.AddSkill("Machine Learning")
    member1.AddSkill("SQL")

    member1.name = "Gilberto Arellano"
    print("Name: ", member1.name)
    print("Interests: ", member1.interests[0])
    print("Skills: ", member1.skills)

 #'''