# HeatX
Team HeatX's solution for the NASA SpaceApps Challenge 2021

## HIGH-LEVEL PROJECT SUMMARY
We developed a web-application that allows users to stay updated with nearby fire-alerts, raise the alarm themselves and find the closest help-line numbers in case of a crisis. They can also calculate the risk of finding themselves in the midst of a forest fire by using the latest climate and vegetation data. Heat maps of nearby areas are also clearly displayed in straight-forward and intuitive maps. Yet, the real deal-breaker of our application is its focus on community-based mitigation measures. After reading our assortment of thoroughly researched articles, users can write and read stories on their experience with forest-fires to motivate the community.


## DETAILED PROJECT DESCRIPTION
A number of 37,059 fires were detected in year 2018 using MODIS (Moderate Resolution Imaging Spectro-radiometer) sensor data. Every year large areas of forests are affected by fires of varying intensity and extent. They pose a threat not only to the forest wealth but also to the entire regime to fauna and flora seriously disturbing the bio-diversity and the ecology and environment of a region. What is really scary is the lack of awareness amongst the mass regarding this grave threat.

## LINK TO PROJECT "DEMO"
https://docs.google.com/presentation/d/1LQcUddhv6tqu9ID82RUkGg_dP_FfhkCZ/edit?usp=sharing&amp;ouid=102643226881637686854&amp;rtpof=true&amp;sd=true

## FEATURES:


In order to address this issue, we decided to build a website with multiple features and tools such as letting people know if they are in the vicinity of an upcoming forest fire via the models we built to predict forest fires or via a quick form that fellow user can fill in order to alert others in real time.

The website has a SOS where users can obtain emergency contacts relevant to them by just typing in the name of the city in the search box. Our website is also equipped with authorized information and resources on everything that people need to know about forest fires (science behind them, cause, impacts, precaution, methods of prevention, etc.). We have also dedicated a portion of our website to "Camping Corner", which provides a safe space for people who want to share their wisdom, advice, trauma, etc. related to the topic at hand. Our website consists of mapping tools such as The Drought Monitor, Transboundary Ecoregions, Transboundary River Basins and Global Drought Data. Later on we shall work on a feature through which people will be able to donate to victims of forest fires, especially the tribal communities, who are often affected the most in these adverse situations.

We have provided a feature where the user can simply enter their location as latitude and longitude coordinates, this is then sent to the MODIS API to get LST, NDVI and Thermal Anomaly data, and then using the model we predict the risk factor for a forest fire around them, we show them a green indicator if the risk is less than 33 percent, yellow if greater than 33 but less than 67 percent, and red if more than that. The model provides a 78.65% accuracy.



## AIMS AND BENEFITS:


Through this project we hope to educate people about forest fires and the adverse effects of climate change. We plan to aid people in decreasing forest fires in their vicinities. We aim to alert people who happen to live in the particular area where the forest fire is happening so that they can take immediate action. We hope to restore people's faith in humanity and mother nature's gifts once the victims see that they are not alone in the struggle.



### CODING LANGUAGES:


- Python 3, Pandas and Related Libraries for ML model
- Node.js - Backend framework of website
- Authorized APIs
- CSS with Bootstrap v5.1.1
- HTML

### Space Agency Data used:
- NASA's MODIS data for calculating and training our model with parameters :
- NDVI,
- LST,
- Temperature_Anomaly
- NASA's data for the heat maps, and to map out risk of nearby areas

## HACKATHON JOURNEY

### Our Experience

#### HUMBLE BEGINNINGS:

We’d formed our complete team around the beginning of September. At this stage, we didn’t have the slightest idea of what we were going to do. Our team lead, Srishti, was the one who roped in all of us folks and made us aware that such a challenge existed.

At first glance, the challenges seemed pretty formidable, requiring us to dig through hours of research papers, make working websites/apps, all within the span of 2 days! Our team specifically was more technologically oriented and wanted to take up some of the more challenging problems provided. We pretty much narrowed our choice of challenges to three, them being “Mapping Space Trash in Real-Time”, “Unlocking the Secrets of the Sun” and “Warning: Things are Heating Up!”. After assessing the areas of expertise in our team more closely, we concluded that we were best fit to solve the latter.

We started brainstorming ideas about what exactly we wanted to do to solve this problem of increasing heatwaves and forest fires. Some of the ideas that got bounced around at this stage were: to make a website that can help users get fast and easy access to SOS information, the ability to alert people in the locality in case a heat extremity is encountered, a machine learning model that can help users predict whether there will be a forest fire in the vicinity, a community blog post that can help people who have experienced heatwaves and forest fires first hand to come together and share their personal experiences and advice that will prove to be an invaluable resource to the general public, and a charity page that allows people to pledge money to various authorized charity funds and alerts that can help people now about any upcoming threats in their areas.

With a plethora of ideas in our bank, we were more than inspired to get cracking!

#### THE TIME HAS COME:

Now, the inaugural ceremony had just ended, and we were all gearing up to get started on our long, arduous journey.

The first order of action was to collect resources and data that could help us train the machine learning model that we were going to deploy. Easier said than done. We checked out the resources given on the resource page of the challenge website, but unfortunately, we were unable to get any datasets that were appropriate for our use case. We were still unsure of which parameters to use for the model we were supposed to train to detect forest fires. After extensive research, we finally came to the conclusion that the NDVI (Normalized Difference Vegetation Index), LST (Land Surface Temperature), and Thermal Anomaly are the key properties to be taken care of while making such a predictive model. Eventually, we found a dataset from a source and trained our Logistic Regression model using the values given. For additional functionality, we have provided a feature where the user can simply enter their location as latitude and longitude coordinates, this is then sent to the MODIS API to get LST, NDVI and Thermal Anomaly data, and then using the model we predict the risk factor for a forest fire around them, we show them a green indicator if the risk is less than 33 percent, yellow if greater than 33 but less than 67 percent, and red if more than that.

We also had the idea of providing users with a heat map of their location that’ll help show them where the local hotspots lie.

This project's other main parallel focus was the user experience and the website features that we provide to help people find ways to mitigate and prevent potential damage caused by forest fires or heat waves. Implementing all these features definitely was not the simplest of tasks. We mainly focused on making the user interface simple and intuitive to use, which is vital during distressing times. The Alert feature hooks up to the local authorities, thus notifying them of danger occurring at a specific place. The community blogpost feature aims to bridge the information gap between people about these concepts by sharing the powerful stories of victims of such heat-related extremities. We need to get users the help they need in case they’re stuck in a dire situation. Thus we’ve implemented the SOS button, which will provide them with details of their local emergency contact such as firefighters or medical professionals.

## CONCLUSION:


All in all, this hackathon was a great way to foster team spirit and the critical thinking required to solve such pressing issues that are actually affecting the world we live in right now. We all got exposed to an assortment of things that we were unfamiliar with, a lot of struggles, and last but not least, we learned a lot about what it really means to make solutions that are part of a concurrent and focused effort to improve the quality of life of others.

## REFERENCES
- Data to train the Risk Factors model: oulad SAYAD, YOUNES; Mousannif, Hajar; Al Moatassime, Hassan (2019), “Data for: Predictive Modeling of Forest Fires: A New Dataset and Machine Learning Approach”, Mendeley Data, V1, doi: 10.17632/85t28npyv7.1
- Understanding the factors affecting the Wild-fire risk: e:WF02061 (fs.fed.us),
- A global wildfire dataset for the analysis of fire regimes and fire behaviour (nature.com)
- 75Report.pdf (ucsd.edu)


## Blog and Resources:

- https://www.anthropocenemagazine.org/2020/09/humans-cause-most-wildfires-that-threaten-homes-in-the-united-states/,
- https://www.directenergy.com/learning-center/heatwave
- https://www.fisheries.noaa.gov/feature-story/ocean-heatwaves-dramatically-shift-habitats
- https://www.epa.gov/heatislands/heat-island-impacts
- https://ygrene.com/blog/property-improvements/how-heat-proof-your-house
- https://www.globalforestwatch.org/blog/fires/placing-global-wildfires-into-local-context/
- https://www.doi.gov/wildlandfire/prescription-safety-burning-wildland-urban-interface
- https://yaleclimateconnections.org/2019/06/heat-waves-and-climate-change-is-there-a-connection/
- https://www.isglobal.org/en/healthisglobal/-/custom-blog-portlet/-como-afectan-las-olas-de-calor-a-nuestra-salud-/5734329/0
- https://www.carbonbrief.org/guest-post-why-africas-heatwaves-are-a-forgotten-impact-of-climate-change
- https://www.climate.gov/news-features/event-tracker/record-breaking-june-2021-heatwave-impacts-us-west
- https://www.ndtv.com/blog/blog-my-firsthand-experience-of-canadas-monster-heat-wave-2476793
- https://cliffmass.blogspot.com/2021/06/the-reason-for-extreme-warmth-on-monday.html
- https://www.weather.gov/safety/heat-survivors
- https://www.cnn.com/2018/11/13/us/california-wildfires-woolsey-camp-hill-testimonies/index.html
- https://www.kibin.com/essay-examples/a-personal-recount-of-a-forest-fire-D9TAaAH3
