# Morss - Get full-text RSS feeds


A powerful tool to get full-text RSS feeds from websites that only provide partial content.

## Overview

morss is a web service that transforms truncated RSS feeds into full-text feeds by:

1. Fetching the original RSS feed
2. Extracting article URLs
3. Visiting each article page
4. Extracting the complete content
5. Generating a new RSS feed with full articles

## Features

- **Full Content Extraction**: Get complete articles in your RSS reader
- **Caching System**: Efficient performance with automatic cache expiration
- **Simple URL Structure**: Just add your target feed URL after the morss domain
- **Security Enhancements**: URL validation and safer caching implementation
- **Multiple Output Formats**: Support for RSS, ATOM, and JSON
- **Customizable**: Various options to control the output

## Usage

### Basic Usage

`https://your-morss-instance.com/https://example.com/feed`

Simply prepend your morss server URL to any RSS feed URL.

### Advanced Options

Add these parameters to customize the output:

- `?format=atom` - Output as ATOM feed
- `?format=json` - Output as JSON
- `?keep=0` - Remove items without full content
- `?links=auto` - Fix relative links
- `?proxy=1` - Fetch images through morss (avoid tracking)

Example:

` https://your-morss-instance.com/https://example.com/feed?format=atom&links=auto`

## Installation

### Requirements

- Python 3.6+
- pip
- virtualenv (recommended)

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/morss.git
   cd morss

2. Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies: 
`pip install -r requirements.txt`

4. Run the development server:
`python main.py
`



