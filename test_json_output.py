#!/usr/bin/env python3
"""Test minimal yt-dlp for JSON stream URL extraction"""

import json
import yt_dlp

def get_stream_urls(video_id, proxy_url=None):
    """
    Extract stream URLs from YouTube video and output as JSON
    """
    ydl_opts = {
        'quiet': False,
        'no_warnings': False,
        'format': 'best',
        'skip_download': True,
        'extract_flat': False,
    }
    
    # Add proxy if provided
    if proxy_url:
        ydl_opts['proxy'] = proxy_url
    
    url = f'https://www.youtube.com/watch?v={video_id}'
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            
            # Extract stream URLs
            output = {
                'video_id': info.get('id'),
                'title': info.get('title'),
                'duration': info.get('duration'),
                'formats': []
            }
            
            # Collect format information
            if 'formats' in info:
                for fmt in info['formats']:
                    if fmt.get('url'):
                        output['formats'].append({
                            'format_id': fmt.get('format_id'),
                            'ext': fmt.get('ext'),
                            'url': fmt.get('url'),
                            'height': fmt.get('height'),
                            'width': fmt.get('width'),
                        })
            
            return output
    except Exception as e:
        return {'error': str(e)}

if __name__ == '__main__':
    # Test with specified video ID and proxy
    test_video_id = 'BAIX2kvBV9Q'
    proxy_url = 'http://ytproxy-siawaseok.duckdns.org:3007'
    
    print("=" * 60)
    print("Testing JSON output with proxy")
    print("=" * 60)
    print(f"Video ID: {test_video_id}")
    print(f"Proxy: {proxy_url}")
    print()
    
    result = get_stream_urls(test_video_id, proxy_url=proxy_url)
    print(json.dumps(result, indent=2))
