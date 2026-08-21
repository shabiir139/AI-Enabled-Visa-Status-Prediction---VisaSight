import sys

search = """
    try:
        query = supabase.table("visa_cases").select("*")

        if user_id:
            query = query.eq("user_id", user_id)

        # Pagination
        start = (page - 1) * per_page
        query = query.range(start, start + per_page - 1)
        query = query.order("created_at", desc=True)

        result = query.execute()

        # Get total count
        count_result = supabase.table("visa_cases").select("id", count="exact")
        if user_id:
            count_result = count_result.eq("user_id", user_id)
        count_data = count_result.execute()
        total = count_data.count if hasattr(count_data, 'count') else len(result.data)
"""

replace = """
    try:
        # ⚡ Bolt: Optimize by combining pagination query with total count
        # Replaces separate count_result query, cutting DB roundtrips in half (~50% latency reduction)
        query = supabase.table("visa_cases").select("*", count="exact")

        if user_id:
            query = query.eq("user_id", user_id)

        # Pagination
        start = (page - 1) * per_page
        query = query.range(start, start + per_page - 1)
        query = query.order("created_at", desc=True)

        result = query.execute()

        # Extract total count directly from the result
        total = result.count if hasattr(result, 'count') and result.count is not None else len(result.data)
"""
print("DIFF READY")
