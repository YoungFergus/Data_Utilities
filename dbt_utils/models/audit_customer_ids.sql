{{
    config(
        materialized='table'
    )
}}

{# This model uses the dbt graph to create a list of all possible test models for the customer test "test_expect_relationship" to surface it for reporting and correcting. #}

{% if execute %}
    {%- set not_null_test_results = get_list_of_nodes('test_relationship_', 'test') %}

    {%- for result in not_null_test_results -%}

        {%- set test_table=adapter.get_relation(database=result.database,
                                                schema=result.schema,
                                                identifier=result.name) -%}
        {%- set table_exists=test_table is not none %}

        {%- if table_exists -%}
            {% set test_table_query %}
                select * from {{ test_table }}
            {%- endset -%}
            {%- set test_results = run_query(test_table_query) -%}
                {{ test_table_query }}
        {%- endif -%}

        { if not loop.last %}
        union all
        {% endif -%}

    {%- endfor -%}
{% endif %}