#!pip install requests-html lxml_html_clean

from requests_html import AsyncHTMLSession
import re
import asyncio

async def extract_m3u8_urls(url):
    """
    Fetches a dynamically loaded webpage and extracts m3u8 URLs asynchronously.

    Args:
        url: The URL of the webpage.

    Returns:
        A list of m3u8 URLs found on the page.
    """
    session = AsyncHTMLSession()
    try:
        r = await session.get(url)
        # Render the page to execute JavaScript
        await r.html.arender()

        # Find all script tags and links that might contain m3u8 URLs
        m3u8_urls = []
        # Look for m3u8 patterns in the rendered HTML
        m3u8_urls.extend(re.findall(r'(https?://[^\s]+\.m3u8)', r.html.html))

        # You might need to inspect the page's network requests to find the exact pattern
        # or look into specific script contents depending on the website.
        # This is a basic example and might need adjustments for different sites.

        return list(set(m3u8_urls)) # Return unique URLs

    except Exception as e:
        print(f"An error occurred: {e}")
        return []

# Example usage will need to be updated to run this async function
# async def main():
#     page_url = 'YOUR_PAGE_URL_HERE'
#     m3u8_files = await extract_m3u8_urls(page_url)

#     if m3u8_files:
#         print("Found m3u8 URLs:")
#         for m3u3_url in m3u3_files:
#             print(m3u3_url)
#     else:
#         print("No m3u8 URLs found or an error occurred.")

# if __name__ == "__main__":
#     asyncio.run(main())

#if __name__ == "__main__":
#    page_url = input("Please enter the URL of the page: ").strip()
#    m3u8_files = await extract_m3u8_urls(page_url)
#
#    if m3u8_files:
#        print("Found m3u8 URLs:")
#        for m3u8_url in m3u8_files:
#            print(m3u8_url)
#    else:
#        print("No m3u8 URLs found or an error occurred.")


