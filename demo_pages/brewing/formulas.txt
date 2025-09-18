z# **Statistics: Master Key, Formulas, Explanations, Plotly Demo, & Knowledge Check**

## 1) Master Key of Variables & Parameters

Below is a “one-stop shop” of symbols, their names, and (where relevant) how they’re computed from other symbols.

| Symbol                                                    | Name / Meaning                                                   | Relationships / Formula                                                                                                     |
| --------------------------------------------------------- | ---------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| \( n \)                                                   | Sample size                                                      |                                                                                                                             |
| \( k \)                                                   | Number of groups (ANOVA, etc.)                                   |                                                                                                                             |
| \( X \)                                                   | Data matrix (predictors), dimension: \(n \times p\)              |                                                                                                                             |
| \( y \)                                                   | Outcome vector (responses), dimension: \(n \times 1\)            |                                                                                                                             |
| \( p \)                                                   | Number of predictors/features                                    |                                                                                                                             |
| \(\bar{x}\)                                               | Sample mean of a set of observations \( x_1, x_2, \ldots, x_n \) | $$ \bar{x} = \frac{1}{n} \sum_{i=1}^n x_i $$                                                                                |
| \( s^2 \)                                                 | Sample variance of \( x_i \)                                     | $$ s^2 = \frac{1}{n-1} \sum_{i=1}^n (x_i - \bar{x})^2 $$                                                                    |
| \( \mu \)                                                 | Population mean                                                  |                                                                                                                             |
| \( \sigma^2 \)                                            | Population variance                                              |                                                                                                                             |
| \( p_1, p_2 \)                                            | Probability of event in Group 1 vs. Group 2                      |                                                                                                                             |
| \( \text{RR} \)                                           | Relative Risk                                                    | $$ \text{RR} = \frac{p_1}{p_2} $$                                                                                           |
| \( \text{OR} \)                                           | Odds Ratio                                                       | $$ \text{OR} = \frac{\frac{p_1}{1 - p_1}}{\frac{p_2}{1 - p_2}} $$                                                           |
| \( \hat{\beta} \)                                         | Estimated regression coefficients (\(\beta_0, \beta_1, \dots\))  | $$ \hat{\beta} = (X^\top X)^{-1} X^\top y $$                                                                                |
| \( \beta_0, \beta_1, \dots, \beta_p \)                    | True (or hypothesized) regression coefficients                   |                                                                                                                             |
| \( \hat{y}_i \)                                           | Fitted value (prediction)                                        | $$ \hat{y}_i = \beta_0 + \beta_1 x_{i1} + \dots + \beta_p x_{ip} $$                                                         |
| \( \varepsilon_i \)                                       | Error (residual) for observation \(i\)                           | $$ \varepsilon_i = y_i - \hat{y}_i $$                                                                                       |
| \( \text{Var}(\varepsilon)\)                              | Variance of errors                                               | Often assumed \(\sigma^2 I\) in linear models                                                                               |
| \( t \)                                                   | t-statistic                                                      | See t-test formulas below                                                                                                   |
| \( F \)                                                   | F-statistic (ANOVA or regression)                                | $$ F = \frac{\text{MS}_{\text{between}}}{\text{MS}_{\text{within}}} $$ or $$ \frac{\text{MSR}}{\text{MSE}} $$ in regression |
| \(\text{MS}_{\text{between}}\)                            | Mean square between groups                                       | $$ \text{MS}_{\text{between}} = \frac{\text{SS}_{\text{between}}}{k - 1} $$                                                 |
| \(\text{MS}_{\text{within}}\)                             | Mean square within groups                                        | $$ \text{MS}_{\text{within}}  = \frac{\text{SS}_{\text{within}}}{n - k} $$                                                  |
| \(\alpha\)                                                | Significance level (Type I error rate)                           | Commonly 0.05                                                                                                               |
| \( p\text{-value} \)                                      | Probability measure for hypothesis tests                         | Computed from distribution of test statistic                                                                                |
| \(\text{SE}\)                                             | Standard Error                                                   | e.g., $$ \text{SE}(\bar{x}) = \frac{\sigma}{\sqrt{n}} $$                                                                    |
| \(\text{CI}\)                                             | Confidence Interval                                              | e.g., $$ \bar{x} \pm z_{\alpha/2}\times \text{SE}(\bar{x}) $$                                                               |
| \(\text{VIF}_j\)                                          | Variance Inflation Factor for predictor \(j\)                    | $$ \text{VIF}_j = \frac{1}{1 - R_j^2} $$ (where \(R_j^2\) is from regressing \( x_j \) on other predictors)                 |
| \( R^2 \)                                                 | Coefficient of Determination (regression)                        | $$ R^2 = 1 - \frac{\text{SS}_{\text{res}}}{\text{SS}_{\text{total}}} $$                                                     |
| \(\text{Adjusted }R^2\)                                   | Adjusted R-squared                                               | $$ 1 - \frac{\text{SS}_{\text{res}}/(n - p - 1)}{\text{SS}_{\text{total}}/(n - 1)} $$                                       |
| \(\text{AIC}\)                                            | Akaike Information Criterion                                     | $$ \text{AIC} = 2p - 2\ln(\hat{L}) $$                                                                                       |
| \(\text{BIC}\)                                            | Bayesian Information Criterion                                   | $$ \text{BIC} = \ln(n)\,p - 2\ln(\hat{L}) $$                                                                                |
| \( d \) (Cohen’s d)                                       | Effect size for mean difference                                  | $$ d = \frac{\bar{x}_1 - \bar{x}_2}{s_{\text{pooled}}} $$                                                                   |
| \(\eta^2\)                                                | ANOVA effect size                                                | $$ \eta^2 = \frac{\text{SS}_{\text{between}}}{\text{SS}_{\text{total}}} $$                                                  |
| \(\rho\)                                                  | Correlation (population)                                         |                                                                                                                             |
| \( r \)                                                   | Correlation (sample)                                             | $$ r = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\sum (x_i - \bar{x})^2}\sqrt{\sum (y_i - \bar{y})^2}} $$            |
| \( I^2 \)                                                 | Heterogeneity statistic in meta-analysis                         | $$ I^2 = \frac{Q - (k - 1)}{Q} \times 100\% $$ (where \(Q\) is Cochran’s Q)                                                 |
| \(\sigma_\alpha^2, \sigma_\beta^2\)                       | Variance components (random effects)                             | In Mixed Models, random intercepts/slopes have distinct variances                                                           |
| \(\text{ICC}\)                                            | Intraclass Correlation                                           | $$ \text{ICC} = \frac{\sigma_{\text{between}}^2}{\sigma_{\text{between}}^2 + \sigma_{\text{within}}^2} $$                   |
| \(\text{CV}\)                                             | Cross-Validation                                                 | Not a formula by itself—technique for model assessment                                                                      |
| \(\text{Bias}^2 + \text{Var} + \text{Irreducible Error}\) | Bias-Variance decomposition                                      | $$ \text{MSE} = \text{Var}(\hat{f}(x)) + [\text{Bias}(\hat{f}(x))]^2 + \text{noise} $$                                      |

---

 Simple Plotly Code Block (CLT Demo)

```python
import plotly.graph_objects as go
import numpy as np

# Parameters
population_mean = 50
population_std = 10
sample_size = 30
num_replications = 10000

# Generate the sampling distribution of the mean
means = []
for _ in range(num_replications):
    sample = np.random.normal(loc=population_mean, scale=population_std, size=sample_size)
    means.append(np.mean(sample))

# Create histogram using Plotly
fig = go.Figure(data=[go.Histogram(x=means, nbinsx=50, marker_color='blue')])
fig.update_layout(
    title='Sampling Distribution of the Mean (CLT Demo)',
    xaxis_title='Sample Means',
    yaxis_title='Frequency',
    bargap=0.1
)

fig.show()
