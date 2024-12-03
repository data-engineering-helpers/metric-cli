

## How does it work ?

### 1. Convert YAML dbt metric into JSON Payload
``` mermaid
graph LR
  A[Metric-CLI] --> B{dbt metric YAML};
  B -->|convert| C[JSON Payload];
```

### 2. Create the new metric
``` mermaid
graph LR
  A[Metric-CLI] --> B{Tableau Pulse?};
  B -->|table name| C[Data Source endpoint];
  C --> D[IDs];
  D --> B;
  B ---->|JSON Payload| E[New Metric !];
```


##### Futur improvement

The format of a metric could be adapted to any input format