# VDF Simulator

This is a simulator of Verifiable Delay Functions (https://vdfresearch.org) which propose a C++ implementation of VDFs using the GMP library for multiple precision numbers. For now we have implemented the Wesolowski VDF (https://eprint.iacr.org/2018/623) and we are studying the use of a multiexponentiation algorithm to speed up the verification part (https://www.bmoeller.de/pdf/multiexp-sac2001.pdf) alongside with Python scripts to analyse the simulations.

This repo is maintained by the Network team of the IOTA Foundation by Vidal Attias, Luigi Vigneri and Vassil Dimitrov.

Next evolutions of the repo will comprise an implementation of the Pietrzak's VDF and better analysis tools.

## COMPILATION OF C++

Dependancies : You will have to install the GMP library. On macOS, do 'brew install ntl'. This has not been tested on linux but it should not be difficult to install.
To compile the C++ simulator, go to **/src/** and do **make**, it should compile.

## RUNNING THE SIMULATOR
To run the simulator, go to the root folder and run **src/bin/vdf tau lambda k w**
With

- **tau** : the VDF challenge but in power 2. For example tau = 4 means the challenge is computing 2**4 squarings. (It is important to understand this point)
- **lambda** : the bit size of the RSA modulus. Better if an even number
- **k** : the bit-level security of the hashing functions used. A k level security yields hashing functions with 2k bits output.
- **w** : the size of the bit window as defined in the Lenstra algorithm (see multiexponentiation paper quoted above). Use w=1 if you don't care.

As an example, you can run **src/vdf 40 2048 128 3** to run the Wesolowski VDF using a 2048 bits modulus, a bit-level security parameter equivalent to 128 bits and a multiexponentiation optimization with w=3.

A python file has been written, located in **scripts/run.py** which allows to easily run a batch of simulations.


## OUTPUT OF THE SIMULATOR
The simulator will not show information in the terminal but will write in in the **result/** folder. In this folder, there are files for each ran configuration, with a name format **tau_lambda_k_w.csv**

## MULTIEXPONENTIATION ANALYSIS
The **scripts/multi_exp_analysis.py** script provides a comparison between naive and optimized multiexponentiation used in the VDF verification part. After having run simulations using the **scripts/run.py** script, you can use it to display a figure describing the percentage of improvement of the Lenstra algorithm over the naive implementation using as different lines as you have set different w values.

## SCHEDULED IMPROVEMENTS
- Implement Pietrzak's VDF
- Change all the GMP C-like types to C++ classes
- Implement other multiexponentiation algorithms
- Provide better analysis tools
