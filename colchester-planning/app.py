"""
Colchester Kitchen Leads - Planning Applications
Finds rear extension planning applications in Colchester postcodes
and splits them into two lead lists:
  1. Submitted but not yet approved (last 3 months) - early leads
  2. Recently approved (last 1 month) - ready-to-buy leads
"""

import re
from datetime import datetime, timedelta
from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

PLANIT_API_BASE = "https://www.planit.org.uk/api/applics/json"
DEFAULT_AUTHORITY = "Colchester"

# Colchester postcodes
COLCHESTER_POSTCODES = re.compile(r"^CO[0-9]", re.IGNORECASE)

# Keywords that indicate a kitchen-relevant rear extension
EXTENSION_KEYWORDS = [
    "rear extension",
    "storey rear",
    "rear infill",
    "rear conservatory",
    "replacing conservatory",
    "replace conservatory",
    "replacement conservatory",
    "rear kitchen",
    "kitchen extension",
    "kitchen-diner",
    "kitchen diner",
    "ground floor rear",
    "ground floor extension",
    "rear flat roof extension",
]


def is_rear_extension(description):
    """Check if a planning application description is for a rear extension."""
    desc = (description or "").lower()
    return any(kw in desc for kw in EXTENSION_KEYWORDS)


def is_colchester_postcode(postcode):
    """Check if a postcode is in the Colchester area (CO*)."""
    if not postcode:
        return False
    return bool(COLCHESTER_POSTCODES.match(postcode.strip()))


def enrich_record(rec):
    """Add parsed fields from other_fields to a record."""
    of = rec.get("other_fields") or {}
    rec["_applicant"] = of.get("applicant_name", "")
    rec["_agent"] = of.get("agent_name", "")
    rec["_ward"] = of.get("ward_name", "")
    rec["_parish"] = of.get("parish", "")
    rec["_status"] = of.get("status", rec.get("app_state", ""))
    rec["_case_officer"] = of.get("case_officer", "")
    rec["_target_date"] = of.get("target_decision_date", "")
    rec["_date_received"] = of.get("date_received", rec.get("start_date", ""))
    rec["_date_validated"] = of.get("date_validated", "")
    rec["_consultation_end"] = of.get("consultation_end_date", "")
    rec["_decision"] = of.get("decision", "")
    rec["_decision_date"] = of.get("decision_date", rec.get("decided_date", ""))
    rec["_docs_url"] = of.get("docs_url", "")
    return rec


def fetch_all_pages(params, max_pages=10):
    """Fetch all pages of results from the PlanIt API."""
    all_records = []
    page_size = params.get("pg_sz", 500)
    for page_num in range(max_pages):
        params["index"] = page_num * page_size
        try:
            resp = requests.get(PLANIT_API_BASE, params=params, timeout=30)
            resp.raise_for_status()
            data = resp.json()
        except requests.RequestException:
            break
        records = data.get("records", [])
        all_records.extend(records)
        total = data.get("total", 0)
        if len(all_records) >= total or not records:
            break
    return all_records


def fetch_kitchen_leads():
    """Fetch and categorise kitchen-relevant planning leads."""
    # Fetch last 90 days of Colchester applications
    params = {
        "auth": DEFAULT_AUTHORITY,
        "recent": 90,
        "pg_sz": 500,
        "sort": "-start_date",
    }
    all_records = fetch_all_pages(params)

    submitted = []  # Undecided rear extensions (last 3 months)
    approved = []   # Approved rear extensions (last 1 month)

    one_month_ago = (datetime.now() - timedelta(days=30)).strftime("%Y-%m-%d")

    for rec in all_records:
        # Must be in a Colchester postcode
        if not is_colchester_postcode(rec.get("postcode", "")):
            continue

        # Must be a rear extension
        if not is_rear_extension(rec.get("description", "")):
            continue

        rec = enrich_record(rec)
        of = rec.get("other_fields") or {}
        decision = of.get("decision", "")
        decision_date = of.get("decision_date", rec.get("decided_date", ""))
        app_state = rec.get("app_state", "")

        if app_state == "Undecided":
            # List 1: Submitted but not yet decided
            submitted.append(rec)
        elif "Approve" in decision or app_state in ("Conditions", "Permitted"):
            # List 2: Approved — but only if decided in the last month
            if decision_date and decision_date >= one_month_ago:
                approved.append(rec)

    return submitted, approved


@app.route("/")
def index():
    """Main kitchen leads dashboard with two lists."""
    submitted, approved = fetch_kitchen_leads()
    error = None
    if not submitted and not approved:
        error = None  # Could be no results, not necessarily an error

    return render_template(
        "leads.html",
        submitted=submitted,
        approved=approved,
        submitted_count=len(submitted),
        approved_count=len(approved),
        error=error,
    )


@app.route("/application/<path:name>")
def application_detail(name):
    """Detail page for a single application."""
    url = f"https://www.planit.org.uk/planapplic/{name}/json"
    try:
        resp = requests.get(url, timeout=30)
        resp.raise_for_status()
        data = resp.json()
    except requests.RequestException as e:
        return render_template("detail.html", record=None, error=str(e))
    return render_template("detail.html", record=data, error=None)


@app.route("/api/leads")
def api_leads():
    """JSON API endpoint for kitchen leads."""
    submitted, approved = fetch_kitchen_leads()
    return jsonify({
        "submitted": submitted,
        "approved": approved,
        "submitted_count": len(submitted),
        "approved_count": len(approved),
    })


if __name__ == "__main__":
    app.run(debug=True, port=5000)
