## 3) Explanations & Significance (With Brief Examples)

1. **Relative Risk (RR) & Odds Ratio (OR):**  
   - *Significance:* In epidemiology, RR is ratio of probabilities (e.g., incidence in exposed vs. non-exposed), while OR is ratio of odds.  
   - *Example:* If \(p_1 = 0.20\) and \(p_2 = 0.40\), then \(\text{RR} = 0.20/0.40 = 0.5\) and \(\text{OR} \approx 0.37\).

2. **Central Limit Theorem:**  
   - *Significance:* Justifies normal-based inference (z, t-tests) for large samples.  
   - *Example:* Repeated random samples of size \(n\); sample means approach normality as \(n\) grows.

3. **OLS Regression Coefficients:**  
   - *Significance:* \(\hat{\beta}\) minimize residual sum of squares.  
   - *Example:* Predict test scores from study hours; slope \(\beta_1\) is how many points gained per additional hour studied.

4. **Model Assumptions:**  
   - *Significance:* Violations can invalidate standard inference (e.g. inaccurate p-values).

5. **Parameter Collinearity:**  
   - *Significance:* Inflates variance of estimates, measured by high VIF.  
   - *Example:* Height and weight both predicting BMI can cause instability if sample is small.

6. **ANOVA F Statistic:**  
   - *Significance:* Tests whether group means differ more than expected by chance.  
   - *Example:* Compare average test scores among 3 teaching methods.

7. **Paired vs. Two-Sample T-Tests:**  
   - *Significance:* Paired accounts for within-subject variability.  
   - *Example:* Blood pressure in same patients before vs. after treatment.

8. **Effect Size vs. Significance:**  
   - *Significance:* p-value can be small even for trivial effects; effect size is crucial.  
   - *Example:* p=0.001 but \(R^2=0.02\) → small practical impact.

9. **Post-Hoc & Multiple Testing:**  
   - *Significance:* Control Type I error inflation.  
   - *Example:* Bonferroni sets \(\alpha_{\text{adjusted}} = \alpha/m\).

10. **Outliers:**  
   - *Significance:* Can skew estimates or violate assumptions.  
   - *Example:* One extreme data point can drastically change \(\hat{\beta}\).

11. **Random Effects:**  
   - *Significance:* Accounts for correlation within clusters or repeated measures.  
   - *Example:* Students within classes → random intercepts per class.

12. **Overfitting:**  
   - *Significance:* Fits noise, not signal; generalizes poorly.  
   - *Example:* High-degree polynomial that closely fits training data but fails on new data.

13. **Scientific vs. Statistical Significance:**  
   - *Significance:* Must consider effect size, not just p < 0.05.  
   - *Example:* Drug lowers cholesterol by 1 mg/dL with p=0.0001 → trivial clinically, but “significant” statistically.

14. **Interaction Terms:**  
   - *Significance:* Effect of one predictor depends on another.  
   - *Example:* Diet effect on weight loss might differ by age → age × diet interaction.

15. **Choosing Model Complexity:**  
   - *Significance:* Balances fit and interpretability (AIC/BIC).  
   - *Example:* Overly complex polynomial can overfit.

16. **Residual Diagnostic Plots:**  
   - *Significance:* Check assumption violations quickly.  
   - *Example:* Residual vs. fitted plot reveals heteroscedasticity if residuals “fan out.”

17. **Bias-Variance Tradeoff:**  
   - *Significance:* Overfit = high variance, underfit = high bias; find a balance.  
   - *Example:* Complex random forest vs. simpler linear model.

18. **Publication Bias & Meta-Analyses:**  
   - *Significance:* Null results often go unpublished, skewing meta-analysis.  
   - *Example:* Funnel plot asymmetry indicates possible bias.

19. **Regression to the Mean:**  
   - *Significance:* Extreme initial values typically revert toward average on repeat.  
   - *Example:* Star athlete’s “career season” often followed by more average performance.

20. **Multi-Analyst Studies:**  
   - *Significance:* Different analysts can yield different conclusions from same data (choices of methods, outlier handling, etc.).

