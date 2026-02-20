from flask import Flask, jsonify
import requests

app = Flask(__name__)

BASE_URL = "https://jsonplaceholder.typicode.com/users"

@app.route("/run-tests")
def run_tests():
    results = {}

    # -------------------------
    # STEP 1: POST - Create Customer
    # -------------------------
    new_customer = {
        "name": "John Test",
        "username": "johntest",
        "email": "john@test.com"
    }

    post_response = requests.post(BASE_URL, json=new_customer)

    results["POST Status Code"] = post_response.status_code

    if post_response.status_code == 201:
        data = post_response.json()
        customer_id = data.get("id")

        results["POST Validation"] = {
            "Has ID": "id" in data,
            "Name Matches": data["name"] == new_customer["name"]
        }
    else:
        return jsonify({"error": "POST Failed"})

    # -------------------------
    # STEP 2: GET - Retrieve Customer
    # -------------------------
    get_response = requests.get(f"{BASE_URL}/{customer_id}")

    results["GET Status Code"] = get_response.status_code

    if get_response.status_code == 200:
        get_data = get_response.json()

        results["GET Validation"] = {
            "Correct ID": get_data["id"] == customer_id,
            "Email Exists": "email" in get_data
        }

    # -------------------------
    # STEP 3: PUT - Update Customer
    # -------------------------
    updated_data = {
        "name": "John Test",
        "username": "johntest",
        "email": "updated@test.com"
    }

    put_response = requests.put(f"{BASE_URL}/{customer_id}", json=updated_data)

    results["PUT Status Code"] = put_response.status_code

    if put_response.status_code == 200:
        put_data = put_response.json()

        results["PUT Validation"] = {
            "Email Updated": put_data["email"] == "updated@test.com",
            "ID Same": put_data["id"] == customer_id
        }

    # -------------------------
    # STEP 4: DELETE - Remove Customer
    # -------------------------
    delete_response = requests.delete(f"{BASE_URL}/{customer_id}")

    results["DELETE Status Code"] = delete_response.status_code

    # Verify deletion
    get_after_delete = requests.get(f"{BASE_URL}/{customer_id}")

    results["GET After DELETE Status"] = get_after_delete.status_code

    return jsonify(results)


if __name__ == "__main__":
    print(app.url_map)

    app.run(debug=True)
