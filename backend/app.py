from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for React frontend

# Pune Attractions Data
pune_attractions = [
    {
        "id": 1,
        "name": "Shaniwar Wada",
        "shortDescription": "Historic grandeur of the Maratha empire in the heart of Pune.",
        "fullDescription": "Shaniwar Wada is a historical fortification in the city of Pune built in 1732. It was the seat of the Peshwas of the Maratha Empire until 1818. The magnificent structure showcases the architectural brilliance of the Maratha period with its impressive gates, gardens, and chambers.",
        "image": "https://www.incredibleindia.gov.in/content/dam/incredible-india/images/trips/maharashtra/amravati/pune-a-fusion-of-history-and-today/shaniwar-wada-pune-maharashtra-tri-iter-day1.jpg",
        "tags": ["#History", "#Architecture", "#Heritage"],
        "timings": "8:00 AM - 6:30 PM",
        "entryFee": "₹30 for Indians, ₹300 for Foreigners",
        "bestTimeToVisit": "October to March",
        "howToReach": "Located in the old city area, easily accessible by auto-rickshaw, bus, or taxi from any part of Pune.",
        "nearbyActivities": "Dagdusheth Halwai Temple, Pune Central Market, Lal Mahal",
        "category": "historical"
    },
    {
        "id": 2,
        "name": "Aga Khan Palace",
        "shortDescription": "Serene memorial where Mahatma Gandhi was imprisoned during the freedom struggle.",
        "fullDescription": "Built in 1892 by Sultan Muhammed Shah Aga Khan III, this beautiful palace served as a prison for Mahatma Gandhi, his wife Kasturba Gandhi, and secretary Mahadev Desai during the Quit India Movement. Today, it houses a Gandhi National Memorial.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/c/cd/Pune_Palace.jpg",
        "tags": ["#History", "#Memorial", "#Heritage"],
        "timings": "9:00 AM - 5:30 PM",
        "entryFee": "₹5 for Indians, ₹100 for Foreigners",
        "bestTimeToVisit": "October to March",
        "howToReach": "Located in Yerwada area, about 8 km from Pune Railway Station. Well-connected by bus and auto-rickshaw.",
        "nearbyActivities": "Osho Ashram, Pune Airport, Shopping at Phoenix Marketcity",
        "category": "historical"
    },
    {
        "id": 3,
        "name": "Sinhagad Fort",
        "shortDescription": "Majestic hilltop fortress offering breathtaking panoramic views and adventure.",
        "fullDescription": "Sinhagad Fort, literally meaning 'Lion Fort', is a hilltop fortress located southwest of Pune. The fort has been the site of many important battles, most notably the Battle of Sinhagad in 1670. Today, it's a popular trekking destination offering spectacular views of the Sahyadri mountains.",
        "image": "https://explorewithsandeep.com/wp-content/uploads/2024/06/WhatsApp-Image-2024-06-21-at-13.39.50_5a2946de.jpg",
        "tags": ["#Adventure", "#History", "#Trekking", "#Nature"],
        "timings": "6:00 AM - 6:00 PM",
        "entryFee": "Free",
        "bestTimeToVisit": "October to February, Early morning or evening",
        "howToReach": "30 km from Pune city. Take a bus to Sinhagad base village, then trek or take a taxi up the winding road.",
        "nearbyActivities": "Adventure sports, Local food stalls, Photography, Trekking",
        "category": "adventure"
    },
    {
        "id": 4,
        "name": "Dagdusheth Halwai Ganapati Temple",
        "shortDescription": "Vibrant temple dedicated to Lord Ganesha, famous for its elaborate festivals.",
        "fullDescription": "One of the most revered Ganpati temples in Maharashtra, this temple was built in 1893 by Dagdusheth Halwai. The temple is especially famous during Ganesh Chaturthi when thousands of devotees visit to seek blessings from the beautifully decorated deity.",
        "image": "https://punetourism.co.in/images/places-to-visit/headers/shreemant-dagdusheth-halwai-ganpati-mandir-pune-tourism-entry-fee-timings-holidays-reviews-header.jpg",
        "tags": ["#Religious", "#Culture", "#Festival"],
        "timings": "4:00 AM - 11:30 PM",
        "entryFee": "Free",
        "bestTimeToVisit": "During Ganesh Chaturthi (August/September), Early morning for peaceful darshan",
        "howToReach": "Located in Budhwar Peth, easily accessible from all parts of Pune by bus, auto-rickshaw, or car.",
        "nearbyActivities": "Shaniwar Wada, Shopping in old Pune markets, Street food exploration",
        "category": "religious"
    },
    {
        "id": 5,
        "name": "Osho Ashram",
        "shortDescription": "Peaceful meditation center promoting spiritual wellness and mindfulness.",
        "fullDescription": "The Osho International Meditation Resort is a spiritual center founded by the followers of Osho (Bhagwan Shree Rajneesh). It offers various meditation techniques, healing therapies, and spiritual programs in a serene, garden-like environment.",
        "image": "https://im.whatshot.in/img/2019/Dec/osho-1577102430.jpg?w=740&h=397&q=80&wp=1",
        "tags": ["#Spiritual", "#Meditation", "#Wellness"],
        "timings": "6:00 AM - 10:00 PM (Programs vary)",
        "entryFee": "Day pass available, fees vary by program",
        "bestTimeToVisit": "Year-round, Early morning for meditation sessions",
        "howToReach": "Located in Koregaon Park, easily accessible by taxi, auto-rickshaw, or bus from city center.",
        "nearbyActivities": "German Bakery, Koregaon Park shopping, Cafes and restaurants",
        "category": "spiritual"
    },
    {
        "id": 6,
        "name": "Saras Baug",
        "shortDescription": "Beautiful garden with a charming Ganesh temple and peaceful boat rides.",
        "fullDescription": "Saras Baug is a beautiful garden and zoo spread over 25 acres in the heart of Pune. The park features a lake with boating facilities, a small zoo, and the famous Saras Baug Ganpati temple. It's a perfect place for families to spend quality time together.",
        "image": "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/0a/8c/2a/39/saras-baug.jpg?w=800&h=-1&s=1",
        "tags": ["#Nature", "#Family", "#Garden", "#Boating"],
        "timings": "6:00 AM - 10:00 PM",
        "entryFee": "₹5 entry, Additional charges for boating",
        "bestTimeToVisit": "Evening for pleasant weather, Weekdays for fewer crowds",
        "howToReach": "Located near Pune Railway Station, easily accessible by local transport.",
        "nearbyActivities": "Pune Railway Station, Local markets, Food courts",
        "category": "nature"
    },
    {
        "id": 7,
        "name": "Raja Dinkar Kelkar Museum",
        "shortDescription": "Fascinating collection of artifacts showcasing Indian art and culture.",
        "fullDescription": "This museum houses an impressive collection of over 21,000 artifacts collected by Dr. Dinkar G. Kelkar. The collection includes sculptures, paintings, textiles, musical instruments, and everyday objects that showcase India's rich cultural heritage.",
        "image": "https://d3sftlgbtusmnv.cloudfront.net/blog/wp-content/uploads/2025/01/raja-dinkar-kelkar-museum-840x425.jpg",
        "tags": ["#Museum", "#Art", "#Culture", "#Heritage"],
        "timings": "10:00 AM - 5:30 PM (Closed on Mondays)",
        "entryFee": "₹50 for Indians, ₹500 for Foreigners",
        "bestTimeToVisit": "Any time during opening hours, Allow 2-3 hours for complete visit",
        "howToReach": "Located in Shukrawar Peth, near Shaniwar Wada. Accessible by auto-rickshaw or taxi.",
        "nearbyActivities": "Shaniwar Wada, Dagdusheth Temple, Traditional markets",
        "category": "cultural"
    },
    {
        "id": 8,
        "name": "Shams-ud-Din Mohammad Shah's Tomb",
        "shortDescription": "Architectural marvel showcasing Indo-Islamic design and historical significance.",
        "fullDescription": "This 14th-century tomb is one of Pune's oldest monuments, representing the Indo-Islamic architectural style. It's the resting place of Shams-ud-Din Mohammad Shah, a local ruler, and stands as a testament to Pune's diverse cultural heritage.",
        "image": "https://staging-jubilee.flickr.com/1849/29490257917_a5152677b8_b.jpg",
        "tags": ["#Architecture", "#History", "#Heritage"],
        "timings": "Sunrise to Sunset",
        "entryFee": "Free",
        "bestTimeToVisit": "Early morning or late afternoon for photography",
        "howToReach": "Located in the old city area, accessible by local transport.",
        "nearbyActivities": "Exploring old Pune architecture, Local street food",
        "category": "historical"
    }
]

# Mumbai Attractions Data
mumbai_attractions = [
    {
        "id": 101,
        "name": "Gateway of India",
        "shortDescription": "Iconic arch monument overlooking the Arabian Sea, symbol of Mumbai.",
        "fullDescription": "The Gateway of India is an arch monument built during the 20th century in Mumbai. The monument was erected to commemorate the landing of King George V and Queen Mary at Apollo Bunder on their visit to India in 1911. Built in Indo-Saracenic style, it's one of Mumbai's most recognized landmarks.",
        "image": "https://images.unsplash.com/photo-1566552881560-0be862a7c445?w=800&auto=format&fit=crop&q=80",
        "tags": ["#Historical", "#Monument", "#Heritage"],
        "timings": "24/7 (Best visited during sunrise/sunset)",
        "entryFee": "Free",
        "bestTimeToVisit": "October to March, Early morning or evening",
        "howToReach": "Located in Colaba, easily accessible by taxi, bus, or local train to CST/Churchgate stations.",
        "nearbyActivities": "Boat rides to Elephanta Caves, Taj Hotel, Colaba Causeway shopping",
        "category": "historical"
    },
    {
        "id": 102,
        "name": "Marine Drive",
        "shortDescription": "Queen's Necklace - Mumbai's picturesque seafront promenade.",
        "fullDescription": "Marine Drive is a 3.6-kilometre-long boulevard in South Mumbai. It is a 'C'-shaped six-lane concrete road along the coast, which is a natural bay. The road links Nariman Point to Bandra via Worli. The street lights resemble a string of pearls when viewed at night from an elevated point anywhere along the drive, hence the name 'Queen's Necklace'.",
        "image": "https://images.unsplash.com/photo-1595658658481-d53d3f999875?w=800&auto=format&fit=crop&q=80",
        "tags": ["#Scenic", "#Drive", "#Sunset", "#Promenade"],
        "timings": "24/7",
        "entryFee": "Free",
        "bestTimeToVisit": "Evening for sunset views, Early morning for jogging",
        "howToReach": "Churchgate or Charni Road railway stations. Multiple bus routes and taxis available.",
        "nearbyActivities": "Chowpatty Beach, Hanging Gardens, Malabar Hill, street food",
        "category": "nature"
    },
    {
        "id": 103,
        "name": "Chhatrapati Shivaji Terminus",
        "shortDescription": "UNESCO World Heritage Victorian Gothic railway station architecture.",
        "fullDescription": "Chhatrapati Shivaji Maharaj Terminus is a UNESCO World Heritage Site and one of the busiest railway stations in India. This Victorian Gothic Revival architectural masterpiece serves as the headquarters of the Central Railways. The station was designed by British architect Frederick William Stevens.",
        "image": "https://images.unsplash.com/photo-1578662996442-48f60103fc96?w=800&auto=format&fit=crop&q=80",
        "tags": ["#Architecture", "#Heritage", "#Victorian", "#UNESCO"],
        "timings": "24/7 (Station), Photography best during daylight",
        "entryFee": "Free",
        "bestTimeToVisit": "Early morning or late afternoon for photography",
        "howToReach": "CST Railway Station is the location itself. Well connected by all local trains, buses, and taxis.",
        "nearbyActivities": "Crawford Market, Fort District, Horniman Circle Gardens",
        "category": "historical"
    },
    {
        "id": 104,
        "name": "Siddhivinayak Temple",
        "shortDescription": "Famous Ganesh temple known for fulfilling devotees' wishes.",
        "fullDescription": "Shree Siddhivinayak Ganapati Mandir is a Hindu temple dedicated to Lord Ganesha. Originally built by Laxman Vithu and Deubai Patil on 19 November 1801, the temple has since become one of the richest temples in Mumbai. The inner roof of the sanctum is plated with gold, and the central statue is of Ganesha.",
        "image": "https://images.unsplash.com/photo-1580477667995-2b94f01c9516?w=800&auto=format&fit=crop&q=80",
        "tags": ["#Religious", "#Temple", "#Ganesha", "#Spiritual"],
        "timings": "3:30 AM - 10:00 PM",
        "entryFee": "Free",
        "bestTimeToVisit": "Early morning for peaceful darshan, avoid Tuesdays (very crowded)",
        "howToReach": "Dadar railway station (both Central and Western lines). Auto-rickshaws and buses available.",
        "nearbyActivities": "Prabhadevi area, local street food, Worli Sea Face",
        "category": "religious"
    },
    {
        "id": 105,
        "name": "Bollywood Studios Tour",
        "shortDescription": "Behind-the-scenes look at the world's largest film industry.",
        "fullDescription": "Experience the magic of Bollywood with guided tours of famous film studios in Mumbai. Visit sets, meet actors, watch live shootings, and learn about the film-making process. Multiple studios offer tours including Film City in Goregaon, which spans over 520 acres and is one of the largest film studio complexes in the world.",
        "image": "https://images.unsplash.com/photo-1489599033596-b58c2eeca165?w=800&auto=format&fit=crop&q=80",
        "tags": ["#Entertainment", "#Bollywood", "#Studios", "#Films"],
        "timings": "9:00 AM - 5:00 PM (Tour timings vary)",
        "entryFee": "₹500 - ₹2000 (depending on studio and package)",
        "bestTimeToVisit": "Weekdays for active shooting schedules",
        "howToReach": "Film City via Goregaon station. Organized tours include transportation.",
        "nearbyActivities": "EsselWorld, Water Kingdom, Sanjay Gandhi National Park",
        "category": "cultural"
    },
    {
        "id": 106,
        "name": "Elephanta Caves",
        "shortDescription": "Ancient rock-cut temples on Elephanta Island with stunning sculptures.",
        "fullDescription": "The Elephanta Caves are a UNESCO World Heritage Site consisting of rock-cut cave temples predominantly dedicated to Lord Shiva. Located on Elephanta Island, these caves date from the 5th to 8th centuries. The main cave features large sculptures including the famous Trimurti (three-faced) Shiva.",
        "image": "https://images.unsplash.com/photo-1582722455003-0174e775f44e?w=800&auto=format&fit=crop&q=80",
        "tags": ["#Heritage", "#Caves", "#Ancient", "#UNESCO"],
        "timings": "9:00 AM - 5:30 PM (Closed Mondays)",
        "entryFee": "₹40 for Indians, ₹600 for Foreigners + Ferry charges",
        "bestTimeToVisit": "November to February, morning hours",
        "howToReach": "Ferry from Gateway of India (1-hour journey). Regular ferry services available.",
        "nearbyActivities": "Island exploration, ferry ride experience, local handicrafts",
        "category": "historical"
    },
    {
        "id": 107,
        "name": "Juhu Beach",
        "shortDescription": "Popular beach destination known for street food and celebrity spotting.",
        "fullDescription": "Juhu Beach is one of the most popular beaches in Mumbai, stretching for 6 kilometers. Known for its street food, sunset views, and as a celebrity residential area, it's a favorite weekend destination for locals and tourists. The beach is famous for bhel puri, pav bhaji, and other Mumbai street food delicacies.",
        "image": "https://images.unsplash.com/photo-1544989164-7dd748dc2b1c?w=800&auto=format&fit=crop&q=80",
        "tags": ["#Beach", "#Food", "#Sunset", "#Entertainment"],
        "timings": "24/7 (Best visited during evening)",
        "entryFee": "Free",
        "bestTimeToVisit": "Evening for sunset and street food, avoid monsoon season",
        "howToReach": "Vile Parle or Andheri railway stations, then bus/auto. Direct buses from various parts of Mumbai.",
        "nearbyActivities": "Street food tasting, horse/camel rides, ISKCON Temple nearby",
        "category": "nature"
    },
    {
        "id": 108,
        "name": "Crawford Market",
        "shortDescription": "Historic market building with Victorian architecture and diverse shopping.",
        "fullDescription": "Crawford Market, officially named Mahatma Jyotiba Phule Market, is one of South Mumbai's most famous markets. Built in 1869, this Victorian Gothic building houses vendors selling fresh produce, spices, textiles, and exotic pets. The market's facade features beautiful stone carvings and a clock tower.",
        "image": "https://images.unsplash.com/photo-1578662996442-48f60103fc96?w=800&auto=format&fit=crop&q=80",
        "tags": ["#Market", "#Shopping", "#Victorian", "#Heritage"],
        "timings": "11:00 AM - 8:00 PM (Closed Sundays)",
        "entryFee": "Free",
        "bestTimeToVisit": "Morning hours for fresh produce, weekdays less crowded",
        "howToReach": "CST railway station is walking distance. Multiple bus routes and taxi services.",
        "nearbyActivities": "Chor Bazaar, Mohammed Ali Road food street, Zaveri Bazaar",
        "category": "cultural"
    }
]

# Delhi Attractions Data
delhi_attractions = [
    {
        "id": 301,
        "name": "Red Fort",
        "shortDescription": "Majestic Mughal fort complex and UNESCO World Heritage Site.",
        "fullDescription": "The Red Fort or Lal Qila is a historic walled city in Delhi that served as the main residence of the Mughal emperors for nearly 200 years. Every year on India's Independence Day, the Prime Minister hoists the Indian flag at the main gate and delivers a nationally broadcast speech from its ramparts.",
        "image": "https://images.unsplash.com/photo-1587474260584-136574528ed5?w=800&auto=format&fit=crop&q=80",
        "tags": ["#Historical", "#Mughal", "#Heritage", "#UNESCO"],
        "timings": "Sunrise to Sunset (Closed on Mondays)",
        "entryFee": "₹35 for Indians, ₹500 for Foreigners",
        "bestTimeToVisit": "October to March, early morning or late afternoon",
        "howToReach": "Lal Qila Metro Station (Violet Line), Old Delhi Railway Station nearby.",
        "nearbyActivities": "Chandni Chowk, Jama Masjid, Raj Ghat, rickshaw rides",
        "category": "historical"
    },
    {
        "id": 302,
        "name": "India Gate",
        "shortDescription": "War memorial arch honoring Indian soldiers who died in World War I.",
        "fullDescription": "India Gate is a war memorial located on the Rajpath in New Delhi. It stands as a memorial to 82,000 soldiers of the undivided Indian Army who died in the period 1914–21 in the First World War. Designed by Sir Edwin Lutyens, it's one of the largest war memorials in India.",
        "image": "https://images.unsplash.com/photo-1590736969955-71cc94901144?w=800&auto=format&fit=crop&q=80",
        "tags": ["#Memorial", "#Architecture", "#Patriotic", "#Landmark"],
        "timings": "24/7 (Best visited during sunrise/sunset)",
        "entryFee": "Free",
        "bestTimeToVisit": "October to March, evening hours for street food",
        "howToReach": "Central Secretariat Metro Station, well connected by bus and metro.",
        "nearbyActivities": "Boat rides, street food, National Museum, Rashtrapati Bhavan",
        "category": "historical"
    },
    {
        "id": 303,
        "name": "Qutub Minar",
        "shortDescription": "World's tallest brick minaret and UNESCO World Heritage Site.",
        "fullDescription": "Qutub Minar is a minaret and victory tower that forms part of the Qutb complex, a UNESCO World Heritage Site. It is the tallest minaret in the world made of bricks. The tower tapers, and has a 14.3-metre (47-foot) base diameter, reducing to 2.7 metres (9 feet) at the top of the peak.",
        "image": "https://images.unsplash.com/photo-1598091383021-15ddea10925d?w=800&auto=format&fit=crop&q=80",
        "tags": ["#Heritage", "#Architecture", "#UNESCO", "#Ancient"],
        "timings": "Sunrise to Sunset",
        "entryFee": "₹35 for Indians, ₹500 for Foreigners",
        "bestTimeToVisit": "October to March, morning hours",
        "howToReach": "Qutb Minar Metro Station (Yellow Line), buses available.",
        "nearbyActivities": "Iron Pillar, Quwwat-ul-Islam Mosque, archaeological sites",
        "category": "historical"
    },
    {
        "id": 304,
        "name": "Lotus Temple",
        "shortDescription": "Bahai House of Worship known for its distinctive lotus-shaped architecture.",
        "fullDescription": "The Lotus Temple is a Baháʼí House of Worship that was dedicated in December 1986. Notable for its flowerlike shape, it has become a prominent attraction in the city. Like all Baháʼí Houses of Worship, the Lotus Temple is open to all, regardless of religion or any other qualification.",
        "image": "https://images.unsplash.com/photo-1578662996442-48f60103fc96?w=800&auto=format&fit=crop&q=80",
        "tags": ["#Architecture", "#Spiritual", "#Modern", "#Peaceful"],
        "timings": "9:00 AM - 6:00 PM (Closed on Mondays)",
        "entryFee": "Free",
        "bestTimeToVisit": "October to March, morning or evening hours",
        "howToReach": "Kalkaji Mandir Metro Station (Violet Line), auto-rickshaws available.",
        "nearbyActivities": "ISKCON Temple, meditation, peaceful walks",
        "category": "spiritual"
    },
    {
        "id": 305,
        "name": "Humayun's Tomb",
        "shortDescription": "Magnificent Mughal garden tomb, precursor to the Taj Mahal.",
        "fullDescription": "Humayun's tomb is the tomb of the Mughal Emperor Humayun in Delhi. The tomb was commissioned by Humayun's first wife and chief consort, Empress Bega Begum, in 1569-70. It was the first garden-tomb on the Indian subcontinent, and is located in Nizamuddin East, Delhi.",
        "image": "https://images.unsplash.com/photo-1593693411515-c20262150fa7?w=800&auto=format&fit=crop&q=80",
        "tags": ["#Mughal", "#Heritage", "#Garden", "#Architecture"],
        "timings": "Sunrise to Sunset",
        "entryFee": "₹35 for Indians, ₹500 for Foreigners",
        "bestTimeToVisit": "October to March, morning or late afternoon",
        "howToReach": "JLN Stadium Metro Station (Violet Line), buses and auto-rickshaws.",
        "nearbyActivities": "Nizamuddin Dargah, Isa Khan's tomb, garden walks",
        "category": "historical"
    },
    {
        "id": 306,
        "name": "Chandni Chowk",
        "shortDescription": "Bustling historic market street famous for food and traditional shopping.",
        "fullDescription": "Chandni Chowk is one of the oldest and busiest markets in Old Delhi. The street was designed by the Mughal princess Jahanara Begum, and was once divided by canals to reflect moonlight. Today it remains a symbol of the vibrant commercial activity of the historic city of Shahjahanabad.",
        "image": "https://images.unsplash.com/photo-1586500036706-41963de24d8b?w=800&auto=format&fit=crop&q=80",
        "tags": ["#Market", "#Food", "#Shopping", "#Culture"],
        "timings": "10:00 AM - 9:00 PM (varies by shop)",
        "entryFee": "Free",
        "bestTimeToVisit": "October to March, avoid peak summer hours",
        "howToReach": "Chandni Chowk Metro Station (Yellow Line), Old Delhi Railway Station.",
        "nearbyActivities": "Street food tours, spice market, traditional crafts shopping",
        "category": "cultural"
    },
    {
        "id": 307,
        "name": "Jama Masjid",
        "shortDescription": "India's largest mosque with stunning Mughal architecture.",
        "fullDescription": "Masjid-i Jehan-Numa, commonly known as the Jama Masjid of Delhi, is one of the largest mosques in India. It was built by Mughal emperor Shah Jahan between 1650 and 1656 at a cost of one million rupees, and was inaugurated by an imam from Bukhara, present-day Uzbekistan.",
        "image": "https://images.unsplash.com/photo-1633349154346-b2c85832e060?w=800&auto=format&fit=crop&q=80",
        "tags": ["#Religious", "#Mosque", "#Mughal", "#Architecture"],
        "timings": "6:00 AM - 12:00 PM, 1:30 PM - 6:30 PM",
        "entryFee": "Free (Camera charges apply)",
        "bestTimeToVisit": "Outside prayer times, October to March",
        "howToReach": "Lal Qila Metro Station (Violet Line), auto-rickshaws from Chandni Chowk.",
        "nearbyActivities": "Red Fort, Chandni Chowk, Old Delhi walking tours",
        "category": "religious"
    },
    {
        "id": 308,
        "name": "Raj Ghat",
        "shortDescription": "Memorial dedicated to Mahatma Gandhi at his cremation site.",
        "fullDescription": "Raj Ghat is a memorial dedicated to Mahatma Gandhi in Delhi. Originally it was the name of a historic ghat of Old Delhi on the banks of Yamuna river. It is a black marble platform that marks the spot of Mahatma Gandhi's cremation, Antyesti on 31 January 1948, a day after his assassination.",
        "image": "https://images.unsplash.com/photo-1582722455003-0174e775f44e?w=800&auto=format&fit=crop&q=80",
        "tags": ["#Memorial", "#Gandhi", "#Peaceful", "#History"],
        "timings": "Sunrise to Sunset",
        "entryFee": "Free",
        "bestTimeToVisit": "October to March, morning hours",
        "howToReach": "Raj Ghat Metro Station (Violet Line), bus services available.",
        "nearbyActivities": "National Gandhi Museum, Yamuna river bank, peaceful walks",
        "category": "historical"
    },
    {
        "id": 309,
        "name": "Akshardham Temple",
        "shortDescription": "Modern Hindu temple complex showcasing traditional architecture and culture.",
        "fullDescription": "Swaminarayan Akshardham is a Hindu temple and spiritual-cultural campus in Delhi. The complex displays millennia of traditional and modern Hindu culture, spirituality, and architecture. Inspired by Yogiji Maharaj and created by Pramukh Swami Maharaj, it was inaugurated on 6 November 2005.",
        "image": "https://images.unsplash.com/photo-1605640842043-e0df924d5da0?w=800&auto=format&fit=crop&q=80",
        "tags": ["#Temple", "#Modern", "#Culture", "#Spiritual"],
        "timings": "9:30 AM - 6:30 PM (Closed on Mondays)",
        "entryFee": "Free (Exhibitions and boat ride charges apply)",
        "bestTimeToVisit": "October to March, allow full day for complete visit",
        "howToReach": "Akshardham Metro Station (Blue Line), shuttle service available.",
        "nearbyActivities": "Musical fountain, boat ride, cultural exhibitions, gardens",
        "category": "spiritual"
    },
    {
        "id": 310,
        "name": "National Museum",
        "shortDescription": "Premier museum showcasing India's cultural heritage and artifacts.",
        "fullDescription": "The National Museum in New Delhi is one of the largest museums in India. Established in 1949, it holds variety of articles ranging from pre-historic era to modern works of art. It functions under the Ministry of Tourism and Culture, Government of India.",
        "image": "https://images.unsplash.com/photo-1566127992631-137a642a90f4?w=800&auto=format&fit=crop&q=80",
        "tags": ["#Museum", "#Culture", "#Heritage", "#Art"],
        "timings": "10:00 AM - 6:00 PM (Closed on Mondays)",
        "entryFee": "₹20 for Indians, ₹650 for Foreigners",
        "bestTimeToVisit": "October to March, allow 2-3 hours for visit",
        "howToReach": "Central Secretariat Metro Station, well connected by metro and bus.",
        "nearbyActivities": "India Gate, Rajpath, National Gallery of Modern Art",
        "category": "cultural"
    }
]

# Kolkata Attractions Data
kolkata_attractions = [
    {
        "id": 501,
        "name": "Victoria Memorial",
        "shortDescription": "Iconic white marble monument dedicated to Queen Victoria's memory.",
        "fullDescription": "The Victoria Memorial is a large marble building in Kolkata, dedicated to the memory of Queen Victoria, Empress of India. It is now a museum and tourist destination. The Memorial lies on the Maidan, the largest urban park in Kolkata. Construction started in 1906 and was completed in 1921.",
        "image": "https://images.unsplash.com/photo-1558431382-27523e4120ea?w=800&auto=format&fit=crop&q=80",
        "tags": ["#Monument", "#Colonial", "#Museum", "#Heritage"],
        "timings": "10:00 AM - 6:00 PM (Closed on Mondays)",
        "entryFee": "₹30 for Indians, ₹500 for Foreigners",
        "bestTimeToVisit": "October to March, morning or evening hours",
        "howToReach": "Park Street Metro Station, well connected by bus, metro, and taxi.",
        "nearbyActivities": "Maidan, St. Paul's Cathedral, Eden Gardens, boat rides",
        "category": "historical"
    },
    {
        "id": 502,
        "name": "Howrah Bridge",
        "shortDescription": "Iconic cantilever bridge over Hooghly River, symbol of Kolkata.",
        "fullDescription": "Howrah Bridge is a balanced cantilever bridge over the Hooghly River in West Bengal. Commissioned in 1943, the bridge was originally named the New Howrah Bridge, because it replaced a pontoon bridge at the same location linking the two cities of Howrah and Kolkata.",
        "image": "https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=800&auto=format&fit=crop&q=80",
        "tags": ["#Bridge", "#Engineering", "#Iconic", "#River"],
        "timings": "24/7 (Best viewed during sunrise/sunset)",
        "entryFee": "Free",
        "bestTimeToVisit": "October to March, evening hours for lighting",
        "howToReach": "Howrah Station or Esplanade Metro Station, multiple bus routes.",
        "nearbyActivities": "Flower market, river cruise, Howrah Station, walking tour",
        "category": "historical"
    },
    {
        "id": 503,
        "name": "Dakshineswar Kali Temple",
        "shortDescription": "Sacred temple complex where Sri Ramakrishna practiced spiritual disciplines.",
        "fullDescription": "Dakshineswar Kali Temple is a Hindu navaratna temple located in Dakshineswar, Kolkata. Situated on the eastern bank of the Hooghly River, the presiding deity of the temple is Bhavatarini, a form of Mahadevi or Parashakti Adya Kali, otherwise known as Adishakti Kalika.",
        "image": "https://images.unsplash.com/photo-1580477667995-2b94f01c9516?w=800&auto=format&fit=crop&q=80",
        "tags": ["#Temple", "#Spiritual", "#Kali", "#Heritage"],
        "timings": "4:00 AM - 12:30 PM, 3:00 PM - 9:00 PM",
        "entryFee": "Free",
        "bestTimeToVisit": "October to March, early morning or evening aarti",
        "howToReach": "Dakshineswar Railway Station, bus services and metro connectivity.",
        "nearbyActivities": "Belur Math, boat rides, temple complex exploration",
        "category": "religious"
    },
    {
        "id": 504,
        "name": "Park Street",
        "shortDescription": "Vibrant street known for restaurants, pubs, and Christmas celebrations.",
        "fullDescription": "Park Street, officially Mother Teresa Sarani, is one of the most happening places in Kolkata. Known for its restaurants, pubs, bars, and nightlife, it's particularly famous during Christmas when the entire street is illuminated. The street has a rich history and colonial architecture.",
        "image": "https://images.unsplash.com/photo-1586500036706-41963de24d8b?w=800&auto=format&fit=crop&q=80",
        "tags": ["#Nightlife", "#Food", "#Christmas", "#Colonial"],
        "timings": "24/7 (restaurants and pubs have specific timings)",
        "entryFee": "Free to walk, dining and entertainment costs vary",
        "bestTimeToVisit": "December for Christmas decorations, evening hours",
        "howToReach": "Park Street Metro Station, well connected by public transport.",
        "nearbyActivities": "Shopping, dining, South Park Street Cemetery, nightlife",
        "category": "cultural"
    },
    {
        "id": 505,
        "name": "Indian Museum",
        "shortDescription": "India's oldest and largest museum with rare collections of artifacts.",
        "fullDescription": "The Indian Museum in Kolkata is the largest and oldest museum in India and has rare collections of antiques, armour and ornaments, fossils, skeletons, mummies and Mughal paintings. It was founded by the Asiatic Society of Bengal in Kolkata in 1814.",
        "image": "https://images.unsplash.com/photo-1566127992631-137a642a90f4?w=800&auto=format&fit=crop&q=80",
        "tags": ["#Museum", "#Heritage", "#Antiques", "#Culture"],
        "timings": "10:00 AM - 6:00 PM (Closed on Mondays)",
        "entryFee": "₹20 for Indians, ₹500 for Foreigners",
        "bestTimeToVisit": "October to March, allow 2-3 hours for visit",
        "howToReach": "Maidan Metro Station, well connected by metro and bus.",
        "nearbyActivities": "Park Street, Victoria Memorial, New Market shopping",
        "category": "cultural"
    },
    {
        "id": 506,
        "name": "Kalighat Temple",
        "shortDescription": "Ancient Kali temple, one of the 51 Shakti Peethas in Hindu tradition.",
        "fullDescription": "Kalighat Kali Temple is a Hindu temple dedicated to the Hindu goddess Kali. It is one of the 51 Shakti Peethas. Kalighat Temple was built by Santosh Pal in 1809. The current temple was built in the 19th century. The temple is regarded as one of the most important Kali temples in West Bengal.",
        "image": "https://images.unsplash.com/photo-1605640842043-e0df924d5da0?w=800&auto=format&fit=crop&q=80",
        "tags": ["#Temple", "#Kali", "#Shakti", "#Ancient"],
        "timings": "5:00 AM - 2:00 PM, 5:00 PM - 10:30 PM",
        "entryFee": "Free",
        "bestTimeToVisit": "October to March, during Kali Puja festival",
        "howToReach": "Kalighat Metro Station, accessible by metro, bus, and taxi.",
        "nearbyActivities": "Nirmal Hriday, Mother Teresa's Missionaries of Charity",
        "category": "religious"
    },
    {
        "id": 507,
        "name": "Belur Math",
        "shortDescription": "Headquarters of Ramakrishna Math and Mission with beautiful architecture.",
        "fullDescription": "Belur Math is the headquarters of the Ramakrishna Math and Mission, founded by Swami Vivekananda. It is located on the west bank of Hooghly River, Belur, in Howrah district. The temple is notable for its architecture that fuses Hindu, Christian and Islamic motifs as a symbol of unity of all religions.",
        "image": "https://images.unsplash.com/photo-1582722455003-0174e775f44e?w=800&auto=format&fit=crop&q=80",
        "tags": ["#Spiritual", "#Architecture", "#Vivekananda", "#Unity"],
        "timings": "6:00 AM - 12:00 PM, 4:00 PM - 7:00 PM",
        "entryFee": "Free",
        "bestTimeToVisit": "October to March, during evening aarti",
        "howToReach": "Belur Railway Station, bus and taxi services available.",
        "nearbyActivities": "Dakshineswar Temple, Hooghly river bank, meditation",
        "category": "spiritual"
    },
    {
        "id": 508,
        "name": "New Market",
        "shortDescription": "Historic covered market famous for shopping and colonial architecture.",
        "fullDescription": "New Market, officially Sir Stuart Hogg Market, is a market in Kolkata. The market was named after Sir Stuart Hogg, the then chairman of the Calcutta Corporation. It was constructed in 1874 and is one of the most popular shopping places in Kolkata, especially among tourists.",
        "image": "https://images.unsplash.com/photo-1578662996442-48f60103fc96?w=800&auto=format&fit=crop&q=80",
        "tags": ["#Shopping", "#Market", "#Colonial", "#Heritage"],
        "timings": "10:00 AM - 8:00 PM (varies by shop)",
        "entryFee": "Free",
        "bestTimeToVisit": "October to March, afternoon hours",
        "howToReach": "Esplanade Metro Station, well connected by all modes of transport.",
        "nearbyActivities": "Street food, bargain shopping, nearby restaurants",
        "category": "cultural"
    },
    {
        "id": 509,
        "name": "Science City",
        "shortDescription": "Interactive science museum and entertainment complex for all ages.",
        "fullDescription": "Science City is a science museum and entertainment complex located in Kolkata. Inaugurated in 1997, it is the largest science centre in the Indian subcontinent. It offers interactive exhibits, planetarium shows, space theatre, and various educational programs for visitors of all ages.",
        "image": "https://images.unsplash.com/photo-1594736797933-d0ca1c9a1293?w=800&auto=format&fit=crop&q=80",
        "tags": ["#Science", "#Education", "#Interactive", "#Family"],
        "timings": "9:00 AM - 8:00 PM (Closed on Mondays)",
        "entryFee": "₹60 for adults, ₹40 for children (varies by section)",
        "bestTimeToVisit": "October to March, allow full day for complete visit",
        "howToReach": "Science City Bus Terminus, special bus services from various points.",
        "nearbyActivities": "Space theatre, planetarium, interactive galleries, food court",
        "category": "modern"
    }
]

# Nearby Attractions Data
nearby_attractions = [
    {
        "id": 9,
        "name": "Lonavala",
        "shortDescription": "Scenic hill station with lush valleys, waterfalls, and pleasant weather.",
        "fullDescription": "Lonavala is a popular hill station located in the Western Ghats, known for its misty valleys, cascading waterfalls, and pleasant climate. Famous for its chikki (a local sweet), beautiful caves, and scenic viewpoints, it's a perfect weekend getaway from Pune.",
        "image": "https://www.grinstays.com/wp-content/uploads/2020/12/5-Must-Visit-Places-In-Lonavala.jpg",
        "tags": ["#HillStation", "#Nature", "#Waterfalls", "#Weekend"],
        "timings": "Best visited during daylight hours",
        "entryFee": "No entry fee for the town, specific attractions may charge",
        "bestTimeToVisit": "June to September (monsoon) for waterfalls, October to March for pleasant weather",
        "howToReach": "64 km from Pune via Mumbai-Pune Highway. Regular bus services and train connectivity available.",
        "nearbyActivities": "Karla Caves, Bhaja Caves, Tiger's Leap, Rajmachi Fort, Chikki shopping",
        "category": "hillstation",
        "distance": "64 km"
    },
    {
        "id": 10,
        "name": "Khandala",
        "shortDescription": "Charming hill station offering stunning valley views and adventure activities.",
        "fullDescription": "Khandala, twin hill station to Lonavala, offers breathtaking views of the Duke's Nose cliff and valleys below. Known for its scenic beauty, pleasant climate, and adventure activities, it's a favorite destination for nature lovers and adventure enthusiasts.",
        "image": "https://dynamic.tourtravelworld.com/blog_images/10-most-beautiful-places-to-visit-in-khandala-on-your-next-trip-20170609023704.jpg",
        "tags": ["#HillStation", "#Adventure", "#Scenic", "#Nature"],
        "timings": "24/7 (specific viewpoints accessible during daylight)",
        "entryFee": "Free",
        "bestTimeToVisit": "June to September for lush greenery, October to March for clear views",
        "howToReach": "67 km from Pune. Accessible by road via Mumbai-Pune Highway or by train to Khandala station.",
        "nearbyActivities": "Duke's Nose trekking, Shooting Point, Sunset Point, Adventure sports",
        "category": "hillstation",
        "distance": "67 km"
    },
    {
        "id": 11,
        "name": "Mulshi Dam",
        "shortDescription": "Serene reservoir surrounded by hills, perfect for picnics and water sports.",
        "fullDescription": "Mulshi Dam is a beautiful gravity dam on the Mula River, creating a massive lake surrounded by hills and greenery. It's a popular destination for weekend picnics, water sports, and photography, offering tranquil surroundings away from city life.",
        "image": "https://i.ytimg.com/vi/B1HyKkeOyB8/maxresdefault.jpg",
        "tags": ["#Dam", "#Nature", "#Picnic", "#WaterSports"],
        "timings": "Sunrise to Sunset",
        "entryFee": "Free",
        "bestTimeToVisit": "Post-monsoon (October to February) when the dam is full",
        "howToReach": "45 km from Pune via Paud-Mulshi Road. Private vehicle recommended for easy access.",
        "nearbyActivities": "Boating, Photography, Tamhini Ghat, nearby resorts and cafes",
        "category": "nature",
        "distance": "45 km"
    },
    {
        "id": 12,
        "name": "Rajgad Fort",
        "shortDescription": "Historic mountain fortress offering challenging treks and royal Maratha heritage.",
        "fullDescription": "Rajgad Fort was the capital of the Maratha Empire under Chhatrapati Shivaji Maharaj for 26 years. Located in the Sahyadri mountains, this fort offers challenging treks and spectacular views. It holds immense historical significance as the royal residence of the great Maratha king.",
        "image": "https://positivedaynewspaper.com/wp-content/uploads/2025/03/1697546443_rajgad_fort.jpg.webp",
        "tags": ["#Fort", "#Trekking", "#History", "#Adventure"],
        "timings": "Sunrise to Sunset",
        "entryFee": "Free",
        "bestTimeToVisit": "October to March for pleasant trekking conditions",
        "howToReach": "60 km from Pune. Drive to Gunjavane village, then trek for 2-3 hours to reach the fort.",
        "nearbyActivities": "Trekking, Historical exploration, Photography, Nearby forts like Torna",
        "category": "historical",
        "distance": "60 km"
    },
    {
        "id": 13,
        "name": "Bhimashankar",
        "shortDescription": "Sacred Jyotirlinga temple nestled in biodiversity-rich Western Ghats.",
        "fullDescription": "Bhimashankar is one of the twelve Jyotirlingas dedicated to Lord Shiva, located in the Bhimashankar Wildlife Sanctuary. The temple is surrounded by dense forests rich in flora and fauna, making it both a spiritual and nature destination.",
        "image": "https://diplomatvisa.com/wp-content/uploads/2024/10/places-to-visit-in-Bhimashankar.webp",
        "tags": ["#Religious", "#Jyotirlinga", "#Wildlife", "#Nature"],
        "timings": "5:00 AM - 9:00 PM",
        "entryFee": "Free for temple, Wildlife sanctuary charges may apply",
        "bestTimeToVisit": "October to March, Avoid monsoon for trekking",
        "howToReach": "125 km from Pune via Rajgurunagar. State transport buses available, private vehicle recommended.",
        "nearbyActivities": "Wildlife sanctuary, Nature trails, Hanuman Lake, Local tribal culture",
        "category": "religious",
        "distance": "125 km"
    },
    {
        "id": 14,
        "name": "Mahabaleshwar",
        "shortDescription": "Popular hill station famous for strawberries, viewpoints, and cool climate.",
        "fullDescription": "Mahabaleshwar is Maharashtra's most popular hill station, known for its strawberry farms, numerous viewpoints, and pleasant climate year-round. The town offers a perfect blend of natural beauty, colonial charm, and modern amenities.",
        "image": "https://taxibazaar.in/assets/images/blog/mahabaleshwar.jpg",
        "tags": ["#HillStation", "#Strawberries", "#Viewpoints", "#Colonial"],
        "timings": "24/7 (specific attractions have their own timings)",
        "entryFee": "No entry fee for the town",
        "bestTimeToVisit": "October to June, Peak season is April-June and December-January",
        "howToReach": "120 km from Pune via Pune-Satara Highway. Regular bus services and taxi options available.",
        "nearbyActivities": "Strawberry farms, Elephant's Head Point, Mapro Garden, Venna Lake boating",
        "category": "hillstation",
        "distance": "120 km"
    },
    {
        "id": 15,
        "name": "Tamhini Ghat",
        "shortDescription": "Spectacular mountain pass with cascading waterfalls and misty landscapes.",
        "fullDescription": "Tamhini Ghat is a mountain pass connecting Pune and Raigad districts, renowned for its breathtaking beauty during monsoons. The ghat features numerous waterfalls, lush green landscapes, and misty weather that creates a magical atmosphere.",
        "image": "https://www.mypunepulse.com/wp-content/uploads/2024/07/WhatsApp-Image-2024-07-22-at-1.07.05-PM.jpeg",
        "tags": ["#MountainPass", "#Waterfalls", "#Monsoon", "#Scenic"],
        "timings": "Daylight hours recommended for safety",
        "entryFee": "Free",
        "bestTimeToVisit": "June to September (monsoon) for maximum beauty",
        "howToReach": "35 km from Pune. Drive carefully on the winding ghat roads, especially during monsoon.",
        "nearbyActivities": "Mulshi Dam, Photography, Nature walks, Waterfall hopping",
        "category": "nature",
        "distance": "35 km"
    },
    {
        "id": 16,
        "name": "Lavasa",
        "shortDescription": "Planned hill city with Italian architecture and modern amenities.",
        "fullDescription": "Lavasa is India's first planned hill city, designed with Italian-inspired architecture around a beautiful lake. The city offers modern amenities, adventure sports, and a unique blend of natural beauty with contemporary urban planning.",
        "image": "https://i.ytimg.com/vi/lQYNmvfYHOw/sddefault.jpg",
        "tags": ["#PlannedCity", "#Lake", "#Adventure", "#Modern"],
        "timings": "24/7 (attractions have specific timings)",
        "entryFee": "Entry to city is free, activities are charged separately",
        "bestTimeToVisit": "October to March for pleasant weather",
        "howToReach": "65 km from Pune via Pune-Bangalore Highway. Well-connected by road.",
        "nearbyActivities": "Watersports, Nature trails, Adventure activities, Spa and wellness centers",
        "category": "modern",
        "distance": "65 km"
    }
]

@app.route('/')
def home():
    return jsonify({"message": "City Explorers API", "status": "running"})

@app.route('/api/pune-attractions', methods=['GET'])
def get_pune_attractions():
    """Get all Pune attractions"""
    return jsonify({
        "success": True,
        "data": pune_attractions,
        "count": len(pune_attractions)
    })

@app.route('/api/mumbai-attractions', methods=['GET'])
def get_mumbai_attractions():
    """Get all Mumbai attractions"""
    return jsonify({
        "success": True,
        "data": mumbai_attractions,
        "count": len(mumbai_attractions)
    })

@app.route('/api/delhi-attractions', methods=['GET'])
def get_delhi_attractions():
    """Get all Delhi attractions"""
    return jsonify({
        "success": True,
        "data": delhi_attractions,
        "count": len(delhi_attractions)
    })

@app.route('/api/kolkata-attractions', methods=['GET'])
def get_kolkata_attractions():
    """Get all Kolkata attractions"""
    return jsonify({
        "success": True,
        "data": kolkata_attractions,
        "count": len(kolkata_attractions)
    })

@app.route('/api/nearby-attractions', methods=['GET'])
def get_nearby_attractions():
    """Get all nearby attractions (Pune specific for backward compatibility)"""
    return jsonify({
        "success": True,
        "data": nearby_attractions,
        "count": len(nearby_attractions)
    })

@app.route('/api/<city>/attractions', methods=['GET'])
def get_city_attractions(city):
    """Get attractions for a specific city"""
    city_data = {
        'pune': pune_attractions,
        'mumbai': mumbai_attractions,
        'delhi': delhi_attractions,
        'kolkata': kolkata_attractions
    }
    
    if city.lower() in city_data:
        attractions = city_data[city.lower()]
        return jsonify({
            "success": True,
            "data": attractions,
            "count": len(attractions),
            "city": city.title()
        })
    else:
        return jsonify({
            "success": False,
            "message": f"City '{city}' not found"
        }), 404

# Delhi Nearby Attractions Data
delhi_nearby_attractions = [
    {
        "id": 401,
        "name": "Agra (Taj Mahal)",
        "shortDescription": "World's most famous monument of love and UNESCO World Heritage Site.",
        "fullDescription": "The Taj Mahal is an ivory-white marble mausoleum on the south bank of the Yamuna river in Agra. It was commissioned in 1632 by the Mughal emperor Shah Jahan to house the tomb of his favourite wife, Mumtaz Mahal. The tomb is the centrepiece of a 17-hectare complex, which includes a mosque and a guest house.",
        "image": "https://images.unsplash.com/photo-1564507592333-c60657eea523?w=800&auto=format&fit=crop&q=80",
        "tags": ["#UNESCO", "#Monument", "#Love", "#Architecture"],
        "timings": "Sunrise to Sunset (Closed on Fridays)",
        "entryFee": "₹50 for Indians, ₹1100 for Foreigners",
        "bestTimeToVisit": "October to March, sunrise and sunset for best views",
        "howToReach": "204 km from Delhi via Yamuna Expressway. Train and bus services available.",
        "nearbyActivities": "Agra Fort, Fatehpur Sikri, Mehtab Bagh, local handicrafts",
        "category": "historical",
        "distance": "204 km"
    },
    {
        "id": 402,
        "name": "Rishikesh",
        "shortDescription": "Yoga capital of the world with spiritual retreats and adventure sports.",
        "fullDescription": "Rishikesh is a city in India's northern state of Uttarakhand, in the Himalayan foothills beside the Ganges River. The river is considered holy, and the city is renowned as a center for studying yoga and meditation. Temples and ashrams line the eastern bank around Swarg Ashram.",
        "image": "https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=800&auto=format&fit=crop&q=80",
        "tags": ["#Spiritual", "#Yoga", "#Ganges", "#Adventure"],
        "timings": "24/7 (specific attractions have their own timings)",
        "entryFee": "Free for city, specific activities are charged",
        "bestTimeToVisit": "September to November, February to May",
        "howToReach": "240 km from Delhi. Regular bus services and train to Haridwar then bus.",
        "nearbyActivities": "River rafting, yoga classes, temple visits, trekking",
        "category": "spiritual",
        "distance": "240 km"
    },
    {
        "id": 403,
        "name": "Mathura-Vrindavan",
        "shortDescription": "Sacred birthplace of Lord Krishna with numerous temples and spiritual sites.",
        "fullDescription": "Mathura is a city in northern India's Uttar Pradesh state. It's the birthplace of Lord Krishna. Vrindavan is a town in the Mathura district. It's considered sacred by followers of Lord Krishna. The area is dotted with hundreds of temples dedicated to Krishna and Radha.",
        "image": "https://images.unsplash.com/photo-1605640842043-e0df924d5da0?w=800&auto=format&fit=crop&q=80",
        "tags": ["#Religious", "#Krishna", "#Temples", "#Spiritual"],
        "timings": "Most temples open sunrise to sunset",
        "entryFee": "Free for most temples",
        "bestTimeToVisit": "October to March, Holi festival in March",
        "howToReach": "150 km from Delhi. Train services and regular bus connectivity.",
        "nearbyActivities": "Temple hopping, Krishna Janmabhoomi, Govind Dev Temple visits",
        "category": "religious",
        "distance": "150 km"
    },
    {
        "id": 404,
        "name": "Shimla",
        "shortDescription": "Colonial hill station with toy train rides and scenic mountain views.",
        "fullDescription": "Shimla is the capital of the northern Indian state of Himachal Pradesh, in the Himalayan foothills. Once the summer capital of British India, it remains the terminus of the narrow-gauge Kalka-Shimla Railway, completed in 1903. It's also known for the handicraft shops that line The Mall, a pedestrian avenue.",
        "image": "https://images.unsplash.com/photo-1626621341517-bbf3d9990a23?w=800&auto=format&fit=crop&q=80",
        "tags": ["#HillStation", "#Colonial", "#ToyTrain", "#Scenic"],
        "timings": "24/7 (attractions have specific timings)",
        "entryFee": "Free for city, toy train and activities charged separately",
        "bestTimeToVisit": "March to June, December to February for snow",
        "howToReach": "342 km from Delhi. Train to Kalka then toy train, or direct bus.",
        "nearbyActivities": "Mall Road, toy train ride, Christ Church, adventure sports",
        "category": "hillstation",
        "distance": "342 km"
    },
    {
        "id": 405,
        "name": "Jaipur",
        "shortDescription": "Pink City with magnificent palaces, forts, and vibrant Rajasthani culture.",
        "fullDescription": "Jaipur is the capital and largest city of the Indian state of Rajasthan. Jaipur is also known as the Pink City, due to the dominant color scheme of its buildings. It is located 268 km from the national capital New Delhi. The city is home to numerous palaces and forts.",
        "image": "https://images.unsplash.com/photo-1599661046289-e31897846cc2?w=800&auto=format&fit=crop&q=80",
        "tags": ["#Royal", "#Palaces", "#Culture", "#Heritage"],
        "timings": "Varies by attraction",
        "entryFee": "Varies by palace/fort",
        "bestTimeToVisit": "October to March",
        "howToReach": "268 km from Delhi. Express trains and luxury buses available.",
        "nearbyActivities": "Amber Fort, City Palace, Hawa Mahal, local markets",
        "category": "historical",
        "distance": "268 km"
    },
    {
        "id": 406,
        "name": "Haridwar",
        "shortDescription": "Sacred city where Ganges enters the plains, famous for evening Ganga Aarti.",
        "fullDescription": "Haridwar is an ancient city and important Hindu pilgrimage site in North India's Uttarakhand state, where the River Ganges exits the Himalayan foothills. The largest of several sacred ghats, Har Ki Pauri hosts a nightly Ganga Aarti ceremony, in which tiny flickering lamps are floated on the river.",
        "image": "https://images.unsplash.com/photo-1586500036706-41963de24d8b?w=800&auto=format&fit=crop&q=80",
        "tags": ["#Religious", "#Ganges", "#Pilgrimage", "#Aarti"],
        "timings": "24/7 (Ganga Aarti at sunset)",
        "entryFee": "Free",
        "bestTimeToVisit": "September to April, Kumbh Mela years",
        "howToReach": "214 km from Delhi. Train and bus services available.",
        "nearbyActivities": "Ganga Aarti, temple visits, cable car to Mansa Devi Temple",
        "category": "religious",
        "distance": "214 km"
    },
    {
        "id": 407,
        "name": "Manali",
        "shortDescription": "Popular hill station with snow-capped mountains and adventure activities.",
        "fullDescription": "Manali is a high-altitude Himalayan resort town in India's northern Himachal Pradesh state. It has a reputation as a backpacking center and honeymoon destination. Set on the Beas River, it's a gateway for skiing in the Solang Valley and trekking in Parvati Valley.",
        "image": "https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b?w=800&auto=format&fit=crop&q=80",
        "tags": ["#HillStation", "#Adventure", "#Snow", "#Trekking"],
        "timings": "24/7 (specific activities have timings)",
        "entryFee": "Free for city, activities charged separately",
        "bestTimeToVisit": "March to June, December to February for snow",
        "howToReach": "570 km from Delhi. Bus services available, drive via Chandigarh.",
        "nearbyActivities": "Solang Valley, Rohtang Pass, paragliding, skiing",
        "category": "hillstation",
        "distance": "570 km"
    },
    {
        "id": 408,
        "name": "Neemrana Fort Palace",
        "shortDescription": "Historic 15th-century fort converted into heritage hotel with zip-lining.",
        "fullDescription": "Neemrana Fort Palace is a 15th-century hill fort-palace in Neemrana, Alwar district, Rajasthan. Built in 1464 AD, it was the third capital of the descendants of Prithviraj Chauhan III. The fort has been converted into a heritage hotel and offers various adventure activities including zip-lining.",
        "image": "https://images.unsplash.com/photo-1571816119607-57e48af1caa6?w=800&auto=format&fit=crop&q=80",
        "tags": ["#Heritage", "#Fort", "#Adventure", "#Luxury"],
        "timings": "Day visits: 11:00 AM - 6:00 PM",
        "entryFee": "₹200 for day visit, activities charged separately",
        "bestTimeToVisit": "October to March",
        "howToReach": "122 km from Delhi via Delhi-Jaipur Highway. Well connected by road.",
        "nearbyActivities": "Zip-lining, fort exploration, heritage walks, spa treatments",
        "category": "historical",
        "distance": "122 km"
    }
]

# Mumbai Nearby Attractions Data
mumbai_nearby_attractions = [
    {
        "id": 201,
        "name": "Lonavala",
        "shortDescription": "Scenic hill station with lush valleys, caves, and pleasant weather.",
        "fullDescription": "Lonavala is a hill station surrounded by green valleys in western India near Mumbai and Pune. The hill station is the center of the Indian version of hard candy, chikki. It's known for its production of the hard candy, plus its caves and waterfalls.",
        "image": "https://images.unsplash.com/photo-1570197788417-0e82375c9371?w=800&auto=format&fit=crop&q=80",
        "tags": ["#HillStation", "#Nature", "#Waterfalls", "#Weekend"],
        "timings": "Best visited during daylight hours",
        "entryFee": "No entry fee for the town, specific attractions may charge",
        "bestTimeToVisit": "June to September (monsoon) for waterfalls, October to March for pleasant weather",
        "howToReach": "83 km from Mumbai via Mumbai-Pune Highway. Regular bus services and train connectivity available.",
        "nearbyActivities": "Karla Caves, Bhaja Caves, Tiger's Leap, Rajmachi Fort, Chikki shopping",
        "category": "hillstation",
        "distance": "83 km"
    },
    {
        "id": 202,
        "name": "Alibaug",
        "shortDescription": "Coastal town with beautiful beaches and historic Kolaba Fort.",
        "fullDescription": "Alibaug is a coastal town known for its clean beaches and the historic Kolaba Fort. It's a popular weekend getaway from Mumbai, offering a perfect blend of history, nature, and relaxation. The town is famous for its fresh seafood and beautiful sunset views.",
        "image": "https://images.unsplash.com/photo-1544551763-46a013bb70d5?w=800&auto=format&fit=crop&q=80",
        "tags": ["#Beach", "#Coast", "#Fort", "#Seafood"],
        "timings": "24/7 (specific attractions have their own timings)",
        "entryFee": "Free for beaches, fort entry may have charges",
        "bestTimeToVisit": "October to March for pleasant weather",
        "howToReach": "108 km from Mumbai. Ferry from Gateway of India or drive via Pen-Alibaug road.",
        "nearbyActivities": "Beach activities, water sports, Kolaba Fort, local seafood restaurants",
        "category": "nature",
        "distance": "108 km"
    },
    {
        "id": 203,
        "name": "Matheran",
        "shortDescription": "Asia's only automobile-free hill station with panoramic valley views.",
        "fullDescription": "Matheran is a hill station and a municipal council in the Raigad district in Maharashtra state. It is a popular hill station and honeymoon destination. Matheran means 'forest on the forehead' in the local language. It's the smallest hill station in India and is distinguished by its unique feature of being an automobile-free zone.",
        "image": "https://images.unsplash.com/photo-1571816119607-57e48af1caa6?w=800&auto=format&fit=crop&q=80",
        "tags": ["#HillStation", "#EcoFriendly", "#Nature", "#Trekking"],
        "timings": "Entry from 6:30 AM to 6:30 PM",
        "entryFee": "₹50 per person (environmental charge)",
        "bestTimeToVisit": "October to May, avoid monsoon season",
        "howToReach": "90 km from Mumbai to Neral, then toy train or horseback to Matheran.",
        "nearbyActivities": "Valley viewpoints, toy train ride, horseback riding, nature walks",
        "category": "hillstation",
        "distance": "90 km"
    },
    {
        "id": 204,
        "name": "Karnala Bird Sanctuary",
        "shortDescription": "Rich biodiversity sanctuary famous for bird watching and Karnala Fort.",
        "fullDescription": "Karnala Bird Sanctuary is located in Panvel taluka, near Panvel. The sanctuary is popular among birdwatchers and hikers. It houses over 150 species of birds and also has the historic Karnala Fort. The sanctuary is an excellent place for nature photography and bird watching.",
        "image": "https://images.unsplash.com/photo-1441974231531-c6227db76b6e?w=800&auto=format&fit=crop&q=80",
        "tags": ["#Wildlife", "#BirdWatching", "#Nature", "#Fort"],
        "timings": "6:00 AM - 6:00 PM",
        "entryFee": "₹25 for Indians, ₹300 for Foreigners",
        "bestTimeToVisit": "November to February for bird watching",
        "howToReach": "65 km from Mumbai via Panvel-Pune Highway. Regular bus services available.",
        "nearbyActivities": "Bird watching, fort trekking, nature photography, guided tours",
        "category": "nature",
        "distance": "65 km"
    },
    {
        "id": 205,
        "name": "Imagica Theme Park",
        "shortDescription": "India's premier theme park with thrilling rides and entertainment.",
        "fullDescription": "Adlabs Imagica is a theme park situated on the Mumbai-Pune Expressway near the village of Khopoli. The park covers 300 acres and is themed around Imagica - the story of a place where the real becomes surreal. It offers various themed attractions, roller coasters, and entertainment shows.",
        "image": "https://images.unsplash.com/photo-1594736797933-d0ca1c9a1293?w=800&auto=format&fit=crop&q=80",
        "tags": ["#ThemePark", "#Adventure", "#Entertainment", "#Family"],
        "timings": "10:30 AM - 7:30 PM (timings may vary)",
        "entryFee": "₹1499 - ₹2199 (depending on package and season)",
        "bestTimeToVisit": "October to March for pleasant weather",
        "howToReach": "76 km from Mumbai via Mumbai-Pune Expressway. Organized transport available.",
        "nearbyActivities": "Rides, water park, snow park, themed restaurants",
        "category": "modern",
        "distance": "76 km"
    },
    {
        "id": 206,
        "name": "Rajmachi Fort",
        "shortDescription": "Historic twin fortresses offering spectacular trekking and monsoon views.",
        "fullDescription": "Rajmachi is known for the twin fortresses of Shrivardhan and Manaranjan that overlook the Mumbai-Pune route. The fort is a popular trekking destination, especially during the monsoon season when the entire region is covered with lush greenery and numerous waterfalls.",
        "image": "https://images.unsplash.com/photo-1464822759844-d150ad6d1c71?w=800&auto=format&fit=crop&q=80",
        "tags": ["#Fort", "#Trekking", "#History", "#Adventure"],
        "timings": "Sunrise to Sunset",
        "entryFee": "Free",
        "bestTimeToVisit": "June to September (monsoon) for scenic beauty, October to February for trekking",
        "howToReach": "82 km from Mumbai. Trek from Lonavala or Karjat railway stations.",
        "nearbyActivities": "Trekking, historical exploration, photography, camping",
        "category": "historical",
        "distance": "82 km"
    },
    {
        "id": 207,
        "name": "Kashid Beach",
        "shortDescription": "Pristine white sand beach perfect for water sports and relaxation.",
        "fullDescription": "Kashid Beach is a pristine beach located between Mumbai and Goa. Known for its white sand and blue waters, it's less crowded than other beaches near Mumbai. The beach offers various water sports activities and is perfect for a peaceful getaway from the city's hustle and bustle.",
        "image": "https://images.unsplash.com/photo-1544551763-46a013bb70d5?w=800&auto=format&fit=crop&q=80",
        "tags": ["#Beach", "#WhiteSand", "#WaterSports", "#Peaceful"],
        "timings": "24/7",
        "entryFee": "Free",
        "bestTimeToVisit": "October to March, avoid monsoon season",
        "howToReach": "130 km from Mumbai via Alibaug route. Ferry and road transport available.",
        "nearbyActivities": "Swimming, water sports, beach volleyball, local seafood",
        "category": "nature",
        "distance": "130 km"
    },
    {
        "id": 208,
        "name": "Lavasa",
        "shortDescription": "Planned hill city with Italian architecture and modern amenities.",
        "fullDescription": "Lavasa is India's first planned hill city, designed with Italian-inspired architecture around a beautiful lake. The city offers modern amenities, adventure sports, and a unique blend of natural beauty with contemporary urban planning. It's known for its colorful buildings and pristine environment.",
        "image": "https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b?w=800&auto=format&fit=crop&q=80",
        "tags": ["#PlannedCity", "#Lake", "#Adventure", "#Modern"],
        "timings": "24/7 (attractions have specific timings)",
        "entryFee": "Entry to city is free, activities are charged separately",
        "bestTimeToVisit": "October to March for pleasant weather",
        "howToReach": "185 km from Mumbai via Pune-Bangalore Highway. Well-connected by road.",
        "nearbyActivities": "Watersports, nature trails, adventure activities, spa and wellness centers",
        "category": "modern",
        "distance": "185 km"
    }
]

# Kolkata Nearby Attractions Data
kolkata_nearby_attractions = [
    {
        "id": 601,
        "name": "Darjeeling",
        "shortDescription": "Queen of Hills famous for tea gardens, toy train, and Himalayan views.",
        "fullDescription": "Darjeeling is a town in the Indian state of West Bengal. It lies in the Mahabharat Range or Lesser Himalaya at an elevation of 6,700 ft. It is noted for its tea industry, the spectacular views of the world's third-highest mountain Kangchenjunga, and the Darjeeling Himalayan Railway.",
        "image": "https://images.unsplash.com/photo-1626621341517-bbf3d9990a23?w=800&auto=format&fit=crop&q=80",
        "tags": ["#HillStation", "#Tea", "#ToyTrain", "#Himalaya"],
        "timings": "24/7 (attractions have specific timings)",
        "entryFee": "Free for town, specific attractions charged separately",
        "bestTimeToVisit": "March to May, September to November",
        "howToReach": "610 km from Kolkata. Train to New Jalpaiguri then toy train or bus.",
        "nearbyActivities": "Tea garden visits, toy train ride, Tiger Hill sunrise, monastery visits",
        "category": "hillstation",
        "distance": "610 km"
    },
    {
        "id": 602,
        "name": "Sundarbans",
        "shortDescription": "UNESCO World Heritage mangrove forests, home to Royal Bengal Tigers.",
        "fullDescription": "The Sundarbans is a mangrove area in the delta formed by the confluence of the Ganges, Brahmaputra and Meghna Rivers in the Bay of Bengal. It spans from the Hooghly River in India's state of West Bengal to the Baleswar River in Bangladesh. It is the world's largest mangrove forest.",
        "image": "https://images.unsplash.com/photo-1441974231531-c6227db76b6e?w=800&auto=format&fit=crop&q=80",
        "tags": ["#Wildlife", "#UNESCO", "#Tigers", "#Mangroves"],
        "timings": "Sunrise to Sunset (specific timings for boat safaris)",
        "entryFee": "₹290 for Indians, ₹1020 for Foreigners + boat charges",
        "bestTimeToVisit": "November to February",
        "howToReach": "110 km from Kolkata to Godkhali, then boat to forest areas.",
        "nearbyActivities": "Tiger spotting, bird watching, boat safaris, village visits",
        "category": "nature",
        "distance": "110 km"
    },
    {
        "id": 603,
        "name": "Shantiniketan",
        "shortDescription": "Cultural town founded by Rabindranath Tagore, center of art and education.",
        "fullDescription": "Shantiniketan is a neighbourhood of Bolpur town in the Birbhum district of West Bengal. It was established by Maharshi Devendranath Tagore, and later expanded by his son Rabindranath Tagore whose vision became what is now a university town, Visva-Bharati University.",
        "image": "https://images.unsplash.com/photo-1605640842043-e0df924d5da0?w=800&auto=format&fit=crop&q=80",
        "tags": ["#Culture", "#Education", "#Tagore", "#Art"],
        "timings": "University: 10:00 AM - 5:00 PM (Closed Sundays)",
        "entryFee": "Free for campus visits, museum charges apply",
        "bestTimeToVisit": "October to March, during Poush Mela (December)",
        "howToReach": "165 km from Kolkata. Train services to Bolpur station.",
        "nearbyActivities": "University campus tour, Tagore's house, local handicrafts, cultural programs",
        "category": "cultural",
        "distance": "165 km"
    },
    {
        "id": 604,
        "name": "Digha",
        "shortDescription": "Popular beach resort town on the Bay of Bengal coast.",
        "fullDescription": "Digha is a seaside resort town in the state of West Bengal, India. It lies in East Midnapur district and at the northern end of the Bay of Bengal. It is the most popular sea resort in West Bengal. The beach is broad and sandy, with gentle waves.",
        "image": "https://images.unsplash.com/photo-1544551763-46a013bb70d5?w=800&auto=format&fit=crop&q=80",
        "tags": ["#Beach", "#Resort", "#Coast", "#Family"],
        "timings": "24/7",
        "entryFee": "Free for beach access",
        "bestTimeToVisit": "October to March, avoid monsoon season",
        "howToReach": "187 km from Kolkata. Train services and bus connectivity available.",
        "nearbyActivities": "Beach activities, water sports, marine aquarium, casuarina groves",
        "category": "nature",
        "distance": "187 km"
    },
    {
        "id": 605,
        "name": "Kalimpong",
        "shortDescription": "Peaceful hill station with Buddhist monasteries and flower nurseries.",
        "fullDescription": "Kalimpong is a hill station in the Indian state of West Bengal. It is located at an average elevation of 1,250 metres. The town is the headquarters of the Kalimpong subdivision, a part of the district of Darjeeling. It is well known for its educational institutions, many of which were established during the British colonial period.",
        "image": "https://images.unsplash.com/photo-1571816119607-57e48af1caa6?w=800&auto=format&fit=crop&q=80",
        "tags": ["#HillStation", "#Buddhist", "#Peaceful", "#Flowers"],
        "timings": "24/7 (monasteries and nurseries have specific timings)",
        "entryFee": "Free for town, monastery visits may have donation",
        "bestTimeToVisit": "March to May, September to November",
        "howToReach": "650 km from Kolkata. Train to New Jalpaiguri then bus or taxi.",
        "nearbyActivities": "Monastery visits, flower nurseries, Deolo Hill, adventure activities",
        "category": "hillstation",
        "distance": "650 km"
    },
    {
        "id": 606,
        "name": "Bishnupur",
        "shortDescription": "Historic town famous for terracotta temples and Baluchari sarees.",
        "fullDescription": "Bishnupur is a city and a municipality of Bankura district in the state of West Bengal. It is famous for its terracotta temples built by the Malla rulers, as well as for its handicrafts and hand-woven silk. The famous Baluchari saris are made here.",
        "image": "https://images.unsplash.com/photo-1598091383021-15ddea10925d?w=800&auto=format&fit=crop&q=80",
        "tags": ["#Heritage", "#Temples", "#Handicrafts", "#Culture"],
        "timings": "Sunrise to Sunset",
        "entryFee": "Free for most temples",
        "bestTimeToVisit": "October to March",
        "howToReach": "132 km from Kolkata. Train services and bus connectivity available.",
        "nearbyActivities": "Temple hopping, handicraft shopping, traditional music performances",
        "category": "historical",
        "distance": "132 km"
    },
    {
        "id": 607,
        "name": "Murshidabad",
        "shortDescription": "Former capital of Bengal with rich Nawabi heritage and silk industry.",
        "fullDescription": "Murshidabad is a historical city in the Indian state of West Bengal. It is located on the eastern bank of the Bhagirathi River, a distributary of the Ganges. The city was the capital of undivided Bengal during the Mughal period and has a rich cultural heritage.",
        "image": "https://images.unsplash.com/photo-1587474260584-136574528ed5?w=800&auto=format&fit=crop&q=80",
        "tags": ["#Heritage", "#Nawabi", "#Silk", "#History"],
        "timings": "Sunrise to Sunset (palaces and monuments)",
        "entryFee": "Varies by monument (₹15-100)",
        "bestTimeToVisit": "October to March",
        "howToReach": "219 km from Kolkata. Train services to Berhampore then bus/taxi.",
        "nearbyActivities": "Palace visits, silk factories, Imambara, boat rides on Bhagirathi",
        "category": "historical",
        "distance": "219 km"
    },
    {
        "id": 608,
        "name": "Purulia",
        "shortDescription": "Tribal district known for Chhau dance, red soil landscapes, and handicrafts.",
        "fullDescription": "Purulia is a district in the state of West Bengal, India. The district is famous for its Chhau dance, a traditional tribal martial dance. The landscape is characterized by red soil, small hills, and dense forests. It's also known for its handicrafts and tribal culture.",
        "image": "https://images.unsplash.com/photo-1464822759844-d150ad6d1c71?w=800&auto=format&fit=crop&q=80",
        "tags": ["#Tribal", "#Dance", "#Culture", "#Landscape"],
        "timings": "24/7 (specific attractions have timings)",
        "entryFee": "Free for most areas",
        "bestTimeToVisit": "October to March, during Chhau festival",
        "howToReach": "292 km from Kolkata. Train services and bus connectivity available.",
        "nearbyActivities": "Chhau dance performances, tribal village visits, handicraft shopping",
        "category": "cultural",
        "distance": "292 km"
    }
]

@app.route('/api/<city>/nearby-attractions', methods=['GET'])
def get_city_nearby_attractions(city):
    """Get nearby attractions for a specific city"""
    nearby_data = {
        'pune': nearby_attractions,
        'mumbai': mumbai_nearby_attractions,
        'delhi': delhi_nearby_attractions,
        'kolkata': kolkata_nearby_attractions
    }
    
    if city.lower() in nearby_data:
        attractions = nearby_data[city.lower()]
        return jsonify({
            "success": True,
            "data": attractions,
            "count": len(attractions),
            "city": city.title()
        })
    else:
        return jsonify({
            "success": False,
            "message": f"City '{city}' not found"
        }), 404

@app.route('/api/attraction/<int:attraction_id>', methods=['GET'])
def get_attraction_by_id(attraction_id):
    """Get specific attraction by ID"""
    # Search in all city attractions and nearby attractions
    all_attractions = pune_attractions + mumbai_attractions + delhi_attractions + kolkata_attractions + nearby_attractions
    attraction = next((attr for attr in all_attractions if attr['id'] == attraction_id), None)
    
    if attraction:
        return jsonify({
            "success": True,
            "data": attraction
        })
    else:
        return jsonify({
            "success": False,
            "message": "Attraction not found"
        }), 404

@app.route('/api/attractions/category/<category>', methods=['GET'])
def get_attractions_by_category(category):
    """Get attractions by category"""
    all_attractions = pune_attractions + nearby_attractions
    filtered_attractions = [attr for attr in all_attractions if attr['category'].lower() == category.lower()]
    
    return jsonify({
        "success": True,
        "data": filtered_attractions,
        "count": len(filtered_attractions)
    })

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000) 