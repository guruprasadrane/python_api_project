from flask import Flask, render_template, request, jsonify, send_from_directory
from monitor import ping_url, validate_functionality
import requests
import os
import certifi

# Set the path to the certificates folder
cert_path = os.path.join(os.path.dirname(__file__), 'certificates', 'ca-bundle.pem')

# Set the REQUESTS_CA_BUNDLE environment variable to cert_path
os.environ['REQUESTS_CA_BUNDLE'] = cert_path

# If REQUESTS_CA_BUNDLE is set but the file doesn't exist, use the default certifi bundle
if not os.path.exists(os.environ['REQUESTS_CA_BUNDLE']):
    os.environ['REQUESTS_CA_BUNDLE'] = certifi.where()

app = Flask(__name__)

# Proxy configuration
http_proxy = os.environ.get('HTTP_PROXY')
https_proxy = os.environ.get('HTTPS_PROXY')
default_proxies = {
    'http': http_proxy,
    'https': https_proxy,
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ping', methods=['POST'])
def ping():
    url = request.json['url']
    proxy_url = request.json.get('proxy_url')
    
    if proxy_url:
        proxies = {'http': proxy_url, 'https': proxy_url}
    else:
        proxies = None  # Don't use any proxy if not specified
    
    result = ping_url(url, proxies=proxies)
    return jsonify(result)

@app.route('/proxy_ping', methods=['POST'])
def proxy_ping():
    url = request.json['url']
    proxy_url = request.json.get('proxy_url')
    
    if proxy_url:
        proxies = {'http': proxy_url, 'https': proxy_url}
    else:
        proxies = default_proxies
    
    try:
        response = requests.get(url, timeout=10, proxies=proxies)
        return jsonify({
            'status_code': response.status_code,
            'content_type': response.headers.get('Content-Type'),
            'content_length': len(response.content),
            'response_time': response.elapsed.total_seconds()
        })
    except requests.RequestException as e:
        return jsonify({'error': str(e)}), 500

@app.route('/validate', methods=['POST'])
def validate():
    app_name = request.json['app_name']
    proxy_url = request.json.get('proxy_url')
    
    if proxy_url:
        proxies = {'http': proxy_url, 'https': proxy_url}
    else:
        proxies = None  # Don't use any proxy if not specified
    
    result = validate_functionality(app_name, proxies=proxies)
    return jsonify(result), 200 if result.get('status') == 'OK' else 400

@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)

if __name__ == '__main__':
    app.run(debug=True)
