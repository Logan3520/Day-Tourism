import React from 'react';
import { Link } from 'react-router-dom';
import './Footer.css';

const Footer = () => {
  return (
    <footer className="footer">
      <div className="container">
        <div className="footer-content">
          <div className="footer-section">
            <h3>Pune Explorer</h3>
            <p>Discover Pune's Heart & Soul - Explore Historic Wonders, Serene Landscapes, and Vibrant Culture.</p>
          </div>
          
          <div className="footer-section">
            <h4>Quick Links</h4>
            <ul className="footer-links">
              <li><Link to="/">Home</Link></li>
              <li><Link to="/pune-attractions">Pune City</Link></li>
              <li><Link to="/nearby-attractions">Nearby Places</Link></li>
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
          <p>&copy; 2025 Pune Tourist Explorer. Made with ❤️ for travelers.</p>
        </div>
      </div>
    </footer>
  );
};

export default Footer; 