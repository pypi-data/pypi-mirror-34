#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from enum import Enum


class UsdaApis(Enum):
    """Data.gov API endpoints for USDA APIs"""
    ndb = "ndb"


class UsdaUriActions(Enum):
    """USDA API available actions"""
    list = "list"
    report = "reports"
    v2report = "V2/reports"
    nutrients = "nutrients"
    search = "search"


class UsdaNdbListType(Enum):
    """USDA API food or nutrients list settings"""
    all_nutrients = "n"
    specialty_nutrients = "ns"
    standard_release_nutrients = "nr"
    food = "f"
    food_groups = "g"
    derivation_codes = "d"


class UsdaNdbReportType(Enum):
    """USDA API food report types"""
    basic = "b"
    full = "f"
    stats = "s"
