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


fig = mod.plot()
lcb, ucb = mod.simultaneous_cb()
ax = fig.get_axes()[0]
ax.fill_between(mod.surv_times, lcb, ucb, color='lightgrey')
ax.set_xlim(365, 365*10)
ax.set_ylim(0.7, 1)
ax.set_ylabel("Proportion alive")
ax.set_xlabel("Days since enrollment")
