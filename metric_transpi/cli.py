import json
import rich_click as click
from dotenv import load_dotenv
import os

from metric_transpi import dbt
from metric_transpi.tableau_cloud import create_metric, list_metric, signin


@click.group()
@click.option("--env", prompt=True, default='')
@click.pass_context
def cli(ctx, env):
    """CLI entry point"""
    click.echo(f'Loading {env}.env file')
    load_dotenv(f"{env}.env")  
    api_token, site_id = signin(
        host=os.getenv('TABLEAU_HOST'),
        site_url_id=os.getenv('TABLEAU_SITE_URL_ID'),
        pat_token_name=os.getenv('TABLEAU_PAT_NAME'),
        pat_token_secret=os.getenv('TABLEAU_PAT_SECRET')
    )
    ctx.obj = {
        'api_token': api_token,
        'site_id': site_id,
        'host': os.getenv('TABLEAU_HOST')
    }

@cli.command()
@click.pass_obj
def list(creds):
    """display all metrics currently deployed in Tableau Pulse

    Args:
        api_token (str): token provided by the authent command
    """
    
    json_result = json.loads(
        s=list_metric(
            host=f"https://{creds['host']}",
            api_token=creds['api_token'])
    )
    
    json_pretty = json.dumps(json_result, indent=4) 
    click.echo(
        json_pretty
    )

@cli.command()
@click.pass_obj
@click.argument('yaml_path', type=click.Path(exists=True))
def create(creds, yaml_path):
    """create into Pulse all metrics found in the YAML file
    
    Args:
        api_token (str): token provided by the authent command
    """
    
    metrics=dbt.from_yaml(yaml_path)
    responses = []
    for m in metrics:
        response = create_metric(creds['host'], creds['api_token'], m)
        responses.append(response)
    
    json_pretty = json.dumps(responses, indent=4) 
    click.echo(
        json_pretty
    )

