#ifndef WESOLOWSKI_H
#define WESOLOWSKI_H

#include <gmp.h>
#include <vector>

#include "proof.h"

class Wesolowski {
public:
Wesolowski();

void setup(int lambda, int k);
void generate(mpz_t& dest);
Proof evaluate(mpz_t l, mpz_t pi, const mpz_t x,
               long challenge);
bool parallel_verify(mpz_t x, long challenge, mpz_t l, mpz_t pi);
bool naive_verify(mpz_t x, long challenge, mpz_t l, mpz_t pi);
bool optimized_verify(mpz_t x, long challenge, mpz_t l, mpz_t pi, int w);
std::chrono::duration<double> setup_time;
std::chrono::duration<double> eval_time;
std::chrono::duration<double> proof_time;
std::chrono::duration<double> verif_time;
std::chrono::duration<double> verif_time_opti;

private:
mpz_t y_saved;
mpz_t N;
mpz_t p;
mpz_t q;
int k;
int lambda;
mpz_t challenge;

gmp_randstate_t rstate;

void HashG(mpz_t& dest, mpz_t hashed);
void hash_prime(mpz_t l, const mpz_t input);

void unit_test();

int bit_length;
};

#endif
