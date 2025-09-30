step = {
    "step": "Step 6 - Competitive Landscape & Substitutes",

    "goal": "Identify incumbent methods and close substitutes (e.g., precast footings, ground screws, helical piles).",

    "prompt":"""
        Role: Competitive intelligence analyst.
        Task: For {SEGMENT} in {GEO}, list incumbent concrete footing methods and substitutes.
        Do:

        Build a table: Competitor/Method | Product Type | Typical Use Cases | Installed Cost Basis | Key Advantages | Key Drawbacks | Distribution | Notable Proof (ESR, code approvals) | Sources.

        Include at least: cast-in-place footings, precast footing bases, helical piles, ground screws, diamond pier/other engineered systems.

        Where available, include ICC-ES/equivalent approvals & cite them.
        Output: The table + short narrative on where each wins/loses versus prefabricated footing.
        """
}