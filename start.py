import subprocess
import time

# 启动mitmproxy并运行代理脚本
mitmproxy_process = subprocess.Popen(
    ["mitmdump", "-s", "modify.py"],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE
)

# 确保mitmproxy启动成功
time.sleep(5)

print("mitmproxy已启动")

# 脚本运行至此保持运行状态，可以在这里添加其他逻辑或保持代理运行
try:
    mitmproxy_process.wait()
except KeyboardInterrupt:
    mitmproxy_process.terminate()
    print("mitmproxy已终止")