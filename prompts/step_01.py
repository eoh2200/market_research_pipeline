step = {
    "step": "Step 1 - Segment & Code Mapping (NAICS/CSI/IRC/IBC)",

    "goal": "Precisely map the segment to industry codes, relevant building codes, inspection touchpoints, and structural load regimes.",

    "prompt":"""
        Role: Construction code & classification researcher.
        Task: Map {SEGMENT} to NAICS, CSI MasterFormat/UniFormat elements, and identify the governing codes/standards for footings (e.g., IRC, IBC, ACI, state/local amendments).
        Do:

        Use web search. For each mapping or code requirement, cite source and quote key language (<=25 words).

        Identify minimum depth, frost line, soil bearing references, lateral/ uplift considerations, typical inspection points.

        List standard footing geometries used in {SEGMENT} (e.g., spread footings, pier/column footings, ground screws/helical piles if common substitutes), with typical dimensions and loads.

        Produce a table: Item | Code/Standard | Clause/Section | Requirement Summary | Why it matters | Source (URL, date).
        Quality checks: prefer ICC, ACI, state code sites, DOT manuals; avoid blogs unless corroborated.
        Output: The table + a short paragraph of implications for prefabricated footings.
        """
}