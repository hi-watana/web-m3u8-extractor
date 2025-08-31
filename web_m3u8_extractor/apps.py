
from . import extract_m3u8_urls
from . import m3u8_to_text

async def web_url_to_m3u8_transcript(url: str, model_size: str="small", language: str="ja") -> str:
    m3u8_files = await extract_m3u8_urls._extract_m3u8_urls(url)
    if m3u8_files:
        print('Found M3U8 files: ', m3u8_files)
        return m3u8_to_text._m3u8_to_transcript(m3u8_files[0], model_size=model_size, language=language)
    raise ValueError("No valid m3u8 URLs found.")

def m3u8_to_transcript(m3u8_url: str, model_size: str="small", language: str="ja") -> str:
    return m3u8_to_text._m3u8_to_transcript(m3u8_url, model_size=model_size, language=language)