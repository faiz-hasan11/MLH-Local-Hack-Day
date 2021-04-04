import React , {useState} from 'react';
import ReactMapGL from "react-map-gl"
function App() {
  const [viewport , setViewport] = useState(
    {
      latitude :26.449923,
      longitude :80.331871,
      width :"100vw",
      height:"100vh",
      zoom:10
    }
  )
  return (
    <div>
      <ReactMapGL 
      {...viewport}
      mapboxApiAccessToken={process.emv.REACT_APP_MAPBOX_TOKEN}
      mapStyle="mapbox://styles/faiz-hasan11/ckn30xjjp3m4m17qat3cg9s48"
      onViewportChange={viewport =>
      {
        setViewport(viewport)
      }}
      >
        
      </ReactMapGL>
    </div>
  );
}

export default App;
