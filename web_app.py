from flask import Flask, render_template, request, redirect
from url_shortener import url_hash_table, add_to_hash, save_to_json

framework = Flask(__name__)

@framework.route('/url_shortener', methods=['GET', 'POST'])
def shorten():
    if request.method == 'GET':
        return render_template('landing.html')
    else:
        #do something with URL here.
        url_request = request.form['response']

        if ('http://' not in url_request) and ('https://' not in url_request):
            url_request = 'http://' + url_request

        print url_request

        generated_code = add_to_hash(url_request)
        url_response = 'http://127.0.0.1:5000/' + generated_code

        return render_template('url_response.html', url_request=url_request,
            url_response=url_response)

@framework.route('/<url_shortname>')
def redirect_to_real_site(url_shortname):
    redirect_url = url_hash_table[url_shortname].url_name
    url_hash_table[url_shortname].used_url()
    save_to_json()
    return redirect(redirect_url)

if __name__ == '__main__':
    framework.run(debug=True)