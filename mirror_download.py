"""
Recursive website mirror downloader - equivalent to: wget -r -np -l 0 <url>
Edit START_URL, OUT_DIR, and OVERWRITE below, then run: python mirror_download.py
"""

import os
import re
import time
from urllib.request import urlretrieve, urlopen
from urllib.parse import urljoin, urlparse
from urllib.error import URLError, HTTPError


visited = set()


def get_links(url, base_url):
    try:
        with urlopen(url, timeout=30) as response:
            html = response.read().decode("utf-8", errors="ignore")
    except (URLError, HTTPError) as e:
        print(f"  [skip] {url} -> {e}")
        return [], None
    links = re.findall(r'href=["\']([^"\']+)["\']', html)
    return links, html


def mirror(url, base_url, output_dir, overwrite=False):
    if url in visited:
        return
    visited.add(url)

    # Only follow links within the same base path (no-parent: -np)
    if not url.startswith(base_url):
        return

    rel_path = url[len(base_url):]
    local_path = os.path.join(output_dir, rel_path.lstrip("/").replace("/", os.sep))

    # If it looks like a directory, fetch index
    if url.endswith("/"):
        links, _ = get_links(url, base_url)
        for link in links:
            abs_link = urljoin(url, link)
            mirror(abs_link, base_url, output_dir, overwrite)
    else:
        # Download the file
        os.makedirs(os.path.dirname(local_path), exist_ok=True)
        if os.path.exists(local_path) and not overwrite:
            print(f"  [skip]  {local_path}")
        else:
            try:
                if os.path.exists(local_path):
                    print(f"  [overwrite] {url}")
                else:
                    print(f"  [download] {url}")
                urlretrieve(url, local_path)
                time.sleep(0.1)  # Be polite to the server
            except Exception as e:
                print(f"  [error] {url} -> {e}")

        # If HTML, also follow links
        if local_path.endswith(".html") or local_path.endswith(".htm"):
            links, _ = get_links(url, base_url)
            for link in links:
                abs_link = urljoin(url, link)
                mirror(abs_link, base_url, output_dir, overwrite)


if __name__ == "__main__":
    
    # --- Settings ---
    START_URL = "http://people.sc.fsu.edu/~jburkardt/py_src/"
    OUT_DIR   = "./"
    OVERWRITE = False  # True: overwrite existing files / False: skip existing files
    # ----------------

    start_url = START_URL.rstrip("/") + "/"
    mode = "overwrite" if OVERWRITE else "skip"
    print(f"Mirroring {start_url} -> {OUT_DIR}  (existing files: {mode})")
    mirror(start_url, start_url, OUT_DIR, OVERWRITE)
    print("Done.")
