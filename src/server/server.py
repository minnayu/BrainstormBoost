from flask import Flask, request, jsonify
from Generator import Generator
from Group import Group
from Member import Member

app = Flask(__name__)

# members API route
@app.route('/api/members', methods=['POST'])
def add_members():
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


    # TODO: Send project desc & member info to generator code to generate 
    # ideas and append each idea to 'ideas' array
    generator = Generator(group)
    generator.CreatePrompt()

#     generator.response = '''\
# 1. Video Game Industry Analysis: Using a dataset of video game sales, create a technical report analyzing the trends in the video game industry. Gilberto can use his C++ and data structure skills to analyze the data, while Minna can use her web design skills to create a visually appealing report.

# 2. Soccer Performance Analysis: Using a dataset of soccer match results, create a technical report analyzing the performance of teams and players. Gilberto can use his C++ and data structure skills to analyze the data, while Minna can use her web design skills to create a visually appealing report.

# 3. Data Science Project: Using a dataset of your choice, create a technical report analyzing the data. Gilberto can use his C++ and data structure skills to analyze the data, while Minna can use her web design skills to create a visually appealing report.

# 4. Social Media Analysis: Using a dataset of social media posts, create a technical report analyzing the trends in social media usage. Gilberto can use his C++ and data structure skills to analyze the data, while Minna can use her web design skills to create a visually appealing report.

# 5. Online Shopping Analysis: Using a dataset of online shopping transactions, create a technical report analyzing the trends in online shopping. Gilberto can use his C++ and data structure skills to analyze the data, while Minna can use her web design skills to create a visually appealing report.
# '''

    generator.Generate()
    generator.ParseIdeas()
    ideas = generator.ideas

    for idea in ideas:
        print(idea)

    return jsonify({'ideas': [{'title': idea.title, 'description': idea.description} for idea in ideas]})

if __name__ == "__main__":
    app.run(debug=True)