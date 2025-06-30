🔍 Parameter Finder
A Python-based terminal tool that scans websites to extract URLs containing GET parameters. Useful for bug bounty hunting, pentesting, or reconnaissance. Built with requests and BeautifulSoup, it identifies query string parameters for further analysis.
✨ Features:

# Colorful terminal UI

# Automatic SSL warning suppression

# Works with or without command-line arguments

# Clears screen and displays a custom banner on start


Features
Automatic URL Extraction: Finds all links with parameters (e.g., ?id=123) from a target web page.
Easy to Use: Just provide a URL and get a list of parameterized URLs.
Supports HTTPS: Works with both HTTP and HTTPS sites.
Colorful Output: Uses color for better readability in the terminal.
Security Research: Useful for reconnaissance, XSS, and parameter fuzzing.
Usage
1. Clone the repository:
`git clone https://github.com/4DN4N4D1F/parameter_finder.git
cd parameter_finder`
2. Install requirements:
`pip install -r requirements.txt`
3. Run the tool:
`python parameter_finder.py`
4. Enter the target website URL when prompted.
Example Output
```
[+] Scanning for parameterized URLs...

  → https://example.com/page.php?id=1
  → https://example.com/search?q=test
  → https://example.com/profile?user=admin

[SECDET] Scan complete.
```

#Note:
This tool is for educational and authorized security testing only.
Always get permission before scanning third-party websites.
