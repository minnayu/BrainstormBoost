import React from "react";
import {Link, BrowserRouter} from "react-router-dom";

function Home() {
    return (
       
        <body>
            <div class="text-center">
                <main class="container">
                    <h1 class="display-1">Welcome to BrainstormBoost!</h1>
                    <p class="display-6 lead"> BrainstormBoost is a program that uses OpenAI to generate project ideas for a group of people. All you need to do is enter the members in your group, what their skills and interests are, and describe what kind of project you want. Then it will generate a list of ideas for your group to vote on.</p>
                    <h2 class="display-5"><Link to="/generator">Get Started</Link></h2>
                </main>
            </div>
        </body>
        
    );
}
export default Home;