// Centralized city configuration data
export const CITIES_CONFIG = {
  pune: {
    id: 'pune',
    name: 'Pune',
    displayName: 'Pune',
    subtitle: 'The Oxford of the East',
    tagline: "Discover Pune's Heart & Soul",
    description: 'Immerse in the cultural capital of Maharashtra with rich heritage and vibrant culture.',
    fullDescription: 'Discover Pune\'s Heart & Soul - Explore Historic Wonders, Serene Landscapes, and Vibrant Culture in the Oxford of the East.',
    heroImage: "https://www.incredibleindia.gov.in/content/dam/incredible-india/images/trips/maharashtra/amravati/pune-a-fusion-of-history-and-today/shaniwar-wada-pune-maharashtra-tri-iter-day1.jpg",
    fallbackImage: "https://images.unsplash.com/photo-1590736969955-71cc94901144?w=1600&auto=format&fit=crop&q=80",
    gradient: 'linear-gradient(135deg, rgba(102, 126, 234, 0.7) 0%, rgba(118, 75, 162, 0.7) 100%)',
    color: "linear-gradient(135deg, #667eea 0%, #764ba2 100%)",
    stats: { 
      attractions: '8+', 
      categories: '5', 
      radius: '125km' 
    },
    features: ["Historic Forts", "Cultural Heritage", "Educational Hub", "IT Capital"]
  },
  mumbai: {
    id: 'mumbai',
    name: 'Mumbai',
    displayName: 'Mumbai',
    subtitle: 'The City of Dreams',
    tagline: "Discover Mumbai's Spirit",
    description: 'Discover the commercial capital with iconic landmarks and bustling street life.',
    fullDescription: 'Explore the Commercial Capital with Iconic Landmarks, Beaches, and Vibrant Street Life in the City of Dreams.',
    heroImage: "https://cdn.guidetour.in/wp-content/uploads/2017/11/Architectural-Brilliance-of-the-Gateway-of-India.jpg.webp",
    fallbackImage: "https://images.unsplash.com/photo-1570168007204-dfb528c6958f?w=1600&auto=format&fit=crop&q=80",
    gradient: 'linear-gradient(135deg, rgba(255, 107, 107, 0.7) 0%, rgba(254, 202, 87, 0.7) 100%)',
    color: "linear-gradient(135deg, #ff6b6b 0%, #feca57 100%)",
    stats: { 
      attractions: '8+', 
      categories: '5', 
      radius: '200km' 
    },
    features: ["Bollywood Hub", "Financial Capital", "Marine Drive", "Street Food"]
  },
  delhi: {
    id: 'delhi',
    name: 'Delhi',
    displayName: 'Delhi',
    subtitle: 'The Heart of India',
    tagline: "Discover Delhi's Heritage",
    description: 'Experience the capital\'s rich history, from Mughal monuments to modern marvels.',
    fullDescription: 'Experience the Capital\'s Rich History, from Mughal Monuments to Modern Marvels in the Heart of India.',
    heroImage: "https://images.unsplash.com/photo-1587474260584-136574528ed5?w=800&auto=format&fit=crop&q=80",
    fallbackImage: "https://images.unsplash.com/photo-1598091383021-15ddea10925d?w=1600&auto=format&fit=crop&q=80",
    gradient: 'linear-gradient(135deg, rgba(168, 237, 234, 0.7) 0%, rgba(254, 214, 227, 0.7) 100%)',
    color: "linear-gradient(135deg, #a8edea 0%, #fed6e3 100%)",
    stats: { 
      attractions: '10+', 
      categories: '5', 
      radius: '300km' 
    },
    features: ["Mughal Heritage", "Political Capital", "Red Fort", "India Gate"]
  },
  kolkata: {
    id: 'kolkata',
    name: 'Kolkata',
    displayName: 'Kolkata',
    subtitle: 'The City of Joy',
    tagline: "Discover Kolkata's Culture",
    description: 'Immerse in Bengali culture, colonial architecture, and intellectual heritage.',
    fullDescription: 'Immerse in Bengali Culture, Colonial Architecture, and Intellectual Heritage in the City of Joy.',
    heroImage: "https://s7ap1.scene7.com/is/image/incredibleindia/howrah-bridge-howrah-west-bengal-city-1-hero?qlt=82&ts=1742154305591",
    fallbackImage: "https://images.unsplash.com/photo-1558431382-27e303142b1d?w=1600&auto=format&fit=crop&q=80",
    gradient: 'linear-gradient(135deg, rgba(150, 251, 196, 0.7) 0%, rgba(249, 245, 134, 0.7) 100%)',
    color: "linear-gradient(135deg, #96fbc4 0%, #f9f586 100%)",
    stats: { 
      attractions: '9+', 
      categories: '4', 
      radius: '250km' 
    },
    features: ["Literary Heritage", "Cultural Capital", "Durga Puja", "Colonial Architecture"]
  }
};

// Array of all cities for dropdowns and listings
export const CITIES_LIST = [
  CITIES_CONFIG.pune,
  CITIES_CONFIG.mumbai,
  CITIES_CONFIG.delhi,
  CITIES_CONFIG.kolkata
];

// Valid city IDs for route validation
export const VALID_CITIES = ['pune', 'mumbai', 'delhi', 'kolkata'];

// Homepage cities data (with additional display properties)
export const HOMEPAGE_CITIES = [
  {
    ...CITIES_CONFIG.pune,
    description: "Explore historic forts, spiritual centers, and vibrant culture in Maharashtra's cultural capital.",
    image: CITIES_CONFIG.pune.heroImage,
    attractions: `${CITIES_CONFIG.pune.stats.attractions} Attractions`,
    categories: `${CITIES_CONFIG.pune.stats.categories} Categories`
  },
  {
    ...CITIES_CONFIG.mumbai,
    description: "Discover the commercial capital with iconic landmarks, beaches, and bustling street life.",
    image: CITIES_CONFIG.mumbai.heroImage,
    attractions: `${CITIES_CONFIG.mumbai.stats.attractions} Attractions`,
    categories: `${CITIES_CONFIG.mumbai.stats.categories} Categories`
  },
  {
    ...CITIES_CONFIG.delhi,
    description: "Experience the capital's rich history, from Mughal monuments to modern marvels.",
    image: CITIES_CONFIG.delhi.heroImage,
    attractions: `${CITIES_CONFIG.delhi.stats.attractions} Attractions`,
    categories: `${CITIES_CONFIG.delhi.stats.categories} Categories`
  },
  {
    ...CITIES_CONFIG.kolkata,
    description: "Immerse in Bengali culture, colonial architecture, and intellectual heritage.",
    image: CITIES_CONFIG.kolkata.heroImage,
    attractions: `${CITIES_CONFIG.kolkata.stats.attractions} Attractions`,
    categories: `${CITIES_CONFIG.kolkata.stats.categories} Categories`
  }
];

// Utility functions
export const getCityConfig = (cityId) => {
  return cityId ? CITIES_CONFIG[cityId.toLowerCase()] : null;
};

export const isValidCity = (cityId) => {
  return VALID_CITIES.includes(cityId?.toLowerCase());
};

export const getCityFromPath = (pathname) => {
  const pathSegments = pathname.split('/').filter(segment => segment);
  const cityFromPath = pathSegments[0];
  return isValidCity(cityFromPath) ? cityFromPath.toLowerCase() : null;
}; 