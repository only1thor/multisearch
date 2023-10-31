from flask import Flask, request
from duckduckgo_search import DDGS

app = Flask(__name__)

@app.route('/search', methods=['GET'])
def search():
 query = request.args.get('q')
 if query:
     with DDGS() as ddgs:
         results = ddgs.search(query, max_results=3)
     return {"duckduckgo": results}
 else:
     return {"error": "No query provided"}

if __name__ == "__main__":
 app.run(port=1234)

