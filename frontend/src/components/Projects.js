import { Container, Row, Col, Tab, Nav } from "react-bootstrap";
import { ProjectCard } from "./ProjectCard";
import colorSharp2 from "../assets/img/color-sharp2.png";
import 'animate.css';
import TrackVisibility from 'react-on-screen';
import React, { useState, useEffect } from "react";
import axios from "axios";

export const Projects = () => {
  const [portfolioitem, setPortfolioItem] = useState([]);

  useEffect(() => {
    const fetchMe = async () => {
      try {
        const response = await fetch("http://localhost:8000/portfolio-item/");
        const data = await response.json();
        setPortfolioItem(data);
      } catch (error) {
        console.log(error);
      }
    };
    fetchMe();
  }, []);
  const [skillsData, setSkillsData] = useState({});

  useEffect(() => {
    axios
      .get("http://localhost:8000/portfolio/")
      .then((response) => {
        setSkillsData(response.data[0]);
      })
      .catch((error) => {
        console.log(error);
      });
  }, []);

  return (
    <section className="project" id="project">
      <Container>
        <Row>
          <Col size={12}>
            <TrackVisibility>
              {({ isVisible }) =>
              <div className={isVisible ? "animate__animated animate__fadeIn": ""}>
                <h2>{skillsData.title}</h2>
                <p>{skillsData.description}</p>
                <Tab.Container id="projects-tabs" defaultActiveKey="first">
                  <Nav variant="pills" className="nav-pills mb-5 justify-content-center align-items-center" id="pills-tab">
                    <Nav.Item>
                      <Nav.Link eventKey="first">Websites</Nav.Link>
                    </Nav.Item>
                    <Nav.Item>
                      <Nav.Link eventKey="second">Apps</Nav.Link>
                    </Nav.Item>
                    <Nav.Item>
                      <Nav.Link eventKey="third">AI_ML</Nav.Link>
                    </Nav.Item>
                  </Nav>
                  <Tab.Content id="slideInUp" className={isVisible ? "animate__animated animate__slideInUp" : ""}>
                    <Tab.Pane eventKey="first">
                       <Container>
                      <Row>
                        
                         {
                          portfolioitem.map((project, index) => {
                            return (
                              
                              <ProjectCard className="h-300"
                                key={index}
                                title={project.title}                          
                                imgUrl={`http://localhost:8000${project.image}`}
                                projectId={project.id}
                                >
                                </ProjectCard>
                              
                            )
                          })
                        }
                        
                      </Row>
                      </Container>
                    </Tab.Pane>
                    <Tab.Pane eventKey="second">
                      {/* <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Cumque quam, quod neque provident velit, rem explicabo excepturi id illo molestiae blanditiis, eligendi dicta officiis asperiores delectus quasi inventore debitis quo.</p> */}
                    </Tab.Pane>
                    <Tab.Pane eventKey="third">
                      {/* <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Cumque quam, quod neque provident velit, rem explicabo excepturi id illo molestiae blanditiis, eligendi dicta officiis asperiores delectus quasi inventore debitis quo.</p> */}
                    </Tab.Pane>
                  </Tab.Content>
                </Tab.Container>
              </div>}
            </TrackVisibility>
          </Col>
        </Row>
      </Container>
      <img className="background-image-right" src={colorSharp2}></img>
    </section>
  )
}