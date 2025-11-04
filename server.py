#!/usr/bin/env python3
"""
Enhanced Globe Visualization Server
Serves the globe application with proper CORS headers and caching disabled
"""
import http.server
import socketserver
from http.server import SimpleHTTPRequestHandler
import os

class MyHTTPRequestHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        # Disable caching for development
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        self.send_header('Expires', '0')
        # CORS headers for external resources
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()

    def do_GET(self):
        # Serve index.html for root path
        if self.path == '/':
            self.path = '/index.html'
        return super().do_GET()
    
    def log_message(self, format, *args):
        # Custom logging format
        print(f"[{self.log_date_time_string()}] {format % args}")

PORT = 8000
HOST = "localhost"

def main():
    print("=" * 60)
    print("Enhanced Globe Visualization Server")
    print("=" * 60)
    print(f"\n🌍 Starting server on http://{HOST}:{PORT}/")
    print(f"📂 Serving files from: {os.getcwd()}")
    print("\n📝 Features:")
    print("   • Interactive country borders with tooltips")
    print("   • Searchable countries")
    print("   • Custom markers and connections")
    print("   • Atmosphere and glow effects")
    print("   • Real-time statistics")
    print("\n⚙️  Controls:")
    print("   • Drag globe to rotate")
    print("   • Use control panel for features")
    print("   • Click countries for information")
    print("\n💡 Press Ctrl+C to stop the server")
    print("=" * 60 + "\n")
    
    try:
        with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
            httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n\n👋 Shutting down server...")
        print("Server stopped successfully!")
    except Exception as e:
        print(f"\n❌ Error: {e}")

if __name__ == "__main__":
    main()