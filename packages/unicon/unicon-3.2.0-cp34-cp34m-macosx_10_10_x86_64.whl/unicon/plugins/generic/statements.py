"""
Module:
    unicon.plugins.generic

Authors:
    ATS TEAM (ats-dev@cisco.com, CSG( STEP) - India)

Description:
    Module for defining all the Statements and callback required for the
    Current implementation
"""
import re
from time import sleep
from unicon.eal.dialogs import Statement
from unicon.eal.helpers import sendline
from unicon.core.errors import UniconAuthenticationError
from unicon.plugins.generic.patterns import GenericPatterns
from unicon.plugins.generic.settings import GenericSettings

pat = GenericPatterns()

#############################################################
#  Callbacks
#############################################################

def connection_refused_handler(spawn):
    """ handles connection refused scenarios
    """
    raise Exception('Connection refused to device %s' % (str(spawn),))


def connection_failure_handler(spawn, err):
    raise Exception(err)


def chatty_term_wait(spawn, trim_buffer=False):
    """ Wait a small amount of time for any chatter to cease from the device.
    """
    prev_buf_len = len(spawn.buffer)
    for retry_number in range(
            spawn.settings.ESCAPE_CHAR_CHATTY_TERM_WAIT_RETRIES):

        sleep(spawn.settings.ESCAPE_CHAR_CHATTY_TERM_WAIT)

        spawn.read_update_buffer()
        
        cur_buf_len = len(spawn.buffer)
        
        if prev_buf_len == cur_buf_len:
            break
        else:
            prev_buf_len = cur_buf_len
            if trim_buffer:
                spawn.trim_buffer()


def escape_char_callback(spawn):
    """ Wait a small amount of time for terminal chatter to cease before
    attempting to obtain prompt, do not attempt to obtain prompt if login message is seen.
    """

    chatty_term_wait(spawn)

    # Device is already asking for authentication
    if re.search('.*(User Access Verification|sername:\s*$|assword:\s*$|login:\s*$)', spawn.buffer):
        return

    # try and get to the first prompt
    # best effort handling of network delays and connection establishing

    # store current know buffer
    known_buffer = len(spawn.buffer.strip())

    for retry_number in range(spawn.settings.ESCAPE_CHAR_PROMPT_WAIT_RETRIES):
        # hit enter
        spawn.sendline()
        spawn.read_update_buffer()

        # incremental sleep logic
        sleep(spawn.settings.ESCAPE_CHAR_PROMPT_WAIT*(retry_number+1))

        # did we get prompt after?
        spawn.read_update_buffer()

        # check buffer
        if known_buffer != len(spawn.buffer.strip()):
            # we got new stuff - assume it's the the prompt, get out
            break

def ssh_continue_connecting(spawn):
    """ handles SSH new key prompt
    """
    sleep(0.1)
    spawn.sendline('yes')


def login_handler(spawn, context, session):
    """ handles login prompt
    """
    spawn.sendline(context['username'])
    session['tacacs_login'] = 1


def user_access_verification(session):
    # Enable the tacacs_login flag
    session['tacacs_login'] = 1


def password_handler(spawn, context, session):
    """ handles password prompt
    """
    if 'password_attempts' not in session:
        session['password_attempts'] = 1
    else:
        session['password_attempts'] += 1
    if session.password_attempts > spawn.settings.PASSWORD_ATTEMPTS:
        raise UniconAuthenticationError('Too many password retries')

    spawn_command = spawn.spawn_command
    spawn_command_list = spawn_command.split()
    protocol = spawn_command_list[0]

    if session.get('try_enable_password'):
        spawn.sendline(context['enable_password'])
        session['try_enable_password'] = 0
    elif session.get('tacacs_login') == 1:
        spawn.sendline(context['tacacs_password'])
        session['tacacs_login'] = 0
        # if this password fails, try with enable password
        session['try_enable_password'] = 1
    elif protocol == 'ssh':
        if '-l' in spawn_command_list \
                or re.search(r'\S+@\S+', spawn_command) \
                or re.search(r'\S+@\S+.*assword:', spawn.match.match_output):
            spawn.sendline(context['tacacs_password'])
            session['tacacs_login'] = 0
            # if this password fails, try with enable password
            session['try_enable_password'] = 1
        else:
            spawn.sendline(context['enable_password'])
            # if this password fails, try with tacacs password
            session['tacacs_login'] = 1
    else:
        spawn.sendline(context['enable_password'])
        # if this password fails, try with tacacs password
        session['tacacs_login'] = 1


def bad_password_handler(spawn):
    """ handles bad password prompt
    """
    raise UniconAuthenticationError('Bad Password send to device %s' % (str(spawn),))

def incorrect_login_handler(spawn, session):


    if 'incorrect_login_retry' not in session:
        session['incorrect_login_attempts'] = 1

    # Let's give a change for unicon to login with right credentials
    # let's give three attempts
    if session['incorrect_login_attempts'] <=3:
        session['incorrect_login_attempts'] = session['incorrect_login_attempts'] + 1
    else:
        raise UniconAuthenticationError('Login failure, either wrong username or password')

def wait_and_enter(spawn):
    sleep(0.5)  # otherwise newline is sometimes lost?
    spawn.sendline()


#############################################################
#  Generic statements
#############################################################

class GenericStatements():
    """
        Class that defines All the Statements for Generic platform
        implementation
    """

    def __init__(self):
        '''
         All generic Statements
        '''
        self.escape_char_stmt = Statement(pattern=pat.escape_char,
                                          action=escape_char_callback,
                                          args=None,
                                          loop_continue=True,
                                          continue_timer=False)
        self.press_return_stmt = Statement(pattern=pat.press_return,
                                           action=sendline, args=None,
                                           loop_continue=True,
                                           continue_timer=False)
        self.connection_refused_stmt = \
            Statement(pattern=pat.connection_refused,
                      action=connection_refused_handler,
                      args=None,
                      loop_continue=False,
                      continue_timer=False)

        self.bad_password_stmt = Statement(pattern=pat.bad_passwords,
                                           action=bad_password_handler,
                                           args=None,
                                           loop_continue=False,
                                           continue_timer=False)

        self.login_incorrect = Statement(pattern=pat.login_incorrect,
                                           action=incorrect_login_handler,
                                           args=None,
                                           loop_continue=True,
                                           continue_timer=False)

        self.disconnect_error_stmt = Statement(pattern=pat.disconnect_message,
                                               action=connection_failure_handler,
                                               args={
                                               'err': 'received disconnect from router'},
                                               loop_continue=False,
                                               continue_timer=False)
        self.login_stmt = Statement(pattern=pat.username,
                                    action=login_handler,
                                    args=None,
                                    loop_continue=True,
                                    continue_timer=False)
        self.useraccess_stmt = Statement(pattern=pat.useracess,
                                         action=user_access_verification,
                                         args=None,
                                         loop_continue=True,
                                         continue_timer=False)
        self.password_stmt = Statement(pattern=pat.password,
                                       action=password_handler,
                                       args=None,
                                       loop_continue=True,
                                       continue_timer=False)
        self.password_ok_stmt = Statement(pattern=pat.password_ok,
                                             action=sendline,
                                             args=None,
                                             loop_continue=True,
                                             continue_timer=False)
        self.more_prompt_stmt = Statement(pattern=pat.more_prompt,
                                          action=sendline,
                                          args={'command': ' '},
                                          loop_continue=True,
                                          continue_timer=False)
        self.confirm_prompt_stmt = Statement(pattern=pat.confirm_prompt,
                                             action=sendline,
                                             args=None,
                                             loop_continue=True,
                                             continue_timer=False)
        self.yes_no_stmt = Statement(pattern=pat.yes_no_prompt,
                                     action=sendline,
                                     args={'command': 'y'},
                                     loop_continue=True,
                                     continue_timer=False)

        self.continue_connect_stmt = Statement(pattern=pat.continue_connect,
                                action=ssh_continue_connecting,
                                args=None,
                                loop_continue=True,
                                continue_timer=False)

        self.hit_enter_stmt = Statement(pattern=pat.hit_enter,
                                action=wait_and_enter,
                                args=None,
                                loop_continue=True,
                                continue_timer=False)

        self.press_ctrlx_stmt = Statement(pattern=pat.press_ctrlx,
                                              action=wait_and_enter,
                                              args=None,
                                              loop_continue=True,
                                              continue_timer=False)

#############################################################
#  Statement lists
#############################################################

generic_statements = GenericStatements()
#############################################################
# Initial connection Statements
#############################################################

pre_connection_statement_list = [generic_statements.escape_char_stmt,
                                 generic_statements.press_return_stmt,
                                 generic_statements.continue_connect_stmt,
                                 generic_statements.connection_refused_stmt,
                                 generic_statements.disconnect_error_stmt,
                                 generic_statements.hit_enter_stmt,
                                 generic_statements.press_ctrlx_stmt]

#############################################################
# Authentication Statements
#############################################################

authentication_statement_list = [generic_statements.bad_password_stmt,
                                 generic_statements.login_incorrect,
                                 generic_statements.login_stmt,
                                 generic_statements.useraccess_stmt,
                                 generic_statements.password_stmt
                                 ]

connection_statement_list = authentication_statement_list + pre_connection_statement_list
