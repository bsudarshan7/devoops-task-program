import paramiko

HOST = "35.154.77.244"
USERNAME = "ec2-user"
KEY_FILE = "my-key.pem"

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect(
    hostname=HOST,
    username=USERNAME,
    key_filename=KEY_FILE
)

sftp = ssh.open_sftp()

sftp.put("main1.py", "/home/ec2-user/main1.py")

print("File uploaded successfully!")

sftp.close()

stdin, stdout, stderr = ssh.exec_command(
    "python3 /home/ec2-user/main1.py"
)

print("Program Output:")
print(stdout.read().decode())

error = stderr.read().decode()
if error:
    print("Errors:")
    print(error)

ssh.close()
