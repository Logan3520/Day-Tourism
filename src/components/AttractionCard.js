import React from 'react';
import { Link } from 'react-router-dom';
import Button from './Button';
import './AttractionCard.css';

const AttractionCard = ({ attraction }) => {
  const { id, name, shortDescription, image, tags, category } = attraction;

  return (
    <div className="attraction-card">
      <div className="card-image">
        <img 
          src={image} 
          alt={name} 
          loading="lazy"
          onError={(e) => {
            e.target.src = "https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3";
          }}
        />
        <div className="card-category">
          <span className={`category-badge category-${category}`}>
            {category}
          </span>
        </div>
      </div>
      
      <div className="card-content">
        <h3 className="card-title">{name}</h3>
        <p className="card-description">{shortDescription}</p>
        
        <div className="card-tags">
          {tags.map((tag, index) => (
            <span key={index} className="tag">
              {tag}
            </span>
          ))}
        </div>
        
        <div className="card-actions">
          <Link to={`/attraction/${id}`}>
            <Button variant="primary" size="small">
              View Details
            </Button>
          </Link>
        </div>
      </div>
    </div>
  );
};

export default AttractionCard; 