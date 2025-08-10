import React, { useState, useEffect, useRef } from 'react';
import { Link, useLocation } from 'react-router-dom';
import { getCityConfig, getCityFromPath, CITIES_LIST } from '../constants/cities';
import './Footer.css';

const Footer = () => {
  const [isDropdownOpen, setIsDropdownOpen] = useState(false);
  const location = useLocation();
  const dropdownRef = useRef(null);

  const toggleDropdown = () => {
    setIsDropdownOpen(!isDropdownOpen);
  };

  // Close dropdown when clicking outside
  useEffect(() => {
    const handleClickOutside = (event) => {
      if (dropdownRef.current && !dropdownRef.current.contains(event.target)) {
        setIsDropdownOpen(false);
      }
    };

    document.addEventListener('mousedown', handleClickOutside);
    return () => {
      document.removeEventListener('mousedown', handleClickOutside);
    };
  }, []);

  // Check if we're on homepage
  const isHomepage = () => {
    return location.pathname === '/';
  };

  const currentCity = getCityFromPath(location.pathname);
  const cityInfo = getCityConfig(currentCity);

  // Dynamic footer title and description
  const getFooterTitle = () => {
    if (cityInfo) {
      return `${cityInfo.displayName} Explorer`;
    }
    return 'City Explorers';
  };

  const getFooterDescription = () => {
    if (cityInfo) {
      return cityInfo.fullDescription;
    }
    return 'Discover India\'s most incredible destinations - Explore Historic Wonders, Vibrant Culture, and Amazing Experiences across multiple cities.';
  };

  // Dynamic navigation links
  const getCityNavLink = () => {
    if (cityInfo) {
      return {
        to: `/${currentCity}/attractions`,
        label: `${cityInfo.displayName} City`
      };
    }
    return {
      to: '/pune/attractions',
      label: 'Cities'
    };
  };

  const getNearbyNavLink = () => {
    if (cityInfo) {
      return {
        to: `/${currentCity}/nearby-attractions`,
        label: 'Nearby Places'
      };
    }
    return {
      to: '/pune/nearby-attractions',
      label: 'Nearby Places'
    };
  };

  const cityNavLink = getCityNavLink();
  const nearbyNavLink = getNearbyNavLink();

  // Dynamic copyright text
  const getCopyrightText = () => {
    if (cityInfo) {
      return `© 2025 ${cityInfo.displayName} Explorer. Made with ❤️ for travelers.`;
    }
    return '© 2025 City Explorers. Made with ❤️ for travelers exploring India.';
  };

  return (
    <footer className="footer">
      <div className="container">
        <div className="footer-content">
          <div className="footer-section">
            <h3>{getFooterTitle()}</h3>
            <p>{getFooterDescription()}</p>
            {cityInfo && (
              <div className="city-tagline">
                <span className="tagline">{cityInfo.subtitle}</span>
              </div>
            )}
          </div>
          
          <div className="footer-section">
            <h4>Quick Links</h4>
            <ul className="footer-links">
              <li><Link to="/">Home</Link></li>
              
              {isHomepage() ? (
                // Show cities dropdown on homepage
                <li className="footer-dropdown" ref={dropdownRef}>
                  <button 
                    className="footer-dropdown-trigger" 
                    onClick={toggleDropdown}
                    aria-expanded={isDropdownOpen}
                  >
                    Cities
                    <span className={`dropdown-arrow ${isDropdownOpen ? 'open' : ''}`}>▼</span>
                  </button>
                  
                                      {isDropdownOpen && (
                      <div className="footer-dropdown-menu">
                        {CITIES_LIST.map(city => (
                          <Link 
                            key={city.id}
                            to={`/${city.id}`} 
                            className="footer-dropdown-item"
                            onClick={() => setIsDropdownOpen(false)}
                          >
                            <div className="footer-city-option">
                              <span className="footer-city-name">{city.name}</span>
                              <span className="footer-city-subtitle">{city.subtitle}</span>
                            </div>
                          </Link>
                        ))}
                      </div>
                    )}
                </li>
              ) : (
                // Show city-specific links when not on homepage
                <>
                  <li><Link to={cityNavLink.to}>{cityNavLink.label}</Link></li>
                  <li><Link to={nearbyNavLink.to}>{nearbyNavLink.label}</Link></li>
                </>
              )}
            </ul>
          </div>
          
          <div className="footer-section">
            <h4>Connect With Us</h4>
            <div className="social-links">
              <a href="#" className="social-link" aria-label="Facebook">
                <span>Facebook</span>
              </a>
              <a href="#" className="social-link" aria-label="Instagram">
                <span>Instagram</span>
              </a>
              <a href="#" className="social-link" aria-label="Twitter">
                <span>Twitter</span>
              </a>
            </div>
          </div>
        </div>
        
        <div className="footer-bottom">
          <p>{getCopyrightText()}</p>
        </div>
      </div>
    </footer>
  );
};

export default Footer; 