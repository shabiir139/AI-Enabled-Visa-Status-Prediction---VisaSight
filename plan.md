1. **Optimize Supabase Pagination Query in `backend/app/api/cases.py`**
   - The current implementation for `list_visa_cases` executes two separate database queries: one to fetch the paginated data and another to count the total rows.
   - This causes unnecessary database round-trips (N+1 query problem).
   - I will optimize this by appending `count='exact'` to the primary `select('*')` query using `replace_with_git_merge_diff`.
   - The merge diff will be:
     SEARCH
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
     REPLACE
        # ⚡ Bolt Optimization: Use count='exact' in the primary query to fetch data and total count in a single round-trip
        query = supabase.table("visa_cases").select("*", count="exact")

        if user_id:
            query = query.eq("user_id", user_id)

        # Pagination
        start = (page - 1) * per_page
        query = query.range(start, start + per_page - 1)
        query = query.order("created_at", desc=True)

        result = query.execute()

        total = result.count if hasattr(result, 'count') and result.count is not None else len(result.data)

2. **Optimize Supabase Pagination Query in `backend/app/api/rules.py`**
   - The current implementation for `list_visa_rules` executes two separate database queries.
   - I will optimize this similarly by appending `count='exact'` to the primary `select('*')` query using `replace_with_git_merge_diff`.
   - The merge diff will be:
     SEARCH
        query = supabase.table("visa_rules").select("*").eq("is_active", True)

        if visa_type:
            query = query.eq("visa_type", visa_type)
        if category:
            query = query.eq("rule_category", category)

        # Pagination
        start = (page - 1) * per_page
        query = query.range(start, start + per_page - 1)
        query = query.order("effective_date", desc=True)

        result = query.execute()

        rules = [
            VisaRuleResponse(
                id=row["id"],
                country=row.get("country", "USA"),
                visa_type=VisaType(row["visa_type"]),
                rule_category=RuleCategory(row["rule_category"]),
                title=row["title"],
                description=row["description"],
                effective_date=row["effective_date"],
                source_url=row.get("source_url"),
                created_at=row["created_at"],
            )
            for row in result.data
        ]

        # Get total count
        count_query = supabase.table("visa_rules").select("id", count="exact").eq("is_active", True)
        if visa_type:
            count_query = count_query.eq("visa_type", visa_type)
        if category:
            count_query = count_query.eq("rule_category", category)
        count_result = count_query.execute()
        total = count_result.count if hasattr(count_result, 'count') and count_result.count else len(result.data)
     REPLACE
        # ⚡ Bolt Optimization: Use count='exact' in the primary query to fetch data and total count in a single round-trip
        query = supabase.table("visa_rules").select("*", count="exact").eq("is_active", True)

        if visa_type:
            query = query.eq("visa_type", visa_type)
        if category:
            query = query.eq("rule_category", category)

        # Pagination
        start = (page - 1) * per_page
        query = query.range(start, start + per_page - 1)
        query = query.order("effective_date", desc=True)

        result = query.execute()

        rules = [
            VisaRuleResponse(
                id=row["id"],
                country=row.get("country", "USA"),
                visa_type=VisaType(row["visa_type"]),
                rule_category=RuleCategory(row["rule_category"]),
                title=row["title"],
                description=row["description"],
                effective_date=row["effective_date"],
                source_url=row.get("source_url"),
                created_at=row["created_at"],
            )
            for row in result.data
        ]

        total = result.count if hasattr(result, 'count') and result.count is not None else len(result.data)

3. **Install Dependencies**
   - I will use `run_in_bash_session` to install test dependencies in `backend`: `python3 -m pip install -r backend/requirements.txt pytest pytest-asyncio httpx --break-system-packages`
   - I will use `python3 -c "import pytest"` to verify the installation.

4. **Verify Changes and Run Tests**
   - I will run backend tests: `cd backend && python3 -m pytest`
   - I will use a simple bash check like `cd backend && python3 -c "from main import app; print('Backend imports successfully')"` to quickly verify there are no syntax errors.
   - I will run frontend lint: `cd frontend && npm run lint`

5. **Complete Pre-commit Steps**
   - Complete pre-commit steps to ensure proper testing, verification, review, and reflection are done.

6. **Submit PR**
   - I will use `submit` tool to create the PR.
   - `branch_name`: "bolt/optimize-supabase-pagination"
   - `title`: "⚡ Bolt: [performance improvement]"
   - `commit_message`: "⚡ Bolt: Optimize Supabase Pagination Queries"
   - `description`: "💡 What: Optimized pagination queries in cases and rules endpoints by using count='exact' on the primary query instead of making a separate count query.\n🎯 Why: The previous implementation suffered from an N+1 query pattern where fetching a paginated list required two separate round-trips to the database.\n📊 Impact: Reduces database round-trips by 50% on list endpoints, significantly improving API response times and reducing database load.\n🔬 Measurement: Monitor API latency on `/api/cases` and `/api/rules` endpoints. The latency should decrease by approximately the duration of one database round-trip."
