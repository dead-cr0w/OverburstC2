import http.server
import socketserver
import os
import socket

PORT = 8080
FOLDER = os.path.dirname(os.path.abspath(__file__))
SERVE_DIR = os.path.join(FOLDER, 'binaries')

# config.json
if not os.path.exists(SERVE_DIR):
    print(f"[!] Error: Directory '{SERVE_DIR}' does not exist!")
    exit(1)

os.chdir(SERVE_DIR)

class Handler(http.server.SimpleHTTPRequestHandler):
    def setup(self):
        super().setup()
        self.request.settimeout(60)
    
    def log_message(self, format, *args):
        # Customiza as mensagens de log
        print(f"[{self.log_date_time_string()}] {format % args}")

def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
        s.close()
        return local_ip
    except:
        return "127.0.0.1"

local_ip = get_local_ip()

print("=" * 60)
print(f"[+] Server started successfully!")
print(f"[+] Directory served: {SERVE_DIR}")
print(f"[+] Port: {PORT}")
print("=" * 60)
print(f"[+] Access the server at:")
print(f"→ http://localhost:{PORT}")
print(f"→ http://127.0.0.1:{PORT}")
print(f"→ http://{local_ip}:{PORT}")
print("=" * 60)
print("[+] Press Ctrl+C to stop the server")
print("=" * 60)

try:
    with socketserver.TCPServer(("0.0.0.0", PORT), Handler) as httpd:
        httpd.serve_forever()
except KeyboardInterrupt:
    print("\n[!] Server terminated by user")
except Exception as e:
    print(f"\n[!] Error starting server: {e}")
