import extract_m3u8_urls
import m3u8_to_text

def web_url_to_m3u8_transcript() -> str:
    url = input("Enter the webpage URL: ")
    m3u8_files = extract_m3u8_urls.extract_m3u8_urls(url)
    if m3u8_files:
        return m3u8_to_text.m3u8_to_transcript(m3u8_files[0])
    raise ValueError("No valid m3u8 URLs found.")

def m3u8_to_transcript() -> str:
    m3u8_url = input("Enter the M3U8 URL: ")
    return m3u8_to_text.m3u8_to_transcript(m3u8_url)