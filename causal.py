# Copyright 2023 Google LLC..
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import re
import causalimpact

def getCiObject(df, pre_period: list, post_period: list):
  return causalimpact.fit_causalimpact(df, pre_period, post_period)

def getCiSummary(impact) -> list:
  summary = causalimpact.summary(impact, output_format='summary')
  summary = re.sub('  +', '|', summary)
  return [r.split('|') for r in [r for r in summary.split('\n')]]

def getCiChart(impact, div="vis"):
  return causalimpact.plot(impact, static_plot=False, chart_width=800).to_html().replace("vis", div)

def getCiReport(impact) -> str:
  report = causalimpact.summary(impact, output_format='report')
  return report.replace('\n\n', '<br><br>')

def getValidation(df) -> list:
  df.corr(method='pearson', numeric_only=False)
  validation=str(df.describe())
  validation = re.sub('  +', '|', validation)
  return [r.split('|') for r in [r for r in validation.split('\n')]]
