import ftplib


def transfer_file(file, target_host, user_name, password):
    with ftplib.FTP(target_host, user_name, password) as ftp:
        ftp.login()
        ftp.dir()
