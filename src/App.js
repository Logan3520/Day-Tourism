import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Header from './components/Header';
import Footer from './components/Footer';
import Homepage from './pages/Homepage';
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
            <Route path="/" element={<Homepage />} />
            <Route path="/pune-attractions" element={<PuneAttractions />} />
            <Route path="/nearby-attractions" element={<NearbyAttractions />} />
            <Route path="/attraction/:id" element={<AttractionDetail />} />
          </Routes>
        </main>
        <Footer />
      </div>
    </Router>
  );
}

export default App;
