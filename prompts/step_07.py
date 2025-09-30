step = {
    "step": "Step 7 - Populate TAM / SAM / SOM",

    "goal": "Fill the calc sheet with real numbers and ranges (low/base/high).",

    "prompt":"""
        Role: Quant analyst.
        Task: Using data from Steps 2-3-5 and formulas from Step 4, compute TAM/SAM/SOM in {BASE_YEAR} USD.
        Do:

        Provide low/base/high scenarios by adjusting the top 3 uncertain inputs (state them explicitly).

        Show all math; attach Assumptions Register entries for any imputed numbers.

        Output three tables: Inputs, Results (units & $), Scenario Drivers.
        Quality checks: Reconcile units (per project vs per sq.ft). Validate results against at least one external market benchmark (if available).
        """
}