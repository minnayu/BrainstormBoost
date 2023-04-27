import React, { useState, useEffect } from 'react'
import Member from "./Member"

function Generator() {
  const [numMembers, setNumMembers] = useState(0)
  const MemberInputs = []

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
  ]

  const getNumMembersDisplay = () => {
    if (numMembers) {
      return numMembers;
    }
  }

  const onDropdownClick = (option) => {
    setNumMembers(option.value)
    // console.log(MemberInputs)
  }

  for (let i = 0; i < numMembers; i++) {
    MemberInputs.push(<Member num={i}/>)
  }
  console.log(MemberInputs)

  return (
      // sample code to get data python code
    // <div>
    //   {(typeof data.members === 'undefined') ? (
    //     <p class="text-center"> Loading...</p>
    //   ) : (
    //     data.members.map((member, i) => (
    //       <p class="text-center" key={i}>{member}</p>
    //     ))
    //   )}
    // </div>
    <div>
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
        {MemberInputs.map(Member)}
        
      </div>
    </div>
  )
}
// pass in data values & updater funtion to child 
// updater function: once changes in child, its gonna run & update parent
// updater function changes info outside of child
// login page sandbox 


export default Generator