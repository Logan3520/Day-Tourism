const API_BASE_URL = 'http://127.0.0.1:5000/api';

class APIService {
  async makeRequest(url) {
    try {
      const response = await fetch(url);
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      const data = await response.json();
      return data;
    } catch (error) {
      console.error('API request failed:', error);
      throw error;
    }
  }

  async getPuneAttractions() {
    const response = await this.makeRequest(`${API_BASE_URL}/pune-attractions`);
    return response.data;
  }

  async getMumbaiAttractions() {
    const response = await this.makeRequest(`${API_BASE_URL}/mumbai-attractions`);
    return response.data;
  }

  async getDelhiAttractions() {
    const response = await this.makeRequest(`${API_BASE_URL}/delhi-attractions`);
    return response.data;
  }

  async getKolkataAttractions() {
    const response = await this.makeRequest(`${API_BASE_URL}/kolkata-attractions`);
    return response.data;
  }

  async getCityAttractions(city) {
    const response = await this.makeRequest(`${API_BASE_URL}/${city}/attractions`);
    return response.data;
  }

  async getCityNearbyAttractions(city) {
    const response = await this.makeRequest(`${API_BASE_URL}/${city}/nearby-attractions`);
    return response.data;
  }

  async getNearbyAttractions() {
    const response = await this.makeRequest(`${API_BASE_URL}/nearby-attractions`);
    return response.data;
  }

  async getAttractionById(id) {
    const response = await this.makeRequest(`${API_BASE_URL}/attraction/${id}`);
    return response.data;
  }

  async getAttractionsByCategory(category) {
    const response = await this.makeRequest(`${API_BASE_URL}/attractions/category/${category}`);
    return response.data;
  }

  async getAllAttractions() {
    try {
      const [puneAttractions, nearbyAttractions] = await Promise.all([
        this.getPuneAttractions(),
        this.getNearbyAttractions()
      ]);
      return [...puneAttractions, ...nearbyAttractions];
    } catch (error) {
      console.error('Failed to fetch all attractions:', error);
      throw error;
    }
  }
}

export default new APIService(); 