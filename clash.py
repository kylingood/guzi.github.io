import requests
import datetime

# 生成当前日期
today = datetime.datetime.now().strftime("%Y/%m/%d")
year, month, day = today.split("/")

# 获取项目根目录
project_dir = f'/home/runner/work/guzi.github.io/guzi.github.io'
# 文件存储目录（可修改）
save_yaml_path = f"{project_dir}/yaml/"
save_txt_path = f"{project_dir}/txt/"
# 遍历 0-4 生成文件名
for i in range(5):
    file_name = f"{i}-{year}{month}{day}.yaml"
    url = f"https://node.freeclashnode.com/uploads/{year}/{month}/{file_name}"
    save_file = f"{save_yaml_path}{i}.yaml"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # 检查请求是否成功

        with open(save_file, "wb") as f:
            f.write(response.content)

        print(f"✅ 成功下载: {save_file}")
    except requests.exceptions.RequestException as e:
        print(f"❌ 下载失败: {url} - {e}")


# 遍历 0-4 生成文件名
for i in range(5):
    file_name = f"{i}-{year}{month}{day}.yaml"
    url = f"https://potatsolite.github.io/uploads/{year}/{month}/{file_name}"
    save_file = f"{save_yaml_path}{i}.yaml"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # 检查请求是否成功

        with open(save_file, "wb") as f:
            f.write(response.content)

        print(f"✅ 成功下载: {save_file}")
    except requests.exceptions.RequestException as e:
        print(f"❌ 下载失败: {url} - {e}")


# 遍历 0-4 生成文件名
for i in range(5):
    file_name = f"{i}-{year}{month}{day}.txt"
    url = f"https://node.freeclashnode.com/uploads/{year}/{month}/{file_name}"
    save_file = f"{save_txt_path}{i}.txt"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # 检查请求是否成功

        with open(save_file, "wb") as f:
            f.write(response.content)

        print(f"✅ 成功下载: {save_file}")
    except requests.exceptions.RequestException as e:
        print(f"❌ 下载失败: {url} - {e}")


# 遍历 0-4 生成文件名
for i in range(5):
    file_name = f"{i}-{year}{month}{day}.txt"
    url = f"https://potatsolite.github.io/uploads/{year}/{month}/{file_name}"
    save_file = f"{save_txt_path}{i}.txt"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # 检查请求是否成功

        with open(save_file, "wb") as f:
            f.write(response.content)

        print(f"✅ 成功下载: {save_file}")
    except requests.exceptions.RequestException as e:
        print(f"❌ 下载失败: {url} - {e}")
