from serpapi import GoogleSearch
from typing import Tuple, List, Dict, Any

class ScholarSearch:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.keyword_counter = {}

    def search(self, keyword: str, page: int = 1) -> Tuple[List[Dict[str, Any]], int]:
        """
        Searches Google Scholar using SerpApi for a given keyword and page number.
        Returns a tuple of (results, total_results).
        """
        params = {
            "engine": "google_scholar",
            "q": keyword,
            "api_key": self.api_key,
            "start": (page - 1) * 10,
        }

        try:
            search = GoogleSearch(params)
            results = search.get_dict()
            papers = results.get("organic_results", [])
            total_results = results.get("search_information", {}).get("total_results", 0)
            
            # Update keyword counter
            self.keyword_counter[keyword] = self.keyword_counter.get(keyword, 0) + 1
            
            return papers, total_results
        except Exception as e:
            print(f"Error: {e}")
            return [], 0

    def get_keyword_count(self, keyword: str) -> int:
        """Returns the number of times a keyword has been searched."""
        return self.keyword_counter.get(keyword, 0)

    def count_keyword_mentions(self, keyword: str, results: List[Dict[str, Any]]) -> int:
        """Counts how many times the keyword appears in the results."""
        return sum(
            keyword.lower() in result.get("title", "").lower() or 
            keyword.lower() in result.get("snippet", "").lower()
            for result in results
        )