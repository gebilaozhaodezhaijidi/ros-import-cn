import requests
import json

# 下载 geoip 数据
url = "https://github.com/MetaCubeX/meta-rules-dat/raw/refs/heads/sing/geo/geoip/cn.json"
response = requests.get(url)
data = response.json()

# 提取 IPv4 地址
ipv4_addresses = data.get("ipv4", [])

# 格式化为 RouterOS 的地址列表命令
formatted_lines = ["/ip firewall address-list"]
formatted_lines += [f"add list=CN address={ip}" for ip in ipv4_addresses]

# 将内容写入 CN.rsc 文件
with open("CN.rsc", "w") as file:
    file.write("\n".join(formatted_lines))

print("CN.rsc 文件已生成")
