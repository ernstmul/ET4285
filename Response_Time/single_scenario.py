from paramiko import SSHClient

def start_iperf3_server(server_ip):

	## Make ssh connection
	port = 22
	ssh = SSHClient()
	ssh.load_system_host_keys()
	ssh.connect(server_ip, port, username="nas", password="naslab")

	## Start iperf3 on the receiving server
	ssh.exec_command("iperf3 -s")

start_iperf3_server("10.10.2.15")
