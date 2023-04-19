import React from "react";
import "./App.css";
import About from "./About";
import Home from "./Home";
import Members from "./Members"
import {Routes, Route, Link, BrowserRouter} from "react-router-dom";
import NavBar from "./NavBar";

function App() {
  return (
    
    <div className="App">
      <NavBar/>
      <Routes>
        <Route path="/" element={<Home/>}/>
        <Route path="/about" element={<About/>}/>
        <Route path="/members" element={<Members/>}/>
      </Routes>
    </div>
  );
}

export default App