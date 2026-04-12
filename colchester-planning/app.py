"""
Colchester Planning Applications Viewer
A basic Plany.co.uk-style tool for browsing planning applications
using the PlanIt.org.uk public API.
"""

import json
from datetime import datetime
from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

PLANIT_API_BASE = "https://www.planit.org.uk/api/applics/json"
DEFAULT_AUTHORITY = "Colchester"


def fetch_applications(authority=DEFAULT_AUTHORITY, days=30, page_size=50,
                       page=1, search=None, app_type=None, app_state=None):
    """Fetch planning applications from the PlanIt API."""
    params = {
        "auth": authority,
        "recent": days,
        "pg_sz": page_size,
        "index": (page - 1) * page_size,
        "sort": "-start_date",
    }
    if search:
        params["search"] = search
    if app_type:
        params["app_type"] = app_type
    if app_state:
        params["app_state"] = app_state

    try:
        resp = requests.get(PLANIT_API_BASE, params=params, timeout=30)
        resp.raise_for_status()
        return resp.json()
    except requests.RequestException as e:
        return {"records": [], "total": 0, "error": str(e)}


def fetch_single_application(name):
    """Fetch a single application by its PlanIt name (e.g. Colchester/260586)."""
    url = f"https://www.planit.org.uk/planapplic/{name}/json"
    try:
        resp = requests.get(url, timeout=30)
        resp.raise_for_status()
        return resp.json()
    except requests.RequestException as e:
        return {"error": str(e)}


@app.route("/")
def index():
    """Main search and listing page."""
    search = request.args.get("search", "").strip()
    days = request.args.get("days", "30", type=str)
    app_type = request.args.get("app_type", "")
    app_state = request.args.get("app_state", "")
    page = request.args.get("page", 1, type=int)
    page_size = 25

    try:
        days_int = int(days)
    except ValueError:
        days_int = 30

    data = fetch_applications(
        days=days_int,
        page_size=page_size,
        page=page,
        search=search or None,
        app_type=app_type or None,
        app_state=app_state or None,
    )

    records = data.get("records", [])
    total = data.get("total", 0)
    error = data.get("error")
    total_pages = max(1, (total + page_size - 1) // page_size)

    # Enrich records with parsed other_fields
    for rec in records:
        of = rec.get("other_fields") or {}
        rec["_applicant"] = of.get("applicant_name", "")
        rec["_agent"] = of.get("agent_name", "")
        rec["_ward"] = of.get("ward_name", "")
        rec["_parish"] = of.get("parish", "")
        rec["_status"] = of.get("status", rec.get("app_state", ""))
        rec["_case_officer"] = of.get("case_officer", "")
        rec["_target_date"] = of.get("target_decision_date", "")
        rec["_date_received"] = of.get("date_received", rec.get("start_date", ""))
        rec["_consultation_end"] = of.get("consultation_end_date", "")

    return render_template(
        "index.html",
        records=records,
        total=total,
        page=page,
        total_pages=total_pages,
        search=search,
        days=days,
        app_type=app_type,
        app_state=app_state,
        error=error,
    )


@app.route("/application/<path:name>")
def application_detail(name):
    """Detail page for a single application."""
    data = fetch_single_application(name)
    if "error" in data:
        return render_template("detail.html", record=None, error=data["error"])
    return render_template("detail.html", record=data, error=None)


@app.route("/api/applications")
def api_applications():
    """JSON API endpoint for applications."""
    search = request.args.get("search")
    days = request.args.get("days", 30, type=int)
    page = request.args.get("page", 1, type=int)
    page_size = request.args.get("page_size", 25, type=int)
    app_type = request.args.get("app_type")
    app_state = request.args.get("app_state")

    data = fetch_applications(
        days=days,
        page_size=page_size,
        page=page,
        search=search,
        app_type=app_type,
        app_state=app_state,
    )
    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
