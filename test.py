from collections import defaultdict

# 输入数据
map1 = {
    "Sunny": ["Jira-6", "Jira-5", "Jira-1"],
    "Bob": ["Jira-10", "Jira-1"]
}
map2 = {
    "Bob": ["Jira-1", "Jira-2"],
    "Alice": ["Jira-3", "Jira-10", "Jira-4"]
}

# 合并两个来源
ticket_owners = defaultdict(set)

for owner_map in (map1, map2):
    for owner, jiras in owner_map.items():
        for jira in jiras:
            ticket_owners[jira].add(owner)

# 排序 JIRA 编号（提取数字部分排序）
def jira_sort_key(jira_id):
    return int(jira_id.split('-')[1])

# 格式化输出
for jira_id in sorted(ticket_owners.keys(), key=jira_sort_key):
    owners = sorted(ticket_owners[jira_id])  # 负责人字母序
    print(f"{jira_id} is taken care by {owners}")