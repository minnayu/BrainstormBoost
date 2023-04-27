import React, { useState, useEffect } from 'react'

function Member( {num} ) {
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
                Member: {num}
            </div>
            <div class="card-body">
                <div class="container-fluid">
                    <div class="form-floating">
                        <textarea class="form-control" placeholder="Input member name" id="floatingTextarea"></textarea>
                        <label for="floatingTextarea">Member Name</label>
                    </div>
                    <div class="form-floating">
                        <textarea class="form-control" placeholder="Input member skills" id="floatingTextarea2" style={{height: "100px"}}></textarea>
                        <label for="floatingTextarea2">Member Skills</label>
                    </div>
                </div>
            </div>
        </div>
        
    )
}

export default Member