# backend file

from flask import Flask, request, jsonify
from Generator import Generator

app = Flask(__name__)

# members API route

@app.route('/api/members', methods=['POST'])
def add_members():
    member_info = request.get_json()['memberInfo']
    # Do something with member_info
    print(member_info) # returns array of each member's values EX: [{'name': 'minna', 'skills': 'C++'}, {'name': 'gil', 'skills': 'c++'}]
    
    # TODO: send this member data to Generator (use sample project description for now until I (Minna) make the project desription input on the page)

    return jsonify(success=True)


if __name__ == "__main__":
    app.run(debug=True)