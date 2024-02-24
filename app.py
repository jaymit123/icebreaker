from flask import jsonify, Flask, render_template, request

from ice_breaker import ice_breaker

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/process", methods=["POST"])
def process():
    name = request.form["name"]
    person_info, profile_photo_url = ice_breaker(name)
    return jsonify(
        {
            "summary": person_info.summary,
            "interests": person_info.topics_of_interests,
            "facts": person_info.facts,
            "ice_breakers": person_info.ice_breaker,
            "picture_url": profile_photo_url,
        }
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=6006, debug=True)
