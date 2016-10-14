```
-> % pytest ftptest/test
============================================== test session starts ===============================================
platform linux -- Python 3.4.3, pytest-3.0.3, py-1.4.31, pluggy-0.4.0
rootdir: /tmp/pytest_mocker, inifile: 
plugins: mock-1.2
collected 2 items 

ftptest/test/test_mock_patch.py .F

==================================================== FAILURES ====================================================
_________________________________________ test_failure_transfer_zip_file _________________________________________

mocker = <pytest_mock.MockFixture object at 0x7fd5f16269e8>

    def test_failure_transfer_zip_file(mocker):
        mocker.patch('ftplib.FTP')
>       failure.transfer_file('a.zip', 'target.host.de', 'user', 'pw')

ftptest/test/test_mock_patch.py:11: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
ftptest/failure.py:5: in transfer_file
    with FTP(target_host, user_name, password) as ftp:
/usr/lib64/python3.4/ftplib.py:118: in __init__
    self.connect(host)
/usr/lib64/python3.4/ftplib.py:153: in connect
    source_address=self.source_address)
/usr/lib64/python3.4/socket.py:494: in create_connection
    for res in getaddrinfo(host, port, 0, SOCK_STREAM):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

host = 'target.host.de', port = 21, family = 0, type = <SocketKind.SOCK_STREAM: 1>, proto = 0, flags = 0

    def getaddrinfo(host, port, family=0, type=0, proto=0, flags=0):
        """Resolve host and port into list of address info entries.
    
        Translate the host/port argument into a sequence of 5-tuples that contain
        all the necessary arguments for creating a socket connected to that service.
        host is a domain name, a string representation of an IPv4/v6 address or
        None. port is a string service name such as 'http', a numeric port number or
        None. By passing None as the value of host and port, you can pass NULL to
        the underlying C API.
    
        The family, type and proto arguments can be optionally specified in order to
        narrow the list of addresses returned. Passing zero as a value for each of
        these arguments selects the full range of results.
        """
        # We override this function since we want to translate the numeric family
        # and socket type values to enum constants.
        addrlist = []
>       for res in _socket.getaddrinfo(host, port, family, type, proto, flags):
E       socket.gaierror: [Errno -3] Temporary failure in name resolution

/usr/lib64/python3.4/socket.py:533: gaierror
======================================= 1 failed, 1 passed in 0.10 seconds =======================================
```