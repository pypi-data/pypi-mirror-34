#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    :platform: Unix
    :synopsis: Processing context used in this module.

"""

import os
import re
from multiprocessing import Lock, cpu_count, Value
from multiprocessing.managers import SyncManager

from ESGConfigParser import SectionParser, NoConfigOption

from utils.constants import CMIP6_FILENAME_PATTERN, IGNORED_FACETS, RUN_CARD, CONF_CARD, FILEDEF_DIRECTORY_FORMAT, \
    FILEDEF_ROOT
from utils.custom_exceptions import InvalidFilters, NoConfigCardFound, NoRunCardFound


class ProcessingContext(object):
    """
    Encapsulates the processing context/information for main process.

    :param ArgumentParser args: The command-line arguments parser
    :returns: The processing context
    :rtype: *ProcessingContext*

    """

    def __init__(self, args):
        # Get directory
        self.directory = args.directory
        # Get max process number
        self.processes = args.max_processes if args.max_processes <= cpu_count() else cpu_count()
        self.use_pool = (self.processes != 1)
        # Get xml path(s)
        if args.xml:
            self.xml = args.xml
        elif args.card:
            self.xml = list(yield_xml_from_card(args.card))
        else:
            self.xml = args.directory
        # Get stdout lock
        self.lock = Lock()
        # Get facet keys
        facets = re.compile(CMIP6_FILENAME_PATTERN).groupindex
        # Add facet for climatologies
        facets['is_clim'] = max(facets.values()) + 1
        for facet in IGNORED_FACETS:
            del (facets[facet])
        self.facets = facets
        # Clear re.compile cache to avoid groupindex deletion
        re.purge()
        # Get filters
        setattr(args, 'set_filter', args.set_filter or tuple())
        self.filters = dict(args.set_filter)
        wrong_filters = set(self.filters.keys()).difference(set(self.facets.keys()))
        if wrong_filters:
            raise InvalidFilters(wrong_filters, self.facets)
        # Set numbers of processes
        self.nbxml = 0
        self.nbcdf = 0
        self.nbentries = 0
        self.notinxml = 0
        self.notinxios = 0
        # Set process counter
        if self.use_pool:
            # Use process manager
            manager = SyncManager()
            manager.start()
            self.progress = manager.Value('i', 0)
        else:
            self.progress = Value('i', 0)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, traceback):
        pass


def yield_xml_from_card(card_path):
    """
    Yields XML path from run.card and config.card attributes.

    :param str card_path: Directory including run.card and config.card
    :returns: The XML paths to use
    :rtype: *iter*

    """
    # Check cards exist
    if RUN_CARD not in os.listdir(card_path):
        raise NoRunCardFound(card_path)
    else:
        run_card = os.path.join(card_path, RUN_CARD)
    if CONF_CARD not in os.listdir(card_path):
        raise NoConfigCardFound(card_path)
    else:
        conf_card = os.path.join(card_path, CONF_CARD)
    # Extract config info from config.card
    config = SectionParser('UserChoices')
    config.read(conf_card)
    xml_attrs = dict()
    xml_attrs['root'] = FILEDEF_ROOT
    xml_attrs['longname'] = config.get('longname').strip('"')
    try:
        xml_attrs['modelname'] = config.get('modelname').strip('"')
    except NoConfigOption:
        xml_attrs['modelname'] = 'IPSL-CM6A-LR'
    xml_attrs['experimentname'] = config.get('experimentname').strip('"')
    xml_attrs['member'] = config.get('member').strip('"')
    # Extract first and last simulated years from run.card
    with open(run_card, 'r') as f:
        lines = f.read().split('\n')
    # Get run table without header
    lines = [line for line in lines if line.count('|') == 8][1:]
    year_start = int(lines[0].split()[3][:4])
    year_end = int(lines[-1].split()[5][:4])
    for year in range(year_start, year_end + 1):
        xml_attrs['year'] = str(year)
        yield FILEDEF_DIRECTORY_FORMAT.format(**xml_attrs)
