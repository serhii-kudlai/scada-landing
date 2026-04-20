"""
View handlers for the landing contact-form backend.
"""
import logging
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from flask import request, jsonify
import base as settings

logger = logging.getLogger(__name__)


def health():
    return _json({'status': 'ok'})


def contact_send():
    """Accept a JSON POST from the landing form and send it by email."""
    if request.method == 'OPTIONS':
        return _cors_preflight()

    data = request.get_json(silent=True) or {}

    name = str(data.get('name', '')).strip()
    company = str(data.get('company', '')).strip()
    email = str(data.get('email', '')).strip()
    phone = str(data.get('phone', '')).strip()
    message = str(data.get('message', '')).strip()

    if not name or not email:
        return _json({'error': 'Имя и email обязательны для заполнения.'}, 400)

    subject = (
        f'Заявка с сайта SCADA — {name} ({company})'
        if company
        else f'Заявка с сайта SCADA — {name}'
    )
    body = (
        'Новая заявка с лендинга SCADA\n'
        f'{"=" * 40}\n\n'
        f'Имя:       {name}\n'
        f'Компания:  {company or "не указана"}\n'
        f'Email:     {email}\n'
        f'Телефон:   {phone or "не указан"}\n\n'
        'Описание задачи:\n'
        f'{message or "не указано"}\n'
    )

    try:
        _send_email(subject, body, recipient=settings.CONTACT_FORM_EMAIL, reply_to=email)
        logger.info('Contact form email sent to %s (reply-to: %s)', settings.CONTACT_FORM_EMAIL, email)
        return _json({'status': 'ok'})
    except Exception as exc:
        logger.error('Failed to send contact form email: %s', exc)
        return _json({'error': 'Не удалось отправить заявку. Попробуйте позже.'}, 500)


def _send_email(subject: str, body: str, recipient: str, reply_to: str = '') -> None:
    msg = MIMEMultipart()
    msg['From'] = settings.EMAIL_HOST_USER
    msg['To'] = recipient
    msg['Subject'] = subject
    if reply_to:
        msg['Reply-To'] = reply_to
    msg.attach(MIMEText(body, 'plain', 'utf-8'))

    password = settings.EMAIL_HOST_PASSWORD.replace(' ', '')
    with smtplib.SMTP(settings.EMAIL_HOST, settings.EMAIL_PORT) as smtp:
        if settings.EMAIL_USE_TLS:
            smtp.starttls()
        if settings.EMAIL_HOST_USER and password:
            smtp.login(settings.EMAIL_HOST_USER, password)
        smtp.sendmail(msg['From'], [recipient], msg.as_string())


def _json(data: dict, status: int = 200):
    resp = jsonify(data)
    resp.status_code = status
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


def _cors_preflight():
    resp = jsonify({})
    resp.headers['Access-Control-Allow-Origin'] = '*'
    resp.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    resp.headers['Access-Control-Allow-Methods'] = 'POST, OPTIONS'
    return resp
