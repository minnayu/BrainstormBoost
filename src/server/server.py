from flask import Flask, request, jsonify
from Generator import Generator
from Group import Group
from Member import Member
from VotingSystem import VotingSystem

app = Flask(__name__)
generator = None
voting_system = None

# members API route
@app.route('/api/members', methods=['POST'])
def add_members():
    global generator
    global voting_system

    projectDesc = request.get_json()['projectDescription'] # string
    memberInfo = request.get_json()['memberInfo'] # array of dictionaries with member 'name' and 'skills'

    # Create a group with the project description
    group = Group()
    group.projectDesc = projectDesc

    for member_data in memberInfo:
        name = member_data['name']
        skills = member_data['skills'].split(', ')
        interests = member_data['interests'].split(', ')
        member = Member(name, skills, interests)
        group.AddMember(member)

    generator = Generator(group)
    generator.CreatePrompt()
    generator.Generate()
    generator.ParseIdeas()
    ideas = generator.ideas

    # Create a new VotingSystem object with the generator's ideas
    voting_system = VotingSystem(generator)

    return jsonify({'ideas': [{'title': idea.title, 'description': idea.description} for idea in ideas]})

@app.route('/vote', methods=['POST'])
def handle_vote():
    global voting_system

    data = request.json
    votes = data.get('votes')
    numMembers = data.get('numMembers')

    # Cast votes on the current VotingSystem object
    voting_system.CastVote(votes[0], votes[1], votes[2])

    # Display the voting results
    message = voting_system.DisplayWinner()

    return jsonify({'success': True, 'message': message})

if __name__ == "__main__":
    app.run(debug=True)
