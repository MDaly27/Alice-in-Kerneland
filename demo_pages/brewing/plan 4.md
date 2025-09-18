# **4) ANOVA / Post-Hoc / Multiple Testing**

## **4.1 ANOVA (Analysis of Variance) Model**

When comparing **three or more** group means, ANOVA addresses whether there’s a statistically significant difference among these means. We focus on **One-Way ANOVA** (one factor with multiple levels).

### **Data Setup**

- We have $$a$$ groups (levels of the factor).
- Let $$n_i$$ be the sample size in the $$i$$-th group (for $$i = 1,2,\dots,a$$).
- Let $$y_{ij}$$ be the observation in the $$j$$-th subject of the $$i$$-th group, where $$j = 1,2,\dots,n_i$$.

We assume each observation follows:

$$
y_{ij} = \mu_i + \varepsilon_{ij},
$$

where:

- $$\mu_i$$ is the true mean of the $$i$$-th group.
- $$\varepsilon_{ij} \sim N(0, \sigma^2)$$ (normal, independent, same variance $$\sigma^2$$ for all groups).

### **Grand Mean & Group Means**

- **Group Mean**:

$$
\bar{y}_i 
= \frac{1}{n_i}\sum_{j=1}^{n_i} y_{ij}.
$$

- **Grand Mean**:

$$
\bar{y}_{\text{grand}} 
= \frac{1}{\sum_{i=1}^a n_i}\,\sum_{i=1}^a \sum_{j=1}^{n_i} y_{ij}.
$$

### **Sums of Squares**

1. **Total Sum of Squares (SST)**: Overall variability around the grand mean.

   $$
   \text{SST} 
   = \sum_{i=1}^a \sum_{j=1}^{n_i} \bigl(y_{ij} - \bar{y}_{\text{grand}}\bigr)^2.
   $$

2. **Between-Groups Sum of Squares (SSB)**: Variability **between** group means and the grand mean.

   $$
   \text{SSB} 
   = \sum_{i=1}^a n_i \bigl(\bar{y}_i - \bar{y}_{\text{grand}}\bigr)^2.
   $$

3. **Within-Groups Sum of Squares (SSW)**: Variability **within** each group.

   $$
   \text{SSW} 
   = \sum_{i=1}^a \sum_{j=1}^{n_i} \bigl(y_{ij} - \bar{y}_i\bigr)^2.
   $$

And note:

$$
\text{SST} 
= \text{SSB} + \text{SSW}.
$$

### **Mean Squares & F-Statistic**

- **Mean Square Between (MSB)**:

$$
\text{MSB}
= \frac{\text{SSB}}{a - 1}.
$$

- **Mean Square Within (MSW)**:

$$
\text{MSW}
= \frac{\text{SSW}}{\sum_{i=1}^a (n_i - 1)}.
$$

- **F-Statistic**:

$$
F
= \frac{\text{MSB}}{\text{MSW}}.
$$

**Interpretation**: A **large** $$F$$ suggests that **between-groups** variation dominates **within-groups** variation → at least one group mean differs from the others.

#### **Every Variable Defined**

- $$y_{ij}$$: The $$j$$-th observation in group $$i$$.
- $$\bar{y}_i$$: Mean of group $$i$$.
- $$\bar{y}_{\text{grand}}$$: Overall mean across all groups/observations.
- $$n_i$$: Number of observations in group $$i$$.
- $$a$$: Number of groups.
- $$\text{SST}$$: Total sum of squares.
- $$\text{SSB}$$: Between-groups sum of squares.
- $$\text{SSW}$$: Within-groups sum of squares.
- $$\text{MSB}$$: Mean square between = $$\text{SSB}/(a-1)$$.
- $$\text{MSW}$$: Mean square within = $$\text{SSW}/(\sum_{i=1}^a (n_i - 1))$$.
- $$F$$: F-statistic = ratio of MSB to MSW.

### **Use Case Example**

- **Comparing 4 Marketing Strategies**: Each group = strategy type. We measure “sales” under each strategy, then run an ANOVA.  
- If $$F$$ is large and $$p < \alpha$$, we conclude at least one strategy’s mean sales differs from the others.

---

## **4.2 Post-Hoc Tests & Multiple Testing**

When ANOVA is significant, **Post-Hoc Tests** identify **which** specific group means differ.

### **Popular Post-Hoc Methods**

1. **Tukey’s HSD (Honest Significant Difference)**
2. **Bonferroni Correction**
3. **Scheffé Test**

All aim to control **familywise error rate (FWER)** or a **false discovery rate** to avoid multiple Type I errors across many comparisons.

### **Multiple Testing**: Problem & Solutions

- **Problem**: More tests → higher chance of spurious significance (false positive).
- **Solutions**:
  - **Bonferroni**: Adjust $$\alpha \to \alpha / m$$, where $$m$$ is number of tests.
  - **Holm, BH/FDR**: More refined corrections to limit total false discoveries.

---

# **5) Regression Basics (Coefficients, Assumptions, Diagnostics)**

## **5.1 The Linear Regression Model**

In **simple linear regression** with one predictor $$x$$:

$$
y_i 
= \beta_0 + \beta_1 x_i + \varepsilon_i,
$$

- $$y_i$$: outcome (dependent variable).
- $$x_i$$: predictor (independent variable).
- $$\beta_0$$: intercept (value of $$y$$ when $$x=0$$).
- $$\beta_1$$: slope (change in $$y$$ for a 1-unit increase in $$x$$).
- $$\varepsilon_i \sim N(0,\sigma^2)$$: error term.

For **multiple linear regression** with $$k$$ predictors $$x_{i1}, x_{i2}, \dots, x_{ik}$$:

$$
y_i 
= \beta_0 + \beta_1 x_{i1} + \beta_2 x_{i2} + \cdots + \beta_k x_{ik} + \varepsilon_i.
$$

### **OLS (Ordinary Least Squares)**

We estimate $$\boldsymbol{\beta}$$ by minimizing sum of squared residuals:

$$
\hat{\boldsymbol{\beta}}
= \underset{\boldsymbol{\beta}}{\mathrm{argmin}} 
  \sum_{i=1}^n 
  \bigl(y_i - \beta_0 - \beta_1 x_{i1} - \cdots - \beta_k x_{ik}\bigr)^2.
$$

In matrix form ($$\mathbf{y} = X \boldsymbol{\beta} + \boldsymbol{\varepsilon}$$):

$$
\hat{\boldsymbol{\beta}}
= (X^\top X)^{-1} X^\top \mathbf{y},
$$

where:

- $$\mathbf{y}$$: $$n \times 1$$ vector of responses.
- $$X$$: $$n \times (k+1)$$ design matrix (first column = 1’s for intercept).
- $$\boldsymbol{\beta}$$: $$(k+1) \times 1$$ vector of parameters.
- $$\boldsymbol{\varepsilon}$$: $$n \times 1$$ vector of errors.

### **Interpretation of $$\beta_j$$**

- $$\beta_j$$ is the estimated change in $$y$$ for a 1-unit increase in $$x_j$$, holding **all other** predictors constant.

## **5.2 Assumptions of OLS Regression**

1. **Linearity**: $$y$$ is linearly related to each predictor.
2. **Independence**: Residuals $$\varepsilon_i$$ are independent.
3. **Homoscedasticity**: $$\mathrm{Var}(\varepsilon_i)=\sigma^2$$ (constant variance).
4. **Normality**: Residuals $$\varepsilon_i$$ are normal (important for small-sample inference).

## **5.3 Diagnostic Plots**

- **Residuals vs. Fitted**: Look for random scatter (no pattern).
- **Q–Q Plot**: Assess normality of residuals.
- **Scale-Location Plot**: Checks if variance is constant across fitted values.
- **Influence/Leverage**: Identify outliers that may heavily affect the fit.

### **Example Use Case**

- Predicting **house prices** from square footage, #bedrooms, region, etc. Coefficients show how each factor influences price.

---

# **6) Advanced Regression Topics**

## **6.1 Collinearity (Multicollinearity)**

When **predictors are highly correlated**, results can show:

- **Inflated standard errors** of $$\hat{\beta}$$.
- **Unstable** coefficient estimates (small data changes → large coefficient swings).

### **Detection Tools**

- **Variance Inflation Factor (VIF)**: For predictor $$X_j$$,

$$
\text{VIF}_j 
= \frac{1}{1 - R_j^2},
$$

where $$R_j^2$$ is from regressing $$X_j$$ on other predictors. A large VIF (>5 or 10) signals strong collinearity.

### **Fixes**

- **Drop** correlated predictors.
- **Combine** them (averaging, principal components).
- **Regularization** (Ridge, Lasso) shrinks large coefficients.

---

## **6.2 Interaction Terms**

Sometimes, the effect of one predictor depends on another (i.e., an interaction). A 2-way interaction with $$X_1$$ and $$X_2$$:

$$
y 
= \beta_0 + \beta_1 X_1 + \beta_2 X_2 + \beta_3 (X_1 \times X_2) + \varepsilon.
$$

- $$\beta_3$$: interaction coefficient.
- If $$\beta_3 \neq 0$$, the slope for $$X_1$$ changes depending on $$X_2$$.

### **Example**

- Effect of medication dosage ($$X_1$$) might be larger for older patients ($$X_2 = \text{age}$$) → synergy or antagonism.

---

## **6.3 Random Effects (Mixed Models)**

In a **mixed-effects** or **multilevel** model:

$$
y_{ij}
= \beta_0 + \beta_1 x_{ij} + u_i + \varepsilon_{ij},
$$

- $$y_{ij}$$: outcome for subject $$j$$ in group $$i$$.
- $$u_i \sim N(0, \sigma_u^2)$$: a random intercept for group $$i$$.
- $$\varepsilon_{ij}$$: residual error.

### **Why Use Random Effects?**

- Accounts for **intra-group correlation** (e.g., repeated measures on same subject).
- More **efficient** than ignoring grouping; yields better fixed-effects inference.

---

# **7) Model Selection & Overfitting (AIC, Cross-Validation, Bias-Variance)**

## **7.1 Overfitting**

- A model is **overfitted** if it fits random noise/idiosyncrasies in training data rather than true structure.
- Symptom: Great training performance, poor test/validation performance.

---

## **7.2 AIC (Akaike Information Criterion)**

For a model with **log-likelihood** $$\hat{L}$$ and **$$k$$ parameters**:

$$
\text{AIC}
= 2k - 2 \ln(\hat{L}).
$$

- $$k$$: total #parameters (intercept, slopes, variance, etc.).
- $$\ln(\hat{L})$$: maximized log-likelihood of the model.
- **Interpretation**: Lower AIC → better balance of fit vs. complexity.

---

## **7.3 Cross-Validation**

### **$$k$$-Fold Cross-Validation**

1. Split dataset into $$k$$ equal **folds**.
2. For each fold $$f = 1,\dots,k$$:
   - Train on the other $$k-1$$ folds.
   - Test on fold $$f$$.
3. Compute average test error (e.g., MSE).

$$
\text{CV Error}
= \frac{1}{k}\,\sum_{f=1}^k (\text{Error on fold } f).
$$

- Lower CV error → better generalization.

---

## **7.4 Bias-Variance Tradeoff**

A simplified formula for expected prediction error at $$x_0$$:

$$
\mathbb{E}\bigl[(\hat{f}(x_0) - f(x_0))^2\bigr]
= \bigl[\mathrm{Bias}(\hat{f}(x_0))\bigr]^2
+ \mathrm{Var}\bigl(\hat{f}(x_0)\bigr)
+ \sigma^2.
$$

- **Bias**: Error from oversimplified assumptions.
- **Variance**: Sensitivity to training-set fluctuations.
- $$\sigma^2$$: Irreducible noise in data.

#### **Every Variable Defined**

- $$\hat{f}(x_0)$$: predicted value at $$x_0$$.
- $$f(x_0)$$: true (unknown) function at $$x_0$$.
- $$\mathrm{Bias}(\hat{f}(x_0))$$: difference between expected prediction & true value.
- $$\mathrm{Var}(\hat{f}(x_0))$$: how sensitive the prediction is to data changes.
- $$\sigma^2$$: noise variance.

---

# **8) Publication Bias, Meta-Analysis, Multi-Analyst**

## **8.1 Publication Bias**

- Phenomenon: _significant_ results are more likely to be published.
- Distorts the scientific record (“file drawer” effect for non-significant findings).

### **Example**

- Out of 20 trials, only 3 with a “significant” drug effect see publication → inflated belief in efficacy.

---

## **8.2 Meta-Analysis**

- Combines **multiple studies** on the **same** question.
- Often a weighted average of effect sizes (weights ~ inverse of variance).

### **Fixed-Effect Model (Simple)**

If $$\theta_i$$ = effect estimate (study $$i$$), variance $$v_i$$, then:

$$
\hat{\Theta}
= \frac{\sum_{i=1}^k \frac{\theta_i}{v_i}}
{\sum_{i=1}^k \frac{1}{v_i}}.
$$

### **Random-Effects Model**

- Adds between-study variance $$\tau^2$$, adjusting each study’s weight.

### **Multi-Analyst Issue**

- Different analysts, same data → differing methods, transformations, subgroups → different results.
- **Solution**: Pre-registration, standard protocols, open data/code, or multi-analyst collaboration.

---

# **Wrap-Up & Applications**

- **ANOVA**: More than 2 groups → compare means via F-statistic.
- **Regression**: Model continuous outcome from predictors.  
- **Advanced Regression**: Interactions, correlated data, random effects.  
- **Model Selection**: Avoid overfitting with AIC/CV.  
- **Publication Bias & Meta-Analysis**: Integrate results carefully and watch for missing “negative” findings.

**Examples**:
1. **ANOVA**: 3 new diets → see if average weight loss differs.
2. **Regression**: Predict employee performance from training hours, job role, and prior experience.
3. **Collinearity**: Highly correlated job role & experience → big standard errors, watch out or reduce dimension.
4. **Overfitting**: 50 predictors, 100 data points → artificially high $$R^2$$. Use cross-validation or AIC to prune.
5. **Meta-Analysis**: Summarize 10 RCTs on a vaccine → check funnel plot for publication bias.

---

## **Dark Humor Memory Nuggets**

- **ANOVA**: Each group is a “torture chamber.” If the screams (means) differ too much, $$F$$ is big → something horrifying is happening.
- **Regression**: Ignored assumptions = “Frankenstein’s monster,” hobbling around with broken residuals.
- **Collinearity**: Evil twins messing up your interpretation of who’s truly responsible.
- **Overfitting**: A model so overloaded it suffocates under its own complexity.
- **Publication Bias**: Many “dead” (null) experiments buried out back, so the living see a skewed reality.

---

## **Key Formulas Recap (with Variables Defined)**

1. **ANOVA F**  

   $$
   F 
   = \frac{\text{MSB}}{\text{MSW}}, 
   \quad
   \text{MSB} 
   = \frac{\text{SSB}}{a - 1},
   \quad
   \text{MSW} 
   = \frac{\text{SSW}}{\sum_{i=1}^a (n_i - 1)}.
   $$

2. **Linear Regression**  

   $$
   y_i 
   = \beta_0 + \beta_1 x_{i1} + \dots + \beta_k x_{ik} + \varepsilon_i.
   $$

3. **OLS Estimator (Matrix Form)**  

   $$
   \hat{\boldsymbol{\beta}}
   = (X^\top X)^{-1} X^\top \mathbf{y}.
   $$

4. **Variance Inflation Factor (VIF)**  

   $$
   \text{VIF}_j
   = \frac{1}{1 - R_j^2}.
   $$

5. **Interaction**  

   $$
   y
   = \beta_0 + \beta_1 X_1 + \beta_2 X_2 + \beta_3 (X_1 \times X_2) + \varepsilon.
   $$

6. **AIC**  

   $$
   \text{AIC}
   = 2k - 2 \ln(\hat{L}).
   $$

7. **Cross-Validation Error** (k-fold)  

   $$
   \text{CV Error}
   = \frac{1}{k}\,\sum_{f=1}^k \text{MSE on fold } f.
   $$

8. **Bias-Variance Decomposition**  

   $$
   \mathbb{E}\bigl[(\hat{f}(x_0) - f(x_0))^2\bigr]
   = [\text{Bias}(\hat{f}(x_0))]^2 
   + \mathrm{Var}(\hat{f}(x_0)) 
   + \sigma^2.
   $$

9. **Meta-Analysis (Fixed-Effect Weighting)**  

   $$
   \hat{\Theta}
   = \frac{\sum_{i=1}^k \left(\frac{\theta_i}{v_i}\right)}
           {\sum_{i=1}^k \frac{1}{v_i}}.
   $$

---

### **Practical Advice**

1. Always **check** assumptions before finalizing a model.  
2. For **multiple groups**, use ANOVA over repeated pairwise tests.  
3. With **multiple predictors**, watch for collinearity; consider interactions or random effects if data is nested.  
4. For **model selection**, don’t rely on $$R^2$$ alone; look at AIC/CV.  
5. Use **meta-analysis** to synthesize multiple studies—but be wary of publication bias.

---

## **Improvement Suggestions**

1. **Memorize Variables**: Make flashcards for symbols ($$\beta_1$$, SSW, $$\hat{\Theta}$$, etc.).  
2. **Derive on Paper**: Work out ANOVA sums of squares to see the $$F$$-stat come alive.  
3. **Simulate**: Code small examples (ANOVA, regression, random effects) to see formulas in action.  
4. **Review Real Papers**: Watch how these formulas are reported, watch for pitfalls or assumptions.  

