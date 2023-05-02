import React, { useState, useEffect } from 'react'
import Member from "./Member"

function Generator() {
  const [numMembers, setNumMembers] = useState(0);
  const [memberInfo, setMemberInfo] = useState([]);
  const [projectDescription, setProjectDescription] = useState('');
  const [generatedIdeas, setGeneratedIdeas] = useState([])

  const options = [
    {value: 1, label: "1"},
    {value: 2, label: "2"},
    {value: 3, label: "3"},
    {value: 4, label: "4"},
    {value: 5, label: "5"},
    {value: 6, label: "6"},
    {value: 7, label: "7"},
    {value: 8, label: "8"},
    {value: 9, label: "9"}
  ];

  const getNumMembersDisplay = () => {
    if (numMembers) {
      return numMembers;
    }
  };

  const onDropdownClick = (option) => {
    const newMemberInfo = Array.from({length: option.value}, () => ({
      name: "",
      skills: ""
    }));
    setNumMembers(option.value);
    setMemberInfo(newMemberInfo);
  };

  function handleSubmitInfo () {
    console.log("Project Description:", projectDescription);
    console.log("Member infos:", memberInfo);
  }

  const memberInputs = Array.from({length: numMembers}, (_, i) => (
    <Member
      key={i}
      num={i+1}
      memberInfo={memberInfo[i]}
      setMemberInfo={(newInfo) => {
        setMemberInfo((prevState) => {
          const newState = [...prevState];
          newState[i] = newInfo;
          return newState;
        });
      }}
    />
  ));

  fetch('/api/members', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ projectDescription: projectDescription, memberInfo: memberInfo })
  })
  .then(response => {
    if (response.ok) {
      response.json().then(data => {
        // console.log('Ideas generated:', data.ideas);
        setGeneratedIdeas(data.ideas)
      });
    } else {
      console.error('Error sending member info to server');
    }
  })
  .catch(error => {
    console.error('Error sending member info to server:', error);
  });
  

  return (
    <div>
      <h1 class="text-center">Project Generator</h1>
      <div class="p-2">
        <div class="form-floating">
          <textarea class="form-control" placeholder="Leave a comment here" id="floatingTextarea2" style={{height: "100px"}} value={projectDescription} onChange={(e) => setProjectDescription(e.target.value)}></textarea>
          <label for="floatingTextarea2">Project Description</label>
        </div>
      </div>
      <p class="text-start">Select number of members:</p>
      <div class="dropdown">
        <button class="btn btn-secondary dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">
          Members: {getNumMembersDisplay()} 
        </button>
        <ul class="dropdown-menu">
          {options.map((option) => (
            <li><a class="dropdown-item" href="#" onClick={() => onDropdownClick(option)} key={option.value}>{option.label}</a></li>
            ))
          }
        </ul>
      </div>

      <div class="container-sm" class="d-flex p-2 grid gap-3 flex-wrap">
        {memberInputs}
      </div>
      <button type="button" class="btn btn-primary" onClick={handleSubmitInfo}>Submit Info</button>
            
      {generatedIdeas.map((idea, index) => (
        <h2 key={index}>{idea}</h2>
      ))}
    </div>
  )
}

export default Generator;
