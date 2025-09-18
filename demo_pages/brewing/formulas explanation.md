### 1) Relative Risk vs. Odds Ratio

**Relative Risk (RR):**

$$
\text{RR} = \frac{p_1}{p_2}
$$

**Odds Ratio (OR):**

$$
\text{OR} = \frac{\frac{p_1}{1 - p_1}}{\frac{p_2}{1 - p_2}}
$$

**Log Transform (common for CI calculations):**

$$
\log(\text{OR}) = \log\!\biggl(\frac{p_1 / (1 - p_1)}{p_2 / (1 - p_2)}\biggr)
$$

---

### 2) Central Limit Theorem (CLT)

**Mean of Sample:**

$$
\bar{X} = \frac{1}{n} \sum_{i=1}^n X_i
$$

**Standard Error of Mean:**

$$
\text{SE}(\bar{X}) = \frac{\sigma}{\sqrt{n}}
$$

**Normal Approximation (as \( n \to \infty \)):**

$$
\bar{X} \xrightarrow{\text{approx}} \mathcal{N}\bigl(\mu, \frac{\sigma^2}{n}\bigr)
$$

---

### 3) Regression Coefficients (OLS)

**OLS Estimation:**

$$
\hat{\beta} = (X^\top X)^{-1} X^\top y
$$

**Fitted Values:**

$$
\hat{y} = X \hat{\beta}
$$

**Residuals:**

$$
e = y - \hat{y}
$$

---

### 4) Model Assumptions & Violations

- **Linearity**: \( y_i = \beta_0 + \beta_1 x_i + \varepsilon_i \)
- **Normality of Residuals**: \( \varepsilon_i \sim \mathcal{N}(0, \sigma^2)\)
- **Homoscedasticity**: \(\text{Var}(\varepsilon_i) = \sigma^2\)

---

### 5) Parameter Collinearity

**Variance Inflation Factor (VIF):**

$$
\text{VIF}_j = \frac{1}{1 - R_j^2}
$$

---

### 6) ANOVA F Statistic

**Sum of Squares Between:**

$$
\text{SS}_{\text{between}} = \sum_{g=1}^k n_g \bigl(\bar{x}_g - \bar{x}_{\text{overall}}\bigr)^2
$$

**Sum of Squares Within:**

$$
\text{SS}_{\text{within}} = \sum_{g=1}^k \sum_{i=1}^{n_g} (x_{ig} - \bar{x}_g)^2
$$

**Mean Squares:**

$$
\text{MS}_{\text{between}} = \frac{\text{SS}_{\text{between}}}{k - 1}, \quad
\text{MS}_{\text{within}}  = \frac{\text{SS}_{\text{within}}}{n - k}
$$

**F-Statistic:**

$$
F = \frac{\text{MS}_{\text{between}}}{\text{MS}_{\text{within}}}
$$

---

### 7) Paired vs. Two-Sample T-Tests

**Two-Sample \(t\)-Test (Independent):**

$$
t = \frac{\bar{x}_1 - \bar{x}_2}{\sqrt{\frac{s_1^2}{n_1} + \frac{s_2^2}{n_2}}}
$$

**Paired \(t\)-Test** (using difference scores \( d_i = x_{i1} - x_{i2} \)):

$$
t = \frac{\bar{d}}{s_d / \sqrt{n}}
$$

---

### 8) Effect Size \((R^2)\) vs. Significance \((p\)-value\)

**Coefficient of Determination:**

$$
R^2 = 1 - \frac{\text{SS}_{\text{res}}}{\text{SS}_{\text{total}}}
$$

**Cohen’s d (for mean difference):**

$$
d = \frac{\bar{x}_1 - \bar{x}_2}{s_{\text{pooled}}}
$$

---

### 9) Post-Hoc Comparisons & Multiple Testing

**Bonferroni Correction:**

$$
\alpha_{\text{adjusted}} = \frac{\alpha}{m}
$$

(Where \(m\) is the number of comparisons.)

---

### 10) Outliers

- **z-Score**: $$ z = \frac{x - \bar{x}}{s} $$
- **Leverage (Hat Values)**: $$ h_{ii} = x_i^\top (X^\top X)^{-1} x_i $$
- **Cook’s Distance**:

$$
D_i = \frac{e_i^2}{p \cdot \text{MSE}} \times \frac{h_{ii}}{(1 - h_{ii})^2}
$$

---

### 11) Random Effects

**Mixed Model (simplified):**

$$
y_{ij} = \beta_0 + b_{0j} + \beta_1 x_{ij} + \varepsilon_{ij}, \quad b_{0j} \sim \mathcal{N}(0, \sigma_\alpha^2)
$$

**Intraclass Correlation (ICC):**

$$
\text{ICC} = \frac{\sigma_{\text{between}}^2}{\sigma_{\text{between}}^2 + \sigma_{\text{within}}^2}
$$

---

### 12) Overfitting

- **Training vs. Test Error** difference
- **AIC** & **BIC**:

$$
\text{AIC} = 2p - 2\ln(\hat{L}), \quad
\text{BIC} = \ln(n)\,p - 2\ln(\hat{L})
$$

---

### 13) Scientific vs. Statistical Significance

- **Effect Size** (Cohen’s d or \(\beta\) magnitude)
- **\(p\)-value**
- **Confidence Intervals**

(No single new formula here.)

---

### 14) Interaction Terms

**Linear Model with Interaction (2 predictors \( x_1, x_2\)):**

$$
y = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + \beta_3 (x_1 \times x_2) + \varepsilon
$$

---

### 15) Choosing Model Complexity

- **Information Criteria** (AIC, BIC)
- **Cross-Validation** (CV error)

(Already covered formulas for AIC and BIC.)

---

### 16) Residual Diagnostic Plots

- **Residual**: \( e_i = y_i - \hat{y}_i \)
- **Cook’s Distance, Leverage** (already shown)

---

### 17) Bias-Variance Tradeoff

**Bias-Variance Decomposition (informal):**

$$
\text{MSE}(\hat{f}) = \underbrace{\text{Var}(\hat{f}(x))}_{\text{Variance}} + \underbrace{\bigl[\mathbb{E}(\hat{f}(x)) - f(x)\bigr]^2}_{\text{Bias}^2} + \underbrace{\sigma^2}_{\text{noise}}
$$

---

### 18) Publication Bias & Meta-Analyses

**Fixed-Effects Meta-Analysis (simplified):**

$$
\hat{\theta} = \frac{\sum_{i=1}^k w_i \hat{\theta}_i}{\sum_{i=1}^k w_i} \quad \text{where} \; w_i = \frac{1}{\text{Var}(\hat{\theta}_i)}
$$

**Heterogeneity (\(I^2\)):**

$$
I^2 = \frac{Q - (k - 1)}{Q} \times 100\%
$$

---

### 19) Regression to the Mean

No single formula, but concept: extreme values in one measurement tend to be closer to the mean in subsequent measurements.

---

### 20) Multi-Analyst Studies

No unique formula—emphasizes how different analysts can yield different results from the same data.

---

