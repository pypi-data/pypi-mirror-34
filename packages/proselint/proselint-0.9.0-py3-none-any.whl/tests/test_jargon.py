"""Tests for jargon.misc check."""
from __future__ import absolute_import

from .check import Check

from proselint.checks.jargon import misc as chk


class TestCheck(Check):
    """The test class for jargon.misc."""

    __test__ = True

    @property
    def this_check(self):
        """Bolierplate."""
        return chk

    def test_smoke(self):
        """Basic smoke test for jargon.misc."""
        assert self.passes("""Smoke phrase with nothing flagged.""")
        assert not self.passes("""I agree it's in the affirmative.""")
