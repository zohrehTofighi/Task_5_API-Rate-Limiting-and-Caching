from flask import Flask, jsonify
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_caching import Cache

app = Flask(__name__)
cache = Cache(app, config={'CACHE_TYPE': 'simple'})

limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=["100 per day", "20 per hour"]
)

# Sample endpoint with rate limiting and caching
@app.route('/api/data')
@limiter.limit("10 per minute")  # Limiting this endpoint to 10 requests per minute
@cache.cached(timeout=60)  # Cache the response for 60 seconds
def get_data():
    # This is a sample response, you can replace it with your actual data retrieval logic
    data = {
        "message": "This is your data!"
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
