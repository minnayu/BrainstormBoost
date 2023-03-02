# Member Class
class Member:
    # attributes of a Member: name, skills, interests 
    name = ""
    global skills
    skills = []
    global interests
    interests = []

    # Gets the Member's name
    def getName(self):
        return name

    # Sets the Member's name
    def setName(self, nameInput):
        global name
        name = nameInput

    # Gets the Member's interests
    def getInterests(self):
        return interests

    # Sets the Member's interests
    def addInterests(self, interestsInput):
        global interests
        interests += interestsInput

    # Gets the Member's skills
    def getSkills(self):
        return skills

    # Sets the Member's skills
    def addSkills(self, skillsInput):
        global skills
        skills += skillsInput


# testing Member class
member1 = Member()

member1.setName("test name")
member1.addInterests(["test interest 1", "test interest 2"])
member1.addSkills(["test skill 1", "test skill 2"])

print("Name: ", member1.getName())
print("Interests: ", member1.getInterests())
print("Skills: ", member1.getSkills())
