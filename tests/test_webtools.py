#!/usr/bin/env python

"""Tests for `webtools` package."""

import pytest


import webtools.colortools as color


# @pytest.fixture
# def response():
#     """Sample pytest fixture.

#     See more at: http://doc.pytest.org/en/latest/fixture.html
#     """
#     # import requests
#     # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


# def test_content(response):
#     """Sample pytest test function with the pytest fixture as an argument."""
#     # from bs4 import BeautifulSoup
#     # assert 'GitHub' in BeautifulSoup(response.content).title.string

def test_rgb_to_hex_for_black():
    results = color.rgb_to_hex(0, 0, 0)
    expected = "#000000"
    assert results == expected


def test_rgb_to_hex_for_white():
    results = color.rgb_to_hex(255, 255, 255)
    expected = "#ffffff"
    assert results == expected


def test_rgb_to_hex_for_336699():
    results = color.rgb_to_hex(51, 102, 153)
    expected = "#336699"
    assert results == expected


def test_rgb_to_hex_for_336699():
    results = color.rgb_to_hex("rgb(51,102,153)")
    expected = "#336699"
    assert results == expected

def test_rgb_to_hsl_deepSkyBlue():
    results = color.rgb_to_hsl((0, 191, 255))
    expected = (195, 100, 50)
    assert results == expected

def test_rgb_to_hsl_for_bada55():
    assert color.rgb_to_hsl((186, 218, 85)) == (74, 64, 59)