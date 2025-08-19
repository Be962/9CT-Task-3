# Project Outline

## Identifying and Defining

### Mindmap:

![Mindmap](/Images/Mindmap.png)

### Purpose

#### Within cricket, there are time periods where it is easier to bat or bowl

### Functional requirements

#### Load a large csv file saved from excel
#### Sort and filter the data to only include the necessary columns
#### Analyse the average runs per wickets in each year
#### Visualise the data in a matplotlib graph

### Non-functional requirements

#### Create a simple ui to make access easier
#### Make the program reliable and transparent

### Use case (unfinished)

#### Actor: User
#### Goal: To access and interact with existing cricket runs per wicket data through the user interface
#### Main flow: 1. User opens the program and is shown a text-based menu /n 2. User selects one of the 

## Researching and Planning

### Chosen issue

#### Different eras in cricket are acknowledged, but there is not exactly hard evidence, only anecdotes from long time fans, e.g the 2010s were easy to bat on, and the 2020s harder. Another factor to be considered is if the batters are relatively better or worse, however that is out of the scope of this project and would require much more analysis.

### Findings (unfinished)



### Data acquisition

#### Sports data is relatively easy to find, I used [statsguru](https://stats.espncricinfo.com/ci/engine/stats/index.html?class=1;filter=advanced;orderby=year;size=150;template=results;type=aggregate;view=year)

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

### Conclusion (unfinished)

#### In conclusion, there is evidence to support eras in test cricket. There are visible peaks and troughs in batting average throughout time, which can be a metric of good and bad batting eras. For example, the early 1970s, (1970-1975) has every year above the overall average 32, marking it an above average batting period.

### Peer verification

### Evaluation

#### System and results in relation to requirements outline:
#### System in relation to peer feedback:
#### Project in relation to project management:
#### System in relation to data validity