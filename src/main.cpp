#include <stdlib.h>
#include <time.h>
#include <fstream>
#include <iostream>
#include <math.h>
#include <gmp.h>


#include "wesolowski.h"

// argv arguments :
//    t : log2 of difficulty (must be an integer)
//    lambda : length of modulus
//    k : bit-level security of hashing function
//    Size of Lenstra window w
int main(int argc, char *argv[]) {

        // Argument parsing
        int t = std::atoi(argv[1]);
        int lambda = std::atoi(argv[2]);
        int k = std::atoi(argv[3]);
        int w = std::atoi(argv[4]);

        srand(time(NULL));


        Wesolowski vdf = Wesolowski();

        // Running the Setup phase of algorithm
        vdf.setup(lambda, k);

        // Drawing a random input from the RSA group
        mpz_t x;
        vdf.generate(x);


        //Here is the evaluation part. We combine the evaluation and proof however there are two chrono for the separate phases.
        mpz_t l, pi;
        mpz_init(l);
        mpz_init(pi);
        vdf.evaluate(l, pi, x, pow(2, t));


        // Here we run the naive and optimized verifications
        auto result_verif = vdf.naive_verify(x, pow(2, t), l, pi);
        result_verif = vdf.optimized_verify(x, pow(2, t), l, pi, w);


        std::ofstream file;


        file.open("result/" + std::to_string(t) + "_" +
                  std::to_string(lambda) + "_" + std::to_string(k)+ "_" + std::to_string(w) + ".csv",
                  std::ofstream::out | std::ofstream::app);
        file << vdf.setup_time.count() << ";" << vdf.eval_time.count() << ";"
             << vdf.proof_time.count() << ";" << vdf.verif_time.count() << ";" << vdf.verif_time_opti.count() << "\n";

        file.close();
        return 0;
}
