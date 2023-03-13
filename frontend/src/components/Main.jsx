import '../App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import { NavBar } from "./NavBar";
import { Banner } from "./Banner";
import { Skills } from "./Skills";
import { Projects } from "./Projects";
import { Contact } from "./Contact";
import { Footer } from "./Footer";
import Spinner from "./spinner";
import styled from "styled-components";
import React, { useState, useEffect } from "react";

function Main() {
    const [home, setHome] = useState(null);
    const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchHome = async () => {
      try {
        const timeout = setTimeout(() => {
          setLoading(false);
          alert("Failed to load. Please check your internet connectivity.");
        }, 10000);
        const response = await fetch("http://localhost:8000/home/");
        
        clearTimeout(timeout);
        setLoading(false);
        const data = await response.json();
        setHome(data[0]);
      } catch (error) {
        console.log(error);
      }
    };

    fetchHome();
  }, []);

  if (loading) {
    return (
      <SpinnerWrapper className="bg-gradient-to-b from-black to-gray-800 w-full">
        <Spinner />
      </SpinnerWrapper>
    );
  }

  if (!home) {
    return null;
  }

  return (
    <div>
      <NavBar />
      <Banner />
      <Skills />
      <Projects />
      <Contact />
      <Footer />
    </div>
  );
}

const SpinnerWrapper = styled.div`
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
`;

export default Main;
