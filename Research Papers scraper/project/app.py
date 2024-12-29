from flask import Flask, render_template, request
from scholar_search import ScholarSearch

app = Flask(__name__)

# Initialize ScholarSearch with your API key
scholar = ScholarSearch(api_key="70bcd518723ea82d25362079dcb2da0a6b76fec65e9660a05f2848180581bb7a")

@app.route("/")
def index():
    keyword = request.args.get("keyword")
    current_page = int(request.args.get("page", 1))
    
    results = []
    total_results = 0
    keyword_mentions_on_page = 0
    total_pages = 0

    if keyword:
        results, total_results = scholar.search(keyword, current_page)
        keyword_mentions_on_page = scholar.count_keyword_mentions(keyword, results)
        total_pages = (total_results // 10) + (1 if total_results % 10 > 0 else 0)

    return render_template(
        "index.html",
        results=results,
        keyword=keyword,
        total_results=total_results,
        current_page=current_page,
        total_pages=total_pages,
        keyword_counter=scholar.get_keyword_count(keyword) if keyword else 0,
        keyword_mentions_on_page=keyword_mentions_on_page
    )

if __name__ == "__main__":
    app.run(debug=True)