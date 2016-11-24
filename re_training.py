import re

A = 'Merge pull request #3558 in EA/ea-configuration from dev-raj-devportal-apps-reimagine to integration'

B = "hello"

C = 'Merge pull request #3558 in EA/ea-configuration from dev-raj-devportal-apps-reimagine to master'


m = re.match(r".*(?<! to integration)$", C)

print m.group(0)
