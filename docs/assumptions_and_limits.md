# Assumptions and Limits

## What is proven vs. what is assumed

### Proven (exact algebra):
- The five equivalences (i)–(v) in the theorem are pairwise equivalent.
- The deviation formula $\Delta E = -k_B T \ln(1+\delta)$ is exact.
- The TICE embedding $E_{\mathrm{bridge}}^{\mathrm{TICE}} = k_B T \ln(2 C_{\mathrm{TICE}})$ is exact for any admissible kernel.
- Three kernel solutions (Drude, algebraic, Gaussian) each have well-defined crossing times.

### Assumed (Conjecture 1):
- $D_{\mathrm{th}} = 2 D_q$ — that thermal diffusion accounts for both time-directed noise channels in Nelson's bidirectional stochastic mechanics.
- This is motivated by five independent observations but **not derived from first principles**.

### Regime of validity:
- **High-temperature Markov regime**: $k_B T \gg \hbar \Omega$ (for the base theorem).
- **Non-Markovian extension**: valid for any Bochner-admissible kernel $K(\tau)$.
- **Single particle**: the theorem concerns one quantum Brownian particle coupled to one thermal bath.

## What Bochner positivity does and does not prove

**Does prove:** All three kernels (Drude, algebraic, Gaussian) with $A, \Omega > 0$ are positive-definite and hence admissible bath correlators.

**Does NOT prove:** Admissibility does not imply uniqueness. Infinitely many positive-definite kernels exist. The closure $D_{\mathrm{th}} = 2 D_q$ selects a relationship between $\gamma_0$ and $T$ but does not select a unique kernel.

## Known limitations

1. **No first-principles derivation** of Conjecture 1. Three routes sketched but not completed:
   - Thermofield-double construction proving forward/backward noise independence
   - Guerra–Morato variational argument connecting Nelson action to Landauer cost
   - Direct experimental measurement of $R$

2. **No experimental test yet.** Three falsification protocols are proposed:
   - Diffusion-ratio measurement in trapped ions / optomechanical oscillators
   - Optimal-erasure friction in colloidal Landauer erasure
   - Superfluid He-4 second-sound attenuation

3. **Mass independence** is a feature, not a bug — but it means the theorem says nothing about mass-dependent physics.

4. **The theorem is conditional.** If Conjecture 1 is false, the equivalences still hold in their general form, but the specific value $R = 2$ loses its physical motivation.
