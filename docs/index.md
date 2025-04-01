# Overview

## Purpose

Convert the **dbt metric** (YAML) into a **Tableau Pulse** payload (JSON)

Use the dbt source code as the truth to deploy metric on top of models.
It has several benefits :

 - light and easy to maintain because it has no infrastructure, 
 - can integrate to a lot of BI tools, decoupling metric definition from the serving
 - link the metric to the code of dbt, using the powerfull dbt lineage

## Commands
 
    Usage: metric-cli [OPTIONS] COMMAND [ARGS]...                                                                                                                               
                                                                                                                                                                             
    Manage relationship between Dbt metrics and Tableau Pulse's metric                                                                                                          
                                                                                                                                                                                
    ╭─ Options ─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
    │ --env     TEXT                                                                                                                                                            │
    │ --help          Show this message and exit.                                                                                                                               │
    ╰───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
    ╭─ Commands ────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
    │ del           Delete a metric in Pulse                                                                                                                                    │
    │ deploy        Deploy to Pulse all metrics found in the YAML file                                                                                                          │
    │ diff          Diff a metric found in the YAML file against the metric definition deployed in Pulse                                                                        │
    │ list          display all metrics currently deployed in Tableau Pulse                                                                                                     │
    ╰───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯