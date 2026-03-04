#!/usr/bin/env python3
"""
inline_components.py — Bcom IT Solutions website builder utility.

Inlines nav.html and footer.html into a target HTML page, replacing
the placeholder comments:
  <!-- @@include('nav.html') -->
  <!-- @@include('footer.html') -->

Usage:
  python inline_components.py <target_page.html> [--assets-dir /path/to/bcom-assets]

If --assets-dir is not provided, defaults to /home/ubuntu/bcom-assets/
"""

import sys
import os
import argparse

def inline_component(html: str, placeholder: str, component_file: str) -> str:
    if not os.path.exists(component_file):
        print(f"  WARNING: Component file not found: {component_file}")
        return html
    with open(component_file, 'r', encoding='utf-8') as f:
        content = f.read()
    if placeholder in html:
        html = html.replace(placeholder, content)
        print(f"  Inlined: {os.path.basename(component_file)}")
    else:
        print(f"  SKIPPED (placeholder not found): {placeholder}")
    return html

def check_escaped_script_tags(html: str, filename: str):
    """Warn if any escaped closing script tags are present — these break DOM parsing."""
    if r'<\/script>' in html:
        count = html.count(r'<\/script>')
        print(f"\n  WARNING: {count} escaped closing script tag(s) found in {filename}.")
        print("  These break DOM parsing. Replace all '<\\/script>' with '</script>'.")
        print("  Run: grep -n '<\\\\/script>' " + filename)

def main():
    parser = argparse.ArgumentParser(description='Inline nav and footer components into an HTML page.')
    parser.add_argument('target', help='Path to the target HTML file')
    parser.add_argument('--assets-dir', default='/home/ubuntu/bcom-assets/', help='Path to bcom-assets directory')
    args = parser.parse_args()

    target = args.target
    assets_dir = args.assets_dir.rstrip('/') + '/'

    if not os.path.exists(target):
        print(f"ERROR: Target file not found: {target}")
        sys.exit(1)

    print(f"Processing: {target}")

    with open(target, 'r', encoding='utf-8') as f:
        html = f.read()

    html = inline_component(html, "<!-- @@include('nav.html') -->", assets_dir + 'nav.html')
    html = inline_component(html, "<!-- @@include('footer.html') -->", assets_dir + 'footer.html')

    check_escaped_script_tags(html, target)

    with open(target, 'w', encoding='utf-8') as f:
        f.write(html)

    print(f"  Done. Saved: {target}")

if __name__ == '__main__':
    main()
