# 🏛️ City Explorers - Indian Tourist Explorer

**Discover India's Heart & Soul** - A comprehensive web application for exploring heritage, culture, and attractions across India's major cities.

[![React](https://img.shields.io/badge/React-19.1.0-blue?logo=react)](https://reactjs.org/)
[![Flask](https://img.shields.io/badge/Flask-2.3.3-green?logo=flask)](https://flask.palletsprojects.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## 🌟 Overview

City Explorers is a modern, responsive web application that helps users discover tourist attractions, cultural sites, and nearby destinations across four major Indian cities: **Pune**, **Mumbai**, **Delhi**, and **Kolkata**. The application provides detailed information about attractions, including historical significance, visiting hours, entry fees, and nearby activities.

## 🚀 Features

### 🏙️ Multi-City Support
- **Pune** - "The Oxford of the East" - 8+ attractions with rich Maratha heritage
- **Mumbai** - "The City of Dreams" - 8+ attractions including Bollywood and marine attractions  
- **Delhi** - "The Heart of India" - 10+ attractions with Mughal monuments and modern marvels
- **Kolkata** - "The City of Joy" - 9+ attractions showcasing Bengali culture and colonial architecture

### 🎯 Core Features

#### Frontend (React)
- **Responsive Design** - Mobile-first responsive UI that works across all devices
- **Dynamic Routing** - Seamless navigation between cities and attractions using React Router
- **Interactive Components** - Modern UI with hover effects, animations, and smooth transitions
- **Category Filtering** - Filter attractions by categories (Historical, Religious, Nature, Adventure, etc.)
- **Detailed Attraction Pages** - Complete information including images, timings, fees, and directions

#### Backend (Flask API)
- **RESTful API** - Clean API endpoints for all data operations
- **City-Specific Data** - Separate endpoints for each city's attractions and nearby destinations
- **Cross-Origin Support** - CORS enabled for seamless frontend-backend communication
- **Comprehensive Data** - Rich attraction data with images, descriptions, and practical information

### 📱 User Experience
- **Fast Loading** - Optimized performance with efficient data loading
- **SEO Friendly** - Semantic HTML structure with proper meta tags
- **Accessibility** - WCAG compliant design with proper contrast and keyboard navigation
- **Modern Typography** - Beautiful Inter and Playfair Display fonts
- **Visual Appeal** - High-quality images with gradient overlays and modern card designs

## 🏗️ Technical Architecture

### Frontend Stack
- **React 19.1.0** - Modern React with hooks and functional components
- **React Router DOM 7.6.3** - Client-side routing and navigation
- **CSS3** - Custom styling with CSS Grid, Flexbox, and animations
- **Google Fonts** - Inter and Playfair Display typography

### Backend Stack
- **Flask 2.3.3** - Lightweight Python web framework
- **Flask-CORS 4.0.0** - Cross-Origin Resource Sharing support
- **Python** - Backend logic and API endpoints

### Project Structure
```
pune-tourist-explorer/
├── frontend/
│   ├── public/              # Static assets and HTML template
│   ├── src/
│   │   ├── components/      # Reusable React components
│   │   ├── pages/          # Page components and routing
│   │   ├── constants/      # Configuration and city data
│   │   ├── data/           # Static attraction data
│   │   ├── services/       # API service functions
│   │   └── assets/         # Images and media files
├── backend/
│   ├── app.py             # Flask application and API routes
│   ├── requirements.txt    # Python dependencies
│   └── README.md          # Backend documentation
└── README.md              # This file
```

## 🛠️ Installation & Setup

### Prerequisites
- **Node.js** (v16 or higher)
- **Python** (v3.8 or higher)
- **npm** or **yarn**
- **pip** (Python package manager)

### Frontend Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/pune-tourist-explorer.git
   cd pune-tourist-explorer
   ```

2. **Install dependencies**
   ```bash
   npm install
   ```

3. **Start the development server**
   ```bash
   npm start
   ```
   
   The application will open at `http://localhost:3000`

### Backend Setup

1. **Navigate to backend directory**
   ```bash
   cd backend
   ```

2. **Create virtual environment (recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Start the Flask server**
   ```bash
   python app.py
   ```
   
   The API will be available at `http://localhost:5000`

## 📋 Available Scripts

### Frontend Scripts
- `npm start` - Start development server
- `npm build` - Build for production
- `npm test` - Run test suite
- `npm run eject` - Eject from Create React App

### Backend Scripts
- `python app.py` - Start Flask development server
- `python test_images.py` - Test image accessibility

## 🌐 API Documentation

### Base URL
```
http://localhost:5000/api
```

### Endpoints

#### City Attractions
- `GET /api/{city}/attractions` - Get all attractions for a specific city
- `GET /api/{city}/nearby-attractions` - Get nearby attractions for a city

#### Specific Endpoints
- `GET /api/pune-attractions` - Pune attractions
- `GET /api/mumbai-attractions` - Mumbai attractions  
- `GET /api/delhi-attractions` - Delhi attractions
- `GET /api/kolkata-attractions` - Kolkata attractions
- `GET /api/nearby-attractions` - Nearby attractions (Pune-specific)

#### Individual Attractions
- `GET /api/attraction/{id}` - Get specific attraction by ID
- `GET /api/attractions/category/{category}` - Get attractions by category

### Response Format
```json
{
  "success": true,
  "data": [...],
  "count": 8,
  "city": "Pune"
}
```

## 🗺️ Supported Cities & Attractions

### 🏛️ Pune (8 Attractions)
**Categories:** Historical, Religious, Nature, Adventure, Cultural
- Shaniwar Wada, Aga Khan Palace, Sinhagad Fort, Dagdusheth Halwai Ganapati Temple
- Osho Ashram, Saras Baug, Raja Dinkar Kelkar Museum, Shams-ud-Din Mohammad Shah's Tomb

### 🌊 Mumbai (8 Attractions)  
**Categories:** Historical, Nature, Religious, Cultural, Entertainment
- Gateway of India, Marine Drive, Chhatrapati Shivaji Terminus, Siddhivinayak Temple
- Bollywood Studios, Elephanta Caves, Juhu Beach, Crawford Market

### 🏰 Delhi (10 Attractions)
**Categories:** Historical, Spiritual, Cultural, Religious
- Red Fort, India Gate, Qutub Minar, Lotus Temple, Humayun's Tomb
- Chandni Chowk, Jama Masjid, Raj Ghat, Akshardham Temple, National Museum

### 🎭 Kolkata (9 Attractions)
**Categories:** Historical, Religious, Cultural, Modern
- Victoria Memorial, Howrah Bridge, Dakshineswar Kali Temple, Park Street
- Indian Museum, Kalighat Temple, Belur Math, New Market, Science City

## 🚗 Nearby Destinations

Each city includes curated nearby attractions within 100-600km radius:
- **Hill Stations** (Lonavala, Mahabaleshwar, Shimla, Darjeeling)
- **Heritage Sites** (Agra, Bishnupur, Murshidabad)  
- **Nature Destinations** (Sundarbans, Mulshi Dam, Tamhini Ghat)
- **Spiritual Centers** (Rishikesh, Mathura-Vrindavan, Bhimashankar)

## 🎨 Design Features

### Visual Design
- **Modern Card Layouts** - Clean, material design inspired cards
- **Gradient Backgrounds** - Beautiful gradient overlays for each city
- **High-Quality Images** - Curated, high-resolution attraction images
- **Responsive Grid System** - CSS Grid and Flexbox for all screen sizes

### User Experience
- **Smooth Animations** - CSS transitions and hover effects
- **Intuitive Navigation** - Clear breadcrumbs and navigation patterns
- **Search & Filter** - Category-based filtering and search functionality
- **Mobile Optimized** - Touch-friendly interface for mobile devices

## 🔧 Configuration

### City Configuration
Cities are configured in `src/constants/cities.js` with:
- Display names and subtitles
- Hero images and color schemes  
- Statistics and features
- Gradient styles and themes

### API Configuration
Backend API routes are configured in `backend/app.py` with CORS support for frontend integration.

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. **Fork the repository**
2. **Create a feature branch** (`git checkout -b feature/AmazingFeature`)
3. **Commit changes** (`git commit -m 'Add some AmazingFeature'`)
4. **Push to branch** (`git push origin feature/AmazingFeature`)  
5. **Open a Pull Request**

### Contribution Guidelines
- Follow React best practices and hooks patterns
- Maintain consistent code style and formatting
- Add appropriate comments and documentation
- Test your changes thoroughly
- Update documentation as needed

## 📝 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Tourism Boards** - For attraction information and images
- **Indian Tourism** - For promoting cultural heritage
- **Open Source Community** - For amazing tools and libraries
- **Contributors** - Thank you to all who have contributed to this project

## 📞 Support

If you encounter any issues or have questions:

1. **Check existing issues** on GitHub
2. **Create a new issue** with detailed description
3. **Contact maintainers** for support

---

**Made with ❤️ for India's Cultural Heritage**

*Discover the incredible diversity and rich heritage of India's most vibrant cities through City Explorers.*
