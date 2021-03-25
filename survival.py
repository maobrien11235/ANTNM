# statsmodels examples of the survival regression techniques.
import statsmodels.api as sm
import statsmodels.formula.api as smf

# Needed to get around SSL: CERTIFICATE_VERIFY_FAILED
# https://alm.rgbk.com/spaces/display/DSP/SSL+error+in+downloading+NLTK+models
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


data = sm.datasets.get_rdataset("flchain", "survival").data
            
data.head()
data.loc[data.death != 1, :].head()
data.loc[data.death == 1, :].head()
df = data.loc[data.sex == "F", :]
mod = sm.SurvfuncRight(df["futime"], df["death"])

mod.summary()

# Plot survival right censored survial analysis with 95% confidence bands
fig = mod.plot()
lcb, ucb = mod.simultaneous_cb()
ax = fig.get_axes()[0]
ax.fill_between(mod.surv_times, lcb, ucb, color='lightgrey')
ax.set_xlim(365, 365 * 10)
ax.set_ylim(0.7, 1)
ax.set_ylabel("Proportion alive")
ax.set_xlabel("Days since enrollment")

# Build survival analysis broken out by gender
gb = data.groupby("sex")
ax = plt.axes()
sexes = []

for g in gb:
    sexes.append(g[0])
    sf = sm.SurvfuncRight(g[1]["futime"], g[1]["death"])
    sf.plot(ax)
    
li = ax.get_lines()
li[1].set_visible(False)
li[3].set_visible(False)
plt.figlegend((li[0], li[2]), sexes, "center right")
plt.ylim(0.6, 1.0)
ax.set_ylabel("Proportion Alive")
ax.set_xlabel("Days since enrollment")

# Compare the survival distributions
stat, pv = sm.duration.survdiff(data.futime, data.death, data.sex)
print(stat)
print(pv)

## Regression Methods
del data['chapter']
data = data.dropna()
data['lam'] = data['lambda']
data['female'] = (data['sex'] == "F").astype(int)
data['year'] = data['sample.yr'] - min(data['sample.yr'])
status = data['death'].values

# Build Cox Proportional Hazard Regression Model (Cox Model)
mod = smf.phreg("futime ~ 0 + age + female + creatinine + "
                "np.sqrt(kappa) + np.sqrt(lam) + year + mgus",
                data, status=status, ties="efron")

result = mod.fit()
print(result.summary())
# Note log HR is the parameter estimate but the HR (Hazard Rate)
# is the most directly applicable. Age's HR of 1.1065 indicates
# a 1 unit (ie 1 year) increase in age increases the hazard by
# 10.65%.

# References for Surival Models
# T Therneau (1996). Extending the Cox model. Technical report.
# http://www.mayo.edu/research/documents/biostat-58pdf/DOC-10027288

# G Rodriguez (2005). Non-parametric estimation in survival models.
# http://data.princeton.edu/pop509/NonParametricSurvival.pdf

# B Gillespie (2006). Checking the assumptions in the Cox proportional
# hazards model.
# http://www.mwsug.org/proceedings/2006/stats/MWSUG-2006-SD08.pdf