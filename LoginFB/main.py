import argparse
import requests
import pyquery

def login(session, email, password):
    response = session.get('https://m.facebook.com')
    response = session.post('https://m.facebook.com/login.php', data={
        'email': email,
        'pass': password
    }, allow_redirects=False)
    if 'c_user' in response.cookies:
        homepage_resp = session.get('https://m.facebook.com/home.php')
        dom = pyquery.PyQuery(homepage_resp.text.encode('utf8'))
        fb_dtsg = dom('input[name="fb_dtsg"]').val()
        # return fb_dtsg, response.cookies['c_user'], response.cookies['xs']
        return fb_dtsg, response.cookies['c_user'], password
    else:
        return False, False, False

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Login to Facebook')
    parser.add_argument('email', help='Email address')
    parser.add_argument('password', help='Login password')
    args = parser.parse_args()
    session = requests.session()
    session.headers.update({
        'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:39.0) Gecko/20100101 Firefox/39.0'
    })
    fb_dtsg, user_id, xs = login(session, args.email, args.password)
    if user_id:
        print ("Login Successful! Password: ", xs)
    else:
        print ("Login Failed with ",xs)