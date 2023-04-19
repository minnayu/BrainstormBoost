# backend file

from flask import Flask
from Member import Member

app = Flask(__name__)

# members API route

@app.route("/members")
def members():
    print("member1's attributes")
    member1 = Member("Luis Rivas", ["Skill1", "Skill2"], ["Interest1", "Interest2"])
    member2 = Member("Minna Yu", ["Skill1", "Skill2"], ["Interest1", "Interest2"])
    member3 = Member("Gil A", ["Skill1", "Skill2"], ["Interest1", "Interest2"])

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
    return {"members": [member1.name, member2.name, member3.name]}

@app.route("/add_members")
def add_members():
    return {"members": ["test1", "test2","test3"]}

if __name__ == "__main__":
    app.run(debug=True)