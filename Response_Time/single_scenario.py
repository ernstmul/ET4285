from paramiko import SSHClient
import subprocess

def make_ssh_connection(server_ip):
	## Make ssh connection
	port = 22
	ssh = SSHClient()
	ssh.load_system_host_keys()
	ssh.connect(server_ip, port, username="nas", password="naslab")
	return ssh

def start_iperf3_server(server_ip):

	ssh = make_ssh_connection(server_ip)

	## Start iperf3 on the receiving server
	ssh.exec_command("iperf3 -s")

def start_iperf3_client(client_ip, server_ip):
	ssh = make_ssh_connection(client_ip)

	stdout = subprocess.PIPE

	## Start iperf3 test
	stdin, stdout, stderr = ssh.exec_command("iperf3 -c " + server_ip + " -i1 -t60")
	stdout.stdout.readlines()
	print(stdout)

#node 15
start_iperf3_server("10.10.2.15")

# node 7 connects to node 15
start_iperf3_client("10.10.2.7","172.16.5.1")


#node 6
start_iperf3_server("10.10.2.6")

#node 5 connects to node 6
start_iperf3_client("10.10.2.5", "172.16.1.1")



