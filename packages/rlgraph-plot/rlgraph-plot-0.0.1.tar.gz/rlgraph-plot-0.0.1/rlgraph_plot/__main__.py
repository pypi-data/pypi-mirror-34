#!/usr/bin/env python3

# Copyright 2018 The RLgraph project. All Rights Reserved.
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
# ==============================================================================

from __future__ import absolute_import
from __future__ import print_function
from __future__ import division

import argparse
import sys

from yarl.components import Component
from yarl.utils.visualization_util import get_graph_markup


def main():
    parser = argparse.ArgumentParser(description='Plot yarl metagraphs.')

    parser.add_argument('--listen', '-L', dest="listen", action='store_true', default=False,
                        help='Listen and wait forr markups')
    parser.add_argument('--token', '-T', default=None,
                        help='Token needed to post graph markups (default empty)')

    parser.add_argument('--file', '-f', help='Python file containing components')

    parser.add_argument('--component', '-c', default=None, help='Component to plot')

    parser.add_argument('--mode', '-m', default="web", help='Mode (web/png/pdf)')

    parser.add_argument('--host', default="localhost", help='Webserver host')
    parser.add_argument('--port', default="8080", type=int, help='Webserver port')

    parser.add_argument('--no-graph-fns', dest='no_graph_fns', action='store_true', default=False)

    args = parser.parse_args()

    if args.listen and args.file:
        print("Please select either --file or --listen, not both.")
        sys.exit(1)

    if args.file:
        # Load python file and read its contents
        with open(args.file, 'r') as fp:
            file_content = fp.read()

        # Execute file contents
        exec(file_content)

        # Loop through local variables to find components
        components = dict()
        for key, var in locals().items():
            if isinstance(var, Component):
                components[key] = var

        if not args.component:
            print("Please select one of the following components: \n{}".format(
                '\n'.join(components)
            ))
            sys.exit(1)
        else:
            if args.component not in components:
                raise ValueError("Did not find component {} in available components: {}".format(
                    args.component, ', '.join(components)
                ))
            else:
                graph_markup = get_graph_markup(components[args.component], draw_graph_fns=not args.no_graph_fns)
    else:
        if args.mode != 'web':
            print("Option --listen only works with mode 'web'.")
            sys.exit(1)

        graph_markup = ''

    if args.mode == 'web':
        import webbrowser as wb
        from rlgraph_plot.web import app, gv

        gv['graph_markup'] = graph_markup
        gv['token'] = args.token
        wb.open_new_tab('http://{host}:{port}'.format(host=args.host, port=args.port))
        app.run(host=args.host, port=args.port)
    else:
        print("Unknown plot mode: {}".format(args.mode))


if __name__ == '__main__':
    main()
