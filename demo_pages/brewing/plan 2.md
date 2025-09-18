# **1) Basic Probability & Sampling**

## **1.1 Probability Fundamentals**

- **Random Experiment**: An action or process whose outcome is subject to uncertainty (e.g., rolling a die).
- **Sample Space (SS)**: The set of all possible outcomes (e.g., for a 6-sided die, \( S = \{1,2,3,4,5,6\} \)).
- **Event**: A subset of the sample space (e.g., “die roll is even”).
- **Probability of an Event (\(P(A)\))**: The long-run relative frequency with which the event \(A\) occurs after many trials.

### **Types of Probability**

- **Classical**: All outcomes assumed equally likely.
- **Frequentist**: Probability as a limit of frequency in repeated experiments.
- **Bayesian**: Probability as a degree of belief, updated with evidence.

## **1.2 Distributions & Random Variables**

- **Random Variable (RV)**: A variable that takes on values according to outcomes of a random process (e.g., \(X =\) “result of a die roll”).
- **Probability Mass Function (PMF)**: For discrete RVs (e.g., \(\mathbb{P}(X = x)\)).
- **Probability Density Function (PDF)**: For continuous RVs (e.g., the area under the curve from \(x\) to \(x + dx\) gives probability).
- **Cumulative Distribution Function (CDF)**: \(\mathbb{P}(X \leq x)\).

## **1.3 Sampling**

- **Population vs. Sample**: Population is the entire group of interest; sample is a subset actually observed.
- **Sampling Methods**:
  - **Simple Random Sampling (SRS)**: every subset of the population has an equal chance of being chosen.
  - **Stratified Sampling**: dividing the population into subgroups (strata) and sampling from each.
  - **Cluster Sampling**: randomly selecting clusters and sampling *within* them.
- **Sampling Error**: The difference between the sample statistic (e.g., \(\bar{X}\)) and the true population parameter (e.g., \(\mu\)).

## **1.4 Example Use Cases**

- Estimating the average height of an entire population by measuring a subset (sample).
- Using coin flips (Bernoulli trials) to illustrate probability fundamentals and the law of large numbers.

---

# **2) Central Limit Theorem & Distribution Behavior**

## **2.1 Central Limit Theorem (CLT)**

- **Statement**: If you take many independent random samples of size \(n\) from *any* distribution with mean \(\mu\) and finite variance \(\sigma^2\), the distribution of the sample means (\(\bar{X}\)) tends toward a **Normal** distribution as \(n\) grows large:

  $$
  \bar{X} \approx N\Bigl(\mu,\frac{\sigma^2}{n}\Bigr)
  $$

- **Why Important**:
  - Justifies using z-tests and t-tests (normal-based methods) with sufficiently large \(n\).
  - The standard deviation of the sample-mean distribution is \(\frac{\sigma}{\sqrt{n}}\) (the standard error).

## **2.2 Distribution Shapes**

- **Normal (Gaussian)**: Bell-shaped, symmetric.
- **Skewed**: Long tail to one side (right skew = tail on the right).
- **Kurtosis**: “Peakedness” of a distribution (heavy vs. light tails).

## **2.3 Law of Large Numbers (LLN)**

- As the sample size grows, \(\bar{X}\) converges to the true mean \(\mu\).
- Different from CLT, but complementary: LLN is about **convergence** of the mean, while CLT is about **distribution shape**.

## **2.4 Example Use Cases**

- Rolling a die many times: the average outcome approaches 3.5 (LLN), and the distribution of sample averages approaches normal (CLT).
- Sampling from a skewed income distribution: the *sample means* still form an approximately normal distribution for large \(n\).

---

# **3) Hypothesis Testing (T-tests, p-values, Effect Sizes)**

## **3.1 Hypothesis Testing Basics**

- **Null Hypothesis (\(H_0\))**: Typically states “no effect,” “no difference,” or “status quo.”
- **Alternative Hypothesis (\(H_1\) or \(H_a\))**: Suggests a difference, effect, or change.
- **Test Statistic**: A standardized value (e.g., t-statistic, z-statistic) that measures how far your sample statistic is from the null’s expectation.
- **p-value**: Probability (under \(H_0\)) of observing a test statistic as extreme or more extreme than your observed one.
- **Significance Level (\(\alpha\))**: Often set to 0.05. If \(p < \alpha\), we *reject* \(H_0\).

## **3.2 T-Tests**

- **One-Sample T-Test**: Compare a sample mean to a known or hypothesized population mean.
- **Two-Sample T-Test**: Compare means of two independent groups (e.g., treatment vs. control).
  - **Equal Variances** (Student’s t-test) vs. **Unequal Variances** (Welch’s t-test).
- **Paired T-Test**: Compare means of *paired* data (before/after measures on the same subjects).

## **3.3 Effect Sizes**

- **Cohen’s d**: Difference between two means (in standard deviation units):

  $$
  d = \frac{\bar{X}_1 - \bar{X}_2}{s_\text{pooled}}
  $$

- **Pearson’s r**: Correlation coefficient (for linear associations).
- **\(R^2\)**: Proportion of variance explained (used in regression, ANOVA context).
- **Practical vs. Statistical Significance**: A very small effect can be significant with large \(n\). Effect size helps judge *practical* importance.

## **3.4 Example Use Cases**

- Checking if a new teaching method (Group A) leads to higher test scores than the traditional method (Group B).
- Comparing average blood pressure in a population to a known threshold (e.g., 120 mmHg) with a one-sample test.

---

# **4) ANOVA / Post-Hoc / Multiple Testing**

## **4.1 ANOVA (Analysis of Variance)**

- **Purpose**: Compare the *means* of 3 or more groups.
- **One-Way ANOVA**: One categorical factor with multiple levels (e.g., 3 teaching methods).
- **F-Statistic**: Ratio of *between-group variance* to *within-group (error) variance*:

  $$
  F = \frac{\text{MS}_{\text{Between}}}{\text{MS}_{\text{Within}}}
  $$

- If \(F\) is large → the group means differ more than expected by random chance.

## **4.2 Post-Hoc Tests & Multiple Comparisons**

- **Post-Hoc Tests**: Used *after* finding a significant overall ANOVA, to pinpoint *which* groups differ.
  - E.g., **Tukey’s HSD**, **Bonferroni**, **Scheffé**, etc.
- **Multiple Testing Problem**: The more tests you do, the higher the chance of a **Type I error** (false positive).
  - Solutions: **Bonferroni correction** (divide \(\alpha\) by the number of tests), **Holm**, **FDR** (False Discovery Rate) control, etc.

## **4.3 Example Use Cases**

- Comparing mean exam scores across 4 different study techniques.
- Pharmaceutical tests of multiple dosages vs. control.

---

# **All-in-One Python Code Block**

```python
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from scipy.stats import ttest_ind, f_oneway
import statsmodels.stats.multicomp as mc

# -------------------------------------------
# 1) BASIC PROBABILITY & SAMPLING (Coin Flips)
# -------------------------------------------
np.random.seed(42)
num_flips = 100
p_head = 0.3  # Probability of heads
flips = np.random.choice(['H','T'], size=num_flips, p=[p_head, 1 - p_head])

num_heads = (flips == 'H').sum()
estimated_p = num_heads / num_flips

print("1) BASIC PROBABILITY & SAMPLING")
print(f"Out of {num_flips} flips, we got {num_heads} heads.")
print(f"Empirical Probability of Heads: {estimated_p:.3f} (true p={p_head})\n")

# -------------------------------------------
# 2) CENTRAL LIMIT THEOREM
# -------------------------------------------
# We'll create a skewed population (exponential)
pop_size = 50000
population = np.random.exponential(scale=5.0, size=pop_size)

num_samples = 1000
sample_size = 50
sample_means = []

for _ in range(num_samples):
    sample = np.random.choice(population, sample_size, replace=False)
    sample_means.append(sample.mean())

fig_clt = px.histogram(sample_means, nbins=40, title="CLT Demonstration: Distribution of Sample Means")
pop_mean = np.mean(population)
fig_clt.add_vline(x=pop_mean, line_width=3, line_dash="dash", line_color="red")
fig_clt.update_layout(xaxis_title="Sample Mean", yaxis_title="Count", showlegend=False)

# -------------------------------------------
# 3) HYPOTHESIS TESTING (Two-sample t-test)
# -------------------------------------------
# Simulate two groups with different means
np.random.seed(123)
groupA = np.random.normal(loc=50, scale=5, size=100)  # mean ~50
groupB = np.random.normal(loc=52, scale=5, size=100)  # mean ~52

# Perform two-sample t-test
t_stat, p_val = ttest_ind(groupA, groupB, equal_var=True)

print("3) HYPOTHESIS TESTING (T-TEST)")
print(f"Group A mean: {groupA.mean():.2f}, Group B mean: {groupB.mean():.2f}")
print(f"T-statistic: {t_stat:.3f}, p-value: {p_val:.3f}")
if p_val < 0.05:
    print("Result: We reject the null hypothesis (means likely differ).")
else:
    print("Result: We fail to reject the null hypothesis (means not significantly different).")
print()

# -------------------------------------------
# 4) ANOVA & POST-HOC
# -------------------------------------------
# Simulate 3 groups with different means
np.random.seed(999)
group1 = np.random.normal(loc=60, scale=5, size=50)  # mean ~60
group2 = np.random.normal(loc=65, scale=5, size=50)  # mean ~65
group3 = np.random.normal(loc=70, scale=5, size=50)  # mean ~70

# One-way ANOVA
f_stat, p_val_anova = f_oneway(group1, group2, group3)

print("4) ANOVA & POST-HOC")
print(f"Group1 mean: {group1.mean():.2f}, Group2 mean: {group2.mean():.2f}, Group3 mean: {group3.mean():.2f}")
print(f"F-statistic: {f_stat:.3f}, p-value: {p_val_anova:.3f}")

if p_val_anova < 0.05:
    print("ANOVA result: At least one group differs significantly.")
    # Post-hoc: Tukey's HSD (using statsmodels' MultiComparison)
    data_all = np.concatenate([group1, group2, group3])
    labels_all = (["Group1"]*len(group1) + ["Group2"]*len(group2) + ["Group3"]*len(group3))

    comp = mc.MultiComparison(data_all, labels_all)
    tukey_result = comp.tukeyhsd()
    print("\nPost-hoc (Tukey HSD) results:")
    print(tukey_result)
else:
    print("ANOVA result: No significant difference among the groups.")

# Show the CLT figure from above
fig_clt.show()
````

### **Explanation of Key Steps**

1. **Coin Flips**: We simulate a series of Bernoulli trials (H vs. T) to show basic probability and estimation of pp.
    
2. **CLT**: We sample from a highly skewed (exponential) distribution multiple times and plot the sample means’ histogram. A red dashed line marks the population mean.
    
3. **Two-Sample T-test**: We create two normally distributed groups with different means, then run a standard t-test.
    
4. **ANOVA & Post-hoc**: We create three groups with clearly different means, run a one-way ANOVA, and if significant, run Tukey’s HSD.
    

---

# **16 Questions (8 Multiple Choice + 8 Open-Ended)**

## **Multiple Choice (8)**

1. **(Q1)** Which of the following is a characteristic of **Simple Random Sampling**?  
    A. Each individual has the same probability of being chosen.  
    B. The population is divided into subgroups, and each subgroup is sampled.  
    C. We only sample individuals who are convenient.  
    D. We intentionally oversample certain demographics for representation.
    
2. **(Q2)** The **Central Limit Theorem** states that, for large nn:  
    A. Any individual measurement will be normally distributed.  
    B. The sample mean distribution approximates normal, regardless of population shape.  
    C. The population becomes normal over time.  
    D. The sample standard deviation always equals the population’s standard deviation.
    
3. **(Q3)** In a **two-sample t-test**, a **p-value < 0.05** typically implies:  
    A. The null hypothesis is definitely true.  
    B. The two group means differ significantly.  
    C. We do not have enough evidence to reject H0H_0.  
    D. No difference in group means.
    
4. **(Q4)** Which of the following is **NOT** an effect size measure?  
    A. Cohen’s d  
    B. Pearson’s r  
    C. p-value  
    D. R2R^2
    
5. **(Q5)** The **F-statistic** in one-way ANOVA is roughly:  
    A. (Within-group variance) / (Between-group variance)  
    B. (Between-group variance) / (Within-group variance)  
    C. The square of the t-statistic  
    D. The standard error of the group means
    
6. **(Q6)** **Multiple Testing** problems arise because:  
    A. Doing several tests inflates the probability of at least one false positive.  
    B. We always expect the same p-value in each test.  
    C. Extra tests automatically reduce sample size.  
    D. There is no way to correct for multiple tests.
    
7. **(Q7)** **Paired t-tests** differ from **two-sample independent t-tests** in that:  
    A. They assume variance is always the same in each group.  
    B. Observations are matched or come from the same subject over two conditions.  
    C. They cannot test for differences in means.  
    D. They ignore within-subject variation.
    
8. **(Q8)** If an ANOVA is **significant**, a **post-hoc test** is used to:  
    A. Decide whether to increase sample size.  
    B. Increase the chance of a Type I error.  
    C. Find out which specific group pairs differ.  
    D. Force all group means to be identical.
    

---

## **Open-Ended (8)**

1. **(Q9)** Explain, in your own words, the main difference between a **population parameter** and a **sample statistic**.
    
2. **(Q10)** Why does the **Central Limit Theorem** make it possible to use normal-based methods (like z-tests) on data that may not be normally distributed?
    
3. **(Q11)** Suppose you run a **two-sample t-test** and get p=0.07p = 0.07. In practical terms, how might you interpret this result?
    
4. **(Q12)** Give an example of how **effect size** can be more informative than the p-value alone.
    
5. **(Q13)** In a **one-way ANOVA** with 4 groups, you get a significant result (p<0.01p < 0.01). What does this tell you, and what additional steps should you consider?
    
6. **(Q14)** Why do we worry about **multiple testing** (familywise error) in the context of ANOVA with many pairwise comparisons?
    
7. **(Q15)** Provide a simple real-world scenario where you’d use a **paired t-test** instead of an independent two-sample t-test.
    
8. **(Q16)** Describe one approach to adjusting for multiple comparisons, and explain how it helps control Type I errors.
    

---