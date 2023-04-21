import React, { useState, useEffect } from 'react'

function Generator() {
  // data: variable 
  // setData: function to set variable
  const [data, setData] = useState([{}])

  useEffect(() => {
    fetch("/members").then(
      res => res.json()
    ).then(
      data => {
        setData(data)
        console.log(data)
      }
    )
  }, [])

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

    // SAMPLE FORM
    <div class="container-sm" class="d-flex p-2">
        <form>
            <div class="mb-3">
                <label for="formGroupExampleInput" class="form-label">Example label</label>
                <input type="text" class="form-control" id="formGroupExampleInput" placeholder="Example input placeholder"/>
            </div>
            <div class="mb-3">
                <label for="formGroupExampleInput2" class="form-label">Another label</label>
                <input type="text" class="form-control" id="formGroupExampleInput2" placeholder="Another input placeholder"/>
            </div>
        </form>
        <form>
            <div class="mb-3">
                <label for="formGroupExampleInput" class="form-label">Example label</label>
                <input type="text" class="form-control" id="formGroupExampleInput" placeholder="Example input placeholder"/>
            </div>
            <div class="mb-3">
                <label for="formGroupExampleInput2" class="form-label">Another label</label>
                <input type="text" class="form-control" id="formGroupExampleInput2" placeholder="Another input placeholder"/>
            </div>
        </form>
    </div>
    
  )
}

export default Generator