import React, { useState, useEffect } from 'react';
import APIService from '../services/api';
import AttractionCard from '../components/AttractionCard';
import './AttractionsPage.css';

function NearbyAttractions() {
  const [attractions, setAttractions] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [filteredAttractions, setFilteredAttractions] = useState([]);
  const [selectedCategory, setSelectedCategory] = useState('all');

  useEffect(() => {
    const fetchAttractions = async () => {
      try {
        setLoading(true);
        const data = await APIService.getNearbyAttractions();
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
  }, []);

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
      <header className="attractions-header">
        <h1>Nearby Getaways</h1>
        <p>Discover amazing destinations within driving distance from Pune</p>
      </header>

      <div className="filter-section">
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
    </div>
  );
}

export default NearbyAttractions; 