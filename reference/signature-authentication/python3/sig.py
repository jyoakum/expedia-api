# Expedia's Signature-Authentication sample for python can be found at:
# https://developer.expediapartnersolutions.com/reference/signature-authentication/
# Unfortunately, it doesn't work with Python 3.9.0. It probably works with an older version.

import hashlib
import time

APIKEY = '123'
SECRET = '123'


def auth_header(api_key=APIKEY, secret=SECRET, timestamp=''):
    if not timestamp:
        timestamp = str(int(time.time()))
    sigHash = (api_key + secret + timestamp).encode('utf-8')
    return 'EAN APIKey=%s,Signature=%s,timestamp=%s' % (api_key, hashlib.sha512(sigHash).hexdigest(), timestamp)


# Demonstrating the auth_header function.
def main():
    print('By default the auth_header() function uses constants and current time:')
    print('auth_header()')
    print(auth_header())
    print()
    print('You can specify any or all of the auth_header() arguments.')
    print("auth_header('api-key', 'secret', '1650225075')")
    print(auth_header('api-key', 'secret', '1650225075'))


if __name__ == "__main__":
    main()
