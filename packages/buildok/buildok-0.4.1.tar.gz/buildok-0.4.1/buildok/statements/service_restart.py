# Copyright 2018 Alexandru Catrina
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

from shlex import split as cmd_split
from subprocess import Popen, CalledProcessError
from time import sleep

from buildok.statements.service_status import StatusService

from buildok.util.log import Log


class RestartService(StatusService):
    r"""Restart running service.

    Args:
        srv (str): Service name to restart.

    Retuns:
        str: Output as string.

    Raises:
        OSError: If an invalid `srv` is provided.

    Accepted statements:
        ^restart service `(?P<srv>.+)`$

    Sample (input):
        - Restart service `urandom`.

    Expected:
        Service 'urandom' => active
    """

    os_distro = {
        ("arch",
         "centos",
         "debian",
         "fedora",
         "gentoo",
         "ubuntu"): "systemctl restart {service}.service"
    }

    def run(self, srv=None, *args, **kwargs):
        cmd = RestartService.check_systemd()
        if cmd is None:
            return self.fail("Unsupported OS: %s" % self.env.os_name)
        try:
            service_cmd = cmd.format(service=srv)
            log_status = (self.env.os_name, service_cmd)
            Log.debug("Service OS (%s) restart: %s ..." % log_status)
            service_output = Popen(cmd_split(service_cmd))
            while service_output.poll() is None:
                sleep(0.5)
            if 0 != service_output.returncode:
                return self.fail(u"Service '%s' => failed to restart" % srv)
            check_cmd = StatusService.check_systemd()
            ok, status = StatusService.get_status(cmd_split(check_cmd))
            output = u"Service '%s' => %s" % (srv, status)
            if ok:
                self.success(output)
            else:
                self.fail(output)
        except CalledProcessError as e:
            self.fail(e.output)
        except Exception as e:
            self.fail(str(e))
