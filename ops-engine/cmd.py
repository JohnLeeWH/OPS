import subprocess


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


def run_iperf_process(iperf_args, ip):
    #
    cmd_args = ["iperf3"]
    cmd_args.append("-c")
    cmd_args.append(ip)
    if "port" in iperf_args:
        cmd_args.append("-p " + str(iperf_args["port"]))
    if "format" in iperf_args:
        cmd_args.append("-f " + str(iperf_args["format"]))
    if "interval" in iperf_args:
        cmd_args.append("-i " + str(iperf_args["interval"]))
    if "file" in iperf_args:
        cmd_args.append("-F " + str(iperf_args["file"]))

    if "time" in iperf_args:
        cmd_args.append("-t " + str(iperf_args["time"]))

    if "parallel" in iperf_args:
        cmd_args.append("-P " + str(iperf_args["parallel"]))
    if "reverse" in iperf_args:
        cmd_args.append("-R ")

    print(cmd_args)
    with subprocess.Popen(cmd_args, stdout=subprocess.PIPE) as proc:
        result = proc.stdout.read().strip()
        print(result)
    return result


def run_nmap_process(nmap_args, ip):
    #
    cmd_args = ["nmap"]

    if "verbose" in nmap_args:
        if nmap_args["verbose"] == "1":
            cmd_args.append("-v")
        if nmap_args["verbose"] == "2":
            cmd_args.append("-vv")
        if nmap_args["verbose"] == "3":
            cmd_args.append("vvv")

    cmd_args.append(ip)
    print(cmd_args)
    with subprocess.Popen(cmd_args, stdout=subprocess.PIPE) as proc:
        result = proc.stdout.read().strip()
        print(result)
    return result