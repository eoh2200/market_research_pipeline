step = {
    "step": "Step 0 - Scope & Variables",

    "goal": "Lock the scope, define key variables, and create an empty Assumptions Register and Source Log.",

    "prompt":"""
        Role: You are a meticulous construction-market analyst.
        Task: Initialize research for {SEGMENT} in {GEO}.
        Inputs:

        END_USER: {END_USER}

        PURCHASER: {PURCHASER}

        BASE_YEAR: {BASE_YEAR} USD
        Do:

        Echo scope & definitions.

        Create an Assumptions Register (empty table with columns: Metric | Placeholder | Rationale | Will be resolved by Step # | Confidence).

        Create a Source Log (empty table: Source | URL | Publisher | Pub Date | What we used | Relevance | Notes).
        Output format: Markdown with two empty tables exactly as specified. No external research yet.
        """
}