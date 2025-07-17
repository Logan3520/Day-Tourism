import React from 'react';
import { Link } from 'react-router-dom';
import AttractionCard from '../components/AttractionCard';
import Button from '../components/Button';
import { puneAttractions } from '../data/puneAttractions';
import './Homepage.css';

const Homepage = () => {
  // Get featured attractions (first 4 from the data)
  const featuredAttractions = puneAttractions.slice(0, 4);

  return (
    <div className="homepage">
      {/* Hero Section */}
      <section className="hero">
        <div className="hero-background">
          <img 
            src="https://images.unsplash.com/photo-1578662996442-48f60103fc96?w=1600&auto=format&fit=crop&q=80" 
            alt="Shaniwar Wada - Historic fort in Pune" 
            className="hero-image"
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
                <Link to="/pune-attractions">
                  <Button variant="primary" size="large">
                    Explore Pune City
                  </Button>
                </Link>
                <Link to="/nearby-attractions">
                  <Button variant="secondary" size="large">
                    Discover Nearby Escapes
                  </Button>
                </Link>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Featured Attractions */}
      <section className="featured-section">
        <div className="container">
          <div className="section-header">
            <h2>Featured Attractions</h2>
            <p>Discover the most popular destinations that make Pune special</p>
          </div>
          
          <div className="featured-grid">
            {featuredAttractions.map(attraction => (
              <AttractionCard 
                key={attraction.id} 
                attraction={attraction} 
              />
            ))}
          </div>
          
          <div className="section-footer">
            <Link to="/pune-attractions">
              <Button variant="ghost" size="medium">
                View All Pune Attractions
              </Button>
            </Link>
          </div>
        </div>
      </section>

      {/* Call to Action Section */}
      <section className="cta-section">
        <div className="container">
          <div className="cta-content">
            <h2>Ready to Explore?</h2>
            <p>
              From ancient forts to serene hill stations, from spiritual centers to modern attractions - 
              Pune and its surroundings offer something for every traveler.
            </p>
            <div className="cta-actions">
              <Link to="/pune-attractions">
                <Button variant="primary" size="large">
                  Start Your Journey
                </Button>
              </Link>
            </div>
          </div>
        </div>
      </section>
    </div>
  );
};

export default Homepage; 