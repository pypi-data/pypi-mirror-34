import requests
import logging

RED = '\033[0;31m'
GREEN = '\033[0;32m'
ORANGE = '\033[0;33m'
NO_COLOR = '\033[0m'

def website_checker(server, session_id, machine):
    """ :account,machine """
    for website in server.list_websites(session_id):
        protocol = 'https' if website['https'] else 'http'
        for subd in website['subdomains']:
            for app in website['website_apps']:
                appurl = "{}://{}{}".format(
                        protocol,
                        subd,
                        app[1]
                    )
                print('Checking: {}'.format(appurl))
                ssl_msg = ''
                color = GREEN
                try:
                    r = requests.get(appurl)
                except requests.exceptions.SSLError:
                    color = ORANGE
                    r = requests.get(appurl, verify=False)
                    ssl_msg = '{}Invalid Certificate{}'.format(RED, NO_COLOR)
                except requests.exceptions.ConnectionError:
                    r = False
                    ssl_msg = '{}Connection Error{}'.format(RED, NO_COLOR)

                if r is False:
                    print("{}Error: {} not available{}".format(
                        RED, appurl, NO_COLOR
                    ))
                elif r.status_code != 200:
                    print("{}Error {}: {} {}{}".format(
                        RED, r.status_code, appurl, ssl_msg, NO_COLOR
                    ))
                    try:
                        r.raise_for_status()
                    except Exception as e:
                        logging.error(e)
                else:
                    print("{}Available: {} {}{}".format(
                        color, appurl, ssl_msg, NO_COLOR
                    ))
