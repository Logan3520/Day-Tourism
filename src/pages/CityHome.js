import React, { useState, useEffect } from "react";
import { Link, useNavigate, useParams } from "react-router-dom";
import { getCityConfig } from "../constants/cities";
import APIService from "../services/api";
import AttractionCard from "../components/AttractionCard";
import Button from "../components/Button";
import "./CityHome.css";

function CityHome() {
  const navigate = useNavigate();
  const { city } = useParams();
  const [attractions, setAttractions] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  const currentCity = getCityConfig(city?.toLowerCase()) || getCityConfig('pune');

  useEffect(() => {
    const fetchAttractions = async () => {
      try {
        setLoading(true);
        let data;
        
        // Make API call based on city
        switch (city?.toLowerCase()) {
          case 'mumbai':
            data = await APIService.getMumbaiAttractions();
            break;
          case 'delhi':
            data = await APIService.getDelhiAttractions();
            break;
          case 'kolkata':
            data = await APIService.getKolkataAttractions();
            break;
          case 'pune':
          default:
            data = await APIService.getPuneAttractions();
            break;
        }
        
        setAttractions(data);
      } catch (err) {
        setError("Failed to load attractions. Please try again later.");
        console.error("Error fetching attractions:", err);
      } finally {
        setLoading(false);
      }
    };

    fetchAttractions();
  }, [city]);

  // Show only first 3 attractions on homepage
  const featuredAttractions = attractions.slice(0, 3);

  return (
    <div className="city-home">
      {/* Hero Section */}
      <section className="hero">
        <div className="hero-background">
          <img
            src={currentCity.heroImage}
            alt={`${currentCity.name} - ${currentCity.subtitle}`}
            className="hero-image"
            onError={(e) => {
              e.target.src = currentCity.fallbackImage;
            }}
          />
          <div className="hero-overlay" style={{ background: currentCity.gradient }}></div>
        </div>

        <div className="hero-content">
          <div className="container">
            <div className="hero-text">
              <h1 className="hero-title">{currentCity.tagline}</h1>
              <p className="hero-subtitle">{currentCity.description}</p>

              <div className="hero-actions">
                <Link to={`/${city}/attractions`}>
                  <Button variant="primary" size="large">
                    Explore {currentCity.name} City
                  </Button>
                </Link>
                <Link to={`/${city}/nearby-attractions`}>
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
              <h3>{currentCity.stats.attractions}</h3>
              <p>Tourist Attractions</p>
            </div>
            <div className="stat-card">
              <h3>{currentCity.stats.categories}</h3>
              <p>Categories</p>
            </div>
            <div className="stat-card">
              <h3>{currentCity.stats.radius}</h3>
              <p>Coverage Radius</p>
            </div>
          </div>
        </div>
      </section>

      {/* Featured Attractions */}
      <section className="featured">
        <div className="container">
          <h2>Featured Attractions</h2>
          <p>Discover some of {currentCity.name}'s most popular destinations</p>
          
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
                  text={`View All ${currentCity.name} Attractions`}
                  onClick={() => navigate(`/${city}/attractions`)}
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
              onClick={() => navigate(`/${city}/attractions`)}
            >
              <div className="category-icon">🏛️</div>
              <h3>Historical</h3>
              <p>Ancient monuments, forts & heritage sites</p>
            </div>
            <div
              className="category-card"
              onClick={() => navigate(`/${city}/attractions`)}
            >
              <div className="category-icon">🕉️</div>
              <h3>Religious</h3>
              <p>Temples, spiritual centers & sacred places</p>
            </div>
            <div
              className="category-card"
              onClick={() => navigate(`/${city}/nearby-attractions`)}
            >
              <div className="category-icon">🏔️</div>
              <h3>Adventure</h3>
              <p>Trekking, hill stations & outdoor activities</p>
            </div>
            <div
              className="category-card"
              onClick={() => navigate(`/${city}/attractions`)}
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
            Start your journey through {currentCity.name}'s incredible attractions and nearby
            destinations
          </p>
          <div className="cta-buttons">
            <Button 
              text="Plan Your Visit" 
              onClick={() => navigate(`/${city}/attractions`)}
              variant="primary"
            />
            <Button 
              text="Discover Nearby" 
              onClick={() => navigate(`/${city}/nearby-attractions`)}
              variant="secondary"
            />
          </div>
        </div>
      </section>
    </div>
  );
}

export default CityHome; 