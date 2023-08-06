# atgcN_count

## 1 Introduction

`atgcN_count` is a tool to stat the counts and percentage of each base in fasta file.

## 2 Installation

    pip install atgcN_count

There will be a command `atgcN_count` created under the same directory as your `pip` command.

## 3 Usage

    usage: atgcN_count[-h] [-i <file>] [-v] [-d <int>] [-N]

    To stat the counts of each base in a fasta file.

    optional arguments:
      -h, --help  show this help message and exit
      -i <file>   input fasta file
      -v          also output statistics for each sequence [False]
      -d <int>    decimals for output result [2]
      -N          do not take non-ATGC bases into account when caculate percentage
                  [False]

## Author
Guanliang MENG

## Citation
Currently I have no plan to publish `atgcN_count`.





