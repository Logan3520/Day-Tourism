import React from 'react';
import './Button.css';

const Button = ({ 
  children, 
  variant = 'primary', 
  size = 'medium', 
  onClick, 
  href, 
  className = '', 
  disabled = false,
  ...props 
}) => {
  const buttonClasses = `btn btn--${variant} btn--${size} ${className}`;

  if (href) {
    return (
      <a 
        href={href} 
        className={buttonClasses}
        {...props}
      >
        {children}
      </a>
    );
  }

  return (
    <button 
      className={buttonClasses}
      onClick={onClick}
      disabled={disabled}
      {...props}
    >
      {children}
    </button>
  );
};

export default Button; 