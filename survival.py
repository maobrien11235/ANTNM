# statsmodels examples of the survival regression techniques.
import statsmodels.api as sm

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

