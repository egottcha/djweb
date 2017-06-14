import pandas as pd
import json
import re

dataframe = pd.read_csv('packetData.csv', index_col='No.')

src_dst = dataframe[["Source", "Destination"]]
grouped_src_dst = src_dst.groupby(["Source", "Destination"]).size().reset_index()

unique_ips = pd.Index(grouped_src_dst["Source"]
                      .append(grouped_src_dst["Destination"])
                      .reset_index(drop=True).unique())

group_dict = {}
counter = 0
for ip in unique_ips:
    breakout_ip = re.match("^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$", ip)
    if breakout_ip:
        net_id = '.'.join(breakout_ip.group(1, 2, 3))
        if net_id not in group_dict:
            counter += 1
            group_dict[net_id] = counter
        else:
            pass

temp_links_list = list(
    grouped_src_dst.apply(lambda row: {"source": row["Source"], "target": row["Destination"], "value": row[0]},
                          axis=1))

links_list = []
for link in temp_links_list:
    record = {"value": link["value"], "source": unique_ips.get_loc(link["source"]),
              "target": unique_ips.get_loc(link["target"])}
    links_list.append(record)

nodes_list = []
for ip in unique_ips:
    breakout_ip = re.match("^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$", ip)
    if breakout_ip:
        net_id = '.'.join(breakout_ip.group(1, 2, 3))
        nodes_list.append({"name": ip, "group": group_dict.get(net_id)})

json_dump = json.dumps({"nodes": nodes_list, "links": links_list})

filename_out = '../../person/static/person/json/FDG.json'
json_out = open(filename_out, 'w')
json_out.write(json_dump)
json_out.close()
