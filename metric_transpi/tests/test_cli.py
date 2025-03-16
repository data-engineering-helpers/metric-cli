from click.testing import CliRunner

from metric_transpi.cli import cli

def test_cli_create():
  runner = CliRunner()
  result = runner.invoke(cli, ['create', 'metric_transpi/tests/metrics_sales.yml'], input='sandbox')
  print(result.output)

  assert "Conflict" in result.output
  #assert result.exit_code == 0