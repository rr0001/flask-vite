"""{{ cookiecutter.project_name }}."""

import json
from pathlib import Path
from typing import Any, Dict

from flask import Flask
from flask_inertia import Inertia

MANIFEST_FILE = Path(__file__).parent / "static/manifest.json"


def load_manifest() -> Dict[str, Dict[str, Any]]:
    """Loads manifest.json from static folder"""
    try:
        manifest = json.loads(MANIFEST_FILE.read_bytes())
    except (AttributeError, FileNotFoundError):
        manifest = {}

    return {"manifest": manifest}


def create_app(instance: str = None) -> Flask:
    """Initialize the Flask app"""
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(INERTIA_TEMPLATE="base.html", SECRET_KEY="changeme")

    # ensure the instance folder exists
    Path(app.instance_path).mkdir(parents=True, exist_ok=True)

    if instance:
        app.config.from_pyfile(f"{instance}.py")

    Inertia(app)

    app.context_processor(load_manifest)

    from flaskr.routes.main import main_routes

    app.register_blueprint(main_routes)

    return app
