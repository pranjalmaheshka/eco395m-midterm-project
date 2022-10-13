<h1 align="center" id="heading"> <span style="color:red"> <em> Publish or perish: </em> <br> What does it take to get tenure in Economics? </span> </h1>
<h3 align="center" id="heading"> 13 October 2022 <br> 
<em> Python, Big Data, and Databases (ECO395m)  </em> <br> <h3>
<h3 align="center" id="heading"> Soo Jee Choi, Shreya Kamble, Pranjal Maheshka, Annie Nguyen, Tarini Sudhakar </h3>
  

 <h3> Introduction </h3> 
 
 This project analyzes the relationship between professor rankings (Assistant Professors, Associate Professors, Professors) and their research publications (measured by the h-index and the citations their papers have received). The goal is to determine a relationship between their current positions (tenure or non-tenure) as professors and research publications and their contribution to the academic discourse. Does the quantity of publications outweigh the quality of publications when considering tenure? Do tenured professors continue to publish high quality papers unencumbered by job security concerns?
  
 <h3> Sources of Data </h3> 
 
 Sources of data include faculty in some of the top 25 graduate Economics departments across the United States. The rankings for the highest ranked departments were obtained from [U.S. News](usnews.com). Only full-time faculty were considered: lecturers, professors of instruction, visiting professors, and professors’ emeriti were excluded. Some of these professors could be teaching and conducting research actively but we have excluded them for simplicity and consistency in our analysis. The final list of universities considered were: 
  
  1. Harvard University
  2. Princeton University
  3. University of Chicago
  4. New York University
  5. Stanford University
  6. Yale University
  7. Northwestern University
  8. Duke University
  9. Columbia University
  10. Brown University
  11. Boston University
  12. University of Wisconsin-Madison
  13. University of Texas at Austin
  
  For each university, the page showing the list of faculty was scraped for information (name of professor and title) (individual links can be found in the code/scrape_pages.py file). Only 13 universities have been considered here but a more comprehensive analysis could be conducted by considering all top 25 universities.
 
  After aggregating university level data for economics professors, the h-index and citation values were scraped by Google Scholar. Each professor’s name was searched, and the correct profile was selected by accounting for the current affiliation (current university where they work). Four values were pulled: the current and since 2017 values for h-indexes and citations. The h-index value is the number of papers (h) published that have been cited the same number (h) of times. A score of 20 is considered good, 40 is great, and 60 is truly exceptional (see [here](https://bitesizebio.com/13614/does-your-h-index-measure-up/)). For professors generally: assistant professors have an h-index of 2-5, associate professors 6-10, and full professors 12-24 (see [here](https://www.aacc.org/cln/articles/2019/september/scientific-impact-and-the-h-index)). One big inherent limitation is that some fields in economics are bigger than others. An applied microeconomics professor might see more discourse around their research on average than an auctions theory professor conducting auctions research. This could be an area for further analysis. 
  
 <h3> Limitations </h3> 
  This analysis would be improved by looking at the number of publications a professor had before 2017 versus publications after 2017. It would also help to know when they were promoted and their contributions to academia at that point (which is to say when they were promoted from associate professor to professor what their h-index value). Unfortunately, we cannot obtain this data directly from Google Scholar. A long-term project could involve periodic scraping of h-indexes and seeing how current assistant and associate professors get promoted and the correlation with their h-index and citations. Another limitation of the project is that we are considering that all Professors are tenured and that none of the Assistant or Associate Professors are tenured. However, there are situations where Associate Professors are tenured, which could be included in a future analysis. 
  
 <h3> Methodology </h3> 
  The data scraped from individual universities included only professors in their respective economics departments. Professor titles vary greatly so a simple string analysis was done to sort the professors into 4 buckets: Assistant Professors, Associate Professors, Professors, and others. Only the first 3 buckets were considered in our final analysis. The names of the professors were used as search criteria in Google Scholar. Their current affiliation was used to determine the correct professor profile. Then the individual profile was scraped for h-index and citation values. The final output was a list of lists in the format [[university, name, title, citations, citations since 2017, h-index, h-index since 2017], … ].  
  
 <h3> Results </h3> 
  Across all universities, the average h-index value is 31 for a Professor, 12 for an Associate Professor, and 7 for an Assistant Professor. The graphs below show the distribution of h-values across universities and professor titles. We can clearly see that tenured professors publish more prolific papers than their junior colleagues. Universities like Harvard University, Columbia University, and University of Chicago see the highest average h-indexes for their professors. These average h-index values are comparable to (and often better than) the 2022 Nobel Prize in Economics which saw three economists with h-indexes 35, 37, and 103 win the prize. UT Austin, Duke University, and Brown University are trailing. Looking at Associate Professors, even at Columbia university their average h-index score of 19.5 is less than the lowest average h-index score of 20.3 for professors at UT Austin. There is a clear distinction between various levels of professors and their contributions to academia. 

Looking at average h-index values across universities, Harvard University leads the pack at an astounding 50 while Duke and UT Austin trail at 18 each. The universities analyzed here have some professors with extremely high h-index values like 233; there are 14 professors with h-index values over 100. Undoubtedly, some professors conduct impressive research. We do not observe any similar values for assistant or associate professors. Assistant Professors are often just starting out their careers, so we see minimum values of 0. The minimum h-index values 
Interestingly enough, the minimum h-index values for a Professor is 4 and for an Associate Professor is 5. Professors see the largest variance in the data, and likely individual university policies play huge roles in determining requirements for promotions. 

  <img src="https://github.com/pranjalmaheshka/eco395m-midterm-project/blob/31405e433e7cfe55ee356cf733ea1d18de3b8ea5/analysis/Avghindex.jpeg" width="700"/>
  <img src="https://github.com/pranjalmaheshka/eco395m-midterm-project/blob/31405e433e7cfe55ee356cf733ea1d18de3b8ea5/analysis/boxplottitle.jpeg" width="700"/>

 <h3> Conclusion </h3> 
  Professors have higher h-index values on average than assistant or associate professors which corresponds to greater contributions to academic discourse. There is a great divide between tenured professors and non-tenured professors. There are lesser discrepancies between Assistant and Associate Professors. We see that the expectation of an h-index for different professors were underestimates. Overall, there is great scope for further analysis including looking at h-index values at the time of promotion, h-index value distributions based on sub-field in economics, and simply looking at a greater sample size of universities and majors. 

 
