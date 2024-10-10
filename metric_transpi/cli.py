from pydoc import cli
import click

from metric_transpi import dbt, tableau


@click.command()
@click.argument('base_path', type=click.Path(exists=True))
def convert(base_path):
    
    metrics = dbt.from_yaml(base_path)
    for m in metrics:
        print(tableau.to_pulse_payload(m))
