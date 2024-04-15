{#
Returns whether the current run is a deployment where custom database/schema names should be used verbatim.
This can be overriden by specifying an 'is_deployment' bool variable.
#}
{% macro is_deployment() %}

    {{ return(var('is_deployment', target.name in var('deployment_target_names'))) }}

{% endmacro %}