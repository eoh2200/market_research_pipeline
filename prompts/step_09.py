step = {
    "step": "Step 9 - Beachhead Readiness & Risk Checklist",

    "goal": "Surface adoption hurdles and niche advantages.",

    "prompt":"""
        Role: Product-market fit diagnostician.
        Task: For {SEGMENT} in {GEO} with {END_USER} and {PURCHASER}, fill the checklist below.
        Checklist (fill Yes/No + notes + sources):

        Code acceptance path identified (ICC-ES/PE stamp/alt materials approval).

        Frost depth & soil class implications handled.

        Inspection sequence compatible without extra visits.

        Crew learning curve minimal (<=1 job).

        Tooling/equipment changes negligible.

        Weather seasonality advantage (cold/hot/wet conditions).

        Clear value proof (time saved quantified from Step 5).

        Channel access to {PURCHASER} is direct (distributors present).

        Obvious lighthouse customers available in {GEO}.
        Output: Completed checklist table + 5-10 bullet "go/no-go" insights.
        """
}