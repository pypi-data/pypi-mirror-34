from xmlrpc.client import ServerProxy
from getpass import getpass


def start_session(account, machine):
    """ returns server and session_id for reuse in API calls """
    server = ServerProxy(
        'https://api.webfaction.com/',
    )
    session_id, returned_account = server.login(
        account, getpass('API password: '), machine, 2,
    )
    return server, session_id
