from flask import Flask, request, jsonify
from selenium_shu import get_grades

app = Flask(__name__)

@app.route("/query-grades", methods=["POST"])
def query_grades():
    data = request.get_json()
    account = data.get("account")
    password = data.get("password")

    try:
        grades = get_grades(account, password)
        return jsonify({"grades": grades})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
