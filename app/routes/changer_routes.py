from flask import Blueprint

changer_bp = Blueprint("changer", __name__)


@changer_bp.get("/")
def info():
    return {"service": "changer", "status": "ready"}
