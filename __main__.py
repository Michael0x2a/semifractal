#!/usr/bin/env python
# -*- coding: utf-8 -*-

import semifractal

if __name__ == '__main__':
    rule = semifractal.Rules.rule150randomized
    semifractal.test_grid_randomized(256, 1, rule)