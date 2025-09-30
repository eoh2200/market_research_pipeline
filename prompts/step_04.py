step = {
    "step": "Step 4 - TAM / SAM / SOM Framework (Definitions & Formulas)",

    "goal": "Lock clear formulas tailored to a footing-replacement product.",

    "prompt":"""
        Role: Go-to-market quant modeler.
        Task: Define TAM/SAM/SOM for a footing replacement product.
        Definitions:

        TAM (units): Total annual instances in {SEGMENT} where footings are installed in {GEO}.

        TAM ($): TAM (units) x traditional footing cost ($/sq.ft supported) x avg supported sq.ft per instance.

        SAM: Subset after applying {END_USER}/{PURCHASER} channels, relevant project sizes, and code constraints.

        SOM: Share achievable in 3-5 years given channel capacity and adoption barriers; justify % via analogs (e.g., ground screws/helical piles adoption).
        Do:

        Propose formulas and list the exact inputs needed (link to Step 2 and Step 3 tables).

        Create a calculation sheet with input placeholders and example math using midpoints; no new data, just structure.
        Output: A formulas section + a blank calculation table to be populated in Step 7.
        """
}