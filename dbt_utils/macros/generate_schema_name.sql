{#
Override the built-in generate_schema_name macro so custom schemas are used verbatim for deployment targets,
and custom database names are incorporated into the schema name for non-deployment targets.

Some examples:

    For a deployment target with target database 'analytics' and target schema 'misc':
        - Models with the custom schema 'core' would go into the schema 'analytics.core'
        - Models with the custom database 'foo' and custom schema 'bar' would go into the schema 'foo.bar'
        - Models without a custom database or schema would go into the schema 'analytics.misc'
        
    For a non-deployment target with target database 'analytics_dev' and target schema 'alice':
        - Models with the custom schema 'core' would go into the schema 'analytics_dev.alice_core'
        - Models with the custom database 'foo' and custom schema 'bar' would go into the schema 'analytics_dev.alice_foo_bar'
        
#}
{% macro generate_schema_name(custom_schema_name, node) %}

    {% set default_schema = target.schema %}

    {% if is_deployment() %}

        {% if custom_schema_name is not none %}
            {{ return(custom_schema_name | trim) }}
        {% else %}
            {{ return(default_schema) }}
        {% endif %}
    
    {% else %}

        {% set generated_schema_name = default_schema %}

        {% if node is not non and node.config is not none and node.config.database is not none and node.config.database != target.database %}
            {% set generated_schema_name = generated_schema_name ~ '_' ~ node.config.database %}
        {% endif %}

        {% if custom_schema_name is not none %}
            {% set generated_schema_name = generated_schema_name ~ '_' ~ (custom_schema_name | trim) %}
        {% endif %}

        {{ return(generated_schema_name) }}
    
    {% endif %}

{% endmacro %}