
RULES = [
    {
        "name": "widespread_service_outage",
        "keywords": [
            "entire website is down",
            "website is unavailable for everyone",
            "all customers cannot access",
            "platform is down",
            "service is unavailable for everyone",
            "system-wide outage",
        ],
        "category": "Service Outages",
        "priority": "Critical",
        "department": "Technical Support",
    },
    {
        "name": "payment_failure",
        "keywords": [
            "payment failed",
            "payment was declined",
            "charged twice",
            "incorrect charge",
            "payment deducted but order not confirmed",
            "money was deducted but order was not confirmed",
            "refund has not arrived",
            "i have not received my refund",
            "refund has not been processed",
            "waiting for my refund",

        ],
        "category": "Payment Issues",
        "priority": "High",
        "department": "Billing Support",
    },
    {
        "name": "account_access",
        "keywords": [
            "cannot log in",
            "can't log in",
            "unable to log in",
            "cannot access my account",
            "forgot my password",
            "password reset is not working",
            "account is locked",
        ],
        "category": "Account Access",
        "priority": "Medium",
        "department": "Account Support",
    },
    {
        "name": "technical_issue",
        "keywords": [
            "page is not loading",
            "website keeps crashing",
            "button is not working",
            "application is freezing",
            "feature is not working",
            "error message appears",
            "upload is failing",
        ],
        "category": "Technical Issues",
        "priority": "Medium",
        "department": "Technical Support",
    },
    {
        "name": "general_inquiry",
        "keywords": [
            # Product inquiries
            "what products do you offer",
            "tell me about this product",
            "product information",

            # Service inquiries
            "what services do you provide",
            "how does your service work",
            "service information",

            # Pricing inquiries
            "what are your prices",
            "how much does this cost",
            "pricing information",

            # Policy inquiries
            "what is your refund policy",
            "what is your return policy",
            "company policy",
            "terms and conditions",

            # Payment information inquiries
            "what payment methods do you accept",
            "which payment methods are available",
            "what are your payment options",
        ],
        "category": "General Inquiries",
        "priority": "Medium",
        "department": "General Support",
    },
]

