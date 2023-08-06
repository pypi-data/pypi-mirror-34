{%- set LEVELS = {
    "CRITICAL": 50,
    "ERROR": 40,
    "WARNING": 30,
    "INFO": 20,
    "DEBUG": 10,
    "NOTSET": 0} -%}


{% macro log(msg, level) -%}
    {% if LEVELS[level] > LEVELS[(LOGGING_LEVEL or "NOTSET")] -%}
        RAISE NOTICE '{{level}}: %', $LOG${{msg}}$LOG$;
    {%- endif %}
{%- endmacro %}


{% macro CRITICAL(msg) -%}{{ log(msg, "CRITICAL") }}{%- endmacro %}


{% macro ERROR(msg) -%}
{{ log(msg, "ERROR") }}
{%- endmacro %}


{% macro WARNING(msg) -%}
{{ log(msg, "WARNING") }}
{%- endmacro %}


{% macro INFO(msg) -%}{{ log(msg, "INFO") }}{%- endmacro %}


{% macro DEBUG(msg) -%}
{{ log(msg, "DEBUG") }}
{%- endmacro %}

-- asdasd
