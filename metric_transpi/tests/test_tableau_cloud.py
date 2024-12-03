
import json
from unittest.mock import MagicMock, call, patch

import requests
from metric_transpi.tableau_cloud import signin

@patch("requests.api")
def test_sigin(mock_requests):
    # Given
    host = "tableau-api-host.toto"
    pat_name = "papat"
    pat_secret = "password"
    site_url_id = "tableau"
    response = MagicMock()
    response.content = json.dumps(
        { 
            "credentials": { "site": {
                "id": "site_id_OK",
                "contentUrl": "site_url_OK"
                },
                "token": "OK"
            }
    })
    requests.api.post = MagicMock(return_value=response)

    
    # When
    token, site_id = signin(
        host=host, 
        site_url_id=site_url_id,
        pat_token_name=pat_name, 
        pat_token_secret=pat_secret
    )

    # Then
    assert requests.api.post.call_args == call(
        'https://tableau-api-host.toto/api/3.4/auth/signin', 
        headers={'accept': 'application/json', 'content-type': 'application/json'}, 
        json={'credentials': {'personalAccessTokenName': 'papat', 'personalAccessTokenSecret': 'password', 'site': {'contentUrl': 'tableau'}}})
    assert token == "OK"
    assert site_id == "site_id_OK"
