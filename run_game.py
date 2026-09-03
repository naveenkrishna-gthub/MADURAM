import http.server
import socketserver
import webbrowser
import threading
import time

PORT = 8000

class Handler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Enable CORS and caching headers
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

def open_browser():
    time.sleep(1.0)
    url = f"http://localhost:{PORT}/index.html"
    print(f"\n[+] Opening game in your browser: {url}")
    webbrowser.open(url)

if __name__ == "__main__":
    print(f"==================================================")
    print(f"  AADYAM KAIKKUM PINNE MADHURIKKUM - SERVER")
    print(f"  TinkerHub Useless Project Edition")
    print(f"==================================================")
    print(f"[*] Starting local server at http://localhost:{PORT}")
    print(f"[*] Press Ctrl+C in terminal to stop server.\n")

    threading.Thread(target=open_browser, daemon=True).start()

    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n[!] Server stopped.")
