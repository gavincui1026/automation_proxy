import subprocess
import time

# 指定端口号
port = 9091

# 启动mitmproxy并运行代理脚本
mitmproxy_process = subprocess.Popen(
    f"mitmdump -p {port} -s modify.py",
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True,  # 确保输出为文本格式
    shell=True  # 在Windows上运行时需要加上
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

# 实时读取和打印mitmproxy的输出
try:
    while True:
        output = mitmproxy_process.stdout.readline()
        if output == '' and mitmproxy_process.poll() is not None:
            break
        if output:
            print(output.strip())
except KeyboardInterrupt:
    mitmproxy_process.terminate()
    print("mitmproxy已终止")
except Exception as e:
    print(f"发生错误: {e}")
    mitmproxy_process.terminate()
