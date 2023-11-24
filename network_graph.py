import networkx as nx
from pyvis.network import Network
import pandas as pd

def network_func(physics,layout):
  
  network_net = Network(
                        height="600px", 
                        width="100%", 
                        bgcolor='#222222',
                        font_color="white",
                        directed=True,
                        layout=layout
                        )
  
  network_net.repulsion(
                        node_distance=420,
                        central_gravity=0.33,
                        spring_length=110,
                        spring_strength=0.10,
                        damping=0.95
                       )

  network_net.barnes_hut()
  network_data = pd.read_csv("graphdata.csv")

  sources = network_data['Source']
  targets = network_data['Target']
  weights = network_data['Weight']
  src_groups = network_data['Source_Group']
  trg_groups = network_data['Target_Group']

  edge_data = zip(
                  sources, 
                  targets, 
                  weights, 
                  src_groups, 
                  trg_groups
                  )

  for e in edge_data:
    src = e[0]
    dst = e[1]
    w = e[2]
    sg = e[3]
    tg = e[4]

    network_net.add_node(
                         n_id=src, 
                         label=src, 
                         title=src,
                         level=sg,
                         group=sg,
                         physics=physics
                        )
    network_net.add_node(
                         n_id=dst, 
                         label=dst, 
                         title=dst,
                         group=tg,
                         level=tg,
                         physics=physics
                        )
    network_net.add_edge(
                         source=src, 
                         to=dst, 
                         title= src + ' to ' + dst + ' symmetry: ' + str(w) + '%',
                         value=w,
                         physics=physics,
                         arrowStrikethrough=True
                        )

  neighbor_map = network_net.get_adj_list()

  for node in network_net.nodes:
    node["title"] += ' Neighbors: ' + ', '.join(neighbor_map[node["id"]])
    node["value"] = len(neighbor_map[node["id"]])
  if physics:
    network_net.show_buttons(
                             filter_=['physics']
                            )
  network_net.save_graph("front.html")
