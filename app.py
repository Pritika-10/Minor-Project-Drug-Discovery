
from flask import Flask, render_template, request, jsonify, send_file
import pandas as pd
from rdkit import Chem
from rdkit.Chem import Draw

app = Flask(__name__)

# Global variable to store uploaded and processed data
uploaded_data = None
filtered_data = None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    global uploaded_data
    file = request.files['file']
    uploaded_data = pd.read_csv(file)
    return jsonify(status="success", message="File uploaded successfully")

@app.route('/filter', methods=['POST'])
def filter_data():
    global uploaded_data, filtered_data
    if uploaded_data is None:
        return jsonify(status="error", message="No dataset uploaded")
    threshold = float(request.form.get('threshold'))
    filtered_data = uploaded_data[uploaded_data['Docking_Score'] < threshold]
    return jsonify(status="success", data=filtered_data.to_dict(orient='records'))

@app.route('/visualize', methods=['POST'])
def visualize():
    global filtered_data
    if filtered_data is None:
        return jsonify(status="error", message="No filtered data available")
    smiles_list = filtered_data['SMILES'].tolist()
    molecules = [Chem.MolFromSmiles(smiles) for smiles in smiles_list]
    img = Draw.MolsToGridImage(molecules, molsPerRow=4, subImgSize=(200, 200))
    img_path = "static/molecules.png"
    img.save(img_path)
    return jsonify(status="success", image_url=img_path)

@app.route('/download', methods=['GET'])
def download_filtered():
    global filtered_data
    if filtered_data is None:
        return jsonify(status="error", message="No filtered data available")
    file_path = "filtered_candidates.csv"
    filtered_data.to_csv(file_path, index=False)
    return send_file(file_path, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
