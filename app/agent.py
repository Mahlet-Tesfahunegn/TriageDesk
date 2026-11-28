from app.rules import RULES

def classify_ticket(ticket):
    if not ticket or not ticket.strip():
        raise ValueError ("Ticket description cannot be empty")
    
    ticket = ticket.lower()
    matched_rules = []

    # Find all matching rules
    for rule in RULES:
        for keyword in rule["keywords"]:
            if keyword in ticket:
                matched_rules.append(rule)
                break

    # Place the categoriesd of the matched rules in a set called matched_categories
    matched_categories = {
        rule["category"] for rule in matched_rules
    }


    if len(matched_categories) == 1:
        rule = matched_rules[0]

        return {
            "category": rule["category"],
            "priority": rule["priority"],
            "department": rule["department"],
            "matched_rules": [
                matched_rule["name"] for matched_rule in matched_rules
            ],
            "explanation": (
                f"The ticket matched the predefined rule: "
                f"{rule['name']}."
            ),
            "recommended_action": (
                f"Recommend routing this ticket to "
                f"{rule['department']}."
            ),
        }
                    
 # No category or multiple categories matched
    if not matched_rules:
        reason = "No predefined classification rule matched the ticket."
    else:
        reason = (
            "Matching rules from multiple ticket categories were detected."
        )

    return {
        "category": "Manual Review",
        "priority": "Undetermined",
        "department": "Human Review",
        "matched_rules": [
            matched_rule["name"] for matched_rule in matched_rules
        ],
        "explanation": reason,
        "recommended_action": (
            "Escalate this ticket for human review."
        ),
    }
