import React, { useState, useEffect } from "react";
import { useParams } from 'react-router-dom';
import Slider from "react-slick";
import styled from "styled-components";
import "slick-carousel/slick/slick.css";
import "slick-carousel/slick/slick-theme.css";
import Spinner from "./spinner";

const Detail = (props) => {
  const { id } = useParams();
  const [portfolioitem, setPortfolioItem] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchPortfolioItem = async () => {
      try {
        const timeout = setTimeout(() => {
          setLoading(false);
          alert("Failed to load. Please check your internet connectivity.");
        }, 10000);

        const response = await fetch(`http://localhost:8000/portfolio-item/${id}/`); // Fetch the specific portfolio item using the ID
        const data = await response.json();

        clearTimeout(timeout);
        setLoading(false);
        setPortfolioItem(data);
      } catch (error) {
        console.log(error);
      }
    };

    fetchPortfolioItem();
  }, [id]);

  if (loading) {
    return (
      <SpinnerWrapper className="bg-gradient-to-b from-black to-gray-800 w-full">
        <Spinner />
      </SpinnerWrapper>
    );
  }

  let settings = {
        dots: true,
        infinite: true,
        speed: 500,
        slidesToShow: 1,
        slidesToScroll: 1,
        autoplay: true,
    }

  return (
 <div 
 className="bg-gradient-to-b from-black to-gray-800 w-full text-white md:h-100%">
    <div className="max-w-screen-lg p-4 mx-auto flex flex-col justify-center w-full overflow-hidden h-full">
        <Carousel {...settings}>
                <Wrap>
                    <button>
                      <img src={`http://localhost:8000${portfolioitem.image}`} alt="Slider" />
                    </button>
                </Wrap>
                <Wrap>
                    <button>
                        <img src={`http://localhost:8000${portfolioitem.image1}`} alt='Slider' />
                    </button>
                </Wrap>
                <Wrap>
                    <button>
                        <img src={`http://localhost:8000${portfolioitem.image2}`} alt='Slider' />
                    </button>
                </Wrap>
                <Wrap>
                    <button>
                        <img src={`http://localhost:8000${portfolioitem.image3}`} alt='Slider' />
                    </button>
                </Wrap>
                <Wrap>
                    <button>
                        <img src={`http://localhost:8000${portfolioitem.image4}`} alt='Slider' />
                    </button>
                </Wrap>
                <Wrap>
                    <button>
                        <img src={`http://localhost:8000${portfolioitem.image5}`} alt='Slider' />
                    </button>
                </Wrap>
                <Wrap>
                    <button>
                        <img src={`http://localhost:8000${portfolioitem.image6}`} alt='Slider' />
                    </button>
                </Wrap>
                <Wrap>
                    <button>
                        <img src={`http://localhost:8000${portfolioitem.image7}`} alt='Slider' />
                    </button>
                </Wrap>
            </Carousel>
              <div className="pb-1 pt-11">
          <p className="text-2xl font-bold inline border-b-4 border-blue-500">
            {portfolioitem.title} {/* Display the title of the portfolio item */}
          </p>
        </div>
        <p className="text-1xl mt-10">{portfolioitem.description}</p> {/* Display the description of the portfolio item */}
        <div className="pb-20 pt-11">
         {portfolioitem.link ? (
          <a
            href={portfolioitem.link}
            className="text-1xl font-bold inline border-b-4 border-red-500"
          >
            {portfolioitem.link}
          </a>
          ) : (
            <span className="text-1xl font-bold inline border-b-4 border-red-500">No link for now but you can check the images</span>
          )}
        </div>
    </div> 
    </div> 
  );
}

const Carousel= styled(Slider)`

    & > button {
        opacity: 0;
        height: 90%;
        width: 5;
        padding-top: 10px;
        z-index: 1;



        &:hover {
            opacity: 1;
            transition: opacity 0.2s ease 0s;
        }
    }
    ul li button {
        &:before {
            font-size: 10px;
            color: rgb(150, 158, 171);
        }
    }
    li.slick-active button:before {
        color: white;
    }
    .slick-list {
        overflow: initial;
    }
    slick-prev {
        left: -75px;
    }
    .slick-next {
        right: -75px;
    }
`;

const Wrap = styled.div`
    border-radius: 4px;
    cursor: pointer;
    position: relative;

    button {
        border-radius: 4px;
        box-shadow: rgb(0 0 0 /69%) 0px 26px 30px -10px,
         rgb(0 0 0 / 73%) 0px 16px 10px -10px;
        cursor: pointer;
        display: block;
        position: relative;
        padding: 4px;

        img {
            width: 100%;
            height: 80%;
        }
        &:hover {
            padding: 0;
            border: 4px solid rgba(249, 249, 249, 0.8);
            transition-duration: 300ms;
        }
    }
`;

const SpinnerWrapper = styled.div`
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
`;


export default Detail;
