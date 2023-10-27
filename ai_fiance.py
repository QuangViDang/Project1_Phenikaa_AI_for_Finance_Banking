from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

responseError = {
    'message': 'Error processing file',
}
responseSuccess = {
    'status': 200
}

file_global = []

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files.get('file')
    print("API", file)
    if not file:
        responseError["status"] = 400
        print(responseError)
        return jsonify(responseError)
    else: 
        file_global.append(file)
        print("Length", file_global[0])
        responseSuccess['message'] = "Success!!!" 
        print("Success!")
        return jsonify(responseSuccess) 

@app.route('/process_file', methods=['GET'])
def process_file():
    # Đọc tệp CSV và lấy 5 dòng đầu
    
    try:
        if (file_global.__len__ != 0):
            for file in file_global:
                df = pd.read_csv(file)
                first_5_rows = df.head(5)

                # Chuyển 5 dòng đầu thành chuỗi HTML
                result = first_5_rows.to_html()
                responseSuccess = {  
                    "code":200,
                    "status":"success",
                    "data":result
                }
                
                return jsonify(responseSuccess)  # Trả về status code 200 (OK) cho thành công
    except Exception as e:
      
        return jsonify(response), 500  # Trả về status code 500 (Internal Server Error) cho lỗi

if __name__ == '__main__':
    app.run(debug=True, port=5000)