#### 1. datasource_id is hardcoded in the YAML
The current design defines relationship between dbt metric YAML file and Tableau's metric definition. 
In order to use it, you must set the `datasource_id` field of setuped in Tableau Pulse corresponding to the dbt model

#### 2. Metric of metric is not currently implemented
For example, derived metrics like conversion rate (count orders / count session) is not possible yet, but it is in high priority

#### 3. Changing aggregation method leads to exception
For an existing metric, if you have made a mistake specifying the wrong aggregation method (for example Sum instead of Count) and you want
to fix it, the `deploy` command will fail with a UniquenessViolationExecption.
It is because the Tableau Pulse REST API does not allow to update the aggregation method, so we need to delete the metric which is already deployed
before redo.