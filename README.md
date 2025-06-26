<img src="./assets/logo.png" width="3%" height="3%">     metric-cli
---

![badge](https://github.com/dktunited/metric-cli/actions/workflows/python-package.yml/badge.svg)

## Purpose :

Deploy **dbt metrics** (YAML) into a **Tableau Pulse**'s MetricDefinition

Use the dbt source code as the truth to deploy metric on top of dbt models.
It has several benefits :
 - light and easy to maintain because it has no additional infrastructure, 
 - can integrate to a lot of BI tools, decoupling metric definition from the serving
 - define Tableau Pulse' metrics as code, leveraged by the powerfull dbt lineage

[Read the doc](https://data-engineering-helpers.github.io/metric-cli/)

## Use it

Create a Personal Access Token in Tableau Pulse : [doc](https://help.tableau.com/current/server/fr-fr/security_personal_access_tokens.htm#cr%C3%A9er-des-jetons-d%E2%80%99acc%C3%A8s-personnels)

Add a new environment file (```.env``` extansion) with the following environment variables (find an [example.env here](example.env))


    TABLEAU_HOST=..
    TABLEAU_SITE_URL_ID=..
    TABLEAU_PAT_NAME=..
    TABLEAU_PAT_SECRET=..

Then install the cli

    pip install metric-cli
    metric-cli --env example list

## Features

- [X] Translate dbt metric into pulse Payload
- [X] CLI managing authent with environment variables
- [X] Generate [Python client](https://help.tableau.com/current/api/rest_api/en-us/REST/rest_api_concepts_versions.htm#per_resource_versioning) for Pulse API ([tableau openapi url](https://eu-west-1a.online.tableau.com/services/specifications/openapi))
- [X] doc with [Mkdocs](https://squidfunk.github.io/mkdocs-material/publishing-your-site/) on Githup pages
- [X] JSON schema validator [dbt manifest](https://schemas.getdbt.com/dbt/manifest/v9/index.html#metrics_additionalProperties_time_grains)
- [x] list all deployed MetricDefinition in Pulse
- [x] deploy metric instead of create or update : should looks more like terraform
- [x] diff local dbt metric vs Tableau's state
- [x] delete a Tableau MetricDefinition
- [ ] retrieve fields ID and datasource ID from Pulse API
- [ ] read dbt manifest.json and match model FQN with Tableau Pulse datasource to establish automatic relationship
- [ ] import a Tableau Pulse' metric into a dbt metric (YAML)
- [ ] search recursively for all metrics YAML to compile
- [ ] check for breaking change or consitency in Pulse's API evolution
- [ ] badge for metric deployed in Tableau 
![Static Badge](https://img.shields.io/badge/metric_sync-today-green?logo=tableau&style=flat)
- [ ] other metric format : metricflow, LookML (Looker), CubeJS

 ## Contributing

```git
git clone
pip install -e .
pip install dev_requirements.txt
git checkout -b feat/my_feature_branch
```
do your stuff, then run tests
```
pytest
```
Push your work and create a Pull Request
