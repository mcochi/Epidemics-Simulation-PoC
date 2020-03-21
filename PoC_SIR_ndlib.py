# PoC NDLIB - Lybrary for epidemics/Social opinion spread simulation
#----------------------------------------------------------------------#

# Based on:https://colab.research.google.com/github/KDDComplexNetworkAnalysis/CNA_Tutorials/blob/master/NDlib.ipynb#scrollTo=pkwC_EnfbifD
# Day: 2020_03_21
# Version: 0.0

#-----------------------------------------------------------------------#

import ndlib
import networkx as nx
import ndlib.models.epidemics as ep
import json
import ndlib.models.ModelConfig as mc
from bokeh.io import output_notebook, show
from ndlib.viz.bokeh.DiffusionTrend import DiffusionTrend
from ndlib.viz.bokeh.DiffusionPrevalence import DiffusionPrevalence


# Graph Selection
""" As a first step we need to deine the network topology that will be used
 as playground to study diffusive phenomena """ 
g = nx.erdos_renyi_graph(763,0.1)

# Model Selection: In our case, SIR model
# Pueden encontrarse el resto de modelos en este enlace: https://ndlib.readthedocs.io/en/latest/reference/reference.html#epidemics
model = ep.SIRModel(g)

# Depends on the model, different parameters should be filled. Just to know
# the parameters, execute following code lines:
print(json.dumps(model.parameters, indent=2))
print(model.available_statuses)

# Configure model: ModelConfig allows to describe the initial condition of the simulation.
# It makes possible for instance, to specify the initial percentage of infected nodes in the network

cfg = mc.Configuration()
cfg.add_model_parameter('beta',0.01) #Infection Probability
cfg.add_model_parameter('gamma', 0.005) #Recovery Probability
cfg.add_model_parameter("percentage_infected", 0.05)
model.set_initial_status(cfg)

# Simulation Execution - Once described the network, the model and the initial conditions
# it is possible to perform the simulation. Ndlib models diffusive phenomena as discrete-time,
# agent-based processes: during every iteration all nodes are evaluated and their statuses
# are updated accordingly to the model rules.

iterations = model.iteration_bunch(200,node_status=True)
#print(iterations)

trends = model.build_trends(iterations)
#print(trends)


# Result Visualization
# Finaly, NDlib allows to inspect the behavior of the simulated model using standard plots
# such as the DiffusionTrend and DiffusionPrevalence ones


# Trend Diffusion Visualization
viz = DiffusionTrend(model, trends)
p = viz.plot(width=600, height=600)
show(p)

# Prevalence Plot
#viz2 = DiffusionPrevalence(model, trends)
#p2 = viz2.plot(width=400, height=400)
#show(p2)













