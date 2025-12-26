def qa_agent(state):
    state["questions"] = {
        "Informational": [
            "What is GlowBoost Vitamin C Serum?",
            "What are its key benefits?",
            "Who can use this serum?"
        ],
        "Usage": [
            "How should GlowBoost be applied?",
            "Can it be used daily?",
            "Should sunscreen be applied after?"
        ],
        "Safety": [
            "Is it safe for sensitive skin?",
            "Does it cause irritation?",
            "Are there side effects?"
        ],
        "Purchase": [
            "What is the price?",
            "Is it worth the cost?",
            "How long does one bottle last?"
        ],
        "Comparison": [
            "How does it compare to other serums?",
            "Is it better than Product B?",
            "Which offers better value?"
        ]
    }
    return state
