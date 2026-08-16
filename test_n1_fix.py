import re

content = """
@router.get("", response_model=PaginatedResponse)
async def list_visa_cases(
    page: int = 1,
    per_page: int = 10,
    authorization: Optional[str] = Header(None)
):
    \"\"\"List all visa cases for the current user.\"\"\"
    user_id = get_user_id_from_token(authorization)

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
print("Fixing...")
