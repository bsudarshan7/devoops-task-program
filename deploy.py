import paramiko

HOST = "35.154.77.244"
USERNAME = "ec2-user"
KEY_FILE = "sab754.pem"

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect(
    hostname=HOST,
    username=USERNAME,
    key_filename=KEY_FILE
)

sftp = ssh.open_sftp()

sftp.put("main1.py", "/home/ubuntu/main1.py")

print("main1.py uploaded successfully!")

sftp.close()
ssh.close()
  
