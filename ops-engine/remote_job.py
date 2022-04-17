from fabric import Connection


def deploy_nginx(ssh_args):
    conn = Connection(ssh_args.host,
                      ssh_args.user,
                      ssh_args.port,
                      connect_kwargs={'password': ssh_args.password})
