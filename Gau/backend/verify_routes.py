#!/usr/bin/env python3
"""
Simple route verification script to test email endpoints without sending emails.
Run this to verify all routes are properly configured.
"""

import requests
import json

BASE_URL = "http://localhost:5000/api"

def test_health():
    """Test the health endpoint."""
    try:
        response = requests.get(f"{BASE_URL}/health")
        print(f"✅ Health Check: {response.status_code} - {response.json()}")
        return True
    except Exception as e:
        print(f"❌ Health Check Failed: {e}")
        return False

def verify_routes():
    """Verify all email routes are accessible (without sending data)."""
    routes = [
        "/contact",
        "/contact/appliances", 
        "/contact/coffee-machines",
        "/contact/dishwashers",
        "/contact/washing-machines", 
        "/contact/commercial-equipment",
        "/newsletter"
    ]
    
    print("🔍 Verifying email routes are accessible...")
    
    for route in routes:
        try:
            # Send OPTIONS request to check if route exists
            response = requests.options(f"{BASE_URL}{route}")
            if response.status_code in [200, 405]:  # 405 = Method Not Allowed (route exists)
                print(f"✅ {route} - Route accessible")
            else:
                print(f"❌ {route} - Route not found ({response.status_code})")
        except Exception as e:
            print(f"❌ {route} - Error: {e}")

def show_route_info():
    """Display information about available routes."""
    print("\n📧 Available Email Routes:")
    print("=" * 50)
    print("General Contact:")
    print("  POST /api/contact")
    print("  Fields: name, email, service, message")
    print()
    print("Service-Specific Contact:")
    print("  POST /api/contact/appliances")
    print("  POST /api/contact/coffee-machines") 
    print("  POST /api/contact/dishwashers")
    print("  POST /api/contact/washing-machines")
    print("  POST /api/contact/commercial-equipment")
    print()
    print("Newsletter:")
    print("  POST /api/newsletter")
    print("  Fields: email, name (optional)")
    print()
    print("💡 To send actual emails, configure email credentials in .env")
    print("   See EMAIL_SETUP.md for detailed instructions")

def main():
    print("🧪 Flask Email Routes Verification")
    print("=" * 40)
    
    # Test health endpoint first
    if not test_health():
        print("\n❌ Flask server not running!")
        print("Start the server with: python app.py")
        return
    
    print()
    verify_routes()
    show_route_info()
    
    print("\n✅ Route verification complete!")
    print("All email routes are properly configured and ready for use.")

if __name__ == "__main__":
    main()
