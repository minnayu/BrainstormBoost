import React from "react";
import {Link, BrowserRouter} from "react-router-dom";

function Home() {
    return (
       
        <body>
            <main class="container">
            <h1 class="text-center">Welcome to BrainstormBoost!</h1>
            <h2 class="text-center"><Link to="/generator">Get Started</Link></h2>
            </main>
        </body>
        
    );
}
export default Home;