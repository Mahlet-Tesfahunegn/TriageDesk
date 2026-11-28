import pytest
from app.agent import classify_ticket

# Payment test
def test_payment_classification():
    ticket = "My payment failed."

    result = classify_ticket(ticket)

    assert result["category"] == "Payment Issues"
    assert result["priority"] == "High"
    assert result["department"] == "Billing Support"
    assert "payment_failure" in result["matched_rules"]

# Account access test
def test_account_access_classification():
    ticket = "I cannot log in to my account."

    result = classify_ticket(ticket)

    assert result["category"] == "Account Access"
    assert result["priority"] == "Medium"
    assert result["department"] == "Account Support"
    assert "account_access" in result["matched_rules"]

# Service outage test
def test_service_outage_classification():
    ticket = "The entire website is down."

    result = classify_ticket(ticket)

    assert result["category"] == "Service Outages"
    assert result["priority"] == "Critical"
    assert result["department"] == "Technical Support"
    assert "widespread_service_outage" in result["matched_rules"]

# Technical issue test
def test_technical_issue_classification():
    ticket = "The application is freezing."

    result = classify_ticket(ticket)

    assert result["category"] == "Technical Issues"
    assert result["priority"] == "Medium"
    assert result["department"] == "Technical Support"
    assert "technical_issue" in result["matched_rules"]

# General quiry test
def test_general_inquiry_classification():
    ticket = "What payment methods do you accept?"

    result = classify_ticket(ticket)

    assert result["category"] == "General Inquiries"
    assert result["priority"] == "Medium"
    assert result["department"] == "General Support"
    assert "general_inquiry" in result["matched_rules"]


# Muliple phrases and same category test
def test_multiple_phrases_same_category():
    ticket = "My payment failed and I was charged twice."

    result = classify_ticket(ticket)

    assert result["category"] == "Payment Issues"
    assert result["priority"] == "High"
    assert result["department"] == "Billing Support"
    # check the rules appear only once
    assert result["matched_rules"] ==  ["payment_failure"]

# Multiple categories test
def test_multiple_categories_require_manual_review():
    ticket = "I cannot log in and my payment failed."

    result = classify_ticket(ticket)

    assert result["category"] == "Manual Review"
    assert result["priority"] == "Undetermined"
    assert result["department"] == "Human Review"
    assert "account_access" in result["matched_rules"]
    assert "payment_failure" in result["matched_rules"]

# Unknown ticket test
def test_unknown_ticket_requires_manual_review():
    ticket = "Something strange is happening."

    result = classify_ticket(ticket)

    assert result["category"] == "Manual Review"
    assert result["priority"] == "Undetermined"
    assert result["department"] == "Human Review"
    assert result["matched_rules"] == []
    assert "No predefined classification rule matched" in result["explanation"]

# Successful classification explanation test
def test_classification_explanation_and_action():
    ticket = "My payment failed."

    result = classify_ticket(ticket)

    assert result["explanation"] == (
        "The ticket matched the predefined rule: payment_failure."
    )
    assert result["recommended_action"] == (
        "Recommend routing this ticket to Billing Support."
    )

# Manual review explanation and action
def test_manual_review_explanation_and_action():
    ticket = "Something strange is happening."

    result = classify_ticket(ticket)

    assert result["explanation"] == (
        "No predefined classification rule matched the ticket."
    )
    assert result["recommended_action"] == (
        "Escalate this ticket for human review."
    )

# Empty ticket test
def test_empty_ticket_raises_value_error():
    with pytest.raises(ValueError):
        classify_ticket("")

# Whitespace test
def test_whitespace_ticket_raises_value_error():
    with pytest.raises(ValueError):
        classify_ticket("   ")
    


