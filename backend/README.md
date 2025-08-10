# City Explorers API

## Setup Instructions

1. Install Python dependencies:
```bash
pip install -r requirements.txt
```

2. Run the Flask server:
```bash
python app.py
```

The API will be available at `http://127.0.0.1:5000`

## API Endpoints

- `GET /` - API status
- `GET /api/pune-attractions` - Get all Pune attractions
- `GET /api/nearby-attractions` - Get all nearby attractions  
- `GET /api/attraction/<id>` - Get specific attraction by ID
- `GET /api/attractions/category/<category>` - Get attractions by category

## Categories
- historical
- religious  
- adventure
- nature
- cultural
- spiritual
- hillstation
- modern

## Image URL Testing

To test if image URLs are working:
```bash
pip install requests
python test_images.py
```

## Recent Updates
- Fixed broken Unsplash image URLs that were returning 404 errors
- Replaced problematic URLs with more reliable iStock images
- Added image URL testing script for quality assurance 