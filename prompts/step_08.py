step = {
    "step": "Step 8 - Distributors & Potential Customers (with Market Shares)",

    "goal": "Identify top channels and major buyers, with share estimates.",

    "prompt":"""
        Role: Channel & account researcher.
        Task: For {SEGMENT} in {GEO}, list top 5-10 distributors and top potential customers (by purchasing influence), with estimated market shares.
        Do:

        Use public filings (10-K), distributor network pages, store counts, category focus, and independent reports.

        Estimate market share via explicit proxies: (category revenue, store penetration in {GEO}, web traffic in category, shipment mentions, installer partner density, or permit data adjacency). State the proxy and its math.

        Provide a table: Name | Type (Distributor / Customer) | URL | Est. Share (%) | Proxy & Method | Why relevant to {SEGMENT} | Sources | Confidence.
        Quality checks: Show at least two proxy methods for the top 3 entries to cross-check share.
        """
}