"""
Email and application settings for the landing contact-form backend.
All values are read from environment variables with sensible defaults.
"""
import os

EMAIL_HOST = os.environ.get('EMAIL_HOST', 'smtp.gmail.com')
EMAIL_PORT = int(os.environ.get('EMAIL_PORT', '587'))
EMAIL_USE_TLS = os.environ.get('EMAIL_USE_TLS', 'True').lower() == 'true'
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER', '')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', '')

# Address that will receive every contact-form submission
CONTACT_FORM_EMAIL = os.environ.get('CONTACT_FORM_EMAIL', 'tsokurdanil@gmail.com')

# Flask secret key (used for session signing; not critical for this service)
SECRET_KEY = os.environ.get('SECRET_KEY', 'landing-contact-secret')
