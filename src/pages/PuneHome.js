import React, { useState, useEffect } from "react";
import { Link, useNavigate } from "react-router-dom";
import APIService from "../services/api";
import AttractionCard from "../components/AttractionCard";
import Button from "../components/Button";
import shaniwarWadaImage from "../assets/pictures/Shaniar wada.jpg";
import "./PuneHome.css";

function PuneHome() {
  const navigate = useNavigate();
  const [puneAttractions, setPuneAttractions] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchAttractions = async () => {
      try {
        setLoading(true);
        const data = await APIService.getPuneAttractions();
        setPuneAttractions(data);
      } catch (err) {
        setError("Failed to load attractions. Please try again later.");
        console.error("Error fetching attractions:", err);
      } finally {
        setLoading(false);
      }
    };

    fetchAttractions();
  }, []);

  // Show only first 3 attractions on homepage
  const featuredAttractions = puneAttractions.slice(0, 3);

  return (
    <div className="pune-home">
      {/* Hero Section */}
      <section className="hero">
        <div className="hero-background">
          <img
            src={shaniwarWadaImage}
            alt="Shaniwar Wada - Historic fort in Pune"
            className="hero-image"
            onError={(e) => {
              e.target.src =
                "https://images.unsplash.com/photo-1590736969955-71cc94901144?w=1600&auto=format&fit=crop&q=80&ixlib=rb-4.0.3";
            }}
          />
          <div className="hero-overlay"></div>
        </div>

        <div className="hero-content">
          <div className="container">
            <div className="hero-text">
              <h1 className="hero-title">Discover Pune's Heart & Soul</h1>
              <p className="hero-subtitle">
                Explore Historic Wonders, Serene Landscapes, and Vibrant Culture
                in and around the Oxford of the East.
              </p>

              <div className="hero-actions">
                <Link to="/pune/attractions">
                  <Button variant="primary" size="large">
                    Explore Pune City
                  </Button>
                </Link>
                <Link to="/pune/nearby-attractions">
                  <Button variant="secondary" size="large">
                    Discover Nearby Escapes
                  </Button>
                </Link>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Quick Stats */}
      <section className="stats">
        <div className="container">
          <div className="stats-grid">
            <div className="stat-card">
              <h3>16+</h3>
              <p>Tourist Attractions</p>
            </div>
            <div className="stat-card">
              <h3>8</h3>
              <p>Categories</p>
            </div>
            <div className="stat-card">
              <h3>125km</h3>
              <p>Coverage Radius</p>
            </div>
          </div>
        </div>
      </section>

      {/* Featured Attractions */}
      <section className="featured">
        <div className="container">
          <h2>Featured Attractions</h2>
          <p>Discover some of Pune's most popular destinations</p>
          
          {loading && (
            <div className="loading-container">
              <div className="loading-spinner"></div>
              <p>Loading featured attractions...</p>
            </div>
          )}

          {error && (
            <div className="error-container">
              <p>{error}</p>
              <button
                onClick={() => window.location.reload()}
                className="retry-button"
              >
                Try Again
              </button>
            </div>
          )}

          {!loading && !error && (
            <>
              <div className="attractions-grid">
                {featuredAttractions.map((attraction) => (
                  <AttractionCard key={attraction.id} attraction={attraction} />
                ))}
              </div>
              
              <div className="view-all">
                <Button 
                  text="View All Pune Attractions" 
                  onClick={() => navigate("/pune/attractions")}
                  variant="primary"
                />
              </div>
            </>
          )}
        </div>
      </section>

      {/* Categories Preview */}
      <section className="categories">
        <div className="container">
          <h2>Explore by Category</h2>
          <div className="categories-grid">
            <div
              className="category-card"
              onClick={() => navigate("/pune/attractions")}
            >
              <div className="category-icon">🏛️</div>
              <h3>Historical</h3>
              <p>Ancient forts, palaces & heritage sites</p>
            </div>
            <div
              className="category-card"
              onClick={() => navigate("/pune/attractions")}
            >
              <div className="category-icon">🕉️</div>
              <h3>Religious</h3>
              <p>Temples, spiritual centers & sacred places</p>
            </div>
            <div
              className="category-card"
              onClick={() => navigate("/pune/nearby-attractions")}
            >
              <div className="category-icon">🏔️</div>
              <h3>Adventure</h3>
              <p>Trekking, hill stations & outdoor activities</p>
            </div>
            <div
              className="category-card"
              onClick={() => navigate("/pune/attractions")}
            >
              <div className="category-icon">🌿</div>
              <h3>Nature</h3>
              <p>Gardens, parks & natural beauty</p>
            </div>
          </div>
        </div>
      </section>

      {/* Call to Action */}
      <section className="cta">
        <div className="container">
          <h2>Ready to Explore?</h2>
          <p>
            Start your journey through Pune's incredible attractions and nearby
            destinations
          </p>
          <div className="cta-buttons">
            <Button 
              text="Plan Your Visit" 
              onClick={() => navigate("/pune/attractions")}
              variant="primary"
            />
            <Button 
              text="Discover Nearby" 
              onClick={() => navigate("/pune/nearby-attractions")}
              variant="secondary"
            />
          </div>
        </div>
      </section>
    </div>
  );
}

export default PuneHome; 