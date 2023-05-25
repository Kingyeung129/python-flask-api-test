from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/get-user/<userID>")
def getUser(userID):
    user_data = {
        "userID": userID,
        "name": "John Doe",
        "email": "john.doe@example.com"
    }
    
    extra = request.args.get("extra")
    if extra:
        user_data["extra"] = extra
        
    return jsonify(user_data), 200


@app.route("/create-user", methods=["POST"])
def createUser():
    data = request.get_json()
    return jsonify(data), 201


@app.route("/update-user", methods=["POST"])
def updateUser():
    data = request.get_json()
    return jsonify(data), 201


@app.route("/")
def home():
    return "My First API"


if __name__ == "__main__":
    app.run(debug=True)