import React, { useState, useEffect } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import APIService from '../services/api';
import Button from '../components/Button';
import './AttractionDetail.css';

function AttractionDetail() {
  const { id } = useParams();
  const navigate = useNavigate();
  const [attraction, setAttraction] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchAttraction = async () => {
      try {
        setLoading(true);
        const data = await APIService.getAttractionById(parseInt(id));
        setAttraction(data);
      } catch (err) {
        setError('Failed to load attraction details. Please try again later.');
        console.error('Error fetching attraction:', err);
      } finally {
        setLoading(false);
      }
    };

    fetchAttraction();
  }, [id]);

  if (loading) {
    return (
      <div className="attraction-detail">
        <div className="loading-container">
          <div className="loading-spinner"></div>
          <p>Loading attraction details...</p>
        </div>
      </div>
    );
  }

  if (error || !attraction) {
    return (
      <div className="attraction-detail">
        <div className="error-container">
          <h2>Attraction Not Found</h2>
          <p>{error || 'The attraction you are looking for does not exist.'}</p>
          <Button 
            text="Go Back Home" 
            onClick={() => navigate('/')}
            variant="primary"
          />
        </div>
      </div>
    );
  }

  return (
    <div className="attraction-detail">
      <div className="detail-hero">
        <img 
          src={attraction.image} 
          alt={attraction.name}
          className="hero-image"
        />
        <div className="hero-overlay">
          <div className="container">
            <div className="hero-content">
              <h1>{attraction.name}</h1>
              <p className="hero-description">{attraction.shortDescription}</p>
              <div className="hero-tags">
                {attraction.tags.map((tag, index) => (
                  <span key={index} className="tag">{tag}</span>
                ))}
              </div>
            </div>
          </div>
        </div>
      </div>

      <div className="detail-content">
        <div className="container">
          <div className="content-grid">
            <div className="main-content">
              <section className="description-section">
                <h2>About This Place</h2>
                <p>{attraction.fullDescription}</p>
              </section>

              <section className="activities-section">
                <h2>Things to Do</h2>
                <p>{attraction.nearbyActivities}</p>
              </section>

              <section className="reach-section">
                <h2>How to Reach</h2>
                <p>{attraction.howToReach}</p>
              </section>
            </div>

            <div className="sidebar">
              <div className="info-card">
                <h3>Quick Information</h3>
                
                <div className="info-item">
                  <strong>⏰ Timings</strong>
                  <p>{attraction.timings}</p>
                </div>

                <div className="info-item">
                  <strong>💰 Entry Fee</strong>
                  <p>{attraction.entryFee}</p>
                </div>

                <div className="info-item">
                  <strong>🌟 Best Time to Visit</strong>
                  <p>{attraction.bestTimeToVisit}</p>
                </div>

                <div className="info-item">
                  <strong>📍 Category</strong>
                  <span className="category-badge">{attraction.category}</span>
                </div>

                {attraction.distance && (
                  <div className="info-item">
                    <strong>📏 Distance from Pune</strong>
                    <p>{attraction.distance}</p>
                  </div>
                )}
              </div>

              <div className="action-buttons">
                <Button 
                  text="Back to Attractions" 
                  onClick={() => navigate(-1)}
                  variant="secondary"
                />
                <Button 
                  text="Plan Your Visit" 
                  onClick={() => window.open(`https://maps.google.com/maps?q=${encodeURIComponent(attraction.name + ' Pune')}`, '_blank')}
                  variant="primary"
                />
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default AttractionDetail; 