"""
Module:
    unicon.plugins.generic.service_implementation

Authors:
    ATS TEAM (ats-dev@cisco.com, CSG( STEP) - India)

Description:
  This module contains dual-rp and single rp service implementation
  code for generic platform. These services are implemented by subclassing
  BaseService and handle majority of platforms.

"""

import re
import collections

from time import sleep

from unicon.bases.routers.services import BaseService
from unicon.core.errors import SubCommandFailure
from unicon.eal.dialogs import Dialog
from unicon.eal.dialogs import Statement
from unicon.eal.utils import expect_log
from unicon.plugins.generic.service_statements import login_stmt, password_stmt
from unicon.plugins.generic.service_statements import reload_statement_list, \
    ping_dialog_list, extended_ping_dialog_list, copy_statement_list, \
    ha_reload_statement_list, switchover_statement_list, \
    standby_reset_rp_statement_list
from unicon.utils import AttributeDict

from unicon.plugins.generic import GenericUtils

utils = GenericUtils()


class Send(BaseService):
    """Service to send the command/string with "\\r" to spawned channel.

    If target is passed as standby, command will be sent to standby spawn.

    Arguments:
        command: Command to be sent.
        target: Target connection, Defaults to active.

    Returns:
        True: on Success

    Raises:
        SubCommandFailure: on failure.

    Example:
        .. code-block:: python

            rtr.send("show clock\\r")
            rtr.send("show clock\\r", target='standby')

    """

    def log_service_call(self):
        pass

    def pre_service(self, *args, **kwargs):
        pass

    def post_service(self, *args, **kwargs):
        pass

    def call_service(self, command, target=None, *args, **kwargs):
        spawn = self.get_spawn(target)
        try:
            spawn.send(command, *args, **kwargs)
        except Exception as err:
            raise SubCommandFailure("Failed to send the command to spawn",
                                    err)
        self.result = True

    def get_service_result(self):
        return self.result


class Sendline(BaseService):
    """ Sendline Service

    Service to  send the command/string to spawned channel,
    "\\r" will be appended to command by sendline. If target
    is passed as standby, command will be sent to standby
    spawn.

    Arguments:
        command: Command to be sent
        target: Target connection, Defaults to active

    Returns:
        True: on Success

    Raises:
        SubCommandFailureError: On failure of service

    Example:
        .. code-block:: python

            rtr.sendline("show clock")
            rtr.sendline("show clock", target='standby')
    """

    def log_service_call(self):
        pass

    def pre_service(self, *args, **kwargs):
        pass

    def post_service(self, *args, **kwargs):
        pass

    def call_service(self, command='', target=None, *args, **kwargs):
        spawn = self.get_spawn(target)
        try:
            spawn.sendline(command, *args, **kwargs)
        except Exception as err:
            raise SubCommandFailure("Failed to send the command to spawn",
                                    err)
        self.result = True

    def get_service_result(self):
        return self.result


class Expect(BaseService):
    """match a list of pattern again the buffer

    Arguments:
        patterns: list of patterns.
        timeout: time to wait for any of the patterns to match.
        size: read size in bytes for reading the buffer.
        trim_buffer: whether to trim the buffer after a successful match.
        target: ``standby`` to match a list of patterns against the buffer on standby spawn channel.
        search_size: maximum size in bytes to search at the end of the buffer

    Returns:
        ExpectMatch instance.
        * It contains the index of the pattern that matched.
        * matched string.
        * re match object.

    Raises:
        TimeoutError: In case no match is found within the timeout period
        or raise SubCommandFailure on failure.

    Example:
        .. code-block:: python

            rtr.sendline("a command")
            rtr.expect([r'^pat1', r'pat2'], timeout=10, target='standby')
    """

    def log_service_call(self):
        pass

    def pre_service(self, *args, **kwargs):
        pass

    def post_service(self, *args, **kwargs):
        pass

    def call_service(self, patterns, timeout=None,
                     size=None, trim_buffer=True,
                     target=None, *args, **kwargs):

        spawn = self.get_spawn(target)
        try:
            self.result = spawn.expect(patterns, timeout, size, *args, **kwargs)
        except Exception as err:
            raise SubCommandFailure("Failed to match buffer on spawn",
                                    err)

    def get_service_result(self):
        return self.result


class LogUser(BaseService):
    """ Service to enable or disable a device logs on screen.

    Arguments:
        enable: True/False

    Example:
        .. code-block:: python

            rtr.log_user(enable=True)
            rtr.log_user(enable=False)
    """

    def log_service_call(self):
        pass

    def pre_service(self, *args, **kwargs):
        pass

    def post_service(self, *args, **kwargs):
        pass

    def call_service(self, enable, target=None, *args, **kwargs):
        con = self.connection
        con.log.debug("+++ log_user  +++")
        spawn = self.get_spawn(target)
        try:
            spawn.log_user = enable
        except Exception as err:
            raise SubCommandFailure("Failed disable/enable screen logging",
                                    err)
        self.result = True

    def get_service_result(self):
        return self.result


class ExpectLogging(BaseService):
    """ Service to enable expect internal logging.

    By default it enables on both file and screen, provided filename is specified.
    If not it will log the message on screen.

    Arguments:
        filename: File name to log the messages
        enable: True/False for enabling and disabling the expect_log
        logto: stdout/file to enable logging on screen/file or both.


    Example:

        .. code::

            rtr.expect_log(filename='/ws/lshekhar-bgl/rtr-expect.log', enable=True)
            rtr.execute("term length 0")
            Expect Sending  term length 0
            Expect Got :: 'term len'
            Expect Got :: 'gth 0\\r\\r\\n\\rn7k2-1# '
            Expect Got  ::  'term length 0\\r\\r\\n\\rn7k2-1# '
            Pattern Matched:: ^(.*?)(n7k2-1|Router|RouterRP|RouterRP-standby|n7k2-1-standby|n7k2-1\(standby\)|n7k2-1-sdby|(S|s)witch|Controller|ios|-Slot[0-9]+)(\(boot\))*#\s?$
            Pattern List:: ['^.*--\\s?[Mm]ore\\s?--', '^.*\\[confirm\\(y/n\\)?\\]', '^.*\\[yes/no\\]\\s?:?$', '^(.*?)(n7k2-1|Router|RouterRP|RouterRP-standby|n7k2-1-standby|n7k2-1\\(standby\\)|n7k2-1-sdby|(S|s)witch|Controller|ios|-Slot[0-9]+)(\\(boot\\))*#\\s?$']

        .. code::

            rtr.execute("term width 511")
            Expect Sending  term width 511
            Expect Got :: 'term width 511\\r\\r\\n'
            Expect Got :: '\\rn7k2-1# '
            Expect Got  ::  'term width 511\\r\\r\\n\\rn7k2-1# '
            Pattern Matched:: ^(.*?)(n7k2-1|Router|RouterRP|RouterRP-standby|n7k2-1-standby|n7k2-1\(standby\)|n7k2-1-sdby|(S|s)witch|Controller|ios|-Slot[0-9]+)(\(boot\))*#\s?$
            Pattern List:: ['^.*--\\s?[Mm]ore\\s?--', '^.*\\[confirm\\(y/n\\)?\\]', '^.*\\[yes/no\\]\\s?:?$', '^(.*?)(n7k2-1|Router|RouterRP|RouterRP-standby|n7k2-1-standby|n7k2-1\\(standby\\)|n7k2-1-sdby|(S|s)witch|Controller|ios|-Slot[0-9]+)(\\(boot\\))*#\\s?$', '^.*--\\s?[Mm]ore\\s?--', '^.*\\[confirm\\(y/n\\)?\\]', '^.*\\[yes/no\\]\\s?:?$', '^(.*?)(n7k2-1|Router|RouterRP|RouterRP-standby|n7k2-1-standby|n7k2-1\\(standby\\)|n7k2-1-sdby|(S|s)witch|Controller|ios|-Slot[0-9]+)(\\(boot\\))*#\\s?$']
    """

    def log_service_call(self):
        pass

    def pre_service(self, *args, **kwargs):
        pass

    def post_service(self, *args, **kwargs):
        pass

    def call_service(self, filename='',
                     enable=False,
                     logto='stdout',
                     *args, **kwargs):

        con = self.connection
        filename = filename
        enable = enable
        logto = logto
        con.log.debug("+++ expect_log  +++")
        try:
            expect_log(filename=filename,
                       enable=enable,
                       logto=logto)
        except Exception as err:
            raise SubCommandFailure("Failed to enable/disable expect_log",
                                    err)
        self.result = True

    def get_service_result(self):
        return self.result


class Enable(BaseService):
    """ Brings device to enable

    Service to change the device mode to enable from any state.
    Brings the standby handle to enable state, if standby is passed as input.

    Arguments:
        target= Target connection, Defaults to active

    Returns:
        True on Success, raise SubCommandFailure on failure

    Example:
        .. code-block:: python

            rtr.enable()
            rtr.enable(target='standby')
    """

    def __init__(self, connection, context, **kwargs):
        # Connection object will have all the received details
        super().__init__(connection, context, **kwargs)
        self.start_state = 'enable'
        self.end_state = 'enable'
        self.service_name = 'enable'
        self.__dict__.update(kwargs)

    def call_service(self, target=None, *args, **kwargs):
        spawn = self.get_spawn(target)
        sm = self.get_sm(target)
        try:
            sm.go_to(self.start_state,
                     spawn,
                     context=self.context)
        except Exception as err:
            raise SubCommandFailure("Failed to Bring device to Enable State",
                                    err)
        self.result = True


class Disable(BaseService):
    """Service to change the device to disable mode from any state.

    Brings the standby handle to disable state, if standby is passed as
    input.

    Arguments:
        target: Target connection, Defaults to active

    Returns:
        True on Success, raise SubCommandFailure on failure

    Example:
        .. code-block:: python

            rtr.disable()
            rtr.disable(target='standby')
    """

    def __init__(self, connection, context, **kwargs):
        super().__init__(connection, context, **kwargs)
        self.start_state = 'disable'
        self.end_state = 'disable'
        self.service_name = 'disable'
        self.__dict__.update(kwargs)

    def call_service(self, target=None, *args, **kwargs):
        spawn = self.get_spawn(target)
        sm = self.get_sm(target)
        try:
            sm.go_to(self.start_state,
                     spawn,
                     context=self.context)
        except Exception as err:
            raise SubCommandFailure("Failed to Bring device to Disable State",
                                    err)
        self.result = True


class Execute(BaseService):
    """ Execute Service implementation

    Service  to executes exec_commands on the device and return the
    console output. reply option can be passed for the interactive exec
    command.

    Arguments:
        command: string or list of strings
        reply: Additional Dialog patterns for interactive exec commands.
        timeout : Timeout value in sec, Default Value is 60 sec
        error_pattern: list of regex to detect command errors
        search_size: maximum size in bytes to search at the end of the buffer

    Returns:
        String for single command, list for repeated single command,
        dict for multiple commands.

        raises SubCommandFailure on failure

    Example:
        .. code-block:: python

              output = rtr.execute("show clock")

    """

    def __init__(self, connection, context, **kwargs):
        # Connection object will have all the received details
        super().__init__(connection, context, **kwargs)
        self.service_name = 'execute'
        self.timeout = connection.settings.EXEC_TIMEOUT
        self.__dict__.update(kwargs)
        self.utils = utils

    def log_service_call(self):
        pass

    def pre_service(self, *args, **kwargs):
        self.prompt_recovery = kwargs.get('prompt_recovery', False)

    def post_service(self, *args, **kwargs):
        pass

    def call_service(self, command=[],
                     reply=Dialog([]),
                     timeout=None,
                     error_pattern=None,
                     search_size=None,
                     *args, **kwargs):

        con = self.connection
        sm = self.get_sm()
        self.start_state = sm.current_state

        timeout = timeout or self.timeout

        if error_pattern is None:
            self.error_pattern = con.settings.ERROR_PATTERN
        else:
            self.error_pattern = error_pattern

        # user specified search buffer size
        if search_size is not None:
            con.spawn.search_size = search_size
        else:
            con.spawn.search_size = con.settings.SEARCH_SIZE

        if not isinstance(reply, Dialog):
            raise SubCommandFailure(
                "dialog passed via 'reply' must be an instance of Dialog")

        dialog = self.service_dialog(service_dialog=reply)
        # Add all known states to detect state changes.
        for state in sm.states:
            # The current state is already added by the service_dialog method
            if state.name != sm.current_state:
                dialog.append(Statement(pattern=state.pattern))

        if isinstance(command, str):
            if len(command) == 0:
                commands = ['']
            else:
                commands = command.splitlines()
        elif isinstance(command, list):
            commands = command
        else:
            raise ValueError('Command passed is not of type string or list (%s)' % type(command))

        command_output = {}
        for command in commands:
            con.log.info("+++ execute command '%s' +++" % command)
            con.sendline(command)
            try:
                self.result = dialog.process(con.spawn,
                                             timeout=timeout,
                                             prompt_recovery=self.prompt_recovery,
                                             context=con.context)
                if self.result:
                    self.result = self.result.match_output
                    self.result = self.get_service_result()
                sm.detect_state(con.spawn)

            except Exception as err:
                raise SubCommandFailure("Command execution failed", err)

            if self.result:
                output = self.utils.truncate_trailing_prompt(
                            sm.get_state(sm.current_state),
                            self.result,
                            self.connection.hostname)
                output = output.replace(command, "", 1)
                # only strip first newline and leave formatting intact
                output = re.sub(r"^\r?\r\n", "", output, 1)
                output = output.rstrip()

                if command in command_output:
                    if isinstance(command_output[command], list):
                        command_output[command].append(output)
                    else:
                        command_output[command] = [command_output[command], output]
                else:
                    command_output[command] = output

        if len(command_output) == 1:
            self.result = list(command_output.values())[0]
        else:
            self.result = command_output

        # revert search size to default
        con.spawn.search_size = con.settings.SEARCH_SIZE


class Configure(BaseService):
    """ Service to configure device with list of `commands`.

    Config without config_command will take device to config mode.
    Commands Should be list, if `config_command` are more than one.
    reply option can be passed for the interactive config command.

    Arguments:
        <commands> : list/single config command
        reply: Addition Dialogs for interactive config commands.
        timeout : Timeout value in sec, Default Value is 30 sec

    Returns:
        True on Success, raise SubCommandFailure on failure

    Example:
        .. code-block:: python

              output = rtr.configure()
              output = rtr.configure("no logging console")
              cmd =["hostname si-tvt-7200-28-41", "no logging console"]
              output = rtr.configure(cmd)

    """

    def __init__(self, connection, context, **kwargs):
        super().__init__(connection, context, **kwargs)
        self.start_state = 'config'
        self.end_state = 'enable'
        self.service_name = 'config'
        self.timeout = connection.settings.CONFIG_TIMEOUT
        self.__dict__.update(kwargs)

    def call_service(self, command=[],
                     reply=Dialog([]),
                     timeout=None,
                     *args, **kwargs):

        timeout = timeout or self.timeout
        if isinstance(command, str):
            command = command.splitlines()
        self.command_list_is_empty = False
        spawn = self.get_spawn()
        sm = self.get_sm()
        if not isinstance(reply, Dialog):
            raise SubCommandFailure(
                "dialog passed via 'reply' must be an instance of Dialog")

        if len(command) == 0:
            sm.go_to(self.start_state,
                     spawn,
                     prompt_recovery=self.prompt_recovery,
                     context=self.connection.context)
            self.result = " "
            self.command_list_is_empty = True
        # if commands is a list
        if isinstance(command, collections.Sequence):
            # No command passed, just move to config mode
            if len(command) == 0:
                self.result = " "
                self.command_list_is_empty = True
            else:
                dialog = self.service_dialog(service_dialog=reply)
                # Commands are list of more than one command
                self.result = ''
                for cmd in command:
                    spawn.sendline(cmd)
                    try:
                        cmd_result = dialog.process(spawn,
                                                     timeout=timeout,
                                                     prompt_recovery=self.prompt_recovery,
                                                     context=self.context)
                    except Exception as err:
                        raise SubCommandFailure("Configuration failed", err)
                    cmd_result = cmd_result.match_output
                    if cmd_result.rfind(self.connection.hostname):
                        cmd_result = cmd_result[:cmd_result.rfind(self.connection.hostname)]
                    self.result += cmd_result
                sm.go_to(self.end_state, spawn, prompt_recovery=self.prompt_recovery, context=self.context)

    def post_service(self, *args, **kwargs):
        if self.command_list_is_empty:
            pass
        else:
            state_machine = self.connection.state_machine
            state_machine.go_to(self.end_state,
                                self.connection.spawn,
                                prompt_recovery=self.prompt_recovery,
                                context=self.connection.context)


class Config(Configure):

    def call_service(self, *args, **kwargs):
        self.connection.log.warn('**** This service is deprecated. ' +
                                 'Please use "configure" service ****')
        super().call_service(*args, **kwargs)

class Reload(BaseService):
    """Service to reload the device.

    Arguments:
        reload_command: reload command to be issued. default is "reload"
        dialog: Dialog which include list of Statements for
                additional dialogs prompted by reload command, in-case
                it is not in the current list.
        timeout: Timeout value in sec, Default Value is 300 sec

    Returns:
        True on Success, raise SubCommandFailure on failure

    Example ::
        .. code-block:: python

                  rtr.reload()
                  # If reload command is other than 'reload'
                  rtr.reload(reload_command="reload location all", timeout=400)

    """

    def __init__(self, connection, context, **kwargs):
        super().__init__(connection, context, **kwargs)
        self.start_state = 'enable'
        self.end_state = 'enable'
        self.service_name = 'reload'
        self.timeout = connection.settings.RELOAD_TIMEOUT
        self.dialog = Dialog(reload_statement_list)
        self.__dict__.update(kwargs)

    def call_service(self,
                     reload_command='reload',
                     dialog=Dialog([]),
                     timeout=None,
                     *args, **kwargs):
        con = self.connection
        timeout = timeout or self.timeout

        fmt_msg = "+++ reloading  %s  " \
                  " with reload_command %s " \
                  "and timeout is %s +++"
        con.log.debug(fmt_msg % (self.connection.hostname,
                                 reload_command,
                                 timeout))

        con.state_machine.go_to(self.end_state,
                                con.spawn,
                                prompt_recovery=self.prompt_recovery,
                                context=self.context)

        if not isinstance(dialog, Dialog):
            raise SubCommandFailure(
                "dialog passed must be an instance of Dialog")

        dialog = dialog
        dialog += self.dialog
        con.spawn.sendline(reload_command)
        try:
            dialog.process(con.spawn,
                           timeout=timeout,
                           prompt_recovery=self.prompt_recovery,
                           context=self.context)
            con.state_machine.go_to(['disable', 'enable'],
                                    con.spawn,
                                    prompt_recovery=self.prompt_recovery,
                                    context=self.context)
        except Exception as err:
            raise SubCommandFailure("Reload failed %s" % err)
        con.state_machine.get_state(self.end_state)
        self.result = True


class Ping(BaseService):
    """ Service to issue ping response request to another network from device.

    Returns:
        ping command response on Success

    Raises:
        SubCommandFailure on failure

    Example:
        .. code-block:: python

            ping(addr="9.33.11.41")
            ping(addr="10.2.1.1", extd_ping='yes')

    """

    def __init__(self, connection, context, **kwargs):
        super().__init__(connection, context, **kwargs)
        self.start_state = 'enable'
        self.end_state = 'enable'
        self.service_name = 'ping'
        self.timeout = 60
        self.dialog = Dialog(extended_ping_dialog_list)
        # Ping error Patterns
        self.error_pattern = ['^.*(% )?DSCP.*does not match any topology',
                              'Bad IP (A|a)ddress', 'Ping transmit failed',
                              'Invalid vrf', 'Unable to find',
                              'No Route to Host.*',
                              'Destination Host Unreachable',
                              'Unable to initialize Windows Socket Interface',
                              'IP routing table .* does not exist',
                              'Invalid input',
                              'bad context', 'Failed to resolve',
                              '(U|u)nknown (H|h)ost',
                              'Success rate is 0 percent',
                              '100.00% packet loss',
                              '100 % packet loss']

        self.__dict__.update(kwargs)

    def call_service(self, addr, command="ping", **kwargs):
        con = self.connection
        con.log.debug("+++ ping +++")
        # Ping Options
        ping_options = ['multicast', 'transport', 'mask', 'vcid', 'tunnel',
                        'dest_start', 'dest_end', 'exp', 'pad', 'ttl',
                        'reply_mode', 'dscp', 'proto', 'count', 'size',
                        'verbose', 'interval', 'timeout_limit',
                        'send_interval', 'vrf', 'src_route_type',
                        'src_route_addr', 'extended_verbose', 'topo',
                        'validate_reply_data', 'force_exp_null_label',
                        'lsp_ping_trace_rev', 'oif', 'tos', 'data_pat',
                        'int', 'udp', 'precedence', 'novell_type',
                        'extended_timeout_limit', 'sweep_min', 'sweep_max',
                        'sweep_interval', 'src_addr', 'df_bit',
                        'ipv6_ext_headers', 'ipv6_hbh_headers',
                        'ipv6_dst_headers', 'ping_packet_timeout',
                        'sweep_ping', 'timestamp_count', 'record_hops',
                        'ping_failures', 'extd_ping', 'addr'
                        ]

        # Default value setting
        timeout = self.timeout

        ping_context = AttributeDict({})
        for a in ping_options:
            if a is "novell_type":
                ping_context[a] = "\r"
            elif a is "sweep_ping":
                ping_context[a] = "n"
            elif a is 'extd_ping':
                ping_context[a] = "n"
            else:
                ping_context[a] = ""

        # Read input values passed
        # Convert to string in case users pass in non-string types such as
        # integer for repeat_count or ipaddress for addr, src_addr or
        # src_route_addr keys.
        # The EAL backend requires all commands to be of string type.
        for key in kwargs:
            ping_context[key] = str(kwargs[key])

        # Validate Inputs
        if ping_context['addr'] is "":
            if addr:
                # Do string conversion on addr, if specified,
                # in case the user passes in an ipaddress object instead of a
                # string.
                ping_context['addr'] = str(addr)
            else:
                raise SubCommandFailure("Address is not specified ")

        if ping_context['src_route_type'] is not "":
            if ping_context['src_route_addr'] in "":
                raise SubCommandFailure("If src route type is set, "
                                        "then src route addr is mandatory \n")
        elif ping_context['src_route_addr'] is not "":
            raise SubCommandFailure("If src route addr is set, "
                                    "then src route type is mandatory \n")
        # Stringify the command in case it is an object.
        ping_str = str(command)

        if ping_context['topo'] is not "":
            ping_str = ping_str + "  topo " + ping_context['topo']

        spawn = self.get_spawn()
        sm = self.get_sm()
        if ping_context['extd_ping'] is "y":
            if self.connection.is_ha:
                dialog = self.service_dialog(service_dialog=self.dialog,
                                             handle=con.active)
            else:
                dialog = self.service_dialog(service_dialog=self.dialog)
        else:
            if self.connection.is_ha:
                dialog = self.service_dialog(
                    service_dialog=Dialog(ping_dialog_list),
                    handle=con.active)
            else:
                dialog = self.service_dialog(
                    service_dialog=Dialog(ping_dialog_list))

        spawn.sendline(ping_str)
        try:
            self.result = dialog.process(
                spawn, context=ping_context, timeout=timeout)
        except Exception as err:
            raise SubCommandFailure("Ping failed", err)

        self.result = self.result.match_output
        if self.result.rfind(self.connection.hostname):
            self.result = self.result[
                          :self.result.rfind(self.connection.hostname)]


class Copy(BaseService):
    """ Implements Copy service

    Service to support variants of the IOS copy command, which basically
    copies images and configs into and out of router Flash memory.

    Arguments:
        timeout: Timeout value in sec, Default Value is 60 sec

    Returns:
        True on Success, raise SubCommandFailure on failure

    Example:
        .. code-block:python

            out = rtr.copy(source='running-conf',
                         dest='startup-config')

            copy_input = {'source' :'tftp:',
                          'dest':'disk0:',
                          'source_file' : 'copy-test',
                          'dest_file':'copy-test'}
            out = rtr.copy(copy_input)

            out = rtr.copy(source = 'tftp:',
                           dest = 'bootflash:',
                           source_file  = 'copy-test',
                           dest_file = 'copy-test',
                           server='10.105.33.158')
    """

    def __init__(self, connection, context, **kwargs):
        super().__init__(connection, context, **kwargs)
        self.start_state = 'enable'
        self.end_state = 'enable'
        self.service_name = 'copy'
        self.timeout = 100
        self.dialog = Dialog(copy_statement_list)
        self.__dict__.update(kwargs)
        if not hasattr(self, 'max_attempts'):
            self.max_attempts = self.connection.settings.MAX_COPY_ATTEMPTS

    def call_service(self, *args, **kwargs):
        con = self.connection
        # Inputs supported
        copy_options = ['source', 'dest', 'dest_file', 'source_file',
                        'server', 'user', 'password', 'vrf', 'erase',
                        'partition', 'overwrite', 'timeout', 'net_type']

        # Default values
        copy_context = AttributeDict({})
        for a in copy_options:
            if a is "partition":
                copy_context[a] = 0
            elif a is "erase":
                copy_context[a] = "n"
            elif a is 'overwrite':
                copy_context[a] = True
            elif a is 'vrf':
                copy_context[a] = "Mgmt-intf"
            elif a is 'timeout':
                copy_context[a] = self.timeout
            else:
                copy_context[a] = ""

        # Read input values passed
        # Stringify input values in case they are objects
        for key in kwargs:
            copy_context[key] = str(kwargs[key])
        # Validate input
        if copy_context['source'] is "" or copy_context['dest'] is "":
            raise SubCommandFailure(
                "Source and Destination must be specified ")

        if copy_context['source_file'] is "":
            copy_context['source_file'] = copy_context['source']
        remote_source = ""
        remote_dest = ""
        copy_match = re.search(
            'ftp:|tftp:|http:|rcp:|scp:', copy_context['source'])
        if copy_match:
            remote_source = copy_match.group()
        copy_match = re.search(
            'ftp:|tftp:|http:|rcp:|scp:', copy_context['dest'])
        if copy_match:
            remote_dest = copy_match.group()

        if remote_dest is not "" or remote_source is not "":
            if copy_context['server'] is "":
                raise SubCommandFailure(
                    "Server address must be specified for remote copy")

        timeout = copy_context['timeout'] or self.timeout
        # get spawn for ha/nan ha handle
        if self.connection.is_ha:
            dialog = self.service_dialog(handle=con.active,
                                         service_dialog=self.dialog)
            handle = con.active
            spawn = con.active.spawn
        else:
            dialog = self.service_dialog(service_dialog=self.dialog)
            handle = con
            spawn = con.spawn

        copy_string = "copy  " + \
                      copy_context['source'] + " " + copy_context['dest']

        if self.max_attempts < 1:
            raise SubCommandFailure(
                "Copy failed : max_attempts must be 1 or greater but "
                "{} was specified.".format(self.max_attempts))

        for retry_num in range(self.max_attempts):
            spawn.sendline(copy_string)
            try:
                self.result = dialog.process(spawn,
                                             context=copy_context,
                                             timeout=timeout)
            except Exception as err:
                if retry_num != (self.max_attempts - 1):
                    # Wait for a prompt before retrying.
                    spawn.sendline()
                    handle.state_machine.go_to('any',
                                               handle.spawn,
                                               context=self.context)

                    con.log.info("Copy failure encountered.  Retrying ...")
                else:
                    raise SubCommandFailure("Copy failed", err)

            else:
                break

        self.result = self.result.match_output
        if self.result.rfind(self.connection.hostname):
            self.result = self.result[
                          :self.result.rfind(self.connection.hostname)]


class GetMode(BaseService):
    """ Service to get the redundancy mode of the device.

    Returns:
        'sso', 'rpr' or raise SubCommandFailure on failure.

    Example ::
        .. code-block:: python

            rtr.get_mode()
    """

    def __init__(self, connection, context, **kwargs):
        super().__init__(connection, context, **kwargs)
        self.start_state = 'enable'
        self.end_state = 'enable'
        self.service_name = 'get_mode'
        self.timeout = connection.settings.EXEC_TIMEOUT
        self.__dict__.update(kwargs)

    def call_service(self,
                     target='active',
                     timeout=None,
                     utils=utils,
                     *args,
                     **kwargs):

        timeout = timeout or self.timeout
        try:
            self.result = utils.get_redundancy_details(self.connection,
                                                 timeout=timeout)
        except Exception as err:
            raise SubCommandFailure("get_mode failed", err)

    def get_service_result(self):
        if 'mode' in self.result:
            return self.result.mode
        else:
            return "None"


class GetRPState(BaseService):
    """ Get Rp state

    Service to get the redundancy state of the device rp.
    Returns  standby rp state if standby is passed as input.

    Arguments:
        target: Service target, by default active

    Returns:
        Expected return values are ACTIVE, STANDBY COLD, STANDBY HOT
        raise SubCommandFailure on failure.

    Example:
        .. code-block:: python

            rtr.get_rp_state()
            rtr.get_rp_state(target='standby')
    """

    def __init__(self, connection, context, **kwargs):
        super().__init__(connection, context, **kwargs)
        self.start_state = 'enable'
        self.end_state = 'enable'
        self.service_name = 'get_rp_state'
        self.timeout = connection.settings.EXEC_TIMEOUT
        self.__dict__.update(kwargs)

    def call_service(self,
                     target='active',
                     timeout=None,
                     utils=utils,
                     *args,
                     **kwargs):
        """send the command on the right rp and return the output"""
        handle = 'my'
        if target is 'standby':
            handle = 'peer'

        try:
            self.result = utils.get_redundancy_details(self.connection,
                                                 timeout=timeout,
                                                 who=handle)
        except Exception as err:
            raise SubCommandFailure("get_rp_state failed", err)

    def get_service_result(self):
        if 'state' in self.result:
            return self.result.state
        else:
            return "None"


class GetConfig(BaseService):
    """Service return running configuration of the device.

    Returns:
        standby running configuration if standby is passed as input.

    Arguments:
        target: Service target, by default active

    Returns:
      running configuration on Success, raise SubCommandFailure on failure.

    Example:
        .. code-block:: python

            rtr.get_config()
            rtr.get_config(target='standby')
    """

    def __init__(self, connection, context, **kwargs):
        super().__init__(connection, context, **kwargs)
        self.start_state = 'enable'
        self.end_state = 'enable'
        self.service_name = 'get_config'
        self.timeout = connection.settings.EXEC_TIMEOUT
        self.__dict__.update(kwargs)

    def pre_service(self, *args, **kwargs):
        pass

    def post_service(self, *args, **kwargs):
        pass

    def call_service(self,
                     target='active',
                     timeout=None,
                     *args,
                     **kwargs):
        try:
            self.result = self.connection.execute("show running-config",
                                                  target=target,
                                                  timeout=timeout)
        except Exception as err:
            raise SubCommandFailure("get_config failed", err)


class SyncState(BaseService):
    """Bring the device to stable state and re-designate the handles role.

    Returns:
        True on Success, raises SubcommandFailure exception on failure

    Example:
        .. code-block:: python

            rtr.sync_state()
    """

    def __init__(self, connection, context, **kwargs):
        super().__init__(connection, context, **kwargs)
        self.start_state = 'enable'
        self.end_state = 'enable'
        self.service_name = 'sync_state'
        self.timeout = connection.settings.EXEC_TIMEOUT
        self.__dict__.update(kwargs)

    def pre_service(self, *args, **kwargs):
        self.prompt_recovery = kwargs.get('prompt_recovery', False)

    def call_service(self,
                     target='active',
                     timeout=None,
                     *args,
                     **kwargs):

        con = self.connection
        try:
            # ToDo: Missing code to bring the device to stable state
            self.result = con.connection_provider.designate_handles()
        except Exception as err:
            raise SubCommandFailure("Failed to bring the device to stable \
                                    state", err)
        self.result = True

    def get_service_result(self):
        return self.result


class HaExecService(BaseService):
    """ DualRp execute service

    Service  to executes exec_commands on the device and return the
    console output. reply option can be passed for the interactive exec
    command. Command will be executed on standby if target is specified
    as standby.

    Arguments:
        command: exec command
        target: Target RP where to execute service
        reply: Additional Dialog( i.e patterns) to be handled
        timeout: Timeout value in sec, Default Value is 60 sec

    Returns:
        String for single command, list for repeated single command,
        dict for multiple commands.

        raises SubCommandFailure on failure.

    Example:
        .. code-block:: python

            output = rtr.execute("show clock")
            output = rtr.execute("show logging", timeout=200)
            output = rtr.execute("show clock", target='standby')
    """

    def __init__(self, connection, context, **kwargs):
        super().__init__(connection, context, **kwargs)
        self.service_name = 'execute'
        self.timeout = connection.settings.EXEC_TIMEOUT
        self.__dict__.update(kwargs)

    def pre_service(self, *args, **kwargs):
        self.prompt_recovery = kwargs.get('prompt_recovery', False)

    def post_service(self, *args, **kwargs):
        pass

    def call_service(self, command,
                     reply=Dialog([]),
                     target='active',
                     timeout=None,
                     error_pattern=None,
                     search_size=None,
                     *args,
                     **kwargs):
        """send the command on the right rp and return the output"""
        # create an alias for connection.
        con = self.connection
        # timeout should not be in init because we don't want it
        # to get constructed. User may change the exec timeout and expect it
        # to take effect.
        timeout = timeout or self.timeout

        if error_pattern is None:
            self.error_pattern = con.settings.ERROR_PATTERN
        else:
            self.error_pattern = error_pattern

        if target is 'active':
            handle = con.active
        elif target is 'standby':
            handle = con.standby
        elif target is 'a':
            handle = con.a
        elif target is 'b':
            handle = con.b

        # user specified search buffer size
        if search_size is not None:
            handle.spawn.search_size = search_size
        else:
            handle.spawn.search_size = con.settings.SEARCH_SIZE

        sm = handle.state_machine
        self.start_state = sm.current_state

        dialog = self.service_dialog(handle=handle, service_dialog=reply)
        dialog.append(login_stmt)
        dialog.append(password_stmt)
        # Add all known states to detect state changes.
        for state in sm.states:
            # The current state is already added by the service_dialog method
            if state.name != sm.current_state:
                dialog.append(Statement(pattern=state.pattern))

        if isinstance(command, str):
            if len(command) == 0:
                commands = ['']
            else:
                commands = command.splitlines()
        elif isinstance(command, list):
            commands = command
        else:
            raise ValueError('Command passed is not of type string or list (%s)' % type(command))

        command_output = {}
        for command in commands:
            con.log.info("+++ execute command '%s' +++" % command)

            handle.spawn.sendline(command)
            try:
                self.result = dialog.process(handle.spawn,
                                             timeout=timeout,
                                             prompt_recovery=self.prompt_recovery,
                                             context=con.context)
                if self.result:
                    self.result = self.result.match_output
                    self.result = self.get_service_result()
            except Exception as err:
                raise SubCommandFailure("Command execution failed", err)

            sm.detect_state(handle.spawn)

            if self.result:
                output = utils.truncate_trailing_prompt(
                            sm.get_state(sm.current_state),
                            self.result,
                            self.connection.hostname)
                output = output.replace(command, "", 1)
                output = re.sub(r"^\r?\r\n", "", output, 1)
                output = output.rstrip()

                if command in command_output:
                    if isinstance(command_output[command], list):
                        command_output[command].append(output)
                    else:
                        command_output[command] = [command_output[command], output]
                else:
                    command_output[command] = output

        if len(command_output) == 1:
            self.result = list(command_output.values())[0]
        else:
            self.result = command_output

        # revert search size to default
        handle.spawn.search_size = con.settings.SEARCH_SIZE


# TODO verify the HA config
class HaConfigureService(BaseService):
    """ DualRp config service

    Service to configure device with list of `commands`.
    Config without config_command will take device to config mode.
    Commands Should be list, if `config_command` are more than one.
    reply option can be passed for the interactive config command.
    Command will be executed on standby if target is specified
    as standby.

    Arguments:
        command: list of configuration commands
        target: Target RP where to execute service
        reply: Additional Dialog( i.e patterns) to be handled
        timeout: Timeout value in sec, Default Value is 30 sec

    Returns:
        console output on Success, raises SubCommandFailure on failure.

    Example:
        .. code-block:: python

            output = rtr.configure()
            output = rtr.configure("no logging console")
            cmd =["hostname si-tvt-7200-28-41", "no logging console"]
            output = rtr.configure(cmd)
            output = rtr.configure(cmd, target='standby')
    """

    def __init__(self, connection, context, **kwargs):
        super().__init__(connection, context, **kwargs)
        self.start_state = 'enable'
        self.end_state = 'enable'
        self.service_name = 'config'
        self.timeout = connection.settings.CONFIG_TIMEOUT
        self.__dict__.update(kwargs)

    def pre_service(self, *args, **kwargs):
        self.prompt_recovery = kwargs.get('prompt_recovery', False)

    def call_service(self, command=[],
                     reply=Dialog(),
                     target='active',
                     timeout=None,
                     *args,
                     **kwargs):
        """send the command on the right rp and return the output"""
        # create an alias for connection.
        con = self.connection
        # timeout should not be in init because we don't want it
        # to get constructed. User may change the exec timeout and expect it
        # to take effect.
        if isinstance(command, str):
            command = [command]
        timeout = timeout or self.timeout

        if target is 'active':
            handle = con.active
        elif target is 'standby':
            handle = con.standby
        elif target is 'a':
            handle = con.a
        elif target is 'b':
            handle = con.b

        self.command_list_is_empty = False
        if len(command) == 0:
            self.command_list_is_empty = True
            handle.state_machine.go_to('config',
                                       handle.spawn,
                                       prompt_recovery=self.prompt_recovery,
                                       context=con.context)
            self.result = ""
        elif isinstance(command, collections.Sequence):
            handle.state_machine.go_to('config',
                                       handle.spawn,
                                       prompt_recovery=self.prompt_recovery,
                                       context=self.connection.context)
            dialog = Dialog()
            dialog += reply
            dialog += handle.state_machine.default_dialog
            config = handle.state_machine.get_state('config')
            dialog.append(Statement(config.pattern, loop_continue=False,
                                    continue_timer=False))
            handle.state_machine.go_to('config',
                                       handle.spawn,
                                       prompt_recovery=self.prompt_recovery,
                                       context=con.context)
            self.result = ''
            for c in command:
                con.log.debug("+++ config %s" % c)

                handle.spawn.sendline(c)
                cmd_result = dialog.process(handle.spawn,
                                             context=self.context,
                                             prompt_recovery=self.prompt_recovery,
                                             timeout=timeout)
                cmd_result = cmd_result.match_output
                if cmd_result.rfind(self.connection.hostname):
                    cmd_result = cmd_result[
                                  :cmd_result.rfind(
                                      self.connection.hostname)].strip()
                self.result += cmd_result
            handle.state_machine.go_to(self.end_state, handle.spawn)

    def post_service(self, *args, **kwargs):
        if self.command_list_is_empty:
            pass
        else:
            state_machine = self.connection.active.state_machine
            state_machine.go_to(self.end_state,
                                self.connection.active.spawn,
                                prompt_recovery=self.prompt_recovery,
                                context=self.connection.context)


class HaConfigure(HaConfigureService):

    def call_service(self, *args, **kwargs):
        self.connection.log.warn('**** This service is deprecated. ' +
                                 'Please use "configure" service ****')
        super().call_service(*args, **kwargs)


# TODO Add option to take additional dialog
class HAReloadService(BaseService):
    """ Service to reload the device.

    Arguments:
        command: reload command to be used. default "redundancy reload shelf"
        target: Target RP where to execute service
        reply: Additional Dialog( i.e patterns) to be handled
        timeout: Timeout value in sec, Default Value is 60 sec

    Returns:
        console True on Success, raises SubCommandFailure on failure.

    Example:
        .. code-block:: python

            rtr.reload()
            # If reload command is other than 'redundancy reload shelf'
            rtr.reload(command="reload location all", timeout=700)
    """

    def __init__(self, connection, context, **kwargs):
        super().__init__(connection, context, **kwargs)
        self.start_state = 'disable'
        self.end_state = 'enable'
        self.service_name = 'reload'
        self.timeout = connection.settings.HA_RELOAD_TIMEOUT
        self.dialog = Dialog(ha_reload_statement_list)
        self.command = 'redundancy reload shelf'
        self.__dict__.update(kwargs)

    def call_service(self, command=None,
                     dialog=Dialog([]),
                     target='active',
                     timeout=None,
                     *args,
                     **kwargs):
        con = self.connection
        timeout = timeout or self.timeout
        command = command or self.command

        # TODO counter value must be moved to settings
        counter = 0
        config_retry = 0
        fmt_str = "+++ reloading  %s  with reload_command %s and timeout is %s +++"
        con.log.debug(fmt_str % (con.hostname, command, timeout))
        dialog = dialog
        dialog += self.dialog
        dialog = self.service_dialog(handle=con.active,
                                     service_dialog=dialog)
        con.active.state_machine.go_to('enable',
                                       self.connection.active.spawn,
                                       prompt_recovery=self.prompt_recovery,
                                       context=self.context)
        # Issue reload command
        con.active.spawn.sendline(command)
        try:
            dialog.process(con.active.spawn,
                           context=self.context,
                           prompt_recovery=self.prompt_recovery,
                           timeout=timeout)
            con.active.state_machine.go_to('any',
                                           con.active.spawn,
                                           prompt_recovery=self.prompt_recovery,
                                           context=self.context)
            con.log.info("Waiting for config sync to finish")
            sleep(100)
            # Bring standby to good state.
            stdby_counter = 0
            while(stdby_counter < 3):
               con.standby.spawn.sendline()
               stdby_counter = stdby_counter + 1
               try:
                 con.standby.state_machine.go_to('any',
                          con.standby.spawn,
                          context=self.context,
                          timeout=100,
                          prompt_recovery=self.prompt_recovery,
                          dialog=con.connection_provider.get_connection_dialog())
                 break
               except Exception as err:
                 if stdby_counter >= 3:
                   raise Exception(' Bringing standby to any state failed even after retries') from err
                 con.log.info('Retry in process')
        except Exception as err:
            raise SubCommandFailure("Reload failed : %s" % err)

        # Re-designate handles before applying config.
        self.connection.connection_provider.designate_handles()

        # Issue init commands to disable console logging
        exec_commands = self.connection.settings.HA_INIT_EXEC_COMMANDS
        for command in exec_commands:
            con.execute(command, prompt_recovery=self.prompt_recovery)
        config_commands = self.connection.settings.HA_INIT_CONFIG_COMMANDS
        while config_retry < \
                self.connection.settings.CONFIG_POST_RELOAD_MAX_RETRIES:
            try:
                con.configure(config_commands, timeout=60, prompt_recovery=self.prompt_recovery)
            except Exception as err:
                if re.search("Config mode cannot be entered",
                             str(err)):
                    sleep(self.connection.settings.\
                        CONFIG_POST_RELOAD_RETRY_DELAY_SEC)
                    con.active.spawn.sendline()
                    config_retry += 1
            else:
                config_retry = 21

        while counter < 31:
            rp_state = con.get_rp_state(target='standby', timeout=30)
            if rp_state.find('STANDBY HOT') != -1:
                counter = 32
            else:
                sleep(6)
                counter += 1
        con.disconnect()
        con.connect()
        con.log.debug("+++ Reload Completed Successfully +++")
        self.result = True


class SwitchoverService(BaseService):
    """ Service to switchover the device.

    Arguments:
        command: command to do switchover. default
                 "redundancy force-switchover"
        dialog: Dialog which include list of Statements for
                additional dialogs prompted by switchover command,
                in-case it is not in the current list.
        timeout: Timeout value in sec, Default Value is 500 sec

    Returns:
        True on Success, raise SubCommandFailure on failure.

    Example:
        .. code-block:: python

            rtr.switchover()
            # If switchover command is other than 'redundancy force-switchover'
            rtr.switchover(command="command which invoke switchover",
            timeout=700)
    """

    def __init__(self, connection, context, **kwargs):
        super().__init__(connection, context, **kwargs)
        self.start_state = 'enable'
        self.end_state = 'enable'
        self.service_name = 'switchover'
        self.timeout = connection.settings.SWITCHOVER_TIMEOUT
        self.dialog = Dialog(switchover_statement_list)
        self.command = 'redundancy force-switchover'
        self.__dict__.update(kwargs)

    def call_service(self, command=None,
                     dialog=Dialog([]),
                     timeout=None,
                     sync_standby=True,
                     *args,
                     **kwargs):
        # create an alias for connection.
        con = self.connection
        timeout = timeout or self.timeout
        command = command or self.command
        switchover_counter = con.settings.SWITCHOVER_COUNTER
        con.log.debug("+++ Issuing switchover on  %s  with "
                      "switchover_command %s and timeout is %s +++"
                      % (con.hostname, command, timeout))

        # Check is switchover possible?
        rp_state = con.get_rp_state(target='standby', timeout=100)
        if rp_state.find('STANDBY HOT') == -1:
            raise SubCommandFailure(
                "Switchover can't be issued in %s state" % rp_state)

        # Save current active and standby handle details
        standby_start_cmd = con.standby.start
        dialog = dialog
        dialog += self.dialog
        dialog = self.service_dialog(handle=con.active,
                                     service_dialog=dialog)

        # Issue switchover command
        con.active.spawn.sendline(command)
        try:
            dialog.process(con.active.spawn,
                           timeout=100,
                           prompt_recovery=self.prompt_recovery,
                           context=con.context)
        except TimeoutError:
            pass
        except SubCommandFailure as err:
            raise SubCommandFailure("Switchover Failed %s" % str(err))

        # Initialise Standby
        try:
            con.standby.spawn.sendline("\r")
            con.standby.spawn.expect(".*")
            con.swap_roles()
        except Exception as err:
            raise SubCommandFailure("Failed to initialise the standby",
                                    err)

        counter = 0
        if not sync_standby:
            con.log.info("Standby state check disabled on user request")

        else:
            while counter < switchover_counter:
                con.active.spawn.sendline("\r")
                con.active.spawn.expect(".*")
                try:
                    rp_state = con.get_rp_state(target='standby',
                                                timeout=60)
                except (SubCommandFailure, TimeoutError):
                    sleep(9)
                    counter += 1
                    continue
                except Exception:
                    con.active.spawn.sendline("\r")
                    con.active.spawn.expect(".*")
                    continue
                else:
                    if re.search('STANDBY HOT', rp_state):
                        counter = switchover_counter + 1
                    else:
                        sleep(9)
                        counter += 1

            # Issue init commands to disable console logging
            exec_commands = self.connection.settings.HA_INIT_EXEC_COMMANDS
            for command in exec_commands:
                con.execute(command, prompt_recovery=self.prompt_recovery)
            config_commands = self.connection.settings.HA_INIT_CONFIG_COMMANDS
            config_retry = 0
            while config_retry < 20:
                try:
                    con.configure(config_commands, timeout=60, prompt_recovery=self.prompt_recovery)
                except Exception as err:
                    if re.search("Config mode cannot be entered",
                                 str(err)):
                        sleep(9)
                        con.active.spawn.sendline()
                        config_retry += 1
                else:
                    config_retry = 21

            # Clear Standby buffer
            con.standby.spawn.sendline("\r")
            con.standby.spawn.expect(".*")
            con.standby.state_machine._current_state = 'disable'
            con.enable(target='standby')
        # Verify switchover is Successful
        if con.active.start == standby_start_cmd:
            con.log.info("Switchover is Successful")
            self.result = True
        else:
            con.log.info("Switchover is Failed")
            self.result = False


class ResetStandbyRP(BaseService):
    """ Service to reset the standby rp.

    Arguments:

        command: command to reset standby, default is"redundancy reload peer"
        dialog: Dialog which include list of Statements for
                 additional dialogs prompted by standby reset command,
                 in-case it is not in the current list.
        timeout: Timeout value in sec, Default Value is 500 sec

    Returns:
        True on Success, raise SubCommandFailure on failure.

    Example:
        .. code-block:: python

            rtr.reset_standby_rp()
            # If command is other than 'redundancy reload peer'
            rtr.reset_standby_rp(command="command which will reset standby rp",
            timeout=600)

    """

    def __init__(self, connection, context, **kwargs):
        super().__init__(connection, context, **kwargs)
        self.start_state = 'enable'
        self.end_state = 'enable'
        self.service_name = 'reset_standby_rp'
        self.timeout = connection.settings.HA_RELOAD_TIMEOUT
        self.dialog = Dialog(standby_reset_rp_statement_list)
        self.__dict__.update(kwargs)

    def pre_service(self, *args, **kwargs):
        if self.connection.is_connected:
            return
        elif self.connection.reconnect:
            self.connection.connect()
        else:
            raise ConnectionError("Connection is not established to device")
        state_machine = self.connection.active.state_machine
        state_machine.go_to(self.start_state,
                            self.connection.active.spawn,
                            context=self.connection.context)

    def post_service(self, *args, **kwargs):
        state_machine = self.connection.active.state_machine
        state_machine.go_to(self.end_state,
                            self.connection.active.spawn,
                            context=self.connection.context)

    def call_service(self, command='redundancy reload peer',
                     reply=Dialog([]),
                     timeout=None,
                     *args,
                     **kwargs):
        # create an alias for connection.
        con = self.connection
        timeout = timeout or self.timeout
        # resetting the standby rp for
        con.log.debug("+++ Issuing reset on  %s  with "
                      "reset_command %s and timeout is %s +++"
                      % (con.hostname, command, timeout))

        # Check is switchover possible?
        rp_state = con.get_rp_state(target='standby', timeout=100)
        if rp_state.find('DISABLED') == -1:
            raise SubCommandFailure("No Standby found")

        dialog = self.service_dialog(handle=con.active,
                                     service_dialog=self.dialog)
        # Issue switchover command
        con.active.spawn.sendline(command)
        try:
            dialog.process(con.active.spawn,
                           timeout=30,
                           context=con.context)
        except TimeoutError:
            pass
        except SubCommandFailure as err:
            raise SubCommandFailure("Failed to reset standby rp %s" % str(err))

        reset_counter = timeout / 10

        counter = 0
        while counter < reset_counter:
            try:
                rp_state = con.get_rp_state(target='standby',
                                            timeout=60)
            except (SubCommandFailure, TimeoutError):
                sleep(10)
                counter += 1
                continue
            else:
                if re.search('STANDBY HOT', rp_state):
                    counter = reset_counter + 1
                else:
                    sleep(10)
                    counter += 1

        # Clear Standby buffer
        try:
            con.standby.spawn.sendline("\r")
            con.standby.spawn.expect(".*")
            con.standby.state_machine._current_state = 'disable'
            con.enable(target='standby')
        except SubCommandFailure as err:
            raise SubCommandFailure("Failed to bring standby to enable: %s" %
                                    str(err))
        con.log.info("Successfully reloaded Standby RP")
        self.result = True


class BashService(BaseService):
    """ Service to provide an console to do shell commands

    Arguments:
        None

    Returns:
        AttributeError: No attributes

    Example:
        .. code-block:: python

            rtr.bash_console(timeout=60).execute('ls')

    """


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.start_state = "enable"
        self.end_state = "enable"
        self.service_name = "bash_console"
        self.bash_enabled = False

    def call_service(self, **kwargs):
        self.result = self.__class__.ContextMgr(connection = self.connection,
                                            enable_bash = not self.bash_enabled,
                                                **kwargs)
        # if bash wasn't enabled, it is now!
        if not self.bash_enabled:
            self.bash_enabled = True

    class ContextMgr(object):
        def __init__(self, connection,
                           enable_bash = False,
                           timeout = None):
            self.conn = connection
            # Specific platforms has its own prompt
            self.timeout = timeout
            self.enable_bash = enable_bash
            self.timeout = timeout or connection.settings.CONSOLE_TIMEOUT

        def __enter__(self):
            raise NotImplementedError('No enter shell method supports in platform {}'
                .format(self.device.os))

        def __exit__(self, exc_type, exc_value, exc_tb):
            self.conn.log.debug('--- detaching console ---')

            if self.conn.is_ha:
                conn = self.conn.active
            else:
                conn = self.conn

            sm = conn.state_machine
            sm.go_to('enable', conn.spawn)

            # do not suppress
            return False

        def __getattr__(self, attr):
            if attr in ('execute', 'sendline', 'send', 'expect'):
                return getattr(self.conn, attr)

            raise AttributeError('%s object has no attribute %s'
                                 % (self.__class__.__name__, attr))

