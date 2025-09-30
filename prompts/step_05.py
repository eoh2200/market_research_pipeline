step = {
    "step": "Step 5 - Indirect Cost of Cure/Delay (Value of 'Build-Immediately')",

    "goal": "Quantify the schedule value unlocked by your product.",

    "prompt":"""
        Role: Construction scheduling economist.
        Task: Compute the indirect cost avoided by eliminating cure/wait time.
        Do:

        From Step 2, extract typical wait duration until load application.

        Quantify at least three pathways of cost:

        Idle labor/remobilization (crew size x wage & burden x idle hours or extra trip).

        General Conditions/Overhead (per-day site overhead allocable to footing wait).

        Opportunity cost of timeline (daily carrying cost of capital or schedule-dependent revenue delay; show sensitivity: 0.5-1.5% monthly).

        Create a simple sensitivity table for 0.5x/1.0x/1.5x baseline assumptions.
        Output: A table: Component | Assumption | Formula | Result ($/sq.ft supported) | Source | Confidence.
        Quality checks: Cite wage/overhead norms (BLS + GC benchmarks). Keep each assumption traceable.
        """
}