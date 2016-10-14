from ftptest import failure, success


def test_success_transfer_zip_file(mocker):
    mocker.patch('ftplib.FTP')
    success.transfer_file('a.zip', 'target.host.de', 'user', 'pw')


def test_failure_transfer_zip_file(mocker):
    mocker.patch('ftplib.FTP')
    failure.transfer_file('a.zip', 'target.host.de', 'user', 'pw')