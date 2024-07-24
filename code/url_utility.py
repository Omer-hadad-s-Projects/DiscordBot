from urllib.parse import urlparse, parse_qs, urlencode, urlunparse

def is_valid_url(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False
    
def get_song_url_from_input(input: str) -> str:
     url = input[5:]
     if(not is_valid_url(url)): return None
     url = trim_url(url)
     return url

def trim_url(url: str) -> str:
    parsed_url = urlparse(url)
    query_params = parse_qs(parsed_url.query)
    filtered_params = { 'v': query_params['v'] } if 'v' in query_params else {}
    new_query_string = urlencode(filtered_params, doseq=True)
    new_url = urlunparse(parsed_url._replace(query=new_query_string))
    return new_url
