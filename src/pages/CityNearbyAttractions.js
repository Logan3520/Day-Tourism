import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import APIService from '../services/api';
import AttractionCard from '../components/AttractionCard';
import './AttractionsPage.css';

function CityNearbyAttractions() {
  const { city } = useParams();
  const [attractions, setAttractions] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [filteredAttractions, setFilteredAttractions] = useState([]);
  const [selectedCategory, setSelectedCategory] = useState('all');

  // City configuration
  const cityConfig = {
    pune: {
      name: 'Pune',
      subtitle: 'Nearby Getaways',
      description: 'Discover amazing destinations within driving distance from Pune',
      gradient: 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)'
    },
    mumbai: {
      name: 'Mumbai',
      subtitle: 'Weekend Escapes',
      description: 'Explore scenic spots and hill stations near the City of Dreams',
      gradient: 'linear-gradient(135deg, #ff6b6b 0%, #feca57 100%)'
    },
    delhi: {
      name: 'Delhi',
      subtitle: 'Capital Surroundings',
      description: 'Experience the beauty around India\'s capital with nearby attractions',
      gradient: 'linear-gradient(135deg, #a8edea 0%, #fed6e3 100%)'
    },
    kolkata: {
      name: 'Kolkata',
      subtitle: 'Bengal Wonders',
      description: 'Immerse in the natural and cultural gems around the City of Joy',
      gradient: 'linear-gradient(135deg, #96fbc4 0%, #f9f586 100%)'
    }
  };

  const currentCity = cityConfig[city?.toLowerCase()] ;

  useEffect(() => {
    const fetchAttractions = async () => {
      try {
        setLoading(true);
        let data;
        
        // Make API call based on city - for now all cities use the same nearby attractions
        // This can be customized later for city-specific nearby attractions
        switch (city?.toLowerCase()) {
          case 'mumbai':
          case 'delhi':
          case 'kolkata':
          case 'pune':
          default:
            data = await APIService.getCityNearbyAttractions(city?.toLowerCase());
            break;
        }
        
        setAttractions(data);
        setFilteredAttractions(data);
      } catch (err) {
        setError('Failed to load nearby attractions. Please try again later.');
        console.error('Error fetching nearby attractions:', err);
      } finally {
        setLoading(false);
      }
    };

    fetchAttractions();
  }, [city]);

  const handleCategoryFilter = (category) => {
    setSelectedCategory(category);
    if (category === 'all') {
      setFilteredAttractions(attractions);
    } else {
      const filtered = attractions.filter(attraction => 
        attraction.category.toLowerCase() === category.toLowerCase()
      );
      setFilteredAttractions(filtered);
    }
  };

  const categories = ['all', ...new Set(attractions.map(attraction => attraction.category))];

  if (loading) {
    return (
      <div className="attractions-page">
        <div className="loading-container">
          <div className="loading-spinner"></div>
          <p>Loading nearby attractions...</p>
        </div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="attractions-page">
        <div className="error-container">
          <h2>Oops! Something went wrong</h2>
          <p>{error}</p>
          <button onClick={() => window.location.reload()} className="retry-button">
            Try Again
          </button>
        </div>
      </div>
    );
  }

  return (
    <div className="attractions-page">
      <header 
        className="attractions-header"
        style={{ background: currentCity.gradient }}
      >
        <h1>{currentCity.subtitle}</h1>
        <p>{currentCity.description}</p>
        <div className="city-badge">
          <span className="city-subtitle">Near {currentCity.name}</span>
        </div>
      </header>

      <div className="filter-section">
        <div className="container">
          <h3>Filter by Category:</h3>
          <div className="category-filters">
            {categories.map(category => (
              <button
                key={category}
                className={`filter-btn ${selectedCategory === category ? 'active' : ''}`}
                onClick={() => handleCategoryFilter(category)}
              >
                {category.charAt(0).toUpperCase() + category.slice(1)}
              </button>
            ))}
          </div>
        </div>
      </div>

      <div className="distance-info">
        <div className="container">
          <p><strong>Note:</strong> All destinations are within driving distance of {currentCity.name}. Travel time may vary based on traffic and route conditions.</p>
        </div>
      </div>

      <div className="attractions-grid">
        {filteredAttractions.map(attraction => (
          <div key={attraction.id} className="nearby-card-wrapper">
            <AttractionCard attraction={attraction} />
            {attraction.distance && (
              <div className="distance-badge">
                📍 {attraction.distance} from {currentCity.name}
              </div>
            )}
          </div>
        ))}
      </div>

      {filteredAttractions.length === 0 && (
        <div className="no-results">
          <p>No nearby attractions found for the selected category.</p>
        </div>
      )}

      <div className="attractions-stats">
        <div className="container">
          <div className="stats-row">
            <div className="stat-item">
              <span className="stat-number">{attractions.length}</span>
              <span className="stat-label">Nearby Destinations</span>
            </div>
            <div className="stat-item">
              <span className="stat-number">{categories.length - 1}</span>
              <span className="stat-label">Categories</span>
            </div>
            <div className="stat-item">
              <span className="stat-number">{filteredAttractions.length}</span>
              <span className="stat-label">Currently Showing</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default CityNearbyAttractions; 