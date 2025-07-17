import React, { useState } from 'react';
import AttractionCard from '../components/AttractionCard';
import { nearbyAttractions } from '../data/nearbyAttractions';
import './AttractionsPage.css';

const NearbyAttractions = () => {
  const [filter, setFilter] = useState('all');
  
  // Get unique categories for filter buttons
  const categories = ['all', ...new Set(nearbyAttractions.map(attraction => attraction.category))];
  
  // Filter attractions based on selected category
  const filteredAttractions = filter === 'all' 
    ? nearbyAttractions 
    : nearbyAttractions.filter(attraction => attraction.category === filter);

  return (
    <div className="attractions-page">
      <div className="page-header">
        <div className="container">
          <h1>Nearby Escapes</h1>
          <p>Explore beautiful destinations within a short drive from Pune - hill stations, forts, and natural wonders</p>
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

          {/* Distance Info */}
          <div className="distance-info">
            <p><strong>Note:</strong> All destinations are within 125km of Pune city center. Distance and travel time may vary based on traffic and route conditions.</p>
          </div>

          {/* Attractions Grid */}
          <div className="attractions-grid">
            {filteredAttractions.map(attraction => (
              <div key={attraction.id} className="nearby-card-wrapper">
                <AttractionCard attraction={attraction} />
                <div className="distance-badge">
                  📍 {attraction.distance} from Pune
                </div>
              </div>
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

export default NearbyAttractions; 