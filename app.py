from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# Directory to save uploaded files
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        if file:
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)
            # Process the file here (e.g., run your recognition algorithm)
            # For this example, we'll just simulate the results
            results = {
                'results': [
                    {'plate': 'ABC123', 'confidence': 98.5, 'approved': True},
                    {'plate': 'XYZ789', 'confidence': 87.2, 'approved': False}
                ]
            }
            return render_template('results.html', results=results)
    return render_template('upload.html')

@app.route('/occupancy')
def occupancy():
    # Simulate occupancy data
    occupancy_data = {
        'Lot1': {'occupied': 10, 'total': 20},
        'Lot2': {'occupied': 5, 'total': 15}
    }
    return render_template('occupancy.html', occupancy=occupancy_data)

@app.route('/movements')
def movements():
    # Simulate vehicle movements data
    movements_data = [
        [1, 'ABC123', '2024-07-15 08:45:00', 'Entrance'],
        [2, 'XYZ789', '2024-07-15 09:00:00', 'Exit']
    ]
    return render_template('movements.html', movements=movements_data)

if __name__ == '__main__':
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    app.run(debug=True)
