"""
Traceplot
=========

_thumb: .8, .8
"""
import arviz as az

az.style.use('arviz-darkgrid')

trace = az.utils.load_trace('data/centered_eight_trace.gzip')
az.traceplot(trace, varnames=('tau', 'theta__0', 'mu__0'))
