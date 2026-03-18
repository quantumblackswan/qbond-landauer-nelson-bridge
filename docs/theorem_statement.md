# Theorem Statement (BT#11)

## Conditional Landauer–Nelson Bridge with Non-Markovian TICE Closure

### Equivalence Theorem

**Theorem.** *The following five conditions are pairwise equivalent for a quantum Brownian particle coupled to a thermal bath:*

1. **(i)** The thermal-to-quantum diffusion ratio is $D_{\mathrm{th}}/D_q = 2$.
2. **(ii)** The friction coefficient is $\gamma_0 = k_B T / \hbar$.
3. **(iii)** The bath correlation time is $\tau_{\mathrm{cor}} = \hbar / (k_B T)$.
4. **(iv)** The bridge energy $E_{\mathrm{bridge}} \equiv k_B T \ln(D_{\mathrm{th}}/D_q) = k_B T \ln 2$ equals one Landauer bit of erasure.
5. **(v)** The ratio $D_{\mathrm{th}}/D_q$ is temperature-independent.

### Definitions

- **Thermal diffusion** (Caldeira–Leggett, Green–Kubo): $D_{\mathrm{th}} = k_B T / (m \gamma_0)$
- **Nelson diffusion** (stochastic mechanics): $D_q = \hbar / (2m)$
- **Diffusion ratio**: $R \equiv D_{\mathrm{th}} / D_q = 2 k_B T / (\gamma_0 \hbar)$
- **Bridge energy**: $E_{\mathrm{bridge}} \equiv k_B T \ln R$

### Proof sketch

- **(i)⇔(ii):** $k_B T/(m\gamma_0) = \hbar/m$ gives $\gamma_0 = k_B T/\hbar$.
- **(ii)⇔(iii):** Definition of $\tau_{\mathrm{cor}} = 1/\gamma_0$.
- **(ii)⇒(iv):** $E_{\mathrm{bridge}} = k_B T \ln[2k_B T/(k_B T)] = k_B T \ln 2$.
- **(iv)⇒(ii):** $k_B T \ln[2k_B T/(\gamma_0 \hbar)] = k_B T \ln 2$ implies $\gamma_0 \hbar = k_B T$.
- **(v)⇔(ii):** $R = 2k_B T/(\gamma_0 \hbar)$ is $T$-independent iff $\gamma_0 \propto T$; combined with $R=2$ this gives $\gamma_0 = k_B T/\hbar$ uniquely.

### Exact Deviation Formula

Write $\gamma_0 = \gamma^*(1+\delta)$ with $\gamma^* = k_B T/\hbar$. Then:

$$\Delta E \equiv E_{\mathrm{bridge}} - E_{\mathrm{Landauer}} = -k_B T \ln(1+\delta)$$

This is **exact** (not perturbative).

### TICE Closure Factor (Non-Markovian Extension)

$$C_{\mathrm{TICE}}(t) \equiv \frac{k_B T}{\hbar \, \gamma_{\mathrm{eff}}(t)}, \qquad E_{\mathrm{bridge}}^{\mathrm{TICE}}(t) = k_B T \ln(2\, C_{\mathrm{TICE}}(t))$$

where $\gamma_{\mathrm{eff}}(t) = \gamma_0 + \beta \int_0^t K(t-\tau) |\psi(\tau)|^2 d\tau$.

### Conjecture 1 (the single unproven assumption)

*The thermal diffusion $D_{\mathrm{th}}$ accounts for both time-directed noise channels in Nelson's bidirectional stochastic mechanics, giving $D_{\mathrm{th}} = 2 D_q$.*

This conjecture is **motivated** by five independent observations but **not derived from first principles**.
