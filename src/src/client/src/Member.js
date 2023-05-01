import React, { useState } from 'react'

function Member( { num, memberInfo, setMemberInfo } ) {
    const [memberValues, setMemberValues] = useState({
        name: "",
        skills: ""
    });

    function update(value, name) {
        // because React state must be a constant,
        // we want to copy the current state
        // and then change what we need to change
        // and then set state to that new object
        let newState = {
          ...memberValues, // spread operator - means all the current key/val pairs
          [name]: value // use the parameter name as the key, param value as the new value
        };
        setMemberValues(newState);
        console.log("Updated state:", newState)
        
        // how to get each Member's recent newState and save it & append to memberInfo
        // setMemberInfo([...memberInfo, newState]);
        setMemberInfo(newState);

        // this is appending every update
    }


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
        
        <div class="card">
            <div class="card-header">
                Member {num}
            </div>
            <div class="card-body">
                <div class="container-fluid">
                    <div class="form-floating">
                        <textarea class="form-control" placeholder="Input member name" id="floatingTextarea" onChange={(e) => update(e.target.value, "name")} value={memberValues.name}></textarea>
                        <label for="floatingTextarea">Member Name</label>
                    </div>
                    <div class="form-floating">
                        <textarea class="form-control" placeholder="Input member skills" id="floatingTextarea2" style={{height: "100px"}} onChange={(e) => update(e.target.value, "skills")} value={memberValues.skills}></textarea>
                        <label for="floatingTextarea2">Member Skills</label>
                    </div>
                </div>
            </div>
        </div>
        
    )
}

export default Member