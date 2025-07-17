import React, { useState } from 'react';
import AttractionCard from '../components/AttractionCard';
import { puneAttractions } from '../data/puneAttractions';
import './AttractionsPage.css';

const PuneAttractions = () => {
  const [filter, setFilter] = useState('all');
  
  // Get unique categories for filter buttons
  const categories = ['all', ...new Set(puneAttractions.map(attraction => attraction.category))];
  
  // Filter attractions based on selected category
  const filteredAttractions = filter === 'all' 
    ? puneAttractions 
    : puneAttractions.filter(attraction => attraction.category === filter);

  return (
    <div className="attractions-page">
      <div className="page-header">
        <div className="container">
          <h1>Pune City Attractions</h1>
          <p>Discover the rich heritage, vibrant culture, and hidden gems within Pune city</p>
        </div>
      </div>

      <div className="page-content">
        <div className="container">
          {/* Filter Buttons */}
          <div className="filter-section">
            <h3>Filter by Category</h3>
            <div className="filter-buttons">
              {categories.map(category => (
                <button
                  key={category}
                  className={`filter-btn ${filter === category ? 'active' : ''}`}
                  onClick={() => setFilter(category)}
                >
                  {category === 'all' ? 'All' : category.charAt(0).toUpperCase() + category.slice(1)}
                </button>
              ))}
            </div>
          </div>

          {/* Attractions Grid */}
          <div className="attractions-grid">
            {filteredAttractions.map(attraction => (
              <AttractionCard 
                key={attraction.id} 
                attraction={attraction} 
              />
            ))}
          </div>

          {filteredAttractions.length === 0 && (
            <div className="no-results">
              <h3>No attractions found</h3>
              <p>Try selecting a different category filter.</p>
            </div>
          )}
        </div>
      </div>
    </div>
  );
};

export default PuneAttractions; 