#
# Copyright 2017 Politecnico di Torino
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
The CyberSecurity Topologies daemon app

@author: Marco De Benedictis
"""

import argparse
from cybertop.log import LOG
from cybertop.cybertop import CyberTop


class CyberTopDaemon(object):
    """Main application.

    This class implements the CyberTop main application. It manages the
    parsing of the input CSV files and HSPL/MSPL generation accordingly.
    """

    def __init__(self):
        """Initialisation method

        Defines the CLI parameters and arguments and instantiates the daemon
        """
        p = argparse.ArgumentParser()

        p.add_argument(
            "-v",
            "--version",
            help="Package's version",
            action='version',
            version='%(prog)s 0.1'
        )
        p.add_argument(
            "-c",
            "--conf",
            dest='conf',
            metavar="FILE",
            default="./cybertop.cfg",
			required=True,
            help="Specifies the app configuration file"
        )
        p.add_argument(
            "-l",
            "--log-conf",
            dest='log_conf',
            metavar="FILE",
            default="./logging.ini",
			required=True,
            help="Specifies the logging configuration file"
        )
        
        args = p.parse_args()
        
        cybertop = CyberTop(args.conf, args.log_conf)
        cybertop.start()


if __name__ == "__main__":
    CyberTopDaemon()
