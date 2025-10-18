from flask import Flask, render_template, request, jsonify, send_from_directory
import os

app = Flask(__name__, template_folder="templates", static_folder="static", instance_path=os.path.abspath(os.path.join(os.path.dirname(__file__), "instance")))


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/why-us")
def why_us():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/output.css")
def output_css():
    return send_from_directory("templates", "output.css", mimetype="text/css")


@app.route("/analyze", methods=["POST"])
def analyze():
    image = request.files.get("image")
    medicine_name = request.form.get("medicine_name", "").strip()

    if not image and not medicine_name:
        return jsonify({"success": False, "error": "Please provide an image or medicine name"}), 400

    # Placeholder analysis response. Replace with real logic as needed.
    result_markdown_parts = []
    if medicine_name:
        result_markdown_parts.append(f"## Medicine\n\n- Name: **{medicine_name}**")
    if image:
        result_markdown_parts.append("- Image uploaded and received successfully ✅")

    result_markdown_parts.append(
        "\n### Details\n- Usage: Follow prescription\n- Dosage: As directed by a professional\n- Side effects: May vary\n- Manufacturer: N/A\n- Shelf life: Check packaging"
    )

    result_markdown = "\n".join(result_markdown_parts)
    return jsonify({"success": True, "data": result_markdown})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="127.0.0.1", port=port, debug=True)