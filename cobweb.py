import json
import yaml
import datetime
import argparse
import os
import sys
from pyvis.network import Network

def init_argparse():
    parser = argparse.ArgumentParser(
        usage="%(prog)s --domain example.com --file subdomains2ips.txt",
        description="Generate Network Graph For Sudomy."
    )
    parser.add_argument('--domain', type=str)
    parser.add_argument('--file', type=str, help="subdomains2ips.txt")
    return parser

parser = init_argparse()
args = parser.parse_args()

if args.file is None or args.domain is None:
    parser.print_help()
    exit(0)

main_domain = args.domain
subdomains2ips = args.file

# 读取文件内容
with open(subdomains2ips, "r") as file:
    content = file.readlines()

data = {}

# 解析每一行的域名和 IP 地址
for line in content:
    domain, ip = line.strip().split(' [')  # 按空格分割域名和 IP 地址
    ip = ip[:-1]
    # 检查 IP 地址是否已经存在于字典中
    if ip in data:
        data[ip].append(domain)
    else:
        data[ip] = [domain]

# 将数据转换为 YAML 格式
yaml_output = yaml.dump(data)
print(yaml_output)

net =  Network(height="2000px", width="100%", heading='<script>document.getElementsByTagName("center")[0].remove()</script>', bgcolor="#2d2e2e", font_color="white", select_menu=True, filter_menu=True)
net.force_atlas_2based(gravity=-80, damping=2.0, overlap=5.0)
net.toggle_physics(True)

try:
    domain_data = yaml.safe_load(yaml_output)
except:
    print("ERROR: File Is Not In Valid")
    exit(-1)

net.add_node(main_domain, color="#162347", label=main_domain, group=main_domain, labelHighlightBold=True)

for ip in domain_data:
    net.add_node(ip,label=ip, color="#bf281d", group=ip, physics=True, labelHighlightBold=True)
    net.add_edge(ip,main_domain,title=main_domain, arrowStrikethrough=True , width=3)

    for domain in domain_data.get(ip):
        net.add_node(domain, label=domain, title=domain, color="#828282", physics=True, group=domain, labelHighlightBold=True)
        net.add_edge(domain, ip, title=ip)

report_path = os.path.dirname(sys.argv[0])
print(report_path)
d = datetime.date.today()
date_now = '{}-{}-{}'.format(d.strftime('%m'),d.strftime('%d'), d.strftime('%Y'))
net.show("{}/{}-nGraph_{}.html".format(report_path, main_domain, date_now))
