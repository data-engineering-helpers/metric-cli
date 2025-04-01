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
- [ ] import a Tableau Pulse' metric into a dbt metric (YAML)
- [ ] search recursively for all metrics YAML to compile
- [ ] parameterize to inject Tableau's resources (datasource, columns hash)
- [ ] retrieve fields ID and datasource ID from Pulse API
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
