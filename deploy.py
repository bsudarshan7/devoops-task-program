import paramiko

EC2_HOST = "YOUR_EC2_PUBLIC_IP"
EC2_USER = "ubuntu"  # Amazon Linux: ec2-user
KEY_FILE = "my-key.pem"

local_file = "main.py"
remote_file = "/home/ubuntu/main.py"

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect(
    hostname=EC2_HOST,
    username=EC2_USER,
    key_filename=KEY_FILE
)

sftp = ssh.open_sftp()

sftp.put(local_file, remote_file)

print(f"{local_file} uploaded successfully to {remote_file}")

sftp.close()
ssh.close()
