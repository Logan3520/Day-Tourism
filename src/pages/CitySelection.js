import React from "react";
import { useNavigate } from "react-router-dom";
import { HOMEPAGE_CITIES } from "../constants/cities";
import "./CitySelection.css";

function CitySelection() {
  const navigate = useNavigate();

  const cities = HOMEPAGE_CITIES;

  const handleCitySelect = (cityId) => {
    navigate(`/${cityId}`);
  };

  return (
    <div className="city-selection">
      {/* Hero Section */}
      <section className="selection-hero">
        <div className="hero-content">
          <h1>Explore India's Cultural Capitals</h1>
          <p>Discover amazing tourist destinations and nearby attractions in India's most vibrant cities</p>
        </div>
      </section>

      {/* City Cards Section */}
      <section className="cities-section">
        <div className="container">
          <h2>Choose Your Destination</h2>
          <div className="cities-grid">
            {cities.map((city) => (
              <div 
                key={city.id}
                className="city-card"
                onClick={() => handleCitySelect(city.id)}
                style={{ background: city.color }}
              >
                <div className="city-image">
                  <img src={city.image} alt={city.name} />
                  <div className="city-overlay"></div>
                </div>
                <div className="city-info">
                  <h3>{city.name}</h3>
                  <h4>{city.subtitle}</h4>
                  <p>{city.description}</p>
                  <div className="city-stats">
                    <span className="stat">{city.attractions}</span>
                    <span className="stat">{city.categories}</span>
                  </div>
                  <button className="explore-btn">
                    Explore {city.name} →
                  </button>
                </div>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Features Section */}
      <section className="features-section">
        <div className="container">
          <h2>What You'll Discover</h2>
          <div className="features-grid">
            <div className="feature-card">
              <div className="feature-icon">🏛️</div>
              <h3>Historical Sites</h3>
              <p>Ancient monuments, forts, and heritage locations</p>
            </div>
            <div className="feature-card">
              <div className="feature-icon">🕉️</div>
              <h3>Spiritual Centers</h3>
              <p>Temples, mosques, churches, and meditation centers</p>
            </div>
            <div className="feature-card">
              <div className="feature-icon">🌿</div>
              <h3>Natural Beauty</h3>
              <p>Parks, gardens, beaches, and scenic landscapes</p>
            </div>
            <div className="feature-card">
              <div className="feature-icon">🎨</div>
              <h3>Cultural Hubs</h3>
              <p>Museums, art galleries, and cultural centers</p>
            </div>
          </div>
        </div>
      </section>
    </div>
  );
}

export default CitySelection; 