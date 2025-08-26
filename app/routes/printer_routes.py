from flask import Blueprint

printer_bp = Blueprint("printer", __name__)


@printer_bp.get("/")
def info():
    return {"service": "printer", "status": "ok"}
