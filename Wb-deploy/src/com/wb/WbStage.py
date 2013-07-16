#!/usr/bin/python
# encoding: utf-8
'''
com.google.wb.WbRelease -- Deployment tool for WBPro and GWTDesigner

com.google.wb.WbRelease is a tool to deploy WBPro and GWTDesigner

It defines classes_and_methods

@author:     mrrussell@google.com
        
@copyright:  2013 Google, Inc. All rights reserved.
        
@contact:    mrussell@google.com
@deffield    updated: Updated
'''

import argparse
import os
import sys

from os import path

__all__ = []
__version__ = 0.1
__date__ = '2013-07-16'
__updated__ = '2013-07-16'

DEBUG = 1
TESTRUN = 0
PROFILE = 0

class CLIError(Exception):
  '''Generic exception to raise and log different fatal errors.'''
  def __init__(self, msg):
    super(CLIError).__init__(type(self))
    self.msg = "E: %s" % msg
  def __str__(self):
    return self.msg
  def __unicode__(self):
    return self.msg

def enum(*sequential, **named):
  enums = dict(zip(sequential, range(len(sequential))), **named)
  reverse = dict((value, key) for key, value in enums.iteritems())
  enums['reverse_mapping'] = reverse
  return type('Enum', (), enums)


def main(argv=None): # IGNORE:C0111
  '''Command line options.'''

  if argv is None:
    argv = sys.argv
  else:
    sys.argv.extend(argv)

  print sys.argv
  products = enum('ALL', 'WBPRO', 'GWTD')
  stage = enum('integration', 'release')

  program_name = os.path.basename(sys.argv[0])
  program_version = "v%s" % __version__
  program_build_date = str(__updated__)
  program_version_message = '%%(prog)s %s (%s)' % (program_version,
                                                   program_build_date)
  program_shortdesc = __import__('__main__').__doc__.split("\n")[1]
  program_license = '''%s

  Created by user_name on %s.
  Copyright 2013 Google Inc.. All rights reserved.
  
  Licensed under the Apache License 2.0
  http://www.apache.org/licenses/LICENSE-2.0
  
  Distributed on an "AS IS" basis without warranties
  or conditions of any kind, either express or implied.

USAGE
''' % (program_shortdesc, str(__date__))
  default_product_base = path.join('/', 'usr', 'local', 'google', 'kalamath',
                                   'builds')
  default_staging_base = path.join(path.expanduser('~'), 'stagging', 'products')
  try:

    # Setup argument parser
    parser = argparse.ArgumentParser()
#                            description=program_license,
#                            formatter_class=RawDescriptionHelpFormatter)
    parser.add_argument('build', help = 'the build to use')
    parser.add_argument('--base_product_dir', dest='base_product_dir',
                        action='store',
                        default=default_product_base,
                        help='base to start looking for WBPro and '
                        'GWTDesigner [default: %(default)s]')
    parser.add_argument('--base_stage_dir', dest='base_stage_dir',
                        action='store',
                        default=default_staging_base,
                        help='base to stage the release '
                        '[default: %(default)s]')
    parser.add_argument('--product', dest='product', action = 'store',
                        default = 'all', choices = ['all', 'wbpro', 'gwtd'],
                        help = 'the product to stage '
                        '[default: %(default)s]')
    parser.add_argument('--stage', dest='stage', action = 'store',
                        default = 'all', choices = ['integration', ''],
                        help = 'the product to stage '
                        '[default: %(default)s]')
    parser.add_argument('-v', '--verbose', dest='verbose', action='count',
                        help='set verbosity level [default: %(default)s]')
    parser.add_argument('-V', '--version', action='version',
                        version=program_version_message)

    print 'parsing'
    # Process arguments
    args = parser.parse_args()

    print 'after parsing'
    verbose = args.verbose
    base_product_dir = args.base_product_dir
    base_stage_dir = args.base_stage_dir
    build = args.build
    if args.product is 'wppro':
      product = products.WBPRO
    elif args.product is 'gwtd':
      product = products.GWTD
    else:
      product = products.ALL

    if verbose > 0:
      print("Verbose mode on")

    if build is None:
      raise CLIError("You must specify a build.")
    print 'Staging product %s' % products.reverse_mapping[product]
    print ' from %s' % base_product_dir
    print ' using build %s' % build
    print ' to %s' % base_stage_dir

  except KeyboardInterrupt:
    print "key"
    ### handle keyboard interrupt ###
    return 1
  except Exception, e:
    print "except"
    if DEBUG or TESTRUN:
      raise(e)
    indent = len(program_name) * " "
    sys.stderr.write(program_name + ": " + repr(e) + "\n")
    sys.stderr.write(indent + "  for help use --help")
    return 2


if __name__ == "__main__":
  print " start"
  if DEBUG:
    sys.argv.append("-v")
  if TESTRUN:
    import doctest
    doctest.testmod()
  if PROFILE:
    import cProfile
    import pstats
    profile_filename = 'com.google.wb.WbRelease_profile.txt'
    cProfile.run('main()', profile_filename)
    statsfile = open("profile_stats.txt", "wb")
    p = pstats.Stats(profile_filename, stream=statsfile)
    stats = p.strip_dirs().sort_stats('cumulative')
    stats.print_stats()
    statsfile.close()
    sys.exit(0)
  sys.exit(main())