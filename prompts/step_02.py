step = {
    "step": "Step 2 - Workflow & Traditional Cost Structure",

    "goal": "Document the as-is installation workflow and cost stack for concrete footings in the segment.",

    "prompt":"""
        Role: Construction means & methods analyst.
        Task: Describe the end-to-end workflow for traditional concrete footings used in {SEGMENT} within {GEO}.
        Do:

        Break the workflow into granular steps: locate utilities, layout, excavation, forms/sonotubes/rebar, inspection(s), pour, finish, cure/wait, set posts/columns, backfill, cleanup, remobilization.

        For each step, provide typical crew composition, productivity rates, equipment, and unit costs (materials, direct labor), citing RSMeans (if accessible), BLS wage data, Home Depot/Lowes SKU pricing, producers (ready-mix), and reputable trade sources.

        Identify the cure/wait time until load can be applied (e.g., post setting), referencing credible sources; describe indirect costs (schedule delay, idle crew or remobilization).

        Build a cost table per pier/footing and per linear foot, then convert to $/sq.ft of: (a) supported structure area (primary) and (b) footing footprint.

        Show all formulas and unit conversions.
        Output:

        A process flow (bulleted steps).

        A cost table with columns: Step | Qty/Units | Unit Cost | Extended Cost | Source | Notes.

        A normalization table showing $/sq.ft (supported area) and $/sq.ft (footing footprint) for {BASE_YEAR}, with CPI/PPI normalization math & sources.
        Quality checks: Provide >=2 price sources for concrete & materials; cross-check wage rates via BLS OES for {GEO}.
        """
}