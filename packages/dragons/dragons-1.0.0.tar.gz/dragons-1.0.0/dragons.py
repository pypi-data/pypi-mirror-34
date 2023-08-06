#!/usr/bin/env python
# -*- encoding: utf-8

import os


if (
    os.environ.get('DANGEROUS_ANIMALS_LICENCE', '').lower() != 'yes' and
    os.environ.get('DANGEROUS_ANIMALS_LICENSE', '').lower() != 'yes'
):
    raise ImportError(
        "You can't import dragons without a dangerous animals licence!"
    )
else:
    print(u'🐉  Here be dragons! 🐉')
