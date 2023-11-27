import subprocess

# 以热更新的方式启动项目
cmd = 'flet run main.py -v -r'  # 这里以运行dir命令为例
result = subprocess.run(cmd, capture_output=True, text=True, shell=True)

# 输出结果
print(result.stdout)
