import subprocess
from unittest import result


def run_ping_process(ip):
    # 运行ping
    cmd_Args = ["ping", "-c3"]
    cmd_Args.append(ip)

    print(cmd_Args)
    with subprocess.Popen(cmd_Args, stdout=subprocess.PIPE) as proc:
        result = proc.stdout.read().strip()

    return result


def run_wrk_process(wrk_args, website):
    # thread 线程数；connections 总连接数
    cmd_args = ["wrk"]
    if wrk_args:
        if "connections" in wrk_args:
            cmd_args.append("-c " + str(wrk_args["connections"]))
        if "duration" in wrk_args:
            cmd_args.append("-d " + str(wrk_args["duration"]))
        if "thread" in wrk_args:
            cmd_args.append("-t " + str(wrk_args["thread"]))
        if "script" in wrk_args:
            cmd_args.append("-s" + str(wrk_args["script"]))
        if "header" in wrk_args:
            cmd_args.append("-H " + str(wrk_args["header"]))
        if "latency" in wrk_args:
            cmd_args.append("--latency")
        if "timeout" in wrk_args:
            cmd_args.append("--timeout")
        print("arguments have been append.")
    else:
        print("no arguments.")

    cmd_args.append(website)
    
    print(cmd_args)

    with subprocess.Popen(cmd_args, stdout=subprocess.PIPE) as proc:
        result = proc.stdout.read().strip()
        #    for line in proc.stdout:
        #        print(str(line))
        #        ws.send_text(line)
        # result = subprocess.call(cmdArgs, shell=False)

        print(result)
    return result

    #return True
