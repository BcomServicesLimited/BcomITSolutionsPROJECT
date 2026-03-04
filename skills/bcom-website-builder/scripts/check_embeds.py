#!/usr/bin/env python3
"""
check_embeds.py — Bcom IT Solutions website builder utility.

Scans all .html files in a directory for escaped closing script tags
(<\/script>) that break DOM parsing when placed directly in HTML.

Usage:
  python check_embeds.py [directory]

If directory is not provided, defaults to /home/ubuntu/bcom-assets/
"""

import sys
import os
import re

def scan_file(filepath: str) -> list:
    issues = []
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    for i, line in enumerate(lines, 1):
        if r'<\/script>' in line:
            issues.append((i, line.strip()))
    return issues

def main():
    directory = sys.argv[1] if len(sys.argv) > 1 else '/home/ubuntu/bcom-assets/'
    html_files = [f for f in os.listdir(directory) if f.endswith('.html')]

    if not html_files:
        print(f"No .html files found in {directory}")
        return

    total_issues = 0
    for filename in sorted(html_files):
        filepath = os.path.join(directory, filename)
        issues = scan_file(filepath)
        if issues:
            print(f"\n{filename}: {len(issues)} issue(s)")
            for line_no, line_text in issues:
                print(f"  Line {line_no}: {line_text[:80]}")
            total_issues += len(issues)

    if total_issues == 0:
        print(f"All clear — no escaped closing script tags found in {len(html_files)} file(s).")
    else:
        print(f"\nTotal: {total_issues} escaped closing script tag(s) found.")
        print("Fix: replace all '<\\/script>' with '</script>' in the affected files.")

if __name__ == '__main__':
    main()
