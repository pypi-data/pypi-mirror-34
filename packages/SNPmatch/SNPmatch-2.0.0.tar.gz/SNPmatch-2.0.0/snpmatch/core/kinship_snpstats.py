"""
    Calculate kinship and pairwise SNP differences
"""

import math
import numpy as np
import numpy.ma
import allel
import pandas
import sys
import os
import h5py
import scipy as sp
import logging

from pygwas.core import genotype
from pygwas.core import kinship

log = logging.getLogger(__name__)

def die(msg):
  sys.stderr.write('Error: ' + msg + '\n')
  sys.exit(1)

def calc_ibs_kinship(g, snp_dtype='int8'):
  """
  Calculates IBS kinship
  Taken from the pygwas.core, kinship.calc_ibs_kinship
  But only for the binary file (0, 1, -1), removes all Hets
  """
  num_lines = len(g.accessions)
  log.info('Allocating matrices for calculation')
  k_mat = sp.zeros((num_lines, num_lines))
  log.info('Starting calculation')
  num_snps = sp.zeros((num_lines, num_lines), dtype="uint32")
  snps = g.get_snps_iterator(is_chunked=True, chunk_size=1000)
  chunk_i = 0
  for snp in snps:
    chunk_i += 1
    snps_array = sp.array(snp)
    snps_array = snps_array.T
    info_array = sp.mat(numpy.copy(snps_array).astype(float))
    info_array[info_array >= 0] = 1
    info_array[info_array < 0] = 0
    num_snps = num_snps + info_array * info_array.T
    snps_array = snps_array.astype(float)
    snps_array[snps_array > 1] = 0.5
    snps_array[snps_array < 0] = 0.5
    sm = sp.mat(snps_array * 2.0 - 1.0)
    k_mat = k_mat + sm * sm.T
    if chunk_i % 100 == 0:
      log.debug("progress: %s chunks", chunk_i)
#  kin_mat = k_mat / (2 * num_snps) + 0.5
  kin_mat = numpy.divide(k_mat, num_snps)
  num_diff_snps = num_snps - k_mat
  return kin_mat, num_diff_snps
