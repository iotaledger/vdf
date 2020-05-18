#include <chrono>
#include <cmath>
#include <ctime>
#include <iostream>
#include <sstream>
#include <string>
#include <thread>
//#include "sha512.h"
//#include "utils.h"
#include "wesolowski.h"
#include <gmpxx.h>


void generate_prime(mpz_t& rop, gmp_randstate_t& rstate, const mp_bitcnt_t& n){
        mpz_urandomb(rop, rstate, n);
        mpz_nextprime(rop, rop);
}

void Wesolowski::hash_prime(mpz_t l, const mpz_t input)
{
        if(mpz_cmp_si(challenge, 0) == 0) {
                mpz_urandomb(challenge, rstate, 2*k);
        }
        mpz_nextprime(l, challenge);
}

Wesolowski::Wesolowski() {
}

void Wesolowski::setup(int _lambda, int _k) {
        auto start = std::chrono::high_resolution_clock::now();

        lambda = _lambda;
        k = _k;

        mpz_init(challenge);

        k = _k;

        gmp_randinit_mt(rstate);

        mpz_init(p);
        generate_prime(p, rstate, lambda/2);

        mpz_init(q);
        generate_prime(q, rstate, lambda/2);

        mpz_init(N);
        mpz_mul(N, p, q);

        auto finish = std::chrono::high_resolution_clock::now();
        setup_time = finish - start;
}

// Creates a random input for the VDF
void Wesolowski::generate(mpz_t& dest) {
        mpz_urandomm(dest, rstate, N);
}

Proof Wesolowski::evaluate(mpz_t l, mpz_t pi, const mpz_t x,
                           const long challenge) {

        // HERE WE START THE EVALUATION
        std::cout << "test" << std::endl;
        auto start_eval = std::chrono::high_resolution_clock::now();

        mpz_t exp_challenge;
        mpz_init(exp_challenge);
        mpz_ui_pow_ui(exp_challenge, 2, challenge);


        mpz_init(y_saved);
        mpz_powm(y_saved, x, exp_challenge, N);

        auto finish_eval = std::chrono::high_resolution_clock::now();

        eval_time = finish_eval - start_eval;

        std::cout << eval_time.count() << std::endl;

        // WE FINISHED THE EVALUATION

        // HERE WE START THE PROOF COMPUTATION

        auto start_proof = std::chrono::high_resolution_clock::now();

        hash_prime(l, x);

        mpz_t q;
        mpz_init(q);
        mpz_fdiv_q(q, exp_challenge, l);

        mpz_powm(pi, x, q, N);


        auto finish_proof = std::chrono::high_resolution_clock::now();
        proof_time = finish_proof - start_proof;


        Proof proof_sent = Proof();
        return proof_sent;
}


bool Wesolowski::naive_verify(mpz_t x, long challenge, mpz_t l, mpz_t pi) {

        auto start_verif = std::chrono::high_resolution_clock::now();


        mpz_t phi_l;
        mpz_init(phi_l);
        mpz_sub_ui(phi_l, l, 1);

        mpz_t tau_mod;
        mpz_init(tau_mod);
        mpz_set_ui(tau_mod, challenge);
        mpz_mod(tau_mod, tau_mod, phi_l);

        mpz_t two;
        mpz_init(two);
        mpz_set_ui(two, 2);

        mpz_t r;
        mpz_init(r);
        mpz_powm(r, two, tau_mod, l);

        mpz_t y, y_tmp;
        mpz_init(y);
        mpz_init(y_tmp);
        mpz_powm(y, pi, l, N);
        mpz_powm(y_tmp, x, r, N);
        mpz_mul(y, y, y_tmp);
        mpz_mod(y, y, N);

        hash_prime(l, x);
        /*
           std::cout << "X = " << x << std::endl;
           std::cout << "PI = " << pi << std::endl;
           std::cout << "R = " << r << std::endl;
           std::cout << "L = " << l << std::endl;
           std::cout << "Y = " << y << std::endl;
         */
        if(mpz_cmp(y, y_saved) == 0) {
                auto finish_verif = std::chrono::high_resolution_clock::now();

                verif_time = finish_verif - start_verif;
                //std::cout << verif_time.count() << std::endl;
                return 1;
        } else {
                std::cout << "NOT WORKING" << std::endl;
                exit(1);
                return 0;
        }
}


void exponentiation(mpz_t ret, mpz_t radix, mpz_t exp, mpz_t N)
{
        mpz_powm(ret, radix, exp, N);
}

void exponentiation_euclidian(mpz_t ret, mpz_t radix, mpz_t exp, mpz_t N, int k)
{
        mpz_t A, B;
        mpz_init(A);
        mpz_init(B);

        mpz_t and_mod;
        mpz_init(and_mod);

        for(int i = 0; i < k; i++)
        {
                mpz_setbit(and_mod, i);
        }

        mpz_and(B, N, and_mod);
        mpz_sub(A, N, B);
        mpz_fdiv_q_2exp(A, A, k);

        /*
           std::cout << l << std::endl;
           std::cout << "N = " << N << std::endl;
           std::cout << "A = " << A << std::endl;
           std::cout << "B = " << B << std::endl;
           //mpz_powm(y, pi, l, N);
           //mpz_powm(y_tmp, x, r, N);
         */
        mpz_powm(ret, radix, exp, N);
}


bool Wesolowski::parallel_verify(mpz_t x, long challenge, mpz_t l, mpz_t pi) {

        auto start_verif = std::chrono::high_resolution_clock::now();


        mpz_t phi_l;
        mpz_init(phi_l);
        mpz_sub_ui(phi_l, l, 1);

        mpz_t tau_mod;
        mpz_init(tau_mod);
        mpz_set_ui(tau_mod, challenge);
        mpz_mod(tau_mod, tau_mod, phi_l);

        mpz_t two;
        mpz_init(two);
        mpz_set_ui(two, 2);

        mpz_t r;
        mpz_init(r);
        mpz_powm(r, two, tau_mod, l);

        mpz_t y, y_tmp;
        mpz_init(y);
        mpz_init(y_tmp);

        std::thread first(exponentiation, y, pi, l, N);
        std::thread second(exponentiation, y_tmp, x, r, N);

        first.join();
        second.join();
        //mpz_powm(y, pi, l, N);
        //mpz_powm(y_tmp, x, r, N);
        mpz_mul(y, y, y_tmp);
        mpz_mod(y, y, N);

        hash_prime(l, x);

        if(mpz_cmp(y, y_saved) == 0) {
                auto finish_verif = std::chrono::high_resolution_clock::now();

                verif_time = finish_verif - start_verif;
                //std::cout << verif_time.count() << std::endl;
                return 1;
        } else {
                std::cout << "NOT WORKING" << std::endl;
                exit(1);
                return 0;
        }
}



bool Wesolowski::parallel_diff_verify(mpz_t x, long challenge, mpz_t l, mpz_t pi) {

        auto start_verif = std::chrono::high_resolution_clock::now();


        mpz_t phi_l;
        mpz_init(phi_l);
        mpz_sub_ui(phi_l, l, 1);

        mpz_t tau_mod;
        mpz_init(tau_mod);
        mpz_set_ui(tau_mod, challenge);
        mpz_mod(tau_mod, tau_mod, phi_l);

        mpz_t two;
        mpz_init(two);
        mpz_set_ui(two, 2);

        mpz_t r;
        mpz_init(r);
        mpz_powm(r, two, tau_mod, l);


        mpz_t diff_exp;
        mpz_init(diff_exp);
        mpz_sub(diff_exp, l, r);

        mpz_t y, y_tmp;
        mpz_init(y);
        mpz_init(y_tmp);

        mpz_t w;
        mpz_init(w);
        mpz_mul(w, pi, x);



        std::thread first(exponentiation_euclidian, y, w, r, N, k);
        std::thread second(exponentiation_euclidian, y_tmp, pi, diff_exp, N, k);

        first.join();
        second.join();


        mpz_mul(y, y, y_tmp);
        mpz_mod(y, y, N);

        hash_prime(l, x);

        if(mpz_cmp(y, y_saved) == 0) {
                auto finish_verif = std::chrono::high_resolution_clock::now();

                verif_time = finish_verif - start_verif;
                //std::cout << verif_time.count() << std::endl;
                return 1;
        } else {
                std::cout << "NOT WORKING" << std::endl;
                exit(1);
                return 0;
        }
}


void print_precomp(std::vector<std::vector<mpz_class> > precomp, int pow_w)
{
        for(int i = 0; i<pow_w; i++)
        {
                for(int j = 0; j<pow_w; j++)
                {
                        std::cout << "\t" << precomp[i][j];
                }
                std::cout << std::endl;
        }
}

void get_bit(mpz_t ret, mpz_t e, int j)
{
        mpz_fdiv_q_2exp(ret, e, j);
        mpz_mod_ui(ret, ret, 2);
}

bool test_while(mpz_t x, mpz_t y, int j)
{
        if(mpz_tstbit(x, j) == 0 && mpz_tstbit(y, j) == 0)
        {
                return true;
        }
        else
        {
                return false;
        }
}

int filter(mpz_t e, int j, int J)
{
        mpz_t ret;
        mpz_init(ret);
        mpz_fdiv_q_2exp(ret, e, J);

        return mpz_fdiv_ui(ret, pow(2, j-J+1));
}



mpz_class multi_exponentiation(mpz_class x, mpz_class y, mpz_t a, mpz_t b, mpz_class N, int k, int w)
{
        int pow_w = pow(2, w);
        std::vector<std::vector<mpz_class> > pc(pow_w, std::vector<mpz_class>(pow_w));

        pc[1][0] = x;
        pc[0][1] = y;
        pc[2][0] = x * x % N;
        pc[0][2] = y * y % N;

        int mid = pow_w/2;
        for(int i = 1; i < mid; i++)
        {
                pc[2*i+1][0] = pc[2*(i-1)+1][0] * pc[2][0] % N;
                pc[0][2*i+1] = pc[0][2*(i-1)+1] * pc[0][2] % N;
        }

        for(int i = 0; i < mid; i++)
        {
                for(int j = 1; j < pow_w; j++)
                {
                        pc[j][2*i+1] = pc[j-1][2*i+1] * x % N;
                }
        }

        for(int i = 0; i < mid; i++)
        {
                for(int j = 1; j < mid; j++)
                {
                        pc[2*i+1][2*j] = pc[2*i+1][2*j-1] * y % N;
                }
        }

        mpz_class R(1);
        int j = k-1;

        while(j>=0)
        {
                if(mpz_tstbit(a, j) == 0 && mpz_tstbit(b, j) == 0)
                {
                        R = (R*R)%N;
                        j--;
                }
                else
                {
                        int j_new = std::max(j-w, -1);
                        int J = j_new+ 1;

                        while(test_while(a,b, J) == true)
                        {
                                J++;
                        }
                        int A = filter(a, j, J);
                        int B = filter(b, j, J);

                        while(j>=J)
                        {
                                R = (R*R)%N;
                                j--;
                        }

                        R = (R*pc[A][B])%N;

                        while(j>j_new)
                        {
                                R = (R*R)%N;
                                j--;
                        }

                }
        }

        return R;
}


bool Wesolowski::optimized_verify(mpz_t x, long challenge, mpz_t l, mpz_t pi, int w) {
        //std::cout << "OPTIMIZED VERIFICATION" << std::endl;
        //this->unit_test();
        auto start_verif = std::chrono::high_resolution_clock::now();

        mpz_t phi_l;
        mpz_init(phi_l);
        mpz_sub_ui(phi_l, l, 1);

        mpz_t tau_mod;
        mpz_init(tau_mod);
        mpz_set_ui(tau_mod, challenge);
        mpz_mod(tau_mod, tau_mod, phi_l);

        mpz_t two;
        mpz_init(two);
        mpz_set_ui(two, 2);

        mpz_t r;
        mpz_init(r);
        mpz_powm(r, two, tau_mod, l);

        mpz_class xx(x);
        mpz_class yy(pi);
        mpz_class NN(N);


        mpz_class R = multi_exponentiation(xx, yy, r, l, NN, 2*k, w);
        hash_prime(l, x);


        if(mpz_cmp(R.get_mpz_t(), y_saved) == 0) {
                auto finish_verif = std::chrono::high_resolution_clock::now();

                verif_time = finish_verif - start_verif;
                //std::cout << verif_time_opti.count() << std::endl;
                return 1;
        } else {
                std::cout << "NOT WORKING" << std::endl;
                exit(1);
                return 0;
        }
}
