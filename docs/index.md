# Welcome to Metric CLI

## Purpose

Convert the **dbt metric** (YAML) into a **Tableau Pulse** payload (JSON)

Use the dbt source code as the truth to deploy metric on top of models.
It has several benefits :

 - light and easy to maintain because it has no infrastructure, 
 - can integrate to a lot of BI tools, decoupling metric definition from the serving
 - link the metric to the code of dbt, using the powerfull dbt lineage

## Commands
                                                                                                                                                                      
    Usage: metric-cli [OPTIONS] COMMAND [ARGS]...                                                                                                                                 
                                                                                                                                                                                
    ╭─ Options ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
    │ --help      Show this message and exit.                                                                                                                                     │
    ╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
    ╭─ Commands ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
    │ authent         Get the session token from authentication with Tableau Cloud using your Personal Access Token (PAT)                                                         │
    │ convert         Convert a dbt metric YAML file (or recurisvely all dbt metrics' files) into a Tableau Cloud's metric definition payload (JSON) to stdout                    │
    │ list-metrics                                                                                                                                                                │
    ╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
