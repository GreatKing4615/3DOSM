import React, { useEffect, useRef } from 'react';
import maplibregl from 'maplibre-gl';

const Map = () => {
  const mapContainer = useRef(null);

  useEffect(() => {
    maplibregl.accessToken = null;

    const map = new maplibregl.Map({
      container: mapContainer.current,
      style: 'http://localhost:8080/styles/custom-3d/style.json', 
      center: [37.6,55.76],
      zoom: 12.2,
      attributionControl: false,
    });

    return () => {
      map.remove();
    };
  }, []);

  return <div ref={mapContainer} style={{ height: '100vh' }} />;
};

export default Map;
