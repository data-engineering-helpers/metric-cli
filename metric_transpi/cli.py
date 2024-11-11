import rich_click as click

from metric_transpi import dbt, tableau
from metric_transpi.tableau_cloud import list_metric, signin


@click.group()
def cli():
    """CLI entry point"""
    pass

@cli.command()
@click.argument('base_path', type=click.Path(exists=True))
def convert(base_path):
    """
    Convert a dbt metric YAML file (or recurisvely all dbt metrics' files) into a Tableau Cloud's metric definition payload (JSON)
    to stdout
    """
    metrics = dbt.from_yaml(path=base_path)    
    for m in metrics:
        print(tableau.to_pulse_payload(m))

@cli.command()
@click.argument("pat_name", envvar='TABLEAU_PAT_NAME')
@click.argument("pat_secret", envvar='TABLEAU_PAT_SECRET')
@click.option("--host", envvar='TABLEAU_HOST', prompt=True)
@click.option("--url-id", envvar='TABLEAU_SITE_URL_ID', prompt=True)
def authent(pat_name, pat_secret, host, url_id):
    """
    Get the session token from authentication with Tableau Cloud using your Personal Access Token (PAT)

    PAT_NAME is the name of the Personal Access Token in your account

    PAT_SECRET is the hexa-secret generated at the creation of the Personal Access Token in your account

    both variables could be specified by Envionement variables: TABLEAU_PAT_NAME, TABLEAU_PAT_SECRET
    """
    token, site_id = signin(
        host=host,
        site_url_id=url_id,
        pat_token_name=pat_name,
        pat_token_secret=pat_secret
    )
    click.echo(f"export TABLEAU_API_TOKEN={token}")
    click.echo(f"export TABLEAU_API_SITE_ID={site_id}")

@cli.command()
@click.argument("api_token", envvar='TABLEAU_API_TOKEN')
@click.option("--host", envvar='TABLEAU_HOST', prompt=True)
def list_metrics(api_token, host):
    """display all available metrics in Pulse

    Args:
        api_token (str): token provided by the authent command
    """
    click.echo(
        list_metric(
            host=f"https://{host}",
            api_token=api_token)
    )
