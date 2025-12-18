#!/usr/bin/env python3
"""
Basic usage examples for TempMailChecker Python SDK
"""

import os
from tempmailchecker import TempMailChecker, ENDPOINT_EU, ENDPOINT_US, ENDPOINT_ASIA

# Get API key from environment or use placeholder
api_key = os.getenv('TEMPMAILCHECKER_API_KEY', 'your_api_key_here')

if api_key == 'your_api_key_here':
    print('⚠️  Warning: Using placeholder API key. Set TEMPMAILCHECKER_API_KEY environment variable.')
    print('   Some tests will fail without a valid API key.\n')

# Initialize the checker (defaults to EU endpoint)
checker = TempMailChecker(api_key)

# Or use a specific regional endpoint:
# checker = TempMailChecker(api_key, endpoint=ENDPOINT_US)
# checker = TempMailChecker(api_key, endpoint=ENDPOINT_ASIA)

print('=' * 60)
print('TempMailChecker Python SDK Test')
print('=' * 60)
print()

# Test 1: Check endpoint constants
print('🌍 Testing Endpoint Constants:')
print(f'   EU:   {ENDPOINT_EU}')
print(f'   US:   {ENDPOINT_US}')
print(f'   Asia: {ENDPOINT_ASIA}\n')

# Test 2: Check disposable email
print('📧 Test 1: Check Disposable Email')
print('-' * 60)

test_emails = [
    ('user@gmail.com', 'Legitimate'),
    ('test@10minutemail.com', 'Disposable'),
    ('spam@guerrillamail.com', 'Disposable'),
]

for email, expected in test_emails:
    try:
        is_disposable = checker.is_disposable(email)
        status = '❌ Disposable' if is_disposable else '✅ Legitimate'
        match = '✓' if (is_disposable and expected == 'Disposable') or (not is_disposable and expected == 'Legitimate') else '✗'
        print(f'   {email:<35} {status} {match}')
    except Exception as e:
        print(f'   {email:<35} ⚠️  Error: {e}')

print()

# Test 3: Get full response
print('📋 Test 2: Get Full Response')
print('-' * 60)

try:
    result = checker.check('user@tempmail.com')
    print(f'   Response: {result}')
except Exception as e:
    print(f'   ⚠️  Error: {e}')

print()

# Test 4: Check domain only
print('🌐 Test 3: Check Domain')
print('-' * 60)

test_domains = ['gmail.com', 'tempmail.com', 'mailinator.com']

for domain in test_domains:
    try:
        is_disposable = checker.is_disposable_domain(domain)
        status = '❌ Disposable' if is_disposable else '✅ Legitimate'
        print(f'   {domain:<35} {status}')
    except Exception as e:
        print(f'   {domain:<35} ⚠️  Error: {e}')

print()

# Test 5: Check usage
print('📊 Test 4: Check API Usage')
print('-' * 60)

try:
    usage = checker.get_usage()
    if 'usage_today' in usage and 'limit' in usage:
        print(f'   Used today: {usage["usage_today"]} / {usage["limit"]}')
        print(f'   Resets: {usage.get("reset", "N/A")}')
    else:
        print(f'   ⚠️  Unexpected response format: {usage}')
except Exception as e:
    print(f'   ⚠️  Error: {e}')

print()

# Test 6: Test regional endpoints
print('🌍 Test 5: Regional Endpoints')
print('-' * 60)

endpoints = [
    ('EU', ENDPOINT_EU),
    ('US', ENDPOINT_US),
    ('Asia', ENDPOINT_ASIA),
]

for name, endpoint_url in endpoints:
    try:
        regional_checker = TempMailChecker(api_key, endpoint=endpoint_url)
        result = regional_checker.check('test@gmail.com')
        print(f'   {name:<10} {endpoint_url:<45} ✅ Working')
    except Exception as e:
        print(f'   {name:<10} {endpoint_url:<45} ⚠️  Error: {e}')

print()
print('=' * 60)
print('✅ Tests completed!')
print('=' * 60)

