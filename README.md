# Introduction
It's always great when I find a new show that hounds
my attention on Hulu or Netflix or HBO Max or YouTube
or ... (seriously, Paramount+ and Peacock were just
released in the last 6 months.) And it's even better
when I find that I want to tie this new obsession 
to a data science learning objective. So, I've found
a question that I wanted to answer as I was watching
Season 22 of America's Next Top Model (ANTM). Was Mame going 
to win the competition? How would height factor into
a contestant's competitiveness? Match that with my 
want to explore new techniques in data science, and 
we have a great start to a side project! We are going
to use survival analysis and a survival regression to
learn how to handle censored data and perform a 
survival regression.

# Problem Statement
So, given a dataset of ANTM contestants' age, height,
and weeks/rounds lasted in their respective season, 
how long would a contestant last in the next season
of ANTM?

Update 11MAR2021: Target will be a "death" variable 
of whether the contestant made it to the TOP 3
of the season. 

Further update. I'm unsure if this is a right 
censored data problem. I have the results from
each season, for each contestant all the way through
to the end, so there is no right censoring. HOWEVER,
the original question can still stand:
1. Predict if a customer will last to the Top 3.
2. Predict how long a 

# Notes and Starting Thoughts
Note: sex is limited to only female contestants
in the dataset. Season 22 had male contestants 
and certainly future seasons may have male 
contestants, but the sample size across is too
small for me to add that dimension in the current
version of the tool. Secondly, I will need to spend
some time thinking about the assumptions/implications
of building a dataset from a fashion show. That is, 
model preferences for high fashion tend to favor
taller, skinnier models. So, like similar issues
in explainability and societal bias in models, I will
need to spend some time understanding any new features
that I may add to the model.

Further, Season 18 or 19 had contestants coming back
from previous seasons which may have have be a bit
of target leakage. My thought is that since the sample
or competition scenario is different from when they
first competed for the different mix of models in that
season. I'm unsure if this is sound yet, but I can explore
that in my write-up of of the model. 

Also, I should probably switch to Jupyter for this to 
replace the scripts that I was planning to use.

