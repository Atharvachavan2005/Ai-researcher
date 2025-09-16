import requests

def search_arxiv_papers(topic:str, max_results: int=5)-> dict:
    query= "+".join(topic.lower().split())
    for char in list('()"'):
        if char in query:
            print(f"Invalid character '{char}' in query: {query}")
            raise ValueError(f"Cannot have characters: '{char}' in query: {query}")
    url= (
        "http://export.arxiv.org/api/query"
        f"?search_query=all:{query}"
        f"&max_results={max_results}"
        "&sortBy=submittedDate"
        "&sortOrder=descending"
    )
    print(f"Making request to arXiv API: {url}")
    resp=requests.get(url)

    if not resp.ok:
        print(f"ArXiv API request failed: {resp.status_code} - {resp.text}")
        raise ValueError(f"Bad response from arXiv API: {resp}\n{resp.text}")
    
    data= parse_arxiv_xml(resp.text)
    return data

import xml.etree.ElementTree as ET
def parse_arxiv_xml(xml_content:str) -> dict:
    """Parse the XML content from arXiv API response"""
    entries =[]
    