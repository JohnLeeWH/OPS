import subprocess


def run_wrk_process(wrkArgs, website):
    # thread 线程数；connections 总连接数
    cmdArgs = ["wrk"]
    if wrkArgs:
        if "connections" in wrkArgs:
            cmdArgs.append("-c " + wrkArgs["connections"])
        if "duration" in wrkArgs:
            cmdArgs.append("-d " + wrkArgs["duration"])
        if "thread" in wrkArgs:
            cmdArgs.append("-t " + wrkArgs["thread"])
        if "script" in wrkArgs:
            cmdArgs.append("-s" + wrkArgs["script"])
        if "header" in wrkArgs:
            cmdArgs.append("-H " + wrkArgs["header"])
        if "latency" in wrkArgs:
            cmdArgs.append("--latency")
        if "timeout" in wrkArgs:
            cmdArgs.append("--timeout")

        print("arguments have been append.")
    else:
        print("no arguments.")
    cmdArgs.append(website)
    print(cmdArgs)
    with subprocess.Popen(cmdArgs, stdout=subprocess.PIPE) as proc:
        for line in proc.stdout:
            print(str(line))

    # result = subprocess.call(cmdArgs, shell=False)
    # print(result)
    # return result

    return True
