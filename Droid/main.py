import http.server
import os
from functools import partial


def run():
    """Serve the repository directory so the Alice in Kerneland theme can be previewed.

    - Serves static files from the repo root
    - Visit / to see index.html or /theme/preview.html for the full demo
    """
    port = int(os.environ.get("PORT", "8000"))
    here = os.path.dirname(os.path.abspath(__file__))

    Handler = partial(http.server.SimpleHTTPRequestHandler, directory=here)
    httpd = http.server.ThreadingHTTPServer(("", port), Handler)

    print(f"Alice in Kerneland server running: http://localhost:{port}/")
    print("Try / (index.html) or /theme/preview.html for tags and jokes.")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        httpd.server_close()


if __name__ == "__main__":
    run()
