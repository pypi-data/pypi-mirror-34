import jsend
import logging
import requests

logger = logging.getLogger(__name__)

from pkg_resources import get_distribution, DistributionNotFound
try:
    __version__ = get_distribution(__name__).version
except DistributionNotFound:
    # package is not installed
    pass

class ComodoCA(object):
    """
    Top level class for the Comodo CA. Only very generic 'things' go here.
    """


class ComodoTLSService(ComodoCA):
    """
    Class that encapsulates methods to use against Comodo SSL/TLS certificates
    """
    def __init__(self, **kwargs):
        """
        :param string api_url: The full URL for the API server
        :param string customer_login_uri: The URI for the customer login (if your login to the Comodo GUI is at
                https://hard.cert-manager.com/customer/foo/, your login URI is 'foo').
        :param string login: The login user
        :param string org_id: The organization ID
        :param string password: The API user's password
        :param bool client_cert_auth: Whether to use client certificate authentication
        :param string client_public_certificate: The path to the public key if using client cert auth
        :param string client_private_key: The path to the private key if using client cert auth
        """
        # Using get for consistency and to allow defaults to be easily set
        self.api_url = kwargs.get('api_url')
        self.customer_login_uri = kwargs.get('customer_login_uri')
        self.login = kwargs.get('login')
        self.org_id = kwargs.get('org_id')
        self.password = kwargs.get('password')
        self.client_cert_auth = kwargs.get('client_cert_auth')
        self.session = requests.Session()
        # Because Comodo is crap at designing APIs (in my opinion) we have to get the wsdl
        # then modify the transport to use client certs after that.
        if self.client_cert_auth:
            self.client_public_certificate = kwargs.get('client_public_certificate')
            self.client_private_key = kwargs.get('client_private_key')
            self.session.cert = (self.client_public_certificate, self.client_private_key)
        self.headers = {
            'login': self.login,
            'password': self.password,
            'customerUri': self.customer_login_uri
        }
        self.session.headers.update(self.headers)


    def _create_url(self, suffix):
        '''

        :param str suffix: The suffix of the URL you wish to create i.e. for https://example.com/foo the suffix would be /foo
        :return: The full URL
        :rtype: str
        '''
        url = self.api_url + suffix
        logger.debug('URL created: %s' % url)

        return url

    def _get(self, url):
        '''

        :param url:
        :return:

        '''
        logger.debug('Performing a GET on url: %s' % url)
        result = self.session.get(url)

        logger.debug('Result headers: %s' % result.headers)
        logger.debug('Text result: %s' % result.text)

        return result

    def get_cert_types(self):
        """
        Collect the certificate types that are available to the customer.

        :return: A list of dictionaries of certificate types
        :rtype: list
        """
        url = self._create_url('types')
        result = self._get(url)

        if result.status_code == 200:
            return jsend.success({'types': result.json()})
        else:
            return jsend.fail(result.json())

    def collect(self, cert_id, format_type):
        """
        Collect a certificate.

        :param int cert_id: The certificate ID
        :param str format_type: The format type to use: Allowed values: 'x509' - for X509, Base64 encoded, 'x509CO' - for X509 Certificate only, Base64 encoded, 'x509IO' - for X509 Intermediates/root only, Base64 encoded, 'base64' - for PKCS#7 Base64 encoded, 'bin' - for PKCS#7 Bin encoded, 'x509IOR' - for X509 Intermediates/root only Reverse, Base64 encoded
        :return: The certificate_id or the certificate depending on whether the certificate is ready (check status code)
        :rtype: dict
        """

        url = self._create_url('collect/{}/{}'.format(cert_id, format_type))

        logger.debug('Collecting certificate at URL: %s' % url)
        result = self._get(url)

        logger.debug('Collection result code: %s' % result.status_code)

        # The certificate is ready for collection
        if result.status_code == 200:
            return jsend.success({'certificate': result.content.decode(result.encoding),
                                  'certificate_status': 'issued',
                                  'certificate_id': cert_id})
        # The certificate is not ready for collection yet
        elif result.status_code == 400 and result.json()['code'] == 0:
            return jsend.fail({'certificate_id': cert_id, 'certificate': '', 'certificate_status': 'pending'})
        # Some error occurred
        else:
            return jsend.fail(result.json())

    def revoke(self, cert_id, reason=''):
        """
        Revoke a certificate.

        :param int cert_id: The certificate ID
        :param str reason: Reason for revocation (up to 512 characters), can be blank: '', but must exist.
        :return: The result of the operation, 'Successful' on success
        :rtype: dict
        """
        url = self._create_url('revoke/{}'.format(cert_id))
        data = {'reason': reason}
        result=self.session.post(url, json=data,)

        if result.status_code == 204:
            return jsend.success()
        else:
            return jsend.error(result.json()['description'])

    def submit(self, cert_type_name, csr, term, subject_alt_names=''):
        """
        Submit a certificate request to Comodo.

        :param string cert_type_name: The full cert type name (Example: 'PlatinumSSL Certificate') the supported
                                      certificate types for your account can be obtained with the
                                      get_cert_types() method.
        :param string csr: The Certificate Signing Request (CSR)
        :param int term: The length, in days, for the certificate to be issued
        :param string subject_alt_names: Subject Alternative Names separated by a ",".
        :return: The certificate_id and the normal status messages for errors.
        :rtype: dict
        """
        cert_types = self.get_cert_types()

        # If collection of cert types fails we simply pass the error back.
        if cert_types['status'] == 'fail':
            return cert_types

        # Find the certificate type ID
        for cert_type in cert_types['data']['types']:
            if cert_type['name'] == cert_type_name:
                cert_type_id = cert_type['id']

        url = self._create_url('enroll')
        data = {'orgId': self.org_id, 'csr': csr, 'subjAltNames': subject_alt_names, 'certType': cert_type_id,
                'numberServers': 1, 'serverType': -1, 'term': term, 'comments': 'Requested with comodo_proxy',
                'externalRequester': ''}
        result = self.session.post(url, json=data)

        if result.status_code == 200:
            return jsend.success({'certificate_id': result.json()['sslId']})
        # Anything else is an error
        else:
            return jsend.error(result.json()['description'])