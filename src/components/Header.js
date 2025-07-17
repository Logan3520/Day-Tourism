import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import './Header.css';

const Header = () => {
  const [isMenuOpen, setIsMenuOpen] = useState(false);

  const toggleMenu = () => {
    setIsMenuOpen(!isMenuOpen);
  };

  const closeMenu = () => {
    setIsMenuOpen(false);
  };

  return (
    <header className="header">
      <div className="container">
        <div className="header-content">
          <Link to="/" className="logo" onClick={closeMenu}>
            <h1>Pune Explorer</h1>
          </Link>
          
          <nav className={`nav ${isMenuOpen ? 'nav-open' : ''}`}>
            <Link to="/" className="nav-link" onClick={closeMenu}>
              Home
            </Link>
            <Link to="/pune-attractions" className="nav-link" onClick={closeMenu}>
              Pune City
            </Link>
            <Link to="/nearby-attractions" className="nav-link" onClick={closeMenu}>
              Nearby Places
            </Link>
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