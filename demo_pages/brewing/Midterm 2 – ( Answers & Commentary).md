
## EXAM II (SPRING 24)

This exam is composed of 21 questions on 6 pages.  
**Note:** You should leave one question blank. If you answer all the questions, your answer for question 21 will not be graded.  
Be sure to write your name on each page of the exam, and check that you have all of the pages. Questions total 40 points.  
You have one hour and fifteen minutes to complete the exam. Think about maximizing the number of points that you earn during the exam period, and read the questions carefully.  
This exam is administered under the Notre Dame Honor Code. All answers are expected to be your own. You may use notes hand-written on ONE regular sheet of paper.  
Please:
- Write neatly.
- Don’t write beyond the space allotted.
- Show your work.

Good Luck!

---

### I. MULTIPLE CHOICE (2 points each)
Circle or write the letter of your choice for each question below.  
**Correct answers in bold.**

1. A difference between relative-risk (RR) and the odds-ratio (OR) is:  
   A) RR measures an association between two categorical variables.  
   B) OR measures an association between two categorical variables.  
   **C) RR assumes unbiased estimates of the probability of two outcomes in the population of interest.**  
   D) None of the above is a difference between RR and OR.

2. The central limit theorem assures us that the mean of a random sample is approximately normally distributed,  
   A) so long as the sample distribution is approximately normal.  
   B) so long as the population distribution is approximately normal.  
   C) so long as the standard deviation of the sample is approximately normal.  
   **D) so long as the sample size is large enough.**

3. The coefficients in a regression model (the β’s) are:  
   **A) parameters**  
   B) variables  
   C) factors  
   D) statistics

4. Which of the following is an inappropriate solution to violations of model assumptions?  
   A) Transform the data.  
   B) Collect more data.  
   **C) Discard data that don’t fit the model assumptions.**  
   D) Use a different model.

5. Parameter collinearity can lead to  
   A) poor estimates of parameter coefficients.  
   B) artificially high or low p-values.  
   C) overfitting.  
   **D) All of the above are true.**

---

### II. SHORT ANSWER QUESTIONS (2 points each)

#### 6. F value in ANOVA and “signal-to-noise”
- **Answer**: The F-ratio is essentially the ratio of between-group variance (signal) to within-group variance (noise). Formally, F = MS_groups / MS_error. A larger F-value indicates that the group/treatment effect is large relative to the unexplained variability.

#### 7. Why paired t-tests are often more powerful
- **Answer**: Paired samples typically share background similarities (e.g., repeated measures on the same subjects), reducing variability unrelated to the main effect. This lower “noise” (variance) boosts statistical power, making it easier to detect true differences.

#### 8. R² as a measure of effect size
- **Answer**: R² indicates the proportion of the total variation in the data explained by the model (i.e., SS_model / SS_total). A p-value speaks to statistical significance (the likelihood of seeing data like this if the null hypothesis were true), while R² measures how much of the variation is actually captured by the model.

#### 9. NEJM discouraging p-values for post-hoc comparisons
- **Answer**: They aim to prevent inflated Type I error (false positives) due to multiple comparisons. One solution is to collect additional data specifically targeted at evaluating post-hoc findings or to use corrections (like Bonferroni or Tukey’s HSD). Another is to validate or replicate results in an independent dataset.

#### 10. Why not discard an outlier?
- **Answer**: Unless an outlier is demonstrably due to an error, it’s part of the true distribution and may provide important information. An alternative is to use robust or non-parametric methods, transform the data if appropriate, or include the outlier but examine its influence (e.g., do the analysis with and without it).

#### 11. Random effects reducing uncertainty in fixed effects
- **Answer**: Random effects account for random variation (e.g., blocks, subjects, measurement error) that is not directly of interest but inflates residual variance. By including random effects, you reduce unexplained error, thus obtaining more precise estimates for your fixed effects.

#### 12. Interpretation of α in Y = α + β₁X₁ + ε
- **Answer**: 
  - If X is continuous (simple linear regression), α is the Y-intercept (the expected value of Y when X=0).  
  - If X is a binary variable (t-test formulation), α can be interpreted as the overall mean (often the “baseline” group’s mean if X=0).

#### 13. Overfitting in complex linear models
- **Answer**: Adding many variables can make the model fit random noise rather than real signal, reducing generalizability (i.e., overfitting). To diagnose overfitting, use methods such as AIC/BIC, cross-validation, or independent data sets to test predictive performance.

#### 14. Scientific reason for including a variable
- **Answer**: You might include a variable because it’s mechanistically important (e.g., a known driver of the outcome). It can be defensible to keep such a variable even if it’s not statistically significant, especially when theory strongly suggests it belongs in the model. The p-value alone doesn’t always dictate whether a variable is important scientifically.

#### 15. Significant interaction term
- **Answer**: If β₃X₁X₂ is significant, the effect of X₁ on Y depends on X₂ (and vice versa). In other words, you can’t interpret the main effects β₁ and β₂ as single, universal slopes; the slope for X₁ changes with X₂.

#### 16. Fitting one model vs. multiple simple models
- **Answer**:  
  - *Argument for one model with many variables*: Real-world processes can be multifactorial; omitting important covariates can bias estimates of the ones you do include.  
  - *Argument for separate simpler models*: Minimizes risk of collinearity, avoids overfitting, and simpler models can be more interpretable.  
  - Either approach can be justified if done thoughtfully, with caution about confounding and overfitting.

#### 17. Diagnostic plots
- **Answer**: You’d look for:  
  - Systematic patterns in residuals (e.g., a curve indicating the model is missing a trend).  
  - Outliers/leverage points (e.g., Cook’s D).  
  - Non-normality in a Q–Q plot.  
  - Heteroskedasticity (residuals showing increasing or decreasing spread).  
  If any of these issues are severe, the model is likely a poor fit.

#### 18. Models too simple (high bias) vs. too complex (high variance)
- **Answer**:  
  - (a) **High bias**: The model is too rigid and fails to capture the underlying relationships, systematically missing the mark.  
  - (b) **High variance**: The model “overreacts” to small fluctuations or noise, fitting idiosyncrasies of the training data that don’t generalize well.

#### 19. Publication bias and meta-analysis
- **Answer**: Publication bias means studies with non-significant or “negative” results may not be published, artificially inflating the apparent effect size in the published literature. A meta-analysis only of published studies ends up with a skewed picture, potentially exaggerating the true effect.

#### 20. “Regression to the mean” in flight cadet performance
- **Answer**: This phenomenon states that an extreme performance is likely to be followed by a performance closer to average. Praising a great maneuver is typically followed by a somewhat worse next attempt (closer to the cadet’s normal), while a terrible maneuver is often followed by a better attempt. It’s not necessarily that punishment works or praise fails; it’s statistical regression.

#### 21. Multi-analyst study of religiosity and well-being
- **Answer**: The variation in results (some large positive, some no effect) suggests uncertainty in the true impact. A next step could be collecting a targeted dataset specifically designed to address the role of cultural norms on religiosity/well-being, or replicating with standardized methods to verify the effect size.

---

**END OF EXAM (ANSWERS INCLUDED)**

