from setuptools import setup, find_packages

setup(
    name='web-m3u8-extractor',
    version='0.1.0',
    description='A tool to extract m3u8 URLs from web sources.',
    author='Hiro Watt',
    packages=find_packages(),
    py_modules=[
        'apps',
    ],
    install_requires=[
        'requests-html',
        'lxml',
        'asyncio',
        'faster-whisper',
        'ffmpeg-python',
    ],
    python_requires='>=3.7',
)
