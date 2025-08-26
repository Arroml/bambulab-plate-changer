# app/__init__.py
from flask import Flask, render_template


def create_app():
    app = Flask(__name__)

    # absolute imports
    from app.routes.printer_routes import printer_bp
    from app.routes.upload_routes import upload_bp
    from app.routes.changer_routes import changer_bp

    app.register_blueprint(printer_bp, url_prefix="/printer")
    app.register_blueprint(upload_bp, url_prefix="/upload")
    app.register_blueprint(changer_bp, url_prefix="/changer")

    @app.route("/")
    def home():
        current_job = {"name": "Testdruck", "Progress": 42}
        return render_template("index.html", current_job=current_job)

    return app
