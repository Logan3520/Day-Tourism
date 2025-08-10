import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Header from './components/Header';
import Footer from './components/Footer';
import Homepage from './pages/Homepage';
import CityHome from './pages/CityHome';
import CityAttractions from './pages/CityAttractions';
import CityNearbyAttractions from './pages/CityNearbyAttractions';
import PuneHome from './pages/PuneHome';
import PuneAttractions from './pages/PuneAttractions';
import NearbyAttractions from './pages/NearbyAttractions';
import AttractionDetail from './pages/AttractionDetail';
import './App.css';

function App() {
  return (
    <Router>
      <div className="App">
        <Header />
        <main className="main-content">
          <Routes>
            {/* Main city selection homepage */}
            <Route path="/" element={<Homepage />} />
            
            {/* Common city routes - dynamic for all cities */}
            <Route path="/:city" element={<CityHome />} />
            <Route path="/:city/attractions" element={<CityAttractions />} />
            <Route path="/:city/nearby-attractions" element={<CityNearbyAttractions />} />
            
            {/* Backward compatibility routes for Pune */}
            <Route path="/pune-home" element={<PuneHome />} />
            <Route path="/pune-attractions" element={<PuneAttractions />} />
            <Route path="/nearby-attractions" element={<NearbyAttractions />} />
            
            {/* Attraction detail page */}
            <Route path="/attraction/:id" element={<AttractionDetail />} />
          </Routes>
        </main>
        <Footer />
      </div>
    </Router>
  );
}

export default App;
