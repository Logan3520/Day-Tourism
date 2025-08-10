import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import APIService from '../services/api';
import AttractionCard from '../components/AttractionCard';
import './AttractionsPage.css';

function CityAttractions() {
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
      subtitle: 'The Oxford of the East',
      description: 'Explore the rich heritage and vibrant culture of the cultural capital of Maharashtra',
      gradient: 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)'
    },
    mumbai: {
      name: 'Mumbai',
      subtitle: 'The City of Dreams',
      description: 'Discover the commercial capital with iconic landmarks and bustling street life',
      gradient: 'linear-gradient(135deg, #ff6b6b 0%, #feca57 100%)'
    },
    delhi: {
      name: 'Delhi',
      subtitle: 'The Heart of India',
      description: 'Experience the capital\'s rich history, from Mughal monuments to modern marvels',
      gradient: 'linear-gradient(135deg, #a8edea 0%, #fed6e3 100%)'
    },
    kolkata: {
      name: 'Kolkata',
      subtitle: 'The City of Joy',
      description: 'Immerse in Bengali culture, colonial architecture, and intellectual heritage',
      gradient: 'linear-gradient(135deg, #96fbc4 0%, #f9f586 100%)'
    }
  };

  const currentCity = cityConfig[city?.toLowerCase()] || cityConfig.pune;

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
        setFilteredAttractions(data);
      } catch (err) {
        setError('Failed to load attractions. Please try again later.');
        console.error('Error fetching attractions:', err);
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
          <p>Loading {currentCity.name} attractions...</p>
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
        <h1>Discover {currentCity.name}</h1>
        <p>{currentCity.description}</p>
        <div className="city-badge">
          <span className="city-subtitle">{currentCity.subtitle}</span>
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

      <div className="attractions-grid">
        {filteredAttractions.map(attraction => (
          <AttractionCard key={attraction.id} attraction={attraction} />
        ))}
      </div>

      {filteredAttractions.length === 0 && (
        <div className="no-results">
          <p>No attractions found for the selected category.</p>
        </div>
      )}

      <div className="attractions-stats">
        <div className="container">
          <div className="stats-row">
            <div className="stat-item">
              <span className="stat-number">{attractions.length}</span>
              <span className="stat-label">Total Attractions</span>
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

export default CityAttractions; 