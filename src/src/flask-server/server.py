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
    member3 = Member("Gilberto Arellano", ["Skill1", "Skill2"], ["Interest1", "Interest2"])

    return {"members": [member1.name, member2.name, member3.name]}

@app.route("/add_members")
def add_members():
    return {"members": ["test1", "test2","test3"]}

if __name__ == "__main__":
    app.run(debug=True)