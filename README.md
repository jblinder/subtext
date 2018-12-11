# Introduction
In 2013, reporters revealed that cable networks have been speeding up older TV shows and movies to make room for more advertisements. For example, *I Love Lucy* episodes have an average runtime of 30 minutes; in contrast, *The Big Bang Theory* averages at 22 minutes per episode. This model translates to other contemporary platforms as well, such as YouTube and Twitch, where content creators compete for viewers' attention by producing shorter content. Essentially, today's movies and TV shows are conceived of and written with de facto compression, but we don’t often consider how this informs the media content we consume. 

This research led to a few key questions I wanted to explore:
> Is the pace of movie dialogue getting faster over time? 
> Are movies becoming “talkier” in a specific way-- with fewer scenes without dialogue, and shorter pauses? 
> Will future films follow this trend, and what variables can predict this?  

# Datasets

I focused on the top-grossing and top-rated films from the 20th and 21st centuries. I used Scrapy to screen scrape the data from [IMDB](imdb.com). To acquire additional financial information, I also scraped movie financial data from [The Numbers](thenumbers.com) and [Box Office Mojo](boxofficemojo.com). Some of the final fields I relied on were:

- Domestic gross
- Worldwide gross
- MPAA rating
- Runtime
- Release data/ year
- Genre
- Number of critic reviews
- IMDB rating
- Popularity 

Determining the dialogue speed of movies proved a bit trickier task. I relied on a widely adopted file format called SubRip (.srt) to extract this information. SupRip files are used by media players to show a film's corresponding subtitles. Viewers can download them in a variety of languages. The file contains 4 fields for each line of dialogue:

- Number of line
- Start time of line
- End time of line
- Dialogue text

I built a scraper using Scrapy that went through each title on IMDB and performed a search on [Subscene](subscene.com) and [Podnapisi](podnapisi.com) (two SubRip aggregators). If a match was found, the script would download the file (which was zip compressed), unzip the file, put it into a directory, and delete the zip file. I built another script to parse each `.srt` file, merge in the corresponding movie title, and convert it to a `.csv`.

*(Before Conversion)*
```
1
00:02:32,276 --> 00:02:33,902
Rosebud.

2
00:03:12,276 --> 00:03:14,276
News on the March.
```
*(After Conversion)*
```
| id | start_time | end_time | duration | pause | text                | title        | 
|----|------------|----------|----------|-------|---------------------|--------------|
| 1  | 2327       | 2339     | 300      | 2327  | Rosebud.            | Citizen Kane |
| 2  | 3122       | 3142     | 2000     | 783   | News on the march.  | Citizen Kane |
 ```
 
I calculated the line duration by subtracting each end time from the start time. The pause was calculated by subtracting each line's start time from the previous line's end time. Overall, I scraped roughly 2000 films and subtitles.

# Analysis

Initially, I wanted to look at a few individual films to see what the dialogue pacing looked like throughout. I decided to use Alfred Hitchcock's *Vertigo* (1958) as a test case. I immediately saw that there was a 15-minute section in the movie that had no dialogue and thought my code might be broken. However, I checked/ watched part of the film and realized that this long, silent scene was indeed in the film. I compared this film to a few other popular films from different decades and genres and noticed that the dialogue pacing does seem to shift quite dramatically depending on the year and genre. *(Here, the x-axis represents each minute of the film and the y -xis is the average dialogue length per minute.)*  

![vertigo](https://jblinder.github.io/images/project02/vertigo.png.png) Vertigo (1958)
![thegodfather](https://jblinder.github.io/images/project02/thegodfather.png) The Godfather (1974)
![Gaurdians](https://jblinder.github.io/images/project02/Gaurdians.png) Gaurdians of the Galaxy (2014)
![americansinper](https://jblinder.github.io/images/project02/americansniper.png) American Sniper (2014)

For instance, *The Godfather* has fairly long lines of dialogue and a good amount of pauses, which makes sense given the film's dramatic pacing. In comparison, *Guardians of the Galaxy* has almost half the length of dialogue in many scenes and very short gaps between dialogue, which is what we would expect from an action film.

I also wanted to see how the pacing of movies has changed over the course of multiple years. For this, I grouped movies by year and calculated the median number length of line dialogue for each year. I graphed this between 1930-2017.
![years](https://jblinder.github.io/images/project02/median.png)

I found this very promising since it showed an overall downward trend-- It was also intriguing that the pacing fell sharply in 2008. 

The next step was to see if there were any strong correlations in the fields I was analyzing. I ran a correlation table on my data (here, shown as a heatmap using the Seaborn graphing library).

![heatmap](https://jblinder.github.io/images/project02/heat-map.png)

There was a very strong relationship between the line duration and the number of IMDB critic reviews and the year a film was released. I noted this as I continued onto my next step of creating a model.

# Modeling

I used used statsmodels and patsy to create my first model. I plugged in all of my data fields, which included numericals like financial data and categoricals like genre and MPAA rating. I ran a summary to see if there were any coefficients that appeared to have stronger relationships to line duration than others. Year clearly had the lowest p-value and still stood as out as a potentially strong indicator of line duration.

![coef](https://jblinder.github.io/images/project02/coef.png)

I also wanted to see what my residuals looked like to see if there was any heteroskedasticity, and if perhaps I was missing some key variables. It appeared that the residuals were fairly randomly dispersed, and have a fairly even distribution above and below the 0 axis.

![resid](https://jblinder.github.io/images/project02/resid.png)

The plotted best fit lines showed a downward trend in the data. However, I didn't take too much stock in the model's predictive power just yet, as the r-squared was `.22`.

![fit](https://jblinder.github.io/images/project02/fit.png)

I then wanted to see if there were key features I should keep in that could improve my model. I used LASSO to see which coefficents are stronger predictors in my model. This revealed that year and number of IMDB critic reviews were strongly correlated with line duration. Also, Comedy appeared to have faster line dialogue, whereas Fantasy, Musical, and Mystery had slower dialogue. This seemed consistent with my conjectures. When I tried to optimize my coefficient using LASSO, I received an r-squared of `.19`.


![fit](https://jblinder.github.io/images/project02/lasso.png)

# Conclusion

Overall, the data suggests that dialogue pacing is becoming faster over time. Year appeared to be the strongest predictor for predicting dialogue pace, followed by the number of IMDB critic reviews and American films. In terms of genres, comedies, family, and animated films appeared to be related to faster dialogue. Mystery, fantasy, drama, and musicals corresponded to longer dialogue.

In the future, I'd like to explore creating a unique index for dialogue pacing. This feature was very hard to understand when first viewing the project, so creating a "pace index" might help abstract and communicate it better. I'm also interested in seeing if sentiment analysis might highlight any hidden relationships or trends in the data. 

I would like to collect more data and conduct further analyses to gauge whether the sharp decline in pacing in 2008 remains consistent. If so, it would be interesting to explore supplemental qualitative research, since this was right around the time the iPhone was released and Google acquired Youtube. With sufficient additional data, it would also be interesting to analyze whether the change in slope around 2008 suggests that some sort of "intervention" accurred around then, and whether this model might be better interpreted as a sort of interrupted time series, rather than traditional linear regression.
