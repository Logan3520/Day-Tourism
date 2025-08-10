import React, { useState, useEffect, useRef } from 'react';
import { Link, useLocation } from 'react-router-dom';
import { getCityConfig, getCityFromPath, CITIES_LIST } from '../constants/cities';
import './Header.css';

const Header = () => {
  const [isMenuOpen, setIsMenuOpen] = useState(false);
  const [isDropdownOpen, setIsDropdownOpen] = useState(false);
  const location = useLocation();
  const dropdownRef = useRef(null);

  const toggleMenu = () => {
    setIsMenuOpen(!isMenuOpen);
  };

  const closeMenu = () => {
    setIsMenuOpen(false);
    setIsDropdownOpen(false);
  };

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

  // Dynamic header title
  const getHeaderTitle = () => {
    if (cityInfo) {
      return `${cityInfo.displayName} Explorer`;
    }
    return 'City Explorers';
  };

  // Dynamic title link
  const getTitleLink = () => {
    if (cityInfo) {
      return `/${currentCity}`;
    }
    return '/';
  };

  // Dynamic navigation links
  const getCityNavLink = () => {
    if (cityInfo) {
      return {
        to: `/${currentCity}/attractions`,
        label: `${cityInfo.displayName} City`
      };
    }
    // Fallback to Pune for backward compatibility
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
    // Fallback to Pune for backward compatibility
    return {
      to: '/pune/nearby-attractions',
      label: 'Nearby Places'
    };
  };

  const titleLink = getTitleLink();
  const cityNavLink = getCityNavLink();
  const nearbyNavLink = getNearbyNavLink();

  return (
    <header className="header">
      <div className="container">
        <div className="header-content">
          <Link to={titleLink} className="logo" onClick={closeMenu}>
            <h1>{getHeaderTitle()}</h1>
          </Link>
          
          <nav className={`nav ${isMenuOpen ? 'nav-open' : ''}`}>
            <Link to="/" className="nav-link" onClick={closeMenu}>
              Home
            </Link>
            
            {isHomepage() ? (
              // Show cities dropdown on homepage
              <div className="dropdown" ref={dropdownRef}>
                <button 
                  className="nav-link dropdown-trigger" 
                  onClick={toggleDropdown}
                  aria-expanded={isDropdownOpen}
                >
                  Cities
                  <span className={`dropdown-arrow ${isDropdownOpen ? 'open' : ''}`}>▼</span>
                </button>
                
                                  {isDropdownOpen && (
                    <div className="dropdown-menu">
                      {CITIES_LIST.map(city => (
                        <Link 
                          key={city.id}
                          to={`/${city.id}`} 
                          className="dropdown-item"
                          onClick={closeMenu}
                        >
                          <div className="city-option">
                            <span className="city-name">{city.name}</span>
                            <span className="city-subtitle">{city.subtitle}</span>
                          </div>
                        </Link>
                      ))}
                    </div>
                  )}
              </div>
            ) : (
              // Show city-specific links when not on homepage
              <>
                <Link to={cityNavLink.to} className="nav-link" onClick={closeMenu}>
                  {cityNavLink.label}
                </Link>
                <Link to={nearbyNavLink.to} className="nav-link" onClick={closeMenu}>
                  {nearbyNavLink.label}
                </Link>
              </>
            )}
          </nav>
          
          <button 
            className="hamburger" 
            onClick={toggleMenu}
            aria-label={isMenuOpen ? 'Close menu' : 'Open menu'}
          >
            <span className={`hamburger-line ${isMenuOpen ? 'active' : ''}`}></span>
            <span className={`hamburger-line ${isMenuOpen ? 'active' : ''}`}></span>
            <span className={`hamburger-line ${isMenuOpen ? 'active' : ''}`}></span>
          </button>
        </div>
      </div>
    </header>
  );
};

export default Header; 