from click.testing import CliRunner

from metric_transpi.cli import cli

def test_cli_deploy():

  runner = CliRunner()
  result = runner.invoke(cli, ['deploy', 'metric_transpi/tests/metrics_sales.yml'], input='metric_transpi/tests/test')
  print(result.output)

  assert "metric_transpi/tests/test.env" in result.output