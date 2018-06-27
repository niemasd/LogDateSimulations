#!/usr/bin/env python3
'''
Simulate sequences down a given tree under the GTR+Gamma model using Seq-Gen.
'''
from gzip import open as gopen
from os import devnull
from random import choice
from string import ascii_uppercase
from subprocess import check_output
from sys import stdin,stdout
from tempfile import NamedTemporaryFile
from treeswift import read_tree_newick
import argparse

if __name__ == "__main__":
    # parse args
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-i', '--input', required=False, type=str, default='stdin', help="Input Tree File")
    parser.add_argument('-r', '--root', required=True, type=str, help="Root Sequence")
    parser.add_argument('-o', '--output', required=False, type=str, default='stdout', help="Output File")
    parser.add_argument('-p', '--seqgen_path', required=False, type=str, default='seq-gen', help="Seq-Gen Path")
    parser.add_argument('gamma_shape', type=float, help="Gamma Shape")
    parser.add_argument('a_to_c', type=float, help="A->C Rate")
    parser.add_argument('a_to_g', type=float, help="A->G Rate")
    parser.add_argument('a_to_t', type=float, help="A->T Rate")
    parser.add_argument('c_to_g', type=float, help="C->G Rate")
    parser.add_argument('c_to_t', type=float, help="C->T Rate")
    parser.add_argument('g_to_t', type=float, help="G->T Rate")
    parser.add_argument('freq_a', type=float, help="A Frequency")
    parser.add_argument('freq_c', type=float, help="C Frequency")
    parser.add_argument('freq_g', type=float, help="G Frequency")
    parser.add_argument('freq_t', type=float, help="T Frequency")
    args,unknown = parser.parse_known_args()
    gtr_params = "-mGTR -a%f -r %f %f %f %f %f %f -f %f %f %f %f" % (args.gamma_shape, args.a_to_c, args.a_to_g, args.a_to_t, args.c_to_g, args.c_to_t, args.g_to_t, args.freq_a, args.freq_c, args.freq_g, args.freq_t)
    if args.input == 'stdin':
        treestr = stdin.read().strip()
    elif args.input.lower().endswith('.gz'):
        treestr = gopen(args.input).read().decode().strip()
    else:
        treestr = open(args.input).read().strip()
    if args.output == 'stdout':
        args.output = stdout
    else:
        args.output = open(args.output,'w')
    tree = read_tree_newick(treestr)

    # safe names for tree leaves
    new2old = dict()
    for node in tree.traverse_preorder():
        if node.is_leaf():
            n = None
            while n is None or n in new2old:
                n = ''.join(choice(ascii_uppercase) for _ in range(5))
            new2old[n] = node.label; node.label = n
        else:
            node.label = None

    # set up seq-gen
    seqgen_file = NamedTemporaryFile(mode='w')
    seqgen_file.write("1 %d\nROOT %s\n1\n%s" % (len(args.root),args.root,str(tree)))
    seqgen_file.flush()
    command = [args.seqgen_path,'-or','-k1']
    command += gtr_params.split()
    command.append(seqgen_file.name)

    # simulate sequences
    seqgen_out = check_output(command, stderr=open(devnull,'w')).decode('ascii').strip().splitlines()[1:]
    for l in seqgen_out:
        k,s = l.strip().split(); args.output.write('>%s\n%s\n' % (new2old[k],s))