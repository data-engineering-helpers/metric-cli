

## How does it work ?

### 1. Functional : deploy metrics to Tableau Pulse

``` mermaid
flowchart TD
    yaml@{ shape: docs, label: "dbt metric.yml" }
    subgraph metric-cli
        deploy
        del
        diff
        list
    end 
    Tableau_Pulse
    subgraph Tableau_Pulse
        list_definition
        create_definition
        update_definition
        delete_definition
        definition1@{ shape: notch-rect, label: "Metric Definition" }
    end
    yaml e1@==read==>deploy
    deploy-->match@{ shape: diamond, label: "match 
    metric & definition" }
    match--if not exists-->create_definition
    match--if exists-->update_definition
    match<--get current-->list_definition
    yaml--read-->diff
    del-->delete_definition
    list-->list_definition
    diff-->list_definition
    e1@{ animate: true }

    list_definition-->definition1
    delete_definition-->definition1
    update_definition-->definition1
    create_definition-->definition1

```

### 2. Technical design : convert dbt metrics (YAML) into Pulse MetricDefinition

```mermaid
flowchart TD
    yaml@{ shape: docs, label: "metric.yml" }
    subgraph metric_transpi
        cli.py
        dbt@{label: "dbt.from_yaml()"}
        dbt.Metric
        translate@{label: "translate.to_pulse()"}
    end 
    subgraph openapi_pulse_client
        MetricDefinition
        create_metric
        update_metric
    end
    cli.py-->dbt-->yaml-->dbt.Metric-->translate-->MetricDefinition
    MetricDefinition-->create_metric
    MetricDefinition-->update_metric
```

##### Futur improvement

The format of a metric could be adapted to any metric input format, for example LookML or CubeJS