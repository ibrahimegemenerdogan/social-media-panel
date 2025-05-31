from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    stats = [
        {'icon': '👥', 'value': '12.5K', 'label': 'Followers', 'color': '#3b82f6'},
        {'icon': '❤️', 'value': '8.2K', 'label': 'Likes', 'color': '#ef4444'},
        {'icon': '🔄', 'value': '4.7K', 'label': 'Shares', 'color': '#10b981'}
    ]
    
    activities = [
        {'text': 'Posted a new article about digital marketing trends', 'time': '2 hours ago'},
        {'text': 'Shared insights on social media strategy', 'time': '4 hours ago'},
        {'text': 'Engaged with community members', 'time': '6 hours ago'}
    ]
    
    return render_template('index.html', stats=stats, activities=activities)

if __name__ == '__main__':
    app.run(debug=True)