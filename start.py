import subprocess
import time

# 指定端口号
port = 8888

# 启动mitmproxy并运行代理脚本
mitmproxy_process = subprocess.Popen(
    ["mitmdump", "-p", str(port), "-s", "modify.py"],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True  # 确保输出为文本格式
)

# 确保mitmproxy启动成功
time.sleep(5)

# 检查进程是否仍在运行
if mitmproxy_process.poll() is None:
    print(f"mitmproxy已启动，监听端口: {port}")
else:
    print("mitmproxy启动失败，输出如下:")
    stdout, stderr = mitmproxy_process.communicate()
    print("标准输出:", stdout)
    print("错误输出:", stderr)

# 脚本运行至此保持运行状态，可以在这里添加其他逻辑或保持代理运行
try:
    mitmproxy_process.wait()
except KeyboardInterrupt:
    mitmproxy_process.terminate()
    print("mitmproxy已终止")
