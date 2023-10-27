from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files.get('file')
    if not file:
        response = {
            'status': 'error',
            'message': 'No file uploaded',
            'data': None
        }
        return jsonify(response), 400  # Trả về status code 400 (Bad Request) cho lỗi

    response = {
        'status': 200,
        'message': 'File uploaded successfully',
        'data': None
    }
    return jsonify(response)  # Trả về status code 200 (OK) cho thành công

@app.route('/process_file', methods=['GET'])
def process_file():
    # Đọc tệp CSV và lấy 5 dòng đầu
    try:
        df = pd.read_csv('path_to_your_csv_file.csv')
        first_5_rows = df.head(5)

        # Chuyển 5 dòng đầu thành chuỗi HTML
        result = first_5_rows.to_html()

        response = {
            'status': 'success',
            'message': 'File processed successfully',
            'data': result
        }
        return jsonify(response), 200  # Trả về status code 200 (OK) cho thành công
    except Exception as e:
        response = {
            'status': 'error',
            'message': 'Error processing file',
            'data': str(e)
        }
        return jsonify(response), 500  # Trả về status code 500 (Internal Server Error) cho lỗi

if __name__ == '__main__':
    app.run(debug=True, port=5001)