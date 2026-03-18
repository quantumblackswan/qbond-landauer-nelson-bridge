# Referee Notes (BT#11)

Pre-submission risk analysis and prepared responses for anticipated referee objections.

## Risk 1: "The closure D_th = 2 D_q is assumed, not proven"

**Severity:** High (certain to be raised)

**Response:** We agree completely. The paper is structured as a *conditional* theorem. Conjecture 1 is stated explicitly (Section V), and Section VII ("What Is and Is Not Proven") draws the line clearly. Five independent motivations are given, but we do not claim a derivation. Three falsification protocols are provided so the conjecture is empirically testable.

## Risk 2: "Why should Nelson diffusion be physically relevant?"

**Severity:** Medium

**Response:** Nelson's stochastic mechanics is mathematically equivalent to Schrödinger quantum mechanics for conservative systems (Nelson 1966, Guerra & Morato 1983). The diffusion coefficient $D_q = \hbar/(2m)$ appears in any stochastic quantization framework. We do not require Nelson's ontological interpretation — only the kinematic identity $D_q = \hbar/(2m)$.

## Risk 3: "The result is trivial / just dimensional analysis"

**Severity:** Medium

**Response:** The ratio $R = 2k_BT/(\gamma_0\hbar)$ is dimensionless, so dimensional analysis alone cannot fix $R = 2$. The content is that (a) the bridge energy at $R = 2$ equals exactly one Landauer bit, (b) $R = 2$ is the unique temperature-independent value, and (c) the TICE kernel framework extends this to non-Markovian dynamics with exact crossing-time solutions.

## Risk 4: "What is new beyond Caldeira–Leggett?"

**Severity:** Medium

**Response:** Caldeira–Leggett gives $D_{\mathrm{th}} = k_BT/(m\gamma_0)$ but does not connect this to Nelson's $D_q$ or to Landauer's bound. The bridge energy $E_{\mathrm{bridge}} = k_BT \ln(D_{\mathrm{th}}/D_q)$ is new. The TICE closure factor $C_{\mathrm{TICE}}(t)$ and the exact deviation law are new. The three kernel solutions with explicit crossing times are new.

## Risk 5: "The TICE framework seems ad hoc"

**Severity:** Low–Medium

**Response:** The TICE closure factor $C_{\mathrm{TICE}}(t) = k_BT/[\hbar \gamma_{\mathrm{eff}}(t)]$ is a natural generalization: it reduces to the Markov theorem when the kernel integral converges, and the master formula $E_{\mathrm{bridge}}^{\mathrm{TICE}} = k_BT\ln(2C_{\mathrm{TICE}})$ is exact. The three kernel solutions demonstrate that the framework is computationally tractable, not just formal.

## Risk 6: "No experimental evidence is presented"

**Severity:** Medium

**Response:** This is a theoretical letter. Three concrete falsification protocols are proposed (Section VI), each targeting existing experimental platforms (trapped ions, colloidal systems, superfluid helium). We encourage experimentalists to test the prediction $R = 2.000 \pm \epsilon$.
