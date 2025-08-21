# HIT140 Foundations of Data Science
Group Project Presentation Assignment 2
<br />
Objective 1: Investigation A 
(Bat vs. Rat)


## Group Members
| Name | Student ID | Role/Contribution| GitHub Username|
|-|-|-|-|
|Alice Li |s394431| |@Raini-impression |
|Duong Quy Vu|s388965| |@duogvuu|
|Susmita Aryal|S388252||@Aalia259|
|Jack David Manning|S303126||@s303126|

## Work flow
Data cleaning -> Establish Hypothesis -> Data analysis -> Data Visualization and presentation
##  Project Resources
OneDrive Folder: <br />
GitHub Repo: https://github.com/HIT140-ECP-GRP61/ASSN-2
<br />
Presentation slides: https://docs.google.com/presentation/d/1_5j1Vq2DnjHZGxWZyJWzALwk8GTSu_aSfm_RBrfqkAA/edit?usp=sharing
<br />
A recorded group presentation youtube link: 
<br />
Meeting Minutes (unit code) (group number) date
<br />
Other notes: [screenshots of Teams, github contribution history]


## How We Collaborated

We used:<br />
GitHub for all code (Jupyter Notebooks, or .py files, and that cursed requirements.txt)<br />
PRs & commits show individual contributions <br />
Slides (Google Slides): Linked above, each section labeled by contributor<br />
OneDrive: Sharing documents<br />

## Data analysis
First calculate with 95% CI the mean bat_landing_to_food and bat_landing_number is what<br />
Hypothesis 1: Avoidance divided by risky/avoidant bats
<br />
Variables:<br />
   risk — split into risky/avoidant bats
   <br />
    test: compare bat_landing_to_food (how much they hesitate after landing)
    <br />
Hypotheses :<br />
     H0: Risky bats and avoidant bats take equally long to approach food.<br />
    H1: Risky and avoidant bats take different time to approach food when they land soon after rat arrival ( vigilance).<br />

   Hypothesis 2: Do bats behave different whether rats are present?<br />
Variables:<br />
test:<br />
     whether rats are present on platform when bats start eating<br />
Compare:<br />
    bat_landing_to_food (how much they hesitate after landing)
    <br />
Hypotheses:<br />
    H0: The mean hesitation time is the same whether rats are present or not when the bat approaches the food.<br />
    H1: The mean hesitation time is different whether rats are present or not when the bat approaches the food. <br />

   Hypothesis 3: Do bats wait longer before eating when rats have left the platform?<br />
Variables:<br />
test:<br />
     whether rats are present on platform when bats start eating<br />
Compare:<br />
    bat_landing_to_food (how much they hesitate after landing)
    <br />
Hypotheses:<br />
    H0: bats wait the same before eating when rats have left the platform<br />
    H1: bats wait longer before eating when rats have left the platform <br />

  Hypothesis 4: Does foraging success (reward = 1) differ based on rat presence at feeding time, separately for risky and avoidant bats?<br />
Variables:<br />
divide risky/avoidant bats and test each group reward rate
test:<br />
     whether rats are present on platform when bats start eating<br />
Compare:<br />
    reward rate
    <br />
Hypotheses:<br />
    H0: Rats being around doesn't affect reward rates for risky/avoidant bats.<br />
    H1: Rats being around affect reward rates for risky/avoidant bats. <br />
    
Hypothesis 5: Rat Presence Reduces Bat Traffic<br />
Variables:<br />
test:<br />
     High vs. Low rat_minutes<br />
Compare:<br />
    bat_landing_number<br />
Hypotheses:<br />
    H0: Rats being around doesn't affect how many bats come.<br />
    H1: Bats land less often when rats dominate the platform. <br />


##  Transcript for Slides / PPT
Use this template as your spoken script—edit for your slides!


Slide 1: Title & Group Introduction<br />
Speaker: [Name]<br />




Slide 2: <br />
Speaker: [Name]<br />


Slide 3: <br />
Speaker: [Name]<br />




Slide 4: <br />
Speaker: [Name]<br />




Slide 5: <br />
Speaker: [Name]<br />




Slide 6:<br /> 
Speaker: [Name]<br />




## Appendix
Screenshots:<br />
Google Docs version history <br />
GitHub contribution graph<br />
Full code snippets (see GitHub for latest)<br />
Extra figures or analysis<br />


[End of Template]<br />






