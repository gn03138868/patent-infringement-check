from flask import Flask, jsonify, request
from infringe_check import check_infringement

app = Flask(__name__)

@app.route("/check_infringement", methods=["POST"])
def infringement_check():
    data = request.get_json()
    patent_id = data.get("patent_id")
    company_name = data.get("company_name")
    
    if not patent_id or not company_name:
        return jsonify({"error": "Patent ID and Company Name are required"}), 400
    
    try:
        result = check_infringement(patent_id, company_name)
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
