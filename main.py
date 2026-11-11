import pathlib
S='''World news for Wednesday, 11 November 2026

At the COP31 climate summit in Antalya, Turkey, UN chief Antonio Guterres warned the world is on a "path to mutually assured destruction" from climate change after a year of climate disasters.

In Abu Dhabi, the second day of the first US-Russia-Ukraine talks since February ended with both sides agreeing in principle to a major prisoner exchange, of up to 1,500 per side. NATO jets scrambled after drones entered Baltic airspace.

On Iran, Rubio said sanctions and a naval blockade make major US combat operations unnecessary, but Tehran denied talks and designated Argentina's navy a terrorist group. The US charged three Iran-backed operatives in European plots. Brent crude hovered near $93.

In Gaza, Israeli strikes killed at least eight Palestinians, incl. a father and his 13-year-old son; a 14-year-old was killed in a West Bank raid. Over 1,600 Palestinians have died since last year's ceasefire. Spain held its first general strike in 14 years over housing; Italy evacuated 300 schools after bomb threats; a US soldier was arrested in Britain over suspected Russia spying.

Markets: October US inflation rose 0.4%, hotter than expected, pushing December Fed-hike odds near certainty - possibly 50 points, officials warned - and two-year Treasury yields rose the most in 19 months. Stocks rebounded on AI optimism after CoreWeave beat forecasts and Anthropic's IPO was eyed at up to $1.5 trillion.

In Washington, House Republicans blocked impeachment of Defense Secretary Hegseth, 211-204. Democrats take the House after last week's midterms; Jim Jordan became the new House GOP leader, and several Democrats said they would not back Chuck Schumer as Senate leader. A judge let Trump's $10 billion BBC defamation suit proceed. Nvidia shares slid as its board investigates CEO Jensen Huang over an affair with a woman linked to Chinese espionage.'''
pathlib.Path("/output/entry.txt").write_text(S,encoding="utf-8")
