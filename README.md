# LogVarSimulations
Simulations for LogVar Project

## Simulating *pol*
Average evolutionary rate from [PANGEA.HIV.sim](https://github.com/olli0601/PANGEA.HIV.sim#evolutionary-rate-model) and GTR+Gamma parameters learned from San Diego HIV-1 *pol* dataset from [Little et al, 2014](http://journals.plos.org/plosone/article?id=10.1371/journal.pone.0098443).

### Evolutionary Rate Model Parameters
* Autocorrelated Exponential Distribution
    * Rate = 1/0.0022
* Exponential Distribution
    * Rate = 1/0.0022
* Gamma Distribution
    * Shape = 2.5
    * Scale = 0.00088
* Log-Normal Distribution
    * Medium Variance
        * Mu = -6.2875339186
        * Sigma = 0.580062
    * High Variance
        * Mu = -6.4658715089
        * Sigma = 0.8325546112

### GTR+Gamma Parameters for Sequence Simulation
* Gamma Shape = 0.405129
* A&rarr;C = 1.765707
* A&rarr;G = 9.587649
* A&rarr;T = 0.691915
* C&rarr;G = 0.863348
* C&rarr;T = 10.282617
* G&rarr;T = 1.0
* Freq. A = 0.392
* Freq. C = 0.165
* Freq. G = 0.212
* Freq. T = 0.232

## Simulating **env**
Average evolutionary rate from [Alizon & Fraser, 2013](https://retrovirology.biomedcentral.com/articles/10.1186/1742-4690-10-49) and GTR+Gamma parameters learned from [HIV-1 *env* dataset](https://github.com/niemasd/Virus-Data/blob/master/HIV/alignments/DNA/HIV1_FLT_2016_env_DNA.fasta.gz?raw=true) from [Los Alamos National Laboratory HIV Sequence Database](https://www.hiv.lanl.gov/content/sequence/HIV/mainpage.html).

### Evolutionary Rate Model Parameters
* Autocorrelated Exponential Distribution
    * Rate = 1/0.003090295433
* Exponential Distribution
    * Rate = 1/0.003090295433
* Gamma Distribution
    * Shape = 2.5
    * Scale = 0.001236118173
* Log-Normal Distribution
    * Medium Variance
        * Mu = -5.9477245833
        * Sigma = 0.580062
    * High Variance
        * Mu = -6.1260621736
        * Sigma = 0.8325546112

### GTR+Gamma Parameters for Sequence Simulation
* Gamma Shape = ???
* A&rarr;C = ???
* A&rarr;G = ???
* A&rarr;T = ???
* C&rarr;G = ???
* C&rarr;T = ???
* G&rarr;T = ???
* Freq. A = 0.350
* Freq. C = 0.172
* Freq. G = 0.235
* Freq. T = 0.243
