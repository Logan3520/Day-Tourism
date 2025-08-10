import requests
import json

def test_image_url(url):
    """Test if an image URL returns a successful response"""
    try:
        response = requests.head(url, timeout=10)
        return response.status_code == 200
    except:
        return False

def main():
    # Test sample URLs from the app
    test_urls = [
        "https://media.istockphoto.com/id/1223512240/photo/mumbai-skyline-colaba.jpg?s=612x612&w=0&k=20&c=BWKSw4ELCOl6II3IOH-mL7H0k3-e3xOSuMJH_Xhw2oo=",
        "https://media.istockphoto.com/id/458700581/photo/mumbai-marine-drive.jpg?s=612x612&w=0&k=20&c=DYWJYaOjUEFjhwwKjsVl_HtOv3GYkKdw5CqgJjQFQz8=",
        "https://images.unsplash.com/photo-1587474260584-136574528ed5?w=800&auto=format&fit=crop&q=80",
        "https://media.istockphoto.com/id/507832607/photo/howrah-bridge-over-hooghly-river-kolkata-india.jpg?s=612x612&w=0&k=20&c=DtXUEgFG7E6M8IcNhZC5_PqJgNsB5O5sHJk8F6ygzCM=",
        "https://media.istockphoto.com/id/175441485/photo/howrah-bridge-calcutta.jpg?s=612x612&w=0&k=20&c=M7qDKyqnJM1N5a4X2GhC9L8yR3A5WjJgHx3f2I8Vn4M="
    ]
    
    print("Testing image URLs...")
    for url in test_urls:
        status = "✅ OK" if test_image_url(url) else "❌ FAILED"
        print(f"{status} - {url[:80]}...")
    
if __name__ == "__main__":
    main() 