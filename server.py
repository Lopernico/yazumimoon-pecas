from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import urllib.request
import urllib.parse
import re
import os
import mimetypes

class MyHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Handle API endpoint for followers
        if self.path.startswith('/api/followers'):
            self.handle_followers_request()
            return
        
        # Route the request
        path = self.path.split('?')[0]  # Remove query parameters
        # URL decode the path to handle spaces and special characters
        path = urllib.parse.unquote(path)
        
        if path == '/' or path == '':
            path = '/index.html'
        
        # Get the file path
        file_path = os.path.join(os.getcwd(), path.lstrip('/'))
        print(f"Requesting: {self.path} -> decoded: {path} -> {file_path}")
        
        try:
            # Check if file exists
            if not os.path.isfile(file_path):
                print(f"File not found: {file_path}")
                self.send_error(404, 'File not found')
                return
            
            # Read and serve the file
            with open(file_path, 'rb') as f:
                content = f.read()
            
            # Determine content type
            content_type, _ = mimetypes.guess_type(file_path)
            if content_type is None:
                content_type = 'application/octet-stream'
            
            self.send_response(200)
            self.send_header('Content-type', content_type)
            self.send_header('Content-Length', len(content))
            self.end_headers()
            self.wfile.write(content)
            print(f"Served: {file_path}")
            
        except Exception as e:
            print(f"Error serving file: {e}")
            self.send_error(500, 'Internal server error')
    
    def handle_followers_request(self):
        try:
            print("Fetching followers from NicheProvider...")
            # Fetch from NicheProwler
            req = urllib.request.Request(
                'https://www.nicheprowler.com/tools/twitch/twitch-follower-checker?query=yazumimoon',
                headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
            )
            with urllib.request.urlopen(req, timeout=10) as response:
                html = response.read().decode('utf-8')
            
            print("NicheProwler page fetched, searching for followers count...")
            
            # Extract followers count from NicheProwler
            # Looking for: <span class="text-2xl font-bold text-purple-800">206</span>
            # or: <div class="inline-flex ... text-lg px-3 py-1">206</div>
            patterns = [
                # Primary pattern - the display number
                r'<span class="text-2xl font-bold text-purple-800">(\d+)</span>',
                # Secondary pattern - the badge
                r'<div class="inline-flex[^>]*bg-purple-100[^>]*>(\d+)</div>',
                # Alternative pattern for total followers
                r'Total Followers:</span>\s*<div[^>]*>(\d+)</div>',
                # Generic pattern
                r'<span class="text-2xl[^>]*>(\d+)</span>',
                r'>(\d+)</(?:span|div)>.*?Yazumimoon',
            ]
            
            followers = None
            for i, pattern in enumerate(patterns):
                match = re.search(pattern, html, re.IGNORECASE | re.DOTALL)
                if match:
                    followers = match.group(1).strip()
                    followers = followers.replace('.', '').replace(',', '').replace(' ', '')
                    if int(followers) > 0:
                        print(f"Found with pattern {i}: '{followers}'")
                        break
                    else:
                        followers = None
            
            if followers:
                print(f"Sending followers count: {followers}")
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                self.wfile.write(json.dumps({'followers': followers}).encode())
            else:
                # Save HTML for debugging
                with open('debug_nicheprowler.html', 'w', encoding='utf-8') as f:
                    f.write(html)
                print("HTML saved to debug_nicheprowler.html")
                raise ValueError('Could not extract follower count from NicheProwler')
                
        except Exception as e:
            print(f"Error fetching followers: {e}")
            import traceback
            traceback.print_exc()
            self.send_response(500)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(json.dumps({'error': str(e)}).encode())
    
    def log_message(self, format, *args):
        # Custom logging
        print(format % args)

if __name__ == '__main__':
    try:
        server_address = ('', 8000)
        httpd = HTTPServer(server_address, MyHTTPRequestHandler)
        print('Server running on http://localhost:8000')
        print(f'Working directory: {os.getcwd()}')
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('\nServer stopped')
        httpd.server_close()
    except Exception as e:
        print(f'Error: {e}')
        import traceback
        traceback.print_exc()
