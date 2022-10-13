<h1 align="center" id="heading"> <span style="color:red"> <em> Publish or perish: </em> <br> What does it take to get tenure in Economics? </span> </h1>
<h3 align="center" id="heading"> 13 October 2022 <br> 
<em> Python, Big Data, and Databases (EC0395m)  </em> <br> <h3>
<h3 align="center" id="heading"> Soo Jee Choi, Shreya Kamble, Pranjal Maheshka, Annie Nguyen, Tarini Sudhakar </h3>
  

  
Introduction
This project analyzes the relationship between professor rankings (assistant professors, associate professors, professors) and their research publications (measured by the h-index and the citations their papers have received). The goal is to determine a relationship between their current positions (tenure or non-tenure) as professors and research publications and their contribution to the academic discourse. Does the quantity of publications outweight the quaklity of publications when considering tenure. Do tenured professors continue to publish high quality papers unencumbered by job security concerns?
  
Sources of data include faculty in some of the top 25 graduate Economics departments across the United States. The rankings for the highest ranked departments were obtained from usnews.com. Only full-time faculty were considered: lecturers, professors of instruction, visiting professors, and professors emeriti were excluded. Some of these professors could be teaching and conduting research actively but we have excluded them for simplicity and consistency in our analysis. The final list of universities considered were: Harvard University, Princeton University, University of Chicago, New York University, Stanford University, The Pennsylvania State University (Penn State), Yale University, Northwestern University, Duke University, Columbia University, Brown University, Boston University, University of Wisonsin-Madison, University of Texas at Austin. For each unversity the page showing the list of faculty was scraped for information (name of professor and title) (individual links can be foound the in the code/scrape_pages.py file). Only 12 universities have been considered here but a more comprerensive analysis could be conducted by considering all top 25 universities.
 
After determining aggregating university level data for economics professors, the h-index and citation values were scraped by Google Scholar. Each professors name was searched and the correct profile was selected by accounting for the current affiliation (current university where they work). Four values were pulled: the current and 2017 values for h-indexes and citations. 
  
  1. Introduction: what we studying? why are we studying it? 
     1. Academia focuses on research: but to what degree does quantity of publications weigh more than quality? 
     2. Tenure is the grand goal: security + freedom to conduct own research as they see fit. What stands in their way? 
     3. We see how economics professors at top universities in the US fare in this regard: what is their h-index score? How many of them have gotten tenure?
  2. Methodology: what did we do? how did we do it? 
     1. Put together a list of colleges
     2. Scraped webpages for names and job titles 
     3. Scraped google scholar for h-index and citation scores 
     4. Combined the two lists for further analysis 
     5. From the instructions: Source(s) of dataset(s) must be clearly documented//Data collection methods must be understood and clearly documented. You should read and summarize the documentation of the data, make sure that you understand and document all columns/features that are relevant to your analysis. You should understand and summarize what isn’t in the data too.//Limitations of the data must be clearly outlined
  3. What do we find? 
     1. Average number/range of faculty members in each econ department
     2. How many Professors and Associate Professors on average in each Econ department? 
     3. h-index score: what is the lowest, what is the highest
     4. Number of citations: what is the lowest, what is the highest
     5. Which university seems to be faring better? 
     6. Scope for further analyis: gender, waterfall of citations (route of one paper citing another paper)
     7. From the instructions: A discussion of extensions of data that would be required to improve the analysis should be included


Notes from the instructions: 
The goal of the analysis is must be clearly articulated
The report must include your methodology
The report must include a description of your project and its findings (or lack of findings)
Your findings (or non-findings) must be clearly documented
The limitations of the analysis must be clearly outlined
Extensions of your analysis or areas for more research must be included in your report
You should not include analysis, plots, discoveries, that aren’t directly related to your findings – you can put them as an appendix in another file if you like
