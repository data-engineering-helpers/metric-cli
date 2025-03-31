import json
import rich_click as click
from dotenv import load_dotenv
import os
from metric_transpi import dbt, translate
from metric_transpi import tableau_cloud


@click.group()
@click.option("--env", prompt=True, default='')
@click.pass_context
def cli(ctx, env):
    """Manage relationship between Dbt metrics and Tableau Pulse's metric"""
    click.echo(f'Loading {env}.env file')
    load_dotenv(f"{env}.env")  
    api_token, site_id = tableau_cloud.signin(
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
    
    json_result = [d.to_dict() for d in tableau_cloud.list_metric(
            host=f"https://{creds['host']}",
            api_token=creds['api_token']
    )]
    
    json_pretty = json.dumps(json_result, indent=4) 
    click.echo(
        json_pretty
    )

@cli.command()
@click.pass_obj
@click.argument('yaml_path', type=click.Path(exists=True))
def deploy(creds, yaml_path):
    """Deploy to Pulse all metrics found in the YAML file

    Args:
        api_token (str): token provided by the authent command
        yaml_path (path): 
    """
    
    local_metrics=dbt.from_yaml(yaml_path)
    remote_definitions=tableau_cloud.list_metric(creds['host'], creds['api_token'])

    updated_metrics = []
    for m in local_metrics:
        local_definition = translate.to_pulse(m)
        remote_m = tableau_cloud.match_definition(remote_definitions, local_definition)
        if remote_m is None:
            click.echo(f"The metric {m.name} does not exist. Trying to create it...")
            response = tableau_cloud.create_metric(creds['host'], creds['api_token'], local_definition)
        else:
            click.echo(f"The metric {m.name} already exists. Trying to update it...")
            if local_definition.specification.basic_specification.measure.var_field == remote_m.specification.basic_specification.measure.var_field \
            and remote_m.specification.basic_specification.measure.aggregation != local_definition.specification.basic_specification.measure.aggregation:
                raise tableau_cloud.UniquenessViolation(status=409, 
                                    reason="Uniqueness violation : metric definition using the same fields but with different aggreation methods",
                                    body=f"hint : Delete the metric definition before deploying it\ndetails : local='{local_definition.metadata.name}'.{local_definition.specification.basic_specification.measure.aggregation}({local_definition.specification.basic_specification.measure.var_field}) remote='{remote_m.metadata.name}'.{remote_m.specification.basic_specification.measure.aggregation}({remote_m.specification.basic_specification.measure.var_field})")
        
            response = tableau_cloud.update_metric(creds['host'], 
                                                    creds['api_token'], 
                                                    local_definition, 
                                                    remote_m.metadata.id)
        updated_metrics.append(response)
    json_result = [m.to_dict() for m in updated_metrics]
    json_pretty = json.dumps(json_result, indent=4) 
    click.echo(
        json_pretty
    )


@cli.command()
@click.pass_obj
@click.argument('yaml_path', type=click.Path(exists=True))
def diff(creds, yaml_path):
    """Diff a metric found in the YAML file against the metric definition deployed in Pulse

    Args:
        yaml_path (path): the file defining the dbt metric(s) to compare with Pulse' state
    """
    local_metrics=dbt.from_yaml(yaml_path)
    remote_definitions=tableau_cloud.list_metric(creds['host'], creds['api_token'])

    conflict = False
    for local_m in local_metrics:
        for remote_d in remote_definitions:
            remote_m = translate.to_dbt(remote_d)
            if remote_m.name == local_m.name or (remote_m.expression == local_m.expression and remote_m.calculation_method != local_m.calculation_method):
                diff = dbt.diff(local_m, remote_m)
                click.echo("Found differences between local and remote")
                click.echo(
                    f"  {local_m.name} : \n\t{diff.pretty()}"
                )
                conflict = True
                click.echo(f"More details using the definition_id : {remote_d.metadata.id}")
    if not conflict:
        click.echo(f"Local metrics not deployed in Pulse : {[m.name for m in local_metrics]}")


@cli.command(name="del")
@click.pass_obj
@click.argument('metric_name', type=click.STRING)
def delete(creds, metric_name: str):
    """Delete a metric in Pulse

    Args:
        metric_name : the name of the metric in pulse. It will remove the first matching
    """
    remote_definitions = tableau_cloud.list_metric(creds['host'], creds['api_token'])

    for remote_d in remote_definitions:
        if remote_d.metadata.name == metric_name:
            to_remove = click.confirm(f"Found existing definition in Pulse with id='{remote_d.metadata.id}' \nWould like to proceed the deletion ?", abort=False)
            if to_remove:
                tableau_cloud.delete_metric(host=creds["host"], api_token=creds["api_token"], definition_id=remote_d.metadata.id)
                click.echo(f"Deletion of '{metric_name}' successfull")
            else:
                click.echo("Abort the mission")    
            return
    
    click.echo(f"'{metric_name}' not found")