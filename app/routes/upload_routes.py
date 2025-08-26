from flask import Blueprint

upload_bp = Blueprint("upload", __name__)


@upload_bp.post("/")
def upload():
    return {"uploaded": True}
