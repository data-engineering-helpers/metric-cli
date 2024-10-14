<img src="./assets/logo.png" width="5%" height="5%">     Metric Transpiler
---

![badge](https://github.com/dktunited/metric-cli/actions/workflows/python-package.yml/badge.svg)

## Purpose :

Convert the **dbt metric** (YAML) into a **Tableau Pulse** payload (JSON)

Use the dbt source code as the truth to deploy metric on top of models.
It has several benefits :
 - light and easy to maintain because it has no infrastructure, 
 - can integrate to a lot of BI tools, decoupling metric definition from the serving
 - link the metric to the code of dbt, using the powerfull dbt lineage

## Features :

- [X] dbt metric to pulse Payload
- [X] CLI
- [ ] search recursively for all metrics YAML to compile
- [ ] parameterize to inject Tableau's resources (datasource, columns hash)
- [ ] JSON schema validator
- [ ] retrieve fields ID and datasource ID from Pulse API
- [ ] check for breaking change or consitency in Pulse's API evolution
- [ ] badge for metric deployed in Tableau 
![Static Badge](https://img.shields.io/badge/metric_sync-today-green?logo=tableau&style=flat)
- [ ] metricflow to pulse
- [ ] dbt metrics to LookML (Looker)
- [ ] Malloy for Databricks

 ## Contributing

```git
git clone
pip install -e .
pip install pytest
git checkout -b feat/my_feature_branch
```
do your stuff, then test
```
pytest
```
Push your work and create a Pull Request