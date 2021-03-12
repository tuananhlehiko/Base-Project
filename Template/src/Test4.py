from test_junkie.runner import Runner
from src.Other.DocumentationSuite import DocuamentationSuite
from src.Other.NavigationSuite import NavigationSuite
runner = Runner(suites=[DocuamentationSuite, NavigationSuite])
runner.run(test_multithreading_limit=6, suite_multithreading_limit=2)