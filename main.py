import pathlib
S = """World in brief — Wednesday, 11 November 2026

1. Iran: Trump called the war "militarily over," but Tehran keeps Hormuz shut and threatened US bases; two tankers burned after mine strikes; Brent closed +2.4% at $93.69.
2. Ukraine: day two of the first US-Russia-Ukraine talks in nine months in Abu Dhabi; Russia and Kyiv agreed a prisoner swap, no breakthrough (Reuters); Witkoff and Kushner to meet Putin and Zelenskyy separately.
3. US: House voted 211-204 to kill impeachment charges against Defense Secretary Hegseth; Fed's Goolsbee called October CPI (0.4%) "borderline disturbing," a December hike near-certain (Bloomberg); Trump tapped Palantir CISO LoSapio to lead CISA.
4. Markets: European shares hit a record close (Stoxx 600 +0.7% to 663.05, DAX +1.2%) on Siemens Energy (+10.8%) and CoreWeave (+26%, Q3 revenue +168%); Nasdaq rebounded +2.0%; German CPI eased to 2.8%; Nvidia fell over the Huang chip scandal ($7.5bn via Singapore).
5. Gaza/Lebanon: Israeli strikes killed more Palestinians, incl. two brothers in Gaza City; toll since the Oct 2025 ceasefire past 1,600; UN: 1M+ in Lebanon face acute food shortages.
6. Yemen: Saudi Arabia intercepted three Houthi missiles over Riyadh; Houthis claimed hits on the airport, an oil pipeline and a financial district.
7. Europe: Storm Charles shut 8,000 Portuguese schools, cancelled 300+ flights; hoax bomb emails hit 300+ Italian schools and schools in Scotland, N. Ireland, Ireland; fog pile-ups killed 11 in Bulgaria; Spain's first general strike in 14 years.
8. Climate: COP31 opened in Antalya; the EU is weighing a major Syria ties upgrade ahead of Nov 16.
9. Security: an object from Belarus closed Vilnius airport amid NATO scrambles; an RSF commander defected in Sudan; 3 killed at a Tata iPhone plant in India; Russia's US ambassador died aged 66.
10. Health/tech: Ebola in Congo hit 10,668; the EU's Digital Fairness Act curbs loot boxes; Scott Wiener, author of California's vetoed AI bill SB 1047, won Pelosi's House seat.
"""
pathlib.Path("/output/entry.txt").write_text(S, encoding="utf-8")
# Deterministic: no network, no clock, no randomness. v4 brief, final entry candidate.
