import time
from crewai.tools import tool
from crewai_tools import SerperDevTool
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

search_tool = SerperDevTool(
    n_results=5,
)


@tool
def scrape_tool(url: str):
    """
    Use this when you need to scrape the content of a given website URL.
    Returns the content of a website, in case the website is not available, it returns "No content".
    The input is a 'url' string. for example: https://www.nytimes.com/2021/09/01/us/politics/biden-border-migrants.html
    The output is a string.
    """
    print(f"Scrapping URL: {url}")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url)
        time.sleep(5)
        content = page.content()
        browser.close()
        soup = BeautifulSoup(content, "html.parser")

        unwanted_tags = [
            "script",
            "style",
            "header",
            "footer",
            "nav",
            "aside",
            "form",
            "input",
            "button",
            "select",
            "textarea",
            "iframe",
            "embed",
            "object",
            "video",
            "audio",
            "map",
            "noscript",
            "noindex",
            "nofollow",
            "noarchive",
            "nocache",
            "noimageindex",
            "noindex, nofollow",
            "noarchive, noindex, nofollow",
            "noindex, nofollow, noarchive",
            "svg",
        ]

        for tag in soup.find_all():
            tag.decompose()

        content = soup.get_text(separator=" ")

        return content if content != "" else "No content"
