import React from "react";
import {Link} from "react-router-dom";

function NavBar() {
    return (
        <nav class="navbar navbar-expand-lg bg-body-tertiary">
            <div class="container-fluid">
                <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
                    <div class="navbar-nav">
                    <a class="nav-link active" aria-current="page"><Link to="/">Home</Link></a>
                    <a class="nav-link"><Link to="/about">About</Link></a>
                    <a class="nav-link"><Link to="/generator">Generator</Link></a>
                    </div>
                </div>
            </div>
        </nav>
    );
}

export default NavBar;