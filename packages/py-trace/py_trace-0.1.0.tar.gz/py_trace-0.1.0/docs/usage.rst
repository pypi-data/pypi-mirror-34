=====
Usage
=====

To use Trace Python Client in a project::

    from py_trace import Trace

    client = Trace(<client_key>, <client_secret>)
    client.get_authorization_url()
    # output should be like https://www.alpinereplay.com/api/oauth_login?oauth_token=<token>, go to the url and authorize the app
    # after authorization, you should see a url like http://snow.traceup.com/api/oauth_login?oauth_token=<token>&oauth_verifier=<verifier>
    client.get_access_token(<verifier>)
    cleint.get_user()
