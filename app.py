from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Sample data from the report
data = {
    'internet': {
        'users': '462 million',
        'penetration': '33%',
        'growth': '7% annually'
    },
    'social_media': {
        'users': '326 million',
        'penetration': '24%',
        'growth': '9% annually'
    },
    'mobile': {
        'connections': '1.2 billion',
        'penetration': '90%',
        'growth': '4% annually'
    }
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/stats/<topic>')
def stats(topic):
    if topic in data:
        return render_template('stats.html', topic=topic)
    else:
        return "Topic not found", 404

@app.route('/api/stats/<topic>')
def api_stats(topic):
    if topic in data:
        return jsonify(data[topic])
    else:
        return jsonify({"error": "Topic not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
