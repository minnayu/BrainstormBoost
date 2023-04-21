import React from "react";
import "./App.css";
import About from "./About";
import Home from "./Home";
import Generator from "./Generator"
import {Routes, Route, Link, BrowserRouter} from "react-router-dom";
import NavBar from "./NavBar";

function App() {
  return (
    
    <div>
      <NavBar/>
      <Routes>
        <Route path="/" element={<Home/>}/>
        <Route path="/about" element={<About/>}/>
        <Route path="/generator" element={<Generator/>}/>
      </Routes>
    </div>
  );
}

export default App