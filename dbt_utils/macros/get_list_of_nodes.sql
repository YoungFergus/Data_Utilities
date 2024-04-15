/*
This macro can be used to generate and obtain the list of nodes (models or tests) that uses a prefixed naming convention. This
macro typically pairs with a model that dynamically unions test results or models together.
The output is the json object for each node so that all of the properties can be accessed.

To see the ouput or troubleshoot, run the following:
dbt run-operation get_list_of_nodes --args '{"search_pattern": 'stg_', "node_type": 'model', "log_enabled":true}'
*/

{% macro get_list_of_nodes(search_pattern, node_type='model', log_enabled=false) %}


{%- set node_list = [] -%}
{% set depends_on_list=[] %}

{%- for node in graph.nodes.values() | selectattr("resource_type", "equalto", node_type) -%}
    {%- if node.name.startswith(search_pattern) -%}
        {%- do node_list.append(node) -%}
        {%- if log_enabled -%}
            {% do depends_on_list.append(node) %}
        {%- endif -%}
    {%- endif -%}
{%- endfor %}

{% if log_enabled %}

    {% set joined = depends_on_list | join ('\n') %}
    {{ log(joined, info=True) }}
    {% do return(joined) %}

{% endif %}

{{ return(node_list) }}

{% endmacro %}