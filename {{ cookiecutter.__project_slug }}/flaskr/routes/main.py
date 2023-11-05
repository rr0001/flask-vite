"""Main site routes."""

from flask import Blueprint
from flask_inertia import render_inertia

main_routes = Blueprint("main", __name__)


@main_routes.route("/")
def index():
    return render_inertia("Index")


@main_routes.route("/about/")
def about():
    return render_inertia("About")


@main_routes.route("/contact/")
def contact():
    return render_inertia("Contact")
