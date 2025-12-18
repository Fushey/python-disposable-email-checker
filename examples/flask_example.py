"""
Flask Integration Example
"""

from flask import Flask, request, jsonify
import os
from tempmailchecker import TempMailChecker
from requests.exceptions import RequestException

app = Flask(__name__)
checker = TempMailChecker(os.getenv('TEMPMAILCHECKER_API_KEY', 'your_api_key_here'))

@app.route('/signup', methods=['POST'])
def signup():
    """Signup endpoint with disposable email validation"""
    data = request.get_json()
    email = data.get('email') if data else None
    
    if not email:
        return jsonify({'error': 'Email is required'}), 400
    
    try:
        if checker.is_disposable(email):
            return jsonify({
                'error': 'Disposable email addresses are not allowed',
                'email': email
            }), 400
    except RequestException as e:
        # Log error but allow signup (fail open)
        app.logger.warning(f'TempMailChecker API error: {e}')
    
    # Proceed with signup
    return jsonify({
        'success': True,
        'message': 'Email validated successfully',
        'email': email
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)

