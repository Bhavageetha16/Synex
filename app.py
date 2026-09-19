import os
import json
import requests

from scraper import fetch_website_links, fetch_website_contents


# ==========================================
# SETUP
# ==========================================

OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL = "llama3.2"


# ==========================================
# FUNCTION TO TALK TO OLLAMA
# ==========================================

def ask_ollama(messages, json_mode=False):

    data = {
        "model": MODEL,
        "messages": messages,
        "stream": False
    }

    if json_mode:
        data["format"] = "json"

    response = requests.post(
        OLLAMA_URL,
        json=data
    )

    response.raise_for_status()

    return response.json()["message"]["content"]


# ==========================================
# 1. SELECT RELEVANT LINKS
# ==========================================

link_system_prompt = """
You are provided with a list of links found on a webpage.

You need to decide which links would be most relevant
for creating a brochure about the company.

Look for links such as:

- About
- Company
- Products
- Services
- Careers
- Contact

Return ONLY valid JSON in exactly this format:

{
    "links": [
        {
            "type": "about page",
            "url": "https://example.com/about"
        }
    ]
}
"""


def get_links_user_prompt(url, links):

    return f"""
Here is the list of links on the website {url}.

Please decide which links are relevant for creating
a brochure about the company.

Here are the links:

{links}
"""


def select_relevant_links(url):

    print(f"Selecting useful links from {url}...")

    # Get all links from the website
    links = fetch_website_links(url)

    # Keep only normal HTTP/HTTPS links
    links = [
        link for link in links
        if link.startswith("http")
    ]

    # Remove duplicate links
    links = list(dict.fromkeys(links))

    # Limit the number of links sent to Llama
    links = links[:20]

    messages = [
        {
            "role": "system",
            "content": link_system_prompt
        },
        {
            "role": "user",
            "content": get_links_user_prompt(url, links)
        }
    ]

    result = ask_ollama(
        messages,
        json_mode=True
    )

    print("Selected links:")
    print(result)

    return json.loads(result)


# ==========================================
# 2. COLLECT WEBSITE DETAILS
# ==========================================

def get_all_details(links):

    result = ""

    for link in links["links"]:

        url = link["url"]
        link_type = link["type"]

        print(f"Reading: {url}")

        result += f"\n\n{link_type}\n"

        result += fetch_website_contents(url)

    return result


# ==========================================
# 3. CREATE COMPANY BROCHURE
# ==========================================

brochure_system_prompt = """
You are an assistant that analyzes information from
several relevant pages of a company website.

Create a short professional brochure about the company
for prospective customers, investors and recruits.

Respond in markdown.

Include:

- Company overview
- Products and services
- Company culture
- Careers
- Any other important information

Be professional, engaging and accurate.

Only use information provided in the website content.
Do not invent facts.
"""


def create_brochure(company_name, details):

    user_prompt = f"""
Here are the contents of the website for {company_name}.

Please create a professional company brochure
using the information below:

{details}
"""

    messages = [
        {
            "role": "system",
            "content": brochure_system_prompt
        },
        {
            "role": "user",
            "content": user_prompt
        }
    ]

    return ask_ollama(messages)


# ==========================================
# 4. RUN THE PROJECT
# ==========================================

url = "https://edwarddonner.com"

print("\nFinding useful pages...")

links = select_relevant_links(url)

print("\nCollecting website information...")

details = get_all_details(links)

print("\nCreating brochure...")

brochure = create_brochure(
    "Edward Donner",
    details
)

print("\n==========================================")
print("             COMPANY BROCHURE")
print("==========================================\n")

print(brochure)