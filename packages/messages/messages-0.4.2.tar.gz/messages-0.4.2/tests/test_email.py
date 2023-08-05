"""messages.email_ tests."""

import getpass
import os
import pytest
import smtplib

from email.mime.multipart import MIMEMultipart

import messages
from messages.email_ import Email
from messages.email_ import configure
from messages._eventloop import MESSAGELOOP


##############################################################################
# FIXTURES
##############################################################################

@pytest.fixture()
def get_email(mocker):
    """Return a valid Email object."""
    config_mock = mocker.patch.object(messages.email_, 'configure')
    e = Email(from_='me@here.com', to='you@there.com',
            server='smtp.gmail.com', port=465, password='password',
            cc='someone@there.com', bcc='them@there.com',
            subject='subject', body='message', attachments=['file1', 'file2'],
            profile='myName', save=False)
    e.from_ = 'me@here.com'
    e.server = 'smtp.gmail.com'
    e.port = 465
    e.password = 'password'
    return e


# skip this test if on travs-ci
travis = pytest.mark.skipif("TRAVIS" in os.environ and
                    os.environ["TRAVIS"] == "true",
                    reason='skipping test if on travis-ci')


# skip this test if NOT on travis-ci
not_travis = pytest.mark.skipif("TRAVIS" not in os.environ,
                    reason='skipping test if not on travis-ci')


##############################################################################
# TESTS: Email.__init__
##############################################################################

def test_email_init_normal(get_email):
    """
    GIVEN a need to create an Email object
    WHEN the user instantiates a new object with required args
    THEN assert Email object is created with given args
    """
    e = get_email
    assert e is not None
    assert e.server == 'smtp.gmail.com'
    assert e.port == 465
    assert e.password == 'password'
    assert e.from_ == 'me@here.com'
    assert e.to == 'you@there.com'
    assert e.cc == 'someone@there.com'
    assert e.bcc == 'them@there.com'
    assert e.subject == 'subject'
    assert e.body == 'message'
    assert e.attachments == ['file1', 'file2']
    assert e.message is None


##############################################################################
# TESTS: Email.__repr__
##############################################################################

def test_email_repr(get_email, capsys):
    """
    GIVEN a valid Email object
    WHEN the user calls repr() or `>>> e`
    THEN assert the correct format prints
    """
    e = get_email
    print(repr(e))
    out, err = capsys.readouterr()
    assert '<messages.Email class> at: ' in out
    assert err == ''


##############################################################################
# TESTS: Email.__str__
##############################################################################

def test_email_str(get_email, capsys):
    """
    GIVEN a valid Email object
    WHEN the user calls print() on the Email object
    THEN assert the correct format prints
    """
    e = get_email
    expected = ('MIMEMultipart Email:'
                '\n\tServer: smtp.gmail.com:465'
                '\n\tFrom: me@here.com'
                '\n\tTo: you@there.com'
                '\n\tCc: someone@there.com'
                '\n\tBcc: them@there.com'
                '\n\tSubject: subject'
                '\n\tbody: message...'
                '\n\tattachments: [\'file1\', \'file2\']\n')
    print(e)
    out, err = capsys.readouterr()
    assert out == expected
    assert err == ''


##############################################################################
# TESTS: Email.get_server
##############################################################################

def test_get_server_known(get_email):
    """
    GIVEN a valid Email object
    WHEN get_server() is called with an email address
    THEN assert a known smtp server is returned
    """
    e = get_email
    server = e.get_server('me@gmail.com')
    assert server == ('smtp.gmail.com', 465)


def test_get_server_guess(get_email):
    """
    GIVEN a valid Email object
    WHEN get_server() is called with an email address
    THEN assert an smtp server guess is returned
    """
    e = get_email
    server = e.get_server('me@test.com')
    assert server == ('smtp.test.com', 465)


def test_get_server_noAddress(get_email):
    """
    GIVEN a valid Email object
    WHEN get_server() is called without an email address
    THEN assert (None, None) is returned
    """
    e = get_email
    e.from_ = None
    server = e.get_server(e.from_)
    assert server == (None, None)


##############################################################################
# TESTS: Email.list_to_string
##############################################################################

def test_list_to_string(get_email):
    """
    GIVEN a valid Email object
    WHEN given a list of recipients
    THEN assert the list is returned as a single string
    """
    e = get_email
    output = e.list_to_string(['her@there.com', 'him@there.com'])
    assert output == 'her@there.com, him@there.com'


##############################################################################
# TESTS: Email.generate_email
##############################################################################

def test_generate_email(get_email, mocker):
    """
    GIVEN a valid Email object
    WHEN Email.generate_email() is called
    THEN assert the email structure is created
    """
    header_mock = mocker.patch.object(Email, 'add_header')
    body_mock = mocker.patch.object(Email, 'add_body')
    attach_mock = mocker.patch.object(Email, 'add_attachments')
    e = get_email
    e.generate_email()
    assert isinstance(e.message, MIMEMultipart)
    assert header_mock.call_count == 1
    assert body_mock.call_count == 1
    assert attach_mock.call_count == 1


##############################################################################
# TESTS: Email.add_header
##############################################################################

def test_add_header(get_email, mocker):
    """
    GIVEN a valid Email object, where Email.generate_email() has been called
    WHEN Email.add_header() is called
    THEN assert correct parameters are set
    """
    body_mock = mocker.patch.object(Email, 'add_body')
    attach_mock = mocker.patch.object(Email, 'add_attachments')
    e = get_email
    e.generate_email()
    assert e.message['From'] == 'me@here.com'
    assert e.message['Subject'] == 'subject'


##############################################################################
# TESTS: Email.add_body
##############################################################################

def test_add_body(get_email, mocker):
    """
    GIVEN a valid Email object, where Email.generate_email() has been called
    WHEN Email.add_body() is called
    THEN assert body_text is attached
    """
    attach_mock = mocker.patch.object(Email, 'add_attachments')
    header_mock = mocker.patch.object(Email, 'add_header')
    mime_attach_mock = mocker.patch.object(MIMEMultipart, 'attach')
    e = get_email
    e.generate_email()
    assert mime_attach_mock.call_count == 1


##############################################################################
# TESTS: Email.add_attachments
##############################################################################

@travis
def test_add_attachments_list_local(get_email, mocker):
    """
    GIVEN a valid Email object, where Email.generate_email() has been called
        and Email.attachments is a list
    WHEN Email.add_attachments() is called
    THEN assert correct attachments are attached
    """
    header_mock = mocker.patch.object(Email, 'add_header')
    body_mock = mocker.patch.object(Email, 'add_body')
    mime_attach_mock = mocker.patch.object(MIMEMultipart, 'attach')
    e = get_email
    e.attachments = ['tests/data/file1.txt', 'tests/data/file2.png',
                     'tests/data/file3.pdf', 'tests/data/file4.xlsx']
    e.generate_email()
    assert mime_attach_mock.call_count == 4


@not_travis
def test_add_attachments_list_travis(get_email, mocker):
    """
    GIVEN a valid Email object, where Email.generate_email() has been called
         and Email.attachments is a list
    WHEN Email.add_attachments() is called
    THEN assert correct attachments are attached
    """
    header_mock = mocker.patch.object(Email, 'add_header')
    body_mock = mocker.patch.object(Email, 'add_body')
    mime_attach_mock = mocker.patch.object(MIMEMultipart, 'attach')
    e = get_email
    PATH = '/home/travis/build/trp07/messages/tests/data/'
    e.attachments = [PATH + 'file1.txt', PATH + 'file2.png',
                     PATH + 'file3.pdf', PATH + 'file4.xlsx']
    e.generate_email()
    assert mime_attach_mock.call_count == 4


@travis
def test_add_attachments_str_local(get_email, mocker):
    """
    GIVEN a valid Email object, where Email.generate_email() has been called
        and Email.attachments is a str
    WHEN Email.add_attachments() is called
    THEN assert correct attachments are attached
    """
    header_mock = mocker.patch.object(Email, 'add_header')
    body_mock = mocker.patch.object(Email, 'add_body')
    mime_attach_mock = mocker.patch.object(MIMEMultipart, 'attach')
    e = get_email
    e = get_email
    e.attachments = 'tests/data/file1.txt'
    e.generate_email()
    assert mime_attach_mock.call_count == 1


@not_travis
def test_add_attachments_str_travis(get_email, mocker):
    """
    GIVEN a valid Email object, where Email.generate_email() has been called
         and Email.attachments is a str
    WHEN Email.add_attachments() is called
    THEN assert correct attachments are attached
    """
    header_mock = mocker.patch.object(Email, 'add_header')
    body_mock = mocker.patch.object(Email, 'add_body')
    mime_attach_mock = mocker.patch.object(MIMEMultipart, 'attach')
    e = get_email
    e = get_email
    PATH = '/home/travis/build/trp07/messages/tests/data/'
    e.attachments = PATH + 'file1.txt'
    e.generate_email()
    assert mime_attach_mock.call_count == 1


##############################################################################
# TESTS: Email.get_session
##############################################################################

def test_get_session_ssl(get_email, mocker):
    """
    GIVEN a valid Email object
    WHEN Email.get_session() is called
    THEN assert the correct functions are called
    """
    getssl_mock = mocker.patch.object(Email, 'get_ssl')
    gen_email_mock = mocker.patch.object(Email, 'generate_email')
    e = get_email
    e.generate_email()
    e.get_session()
    assert getssl_mock.call_count == 1


def test_get_session_tls(get_email, mocker):
    """
    GIVEN a valid Email object
    WHEN Email.get_session() is called
    THEN assert the correct functions are called
    """
    gettls_mock = mocker.patch.object(Email, 'get_tls')
    gen_email_mock = mocker.patch.object(Email, 'generate_email')
    e = get_email
    e.port = 587
    e.generate_email()
    e.get_session()
    assert gettls_mock.call_count == 1


##############################################################################
# TESTS: Email.get_ssl
##############################################################################

def test_get_ssl(get_email, mocker):
    """
    GIVEN a valid Email object
    WHEN Email.get_ssl() is called
    THEN assert an SMTP_SSL instance is invoked
    """
    smtpssl_mock = mocker.patch.object(smtplib, 'SMTP_SSL')
    e = get_email
    e.get_ssl()
    assert smtpssl_mock.call_count == 1


##############################################################################
# TESTS: Email.get_tls
##############################################################################

def test_get_tls(get_email, mocker):
    """
    GIVEN a valid Email object
    WHEN Email.get_tls() is called
    THEN assert an SMTP instance is invoked
    """
    smtp_mock = mocker.patch.object(smtplib, 'SMTP')
    e = get_email
    e.get_tls()
    assert smtp_mock.call_count == 1


##############################################################################
# TESTS: Email.send
##############################################################################

def test_send(get_email, capsys, mocker):
    """
    GIVEN a valid Email object
    WHEN Email.send() is called
    THEN assert the correct functions are called and correct attributes
        updated
    """
    header_mock = mocker.patch.object(Email, 'add_header')
    body_mock = mocker.patch.object(Email, 'add_body')
    attach_mock = mocker.patch.object(Email, 'add_attachments')
    session_mock = mocker.patch.object(Email, 'get_session')
    e = get_email
    e.send()
    out, err = capsys.readouterr()
    assert out == 'Message sent...\n'
    assert err == ''


##############################################################################
# TESTS: Email.send_async
##############################################################################

def test_send_async(get_email, mocker):
    """
    GIVEN a valid Email object
    WHEN Email.send_async() is called
    THEN assert it is added to the event loop for async sending
    """
    msg_loop_mock = mocker.patch.object(MESSAGELOOP, 'add_message')
    e = get_email
    e.send_async()
    assert msg_loop_mock.call_count == 1
