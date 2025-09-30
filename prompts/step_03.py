step = {
    "step": "Step 3 - Production Volumes & Activity Drivers",

    "goal": "Size how much of the segment happens annually in the chosen geography.",

    "prompt":"""
        Role: Market sizing analyst.
        Task: Estimate annual activity volume for {SEGMENT} in {GEO}.
        Do:

        Identify the right counting unit (projects, square feet built, number of piers, housing starts, remodeling permits, etc.).

        Pull counts from U.S. Census (e.g., Building Permits Survey, New Residential Construction), ACS, BEA, BLS, Dodge Construction Network (if public), NAHB, and relevant trade associations.

        If {GEO} is regional/state/metro, use Census/ACS regional tables or state permit data.

        Triangulate with home improvement datasets (e.g., NAHB remodeling indices), and retailer category insights if available.

        Create a Volume Table: Metric | Value | Unit | Geography | Year | Source | Notes | Confidence.
        Output: Volume Table + a paragraph explaining the triangulation and any gaps.
        Quality checks: At least two independent public sources. Flag any discrepancies >20% and choose a consensus value with rationale.
        """
}