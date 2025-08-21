# Project Outline

## Identifying and Defining

### Mindmap:

![Mindmap](/Images/Mindmap.png)

### Hypothesis

#### High level test cricket cycles between batting and bowling dominant eras. 

### Functional requirements

1. Load a large csv file saved from excel
2. Sort and filter the data to only include the necessary columns and rows
3. Output the data in a table
4. Analyse the mean runs per wicket in each year
5. Visualise the data in a matplotlib graph
6. The program should output the graph for the user

### Non-functional requirements

1. Create a simple ui to make access easier, and include instructions on the README document
2. Make the program reliable and transparent

### Use case

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
* Show data (as table)
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
| Balls | int | NN..NN | How many balls were bowled in every match that year | 10121 | Must be a positive whole integer |
| Ave | float64 | N.NN... | How many runs were scored over wickets taken for the entire year | 32.40 | Must be a positive decimal to atleast 2 decimal places |
| RPO | float64 | N.NN... | How many runs were scored over how many balls multiplied by 6 | 2.46 | Must be a positive decimal to atleast 2 decimal places |
| Year | datetime64 | YYYY | What year were these matches played | 1949 | Must be in the format YYYY, must be equal or greater than 1946, equal or less than 2025 |
## Producing and implementing

### Conclusion

#### In conclusion, the average runs per wicket supports the idea of the cyclical pattern of test cricket, between batting friendly and bowling friendly time periods. The data shows that across different eras, the runs per wicket may get higher, only to recede in the next 5-10 years. For instance, the early 1970s have a high average (all above the overall average of ~32), which then fades into a low average in the late 1970s. This also confirms anecdotes about 2000s and 2010s being easy to bat, with a clear 10-15 year period with higher averages. Additionally this validates the notion of the bat and ball struggle in test cricket being like the tide, always ebbing and flowing to each side over and over again.

### Peer verification


#### Feedback I gave to others:


| Person | Plus | Minus | Implication |
|--------|------|-------|-------------|
| Marlon B| Very effective to visualise the sales of individual albums. Uses multiple graphs to show different pieces of data. Interface gives clean and efficient user experience. | No error handling if you do not enter a valid artist, the program quits instead. Artists are not ordered by sales (minor) | The program is very good when you enter knowing exactly what data you hope to get, e.g. wanting to know how much Cold Chisel sold. Visualising with multiple graphs is very helpful to understand scale as well, however the case sensitivity can make it difficult to navigate individual artists if you are not well versed in music. Overall extremely solid work. |
| Maxi F| It is obvious that a lot of effort was put into this project. The program is very in depth, there are multiple options for everything, like viewing datasets. There are also multiple graphs which help to visualise the data. UX is clean and efficient, and error handling seemed to be sound. | The consumer price index graph is a little hard to understand. Also, there is limited filtering. You can look for a specific data point, however you can't filter the graphs. | The program is overall extremely solid. It is well tailored to experienced users with a good grasp of economics terminology. There is a lot of information packed into this program, and the user experience ensures that even if you are not an expert, there is still useful data to be found. It achieves its aim of showing console prices quite well. Great work. |
| Oscar D| Lots of raw information to choose from. Tables are put together well and there are many options. Error handling seems good and there is filtering by keyword. | Minus: Not sure if this is exclusive to my testing, but I couldn't get any graphs to show, it would only say 'error while trying to show graph'. Also the options are buried in multiple inputs which can make it a little clunky, and trying to cancel, in keywords triggers an error. | Implication: The program is good for finding raw information with tables, due to the abundance of different information, Visualisation is mostly good, however some of the graphs are not really useful, e.g. "Do you study in public spaces (scatter graph)", although it is designed to have options for everything. Keyword filtering is well implemented which means that users can find information if they want only a specific thing. |

#### Feedback I received:

| Person | Plus | Minus | Implication |
|--------|------|-------|-------------|
| Marlon B| User interface is smooth and provides a nice, friendly user experience. Graphs are visualised well, and it is easy to view the data for a certain period of time (e.g 1991-2002) | Only uses 1 graph which becomes a bit clunky when the whole time period is seen. | Implication: The program makes it easy to view data on batting-friendly and bowling-friendly periods in cricket, especially in different periods (e.g. whether Mark Waugh played in a bowling or batting-friendly period). Graph for whole dataset does get a bit clunky. Overall a really good effort |
| Maxi F| Easy and simple UI was well-done, making the program navigable. Everything about the visualisations were excellent, communicating data I did not understand in other forms into interesting graphs. Error handling was smart. Special commendations to the year-filtering function, which was inexplicably intriguing. Additionally, the data goes back an entire 75 years. | The UX was somewhat small, especially with my basic understanding of the dataset. While not directly related to the hypothesis, the other stats in the dataset would've been interesting to see visualised. | Overall a fantastic piece of work that allows for a good user experience, with outstanding visualisation functions, which I definitely used somewhat excessively. The data was easy-to-verify, and matches up with the sourced data (though, I don't understand much of it), making for clearly correct and good data, bolstered by a great scale. My only concerns are but minor nitpicks. Clearly a lot of effort was put into this, and it paid off. |
| Oscar D | Plus: Very easy to understand, and can be operated by pretty much anyone. Everything works well without any errors or bugs. When filtering you can't start high and end low, and you have to input a valid number which is great. | A tiny problem I encountered which isn't a bug or error, is that if I type something incorrectly when filtering, I don't get any feedback on what the problem was. Also you can type up to 1946 even though it says from 1950-2025. After some further testing i've found that if you type a letter when filtering it gives an error, which could have been fixed with try except. | Implication: Overall everything works well and is good for getting simple and easy to understand data. Only ui issue was that there was no feedback sometimes. Great that you included a way to show the other interesting facts. Not much else to say but great job :) |


## Evaluation

### System and results in relation to requirements outline:
#### The system and results hits every functional and non functional requirement. For functional requirements, it uses a large csv file from excel, sorts and filters the data correctly, can be used to analyse runs per wicket in each year, and visualises the data in a matplotlib graph, that changes based on the filter. As for non-functional requirements, the ui is sleek and user friendly, and the program is reliable to use. Overall, project satisfies every requirement.

### System in relation to peer feedback:
#### Overall it seems like it could have been improved. Mostly the issues seem to have been small inconsistencies with the UX, from small filtering issues to clunky graphs and lack of information on errors. These could easily have been improved with more reflection, especially with multiple feedback-update cycles. What consistently came back as positive was the simplicity of the ui, and data. With more reflection peer reviews seem to be the best way to find small errors and inconsistencies, although because everyone works on a different timetable and we only have 1 final review we cannot do multiple rounds. This leads to inactionable feedback, which is less helpful. I would love to act on this feedback but it would become invalid if I were to change my code now. So my point is, in the future I think evidence of multiple peer reviews and followups would be a good thing to assess, even though that was not the case this task.

### Project in relation to project management:
#### The project was not managed well overall, many aspects could have gone better. For example, I started with the idea of making the user interface graphical, this took a lot of time and I eventually discarded the progress as I thought it would be too messy. This took up at least a week, and was a huge time waste that should have been avoided with more planning. The lack of time on the current functioning program leaves it feeling barebones, with only one table and dataset. The project was completed in time and hits the requirements, but it could have been much more fleshed out with better time management and planning/foresight. Overall slightly to moderately disappointed in how it turned out, especially upon seeing how well projects from peers have gone, and how in depth they are.

### System in relation to data validity
#### The data is valid, accurate, and timely because it comes from a trusted data source, statsguru, which has accurately recorded test cricket data since the first one in 1877. The dataset has no anomalies, although I had to adjust my range due to the lack of games in the first and second world war. The data is unbiased because statsguru shows factual information that is easily fact checkable. The UX could possible be more accessible with a graphical interface, however that might come at the cost of unforeseen bugs and other problems.   

