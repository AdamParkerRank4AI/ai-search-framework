"""
Kitchen Leads - Colchester & Surrounding Area
Finds rear extension planning applications within 20 miles of Colchester
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

# Councils within ~20 miles of Colchester town centre
AUTHORITIES = [
    "Colchester",
    "Tendring",
    "Maldon",
    "Chelmsford",
    "Babergh Mid Suffolk",
    "Ipswich",
    "East Suffolk",
    "Uttlesford",
]

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


def fetch_all_pages(params, max_pages=20):
    """Fetch all pages of results from the PlanIt API."""
    all_records = []
    # Use 200 per page - some councils fail at 500
    page_size = 200
    params["pg_sz"] = page_size
    for page_num in range(max_pages):
        params["index"] = page_num * page_size
        try:
            resp = requests.get(PLANIT_API_BASE, params=params, timeout=45)
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
    """Fetch and categorise kitchen-relevant planning leads from all authorities."""
    submitted = []  # Undecided rear extensions (last 3 months)
    approved = []   # Approved rear extensions (last 1 month)
    one_month_ago = (datetime.now() - timedelta(days=30)).strftime("%Y-%m-%d")
    councils_searched = []

    for authority in AUTHORITIES:
        params = {
            "auth": authority,
            "recent": 90,
            "pg_sz": 500,
            "sort": "-start_date",
        }
        records = fetch_all_pages(params, max_pages=4)
        council_count = 0

        for rec in records:
            if not is_rear_extension(rec.get("description", "")):
                continue

            rec = enrich_record(rec)
            of = rec.get("other_fields") or {}
            decision = of.get("decision", "")
            decision_date = of.get("decision_date", rec.get("decided_date", ""))
            app_state = rec.get("app_state", "")

            is_approved = (
                "Approve" in decision
                or "Permitted" in decision
                or "Approval" in decision
                or app_state == "Permitted"
                or app_state == "Conditions"
            )

            if app_state == "Undecided":
                submitted.append(rec)
                council_count += 1
            elif is_approved:
                if decision_date and decision_date >= one_month_ago:
                    approved.append(rec)
                    council_count += 1

        councils_searched.append({"name": authority, "leads": council_count})

    # Sort by date
    submitted.sort(key=lambda r: r.get("_date_received", ""), reverse=True)
    approved.sort(key=lambda r: r.get("_decision_date", ""), reverse=True)

    return submitted, approved, councils_searched


@app.route("/")
def index():
    """Main kitchen leads dashboard with two lists."""
    submitted, approved, councils = fetch_kitchen_leads()

    return render_template(
        "leads.html",
        submitted=submitted,
        approved=approved,
        submitted_count=len(submitted),
        approved_count=len(approved),
        councils=councils,
        error=None,
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
    submitted, approved, councils = fetch_kitchen_leads()
    return jsonify({
        "submitted": submitted,
        "approved": approved,
        "submitted_count": len(submitted),
        "approved_count": len(approved),
        "councils": councils,
    })


if __name__ == "__main__":
    app.run(debug=True, port=5000)
