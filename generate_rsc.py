# import requests
# import json

# # 下载 geoip 数据
# url = "https://raw.githubusercontent.com/MetaCubeX/meta-rules-dat/refs/heads/sing/geo/geoip/cn.json"
# response = requests.get(url)
# data = response.json()

# # 提取 IPv4 地址
# ipv4_addresses = data.get("ipv4", [])

# # 格式化为 RouterOS 的地址列表命令
# formatted_lines = ["/ip firewall address-list"]
# formatted_lines += [f"add list=CN address={ip}" for ip in ipv4_addresses]

# # 将内容写入 CN.rsc 文件
# with open("CN.rsc", "w") as file:
#     file.write("\n".join(formatted_lines))

# print("CN.rsc 文件已生成")

import requests
import json

# 下载 geoip 数据
url = "https://github.com/MetaCubeX/meta-rules-dat/raw/refs/heads/sing/geo/geoip/cn.json"
response = requests.get(url)

# 确保请求成功
if response.status_code == 200:
    data = response.json()

    # 输出数据结构检查
    print(json.dumps(data, indent=4))  # 打印 JSON 数据结构，方便调试

    # 提取 IPv4 地址
    ipv4_addresses = []
    for rule in data.get("rules", []):
        for cidr in rule.get("ip_cidr", []):
            # 只提取 IPv4 地址（排除 IPv6 地址）
            if ':' not in cidr:
                ipv4_addresses.append(cidr)

    # 格式化为 RouterOS 的地址列表命令
    formatted_lines = ["/ip firewall address-list"]
    formatted_lines += [f"add list=CN address={ip}" for ip in ipv4_addresses]

    # 将内容写入 CN.rsc 文件
    with open("CN.rsc", "w") as file:
        file.write("\n".join(formatted_lines))

    print("CN.rsc 文件已生成")
else:
    print(f"请求失败，状态码：{response.status_code}")
