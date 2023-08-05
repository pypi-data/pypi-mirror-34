# oeis-cli
A command line interface for The On-Line Encyclopedia of Integer Sequences.

## Installation

```
$ pip install oeis_cli
```

or, if you're feeling adventurous:

```
$ git clone https://github.com/dfbenjamin/oeis_cli/
$ cd oeis_cli
$ python3 setup.py install
```

## Usage

Use the command `oeis`. For example:

```
$ oeis 2 3 5 7
A000040: The prime numbers.
2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89
```

Can also add the `--unordered` tag, which does the equivalent of searching with spaces instead of commas on OEIS:

```
$ oeis --unordered 256 128 4 2048
A000079: Powers of 2: a(n) = 2^n.
1,2,4,8,16,32,64,128,256,512,1024,2048,4096,8192,16384,32768,65536
```

Use `--name` or `-n` to search by name:

``` 
$ oeis --name fibonacci
A000045: Fibonacci numbers: F(n) = F(n-1) + F(n-2) with F(0) = 0 and F(1) = 1.
0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,1597,2584,4181,6765
```

## About OEIS

The author is not affiliated with OEIS in any way. For more information on the website, visit https://oeis.org/

The OEIS is made available under the [Creative Commons Attribution Non-Commercial 3.0 license](https://creativecommons.org/licenses/by-nc/3.0/).
