# Synex

### LLM-Powered Web Intelligence & Content Generation

Synex is a Python-based LLM application that analyzes website content and generates a structured company brochure using a locally running Llama 3.2 model through Ollama.

## Overview

Synex takes a website URL and:

1. Extracts links from the website.
2. Uses Llama 3.2 to identify relevant pages.
3. Fetches the content from those pages.
4. Combines the collected information.
5. Uses Llama 3.2 again to generate a professional company brochure.
6. Outputs the generated brochure in Markdown format.

## Architecture

```text
Website URL
     ↓
Web Scraper
     ↓
Extract Website Links
     ↓
Llama 3.2
Select Relevant Pages
     ↓
Fetch Selected Page Content
     ↓
Combine Website Information
     ↓
Llama 3.2
Generate Brochure
     ↓
Markdown Output
Tech Stack
Python
Ollama
Llama 3.2
Requests
BeautifulSoup
JSON
python-dotenv
Project Structure
Synex/
│
├── app.py
├── scraper.py
├── .gitignore
└── README.md
How It Works
1. Website Scraping

Synex uses Requests and BeautifulSoup to retrieve website content and extract links.

2. Relevant Link Selection

The extracted links are sent to the local Llama 3.2 model.

The model identifies pages that may contain useful information such as:

About
Company
Products
Services
Careers
Contact
3. Content Collection

Synex fetches the selected pages and combines their contents into a single information set.

4. Brochure Generation

The collected website information is sent to Llama 3.2 with a structured prompt.

The model generates a professional brochure containing information such as:

Company overview
Products and services
Company culture
Careers
Other relevant information
Local Setup
Prerequisites

Install:

Python 3.x
Git
Ollama

Make sure the Llama 3.2 model is available in Ollama:

ollama run llama3.2
Clone the Repository
git clone https://github.com/Bhavageetha16/Synex.git
cd Synex
Create a Virtual Environment
python -m venv .venv

Activate it on Windows:

.venv\Scripts\activate
Install Dependencies
pip install openai requests python-dotenv beautifulsoup4
Run Synex

Make sure Ollama is running with Llama 3.2, then run:

python app.py
Configuration

The current application uses the local Ollama API:

http://localhost:11434/api/chat

The model used by Synex is:

llama3.2

No paid OpenAI API key is required for the current local implementation.

Example

The current project can analyze:

https://edwarddonner.com

and generate a company brochure based on the relevant website content.

Key Concepts Demonstrated

This project demonstrates practical use of:

Large Language Models
Local LLM inference
Ollama
Prompt engineering
Structured JSON responses
Web scraping
HTTP APIs
Python automation
Multi-step LLM pipelines
Content generation
Future Improvements

Possible future improvements include:

Interactive URL input
Better website link filtering
Improved error handling
Web-based user interface
Streaming generated responses
Exporting brochures to PDF
More advanced LLM workflows
Author

Bhavageetha S

GitHub: https://github.com/Bhavageetha16


### Then

Save it as:

```text
C:\brochure\README.md

Then run:

git add README.md
git commit -m "Add project documentation"
git push
