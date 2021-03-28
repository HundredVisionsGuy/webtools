#!/usr/bin/env python

"""Tests for `webtools` package."""

import pytest


import webtools.colortools as color


@pytest.fixture
def indigo_rgb():
    indigo = "#4b0082"
    indigo_rgb = color.hex_to_rgb(indigo)
    return indigo_rgb

@pytest.fixture
def palette336699():
    code = "#336699"
    palette = color.color_palette_inator(code)
    return palette

def test_hex_to_decimal_for_bc():
    bc_hex = "bc"
    expected = 188
    results = color.hex_to_decimal(bc_hex)
    assert expected == results

def test_hex_to_decimal_for_CB():
    cb_hex = "CB"
    expected = 203
    results = color.hex_to_decimal(cb_hex)
    assert expected == results

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


def test_is_hex_for_no_hash():
    assert color.is_hex("336699") == False


def test_is_hex_for_valid_hex():
    assert color.is_hex("#336699")


def test_is_hex_for_invalid_not_hex_digit():
    assert not color.is_hex("#3366lh")

def test_contrast_ratio_for_inverted_indigo_white(indigo_rgb):
    expected = 12.95
    results = color.contrast_ratio("#4B0082", "#ffffff")
    assert expected == results


def test_get_triadic_for_210_50_40():
    assert color.get_triadic((210, 50, 40)) == [(
        210, 50, 40), (330, 50, 40), (90, 50, 40)]


def test_get_tetradic_for_210_50_40():
    assert color.get_tetradic((210, 50, 40)) == [(
        210, 50, 40), (300, 50, 40), (30, 50, 40), (120, 50, 40)]

def test_hsl_to_rgb_for_210_50_40():
    hsl = (210, 50, 40)
    results = color.hsl_to_rgb(hsl)
    expected = (51, 102, 153)
    assert results == expected

def test_hsl_to_rb_for_various_values():
    black = (0, 0, 0)
    white = (0, 0, 100)
    lime = (120, 100, 50)
    silver = (0, 0, 75)
    yellow = (60, 100, 50)
    assert color.hsl_to_rgb(black) == (0, 0, 0)
    assert color.hsl_to_rgb(white) == (255, 255, 255)
    assert color.hsl_to_rgb(lime) == (0, 255, 0)
    assert color.hsl_to_rgb(silver) == (191, 191, 191)
    assert color.hsl_to_rgb(yellow) == (255, 255, 0)
    
    # gray = (0, 0, 50)
    # maroon = (0, 100, 25)
    # olive = (60, 100, 25)
    # assert color.hsl_to_rgb(gray) ==  (128, 128, 128)
    # assert color.hsl_to_rgb(maroon) == (128, 0, 0)
    # assert color.hsl_to_rgb(olive) == (128, 128, 0)

    # NOTE: 1 HSL could represent up to 5 different RGB values
    #       same thing would go for hex, so converting
    #       from hsl to rgb or hex is not exact