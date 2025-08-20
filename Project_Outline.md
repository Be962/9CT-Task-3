# Project Outline

## Identifying and Defining

### Mindmap:

![Mindmap](/Images/Mindmap.png)

### Hypothesis

#### High level test cricket cycles between batting and bowling dominant eras, 

### Functional requirements

1. Load a large csv file saved from excel
2. Sort and filter the data to only include the necessary columns and rows
3. Analyse the mean runs per wicket in each year
4. Visualise the data in a matplotlib graph
5. The program should output the graph for the user

### Non-functional requirements

1. Create a simple ui to make access easier, and include instructions on the README document
2. Make the program reliable and transparent

### Use case (unfinished)

#### Actor: User
#### Goal: To access and interact with existing cricket runs per wicket data through the user interface
#### Preconditions: 
 * The Dataset.csv, data_module.py, and main.py files have been downloaded
 * The user has access the the user interface
#### Main flow:
1. User opens the program and is shown a text-based menu
2. User selects one of the following options:
* Show data
* Filter data
* Other stats
* Exit
3. System completes the selected action
#### Postconditions:
* User has looked at whole data, and/or filtered the data to look at specific years
* System remains unchanged and reliable

## Researching and Planning

### Research on chosen issue

#### Test cricket has batting and bowling friendly eras, this is mentioned anecdotally by many fans of the game and many articles. Currently it is widely acknowledged to be a bowling friendly era, from articles such as [this article on bowlers reclaiming test cricket](https://www.abc.net.au/news/2024-12-06/cricket-test-bowling-averages-analysis-team-by-team/104664884), and [this article on the difficulties of opening the batting in Australia](https://www.smh.com.au/sport/cricket/why-opening-the-batting-has-become-a-fool-s-errand-in-australia-20241117-p5kr8s.html). However, go back 10 years to 2015, and articles seem the other way around. For example, [this article by a famous fast bowler, Brett Lee](https://www.rediff.com/cricket/interview/cricket-is-becoming-harder-for-bowlers/20151029.htm) which talks about cricket becoming harder for bowlers, and [this article from ESPN](https://www.espncricinfo.com/story/decade-review-why-the-2000s-belonged-to-batsmen-442008) which talks about the 2000s belonging to batsmen. This could be happening for any number of reasons, such as bowling innovations (wobble seam ball), easier and harder pitches, and larger and smaller stadiums/boundaries on the playing field. Overall however these articles seem to point to test cricket having high batting periods and high bowling periods, although nothing on the cyclical nature of them.

### Findings (SEE-I)

#### The balance between batting and bowling in test cricket has repeatedly shifted in a cyclical nature over time. This reflects a wider pattern of innovation and counter innovation that drives the evolution of the changing game. Teams constantly seek new strategies to get the edge over their opponents, in technique, pitches, and rule changes. For example, the 2020s have been dominated by bowling, due to many factors such as the unpredictability of the wobble seam delivery, more bowler friendly pitches that give extra swing, seam, or pace, and rules that incentivise wins, especially at home, rather than settling for draws. The struggle between bat and ball is like the tide, it surges forward, only to recede again time after time.

### Data acquisition

#### Sports data is relatively easy to find, I used [statsguru](https://stats.espncricinfo.com/ci/engine/stats/index.html?class=1;filter=advanced;orderby=year;size=150;template=results;type=aggregate;view=year) to sort results by year, and list various stats such as average (runs per wicket), runs per over, wickets, runs, etc.

### Planning

| Field | Datatype | Format for Display | Description | Example | Validation | 
|-------|----------|--------------------|-------------|---------|-----------|
| Mat | int | NN | How many matches were played | 12 | Must be a positive whole integer |
| Runs | int | NN...NN | How many runs were scored in every match that year | 3456 | Must be a positive whole integer |
| Wkts | int | NNN |  How many wickets were taken in every match that year | 789 | Must be a positive whole integer |
| Ave | float64 | N.NN... | How many runs were scored over wickets taken for the entire year | 32.40 | Must be a positive decimal to atleast 2 decimal places |
| RPO | float64 | N.NN... | How many runs were scored over how many balls multiplied by 6 | 2.46 | Must be a positive decimal to atleast 2 decimal places |
| Year | datetime64 | YYYY | What year were these matches played | 1949 | Must be in the format YYYY, must be equal or greater than 1946, equal or less than 2025 |
## Producing and implementing

### User Interface

###

## Testing and analysis

### Conclusion

#### In conclusion, the average runs per wicket supports the idea of the cyclical pattern of test cricket, between batting friendly and bowling friendly time periods. The data shows that across different eras, the runs per wicket may get higher, only to recede in the next 5-10 years. For instance, the early 1970s have a high average (all above the overall average of ~32), which then fades into a low average in the late 1970s. This also confirms anecdotes about 2000s and 2010s being easy to bat, with a clear 10-15 year period with higher averages. Additionally this validates the notion of the bat and ball struggle in test cricket being like the tide, always ebbing and flowing to each side over and over again.

### Peer verification

### Evaluation

#### System and results in relation to requirements outline: The system and results hits every functional and non functional requirement. For functional requirements, it uses a large csv file from excel, sorts and filters the data correctly, can be used to analyse runs per wicket in each year, and visualises the data in a matplotlib graph, that changes based on the filter. As for non-functional requirements, the ui is sleek and user friendly, and the program is reliable to use. Overall, project satisfies every requirement.

#### System in relation to peer feedback:

#### Project in relation to project management: The project was managed well overall, as there was no point where it felt like I was behind. Some aspects could have gone better though. For example, I started with the idea of making the user interface graphical, this took a lot of time and I eventually discarded the progress as I thought it would be too messy. Despite this, the actual project was completed with lots of time to spare. Overall project was managed well, with room for improvement.

#### System in relation to data validity

#### The data is valid, accurate, and timely because it comes from a trusted data source, statsguru, which has accurately recorded test cricket data since the first one in 1877. The dataset has no anomalies, although I had to adjust my range due to the lack of games in the first and second world war.
#### The data is unbiased because statsguru shows factual information that is easily fact checkable.
#### The UX could possible be more accessible with a graphical interface, however that might come at the cost of unforeseen bugs and other problems.