import { Container, Row, Col } from "react-bootstrap";
import contactImg from "../assets/img/contact-img.svg";
import 'animate.css';
import TrackVisibility from 'react-on-screen';

export const Contact = () => {

  return (
    <section className="contact" id="connect">
      <Container>
        <Row className="align-items-center">
          <Col size={12} md={6}>
            <TrackVisibility>
              {({ isVisible }) =>
                <img className={isVisible ? "animate__animated animate__zoomIn" : ""} src={contactImg} alt="Contact Us"/>
              }
            </TrackVisibility>
          </Col>
          <Col size={12} md={6}>
            <TrackVisibility>
              {({ isVisible }) =>
                <div className={isVisible ? "animate__animated animate__fadeIn" : ""}>
                <h2>Get In Touch</h2>
                <form action="https://getform.io/f/1c5b8f16-07a0-4e1a-bf98-7d1c7257813c" method="POST">
  <Row>
    <Col size={12} sm={6} className="px-1">
      <input type="text" name="first_name" placeholder="First Name"/>
    </Col>
    <Col size={12} sm={6} className="px-1">
      <input type="text" name="last_name" placeholder="Last Name"/>
    </Col>
    <Col size={12} sm={6} className="px-1">
      <input type="email" name="email_address" placeholder="Email Address"  />
    </Col>
    <Col size={12} sm={6} className="px-1">
      <input type="tel" name="phone_number" placeholder="Phone No."/>
    </Col>
    <Col size={12} className="px-1">
      <textarea name="message" rows="6" placeholder="Message"></textarea>
      <button type="submit"><span>Send</span></button>
    </Col>
   
  </Row>
</form>

              </div>}
            </TrackVisibility>
          </Col>
        </Row>
      </Container>
    </section>
  )
}
