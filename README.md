Metric Transpiler
---

## Purpose :

Convert the **dbt metric** (YAML) into a **Tableau Pulse** payload (JSON)

Use the dbt source code as the truth to deploy metric on top of models.
It has several benefits :
 - light and easy to maintain because it has no infrastructure, 
 - can integrate to a lot of BI tools, decoupling metric definition from the serving
 - link the metric to the code of dbt, using the powerfull dbt lineage

## Features :

- [ ] dbt metric to pulse
- [ ] JSON schema validator
- [ ] metricflow to pulse
- [ ] input metric to LookML (Looker)

 ## Contributing

```git
git clone
pip install -e .
git checkout -b feat/my_feature_branch
```
