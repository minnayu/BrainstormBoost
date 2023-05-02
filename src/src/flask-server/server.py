# backend file

from flask import Flask, request, jsonify
from Generator import Generator

app = Flask(__name__)

# members API route

@app.route('/api/members', methods=['POST'])
def add_members():
    projectDesc = request.get_json()['projectDescription'] # string
    memberInfo = request.get_json()['memberInfo'] # array of dictionaries with member 'name' and 'skills'
    
    print(projectDesc) # string
    print(memberInfo) # returns array of each member's values EX: [{'name': 'minna', 'skills': 'C++'}, {'name': 'gil', 'skills': 'c++'}]
    
    # TODO: Send project desc & member info to generator code to generate 
    # ideas and append each idea to 'ideas' array
    generator = Generator()
    ideas = ["first generated idea", "second generated idea"]
    
    return jsonify({'ideas': ideas})


if __name__ == "__main__":
    app.run(debug=True)