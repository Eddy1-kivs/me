import React from 'react';
import PropagateLoader from "react-spinners/PropagateLoader"



function Spinner() {
  return (
    <div className="sweet-loading">
      <PropagateLoader color="#36d7b7" size={20} />
    </div>
  )
}

export default Spinner
