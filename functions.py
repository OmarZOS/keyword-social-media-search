import xmlrpc.client

def connect_rpc(url):
    return xmlrpc.client.ServerProxy(url)

def get_session(url):
    session=None
    try:
        session = connect_rpc(url)
    except BaseException as e:
        session = connect_rpc(url)
        print (f"Something's wrong about the url {url},{str(e)}")
    return session
    


