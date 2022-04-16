import subprocess
from unittest import result


def run_ping_process(ip):
    print(ip)
    cmd_Args = ["ping", "-c3"]
    cmd_Args.append(ip)
    #cmdArgs.append('>')
    #cmdArgs.append("nohup.out")
    # cmdArgs=['ls']
    #cmdArgs = "tail -f /var/log/messages"
    print(cmd_Args)
    proc = subprocess.Popen(cmd_Args, stdout=subprocess.STDOUT, shell=True)
    return proc


def run_wrk_process(wrk_args, website):
    # thread 线程数；connections 总连接数
    cmd_args = ["wrk"]
    if wrk_args:
        if "connections" in wrk_args:
            cmd_args.append("-c " + wrk_args["connections"])
        if "duration" in wrk_args:
            cmd_args.append("-d " + wrk_args["duration"])
        if "thread" in wrk_args:
            cmd_args.append("-t " + wrk_args["thread"])
        if "script" in wrk_args:
            cmd_args.append("-s" + wrk_args["script"])
        if "header" in wrk_args:
            cmd_args.append("-H " + wrk_args["header"])
        if "latency" in wrk_args:
            cmd_args.append("--latency")
        if "timeout" in wrk_args:
            cmd_args.append("--timeout")
        print("arguments have been append.")
    else:
        print("no arguments.")
    cmd_args.append('-d 2s')
    cmd_args.append(website)
    print(cmd_args)
    proc = subprocess.Popen(cmd_args, stdout=subprocess.PIPE)
    #proc = subprocess.Popen(cmdArgs, bufsize=0)
    #return proc

    with subprocess.Popen(cmd_args, stdout=subprocess.PIPE) as proc:
        result = proc.stdout.read().strip()
        #result = str(cmd_stdout,"utf-8")
        #    for line in proc.stdout:
        #        print(str(line))
        #        ws.send_text(line)
        # result = subprocess.call(cmdArgs, shell=False)
        
        print(result)
    return result

    #return True
