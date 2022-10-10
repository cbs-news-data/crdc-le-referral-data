# {{ market_name }} Handcuffs in Hallways Data Report

_[Questions? Check the FAQ](#frequently-asked-questions-about-this-data)_

## Data summary

Use these summary lines as a starting point for your local package. 

*NOTE: all data below is from the 2017-2018 Civil Rights Data Collection publication, unless otherwise specified.*

*NOTE: all tracks referencing this data must attribute it to CBS News' analysis of CRDC data. See [the "Attribution" section](#attribution) for details*

### National data

> Hundreds of young children are arrested every year in US elementary schools. 

> As many as {{ _1718_national_total_arrests | round(-2) |int }} ({{ _1718_national_total_arrests |int }}) kids were arrested at US elementary schools in a single year. 

> US elementary schools called police on kids {{ _1718_national_total_referrals | round(-3) |int }} ({{ _1718_national_total_referrals |int }}) times in a single year. 

> When an elementary school calls the police on a student, it's rare for that student to actually be arrested. Only about one out of every {{ _1718_pct_arrested_1_in_x |int }} of so-called law enforcement "referrals" end with a documented arrest. But that still means that hundreds of the youngest schoolchildren are arrested at school every year. 

> Black children and children with disabilities are more likely to be arrested at school than their white and non-disabled peers.

> Black elementary school students are {{ _1718_arrest_rate_black_vs_white |int }} times as likely to be arrested in school than their white peers. 

> Elementary school students with disabilities are {{ _1718_arrest_rate_idea_vs_nondis |int }} times as likely to be arrested in school than their peers without disabilities. 

### {{ state }} data

> {{ state }} elementary schools called the police on kids {{ _1718_state_total_referrals |int }} times in a single year. {{ _1718_state_total_arrests |int }} of those kids were arrested. 

> Of those arrested, {{ _1718_state_total_arrests_white |int }} were white, {{ _1718_state_total_arrests_black |int }} were black, and {{ _1718_state_total_arrests_hispanic |int }} were hispanic. 

> Of those arrested, {{ _1718_state_total_arrests_idea |int }} had disabilities, and {{ _1718_state_total_arrests_nondis |int }} didn't have disabilities. 

> Of those who had the police called on them, {{ _1718_state_total_referrals_white |int }} were white, {{ _1718_state_total_referrals_black |int }} were black, and {{ _1718_state_total_referrals_hispanic |int }} were hispanic.

> Of those who had police called on them, {{ _1718_state_total_referrals_idea |int }} had disabilities, and {{ _1718_state_total_referrals_nondis |int }} didn't have disabilities. 

## Attribution

All references to this data analysis must be attributed to CBS News' analysis of this data. 

### On first reference

Attribution must inlude the words "CBS News' analysis" and  "US Department of Education data", for example "According to an analysis of US Department of Education data by CBS News."

### On subsequent reference

After first reference, you can simply refer to "CBS News' analysis", "the CBS data analysis", or simply "our analysis." 

## Frequently-asked questions about this data

### Where does this data come from? 

The data used in this analysis is from the 2017-2018 Civil Rights Data Collection by the United States Department of Education's Office for Civil Rights. It's a survey of every school in the country conducted every two years, and contains data on everything from enrollment numbers to graducation rates to test scores to disciplinary data. The survey is the primary way the federal government studies schools' performance and is a critical component of its efforts to ensure federal dollars don't contribute to discrimination on the basis of race, sex, and disability. 

### Why is this data so old? 

The 2017-2018 survey is the most recent data available. We're told by the Department of Education that the new data won't be released until 2023.

### What does "X" mean? 

Here are definitions of most of the terms used in this analysis: 
1. **Referral to law enforcement**: "...an action by which a student is reported to any law enforcement agency or official, including a school police unit, for an incident that occurs on school grounds, during school-related events, or while taking school transportation, regardless of whether official action is taken. Citations, tickets, court referrals, and school-related arrests are considered referrals to law enforcement."
    - To simplify, the Lab is describing this as “calls to law enforcement"
2. **School-Related Arrest**: "...an arrest of a student for any activity conducted on school grounds, during off-campus school activities (including while taking school transportation), or due to a referral by any school official. All school-related arrests are considered referrals to law enforcement." 
3. **Referral rate**: The number of referrals reported in the school during the 2017-2018 school year divided by the total student enrollment during that year. 
4. **Arrest rate**: The number of arrests reported in the school during the 2017-2018 school year divided by the total student enrollment during that year. 

### How do I know this data is accurate? 

We undertook a rigorous data cleaning and verification process prior to this analysis, which included us contacting individual school districts and state education departments to verify their data. If we weren't confident about a school's data, we removed that school from the analysis, and took steps to ensure other schools with similar issues were also removed. 

We dropped schools that met any of the following criteria: 
1. Data entry errors
    - We were able to identify a small number of schools that had arrest or referral rates over 100%, which shouldn't be possible according to the CRDC data manual. 
    - We also identified a larger number of schools with more arrests than referrals. This should not be the case, as all arrests are considered referrals but not all referrals are considered arrests. 
    - We dropped a small number of schools with extremely high arrest and referral totals
2. Alternative schools and juvenile justice facilities
3. Schools with fewer than 50 students
4. Online-only schools