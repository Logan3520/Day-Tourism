import React from 'react';
import { useParams, Link, Navigate } from 'react-router-dom';
import Button from '../components/Button';
import { puneAttractions } from '../data/puneAttractions';
import { nearbyAttractions } from '../data/nearbyAttractions';
import './AttractionDetail.css';

const AttractionDetail = () => {
  const { id } = useParams();
  
  // Combine both data sources to find the attraction
  const allAttractions = [...puneAttractions, ...nearbyAttractions];
  const attraction = allAttractions.find(attr => attr.id === parseInt(id));

  // If attraction not found, redirect to homepage
  if (!attraction) {
    return <Navigate to="/" replace />;
  }

  const isPuneAttraction = puneAttractions.some(attr => attr.id === attraction.id);
  const backLink = isPuneAttraction ? '/pune-attractions' : '/nearby-attractions';
  const backText = isPuneAttraction ? 'Back to Pune Attractions' : 'Back to Nearby Attractions';

  return (
    <div className="attraction-detail">
      {/* Hero Image Section */}
      <div className="detail-hero">
        <img src={attraction.image} alt={attraction.name} className="detail-hero-image" />
        <div className="detail-hero-overlay">
          <div className="container">
            <div className="detail-hero-content">
              <h1 className="detail-title">{attraction.name}</h1>
              <div className="detail-tags">
                {attraction.tags.map((tag, index) => (
                  <span key={index} className="detail-tag">
                    {tag}
                  </span>
                ))}
              </div>
              {attraction.distance && (
                <div className="detail-distance">
                  📍 {attraction.distance} from Pune
                </div>
              )}
            </div>
          </div>
        </div>
      </div>

      {/* Content Section */}
      <div className="detail-content">
        <div className="container">
          <div className="detail-grid">
            {/* Main Content */}
            <div className="detail-main">
              <section className="detail-section">
                <h2>About This Place</h2>
                <p className="detail-description">{attraction.fullDescription}</p>
              </section>

              <section className="detail-section">
                <h2>Nearby Food & Activities</h2>
                <p>{attraction.nearbyActivities}</p>
              </section>
            </div>

            {/* Sidebar */}
            <div className="detail-sidebar">
              <div className="info-card">
                <h3>Key Information</h3>
                <div className="info-list">
                  <div className="info-item">
                    <strong>Timings:</strong>
                    <span>{attraction.timings}</span>
                  </div>
                  <div className="info-item">
                    <strong>Entry Fee:</strong>
                    <span>{attraction.entryFee}</span>
                  </div>
                  <div className="info-item">
                    <strong>Best Time to Visit:</strong>
                    <span>{attraction.bestTimeToVisit}</span>
                  </div>
                </div>
              </div>

              <div className="info-card">
                <h3>How to Reach</h3>
                <p>{attraction.howToReach}</p>
              </div>

              {/* Static Map Placeholder */}
              <div className="info-card">
                <h3>Location</h3>
                <div className="map-placeholder">
                  <div className="map-content">
                    <span className="map-icon">📍</span>
                    <p>Interactive map coming soon</p>
                    <small>For now, use the directions above to reach this destination</small>
                  </div>
                </div>
              </div>
            </div>
          </div>

          {/* Back Button */}
          <div className="detail-actions">
            <Link to={backLink}>
              <Button variant="secondary" size="medium">
                ← {backText}
              </Button>
            </Link>
          </div>
        </div>
      </div>
    </div>
  );
};

export default AttractionDetail; 