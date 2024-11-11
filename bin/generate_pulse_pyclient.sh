#!/usr/bin/env bash

# From the openAPI specification in YAML to generate a Python Http based client specific for this API
# For more informations, check https://help.tableau.com/current/api/rest_api/en-us/REST/rest_api_concepts_versions.htm#per_resource_versioning

#curl https://eu-west-1a.online.tableau.com/services/specifications/openapi > pulse_openapi.yaml
openapi-generator generate -i <(curl "https://eu-west-1a.online.tableau.com/services/specifications/openapi") \
                            -g python -o ./ \
                            -c conf/openapi_generator_config.json \
                            --strict-spec false \
                            --ignore-file-override=conf/.openapi-generator-ignore
pip install -e .