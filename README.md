# NBA Metric Visualization Tool

## Purpose

This tool will serve as a way for NBA fans and analysts to visualize specified statistics and advanced metrics for a defined set of NBA players, of which will be able to pull from a database that can be adjusted for the targeted season.

## Table of Contents
1. [**Background**](#background)
2. [**Tech Stack**](#tech-stack)
3. [**Roadmap**](#roadmap)

## Background

The conception of this project came about when deciding what to build with my newfound set of skills acquired after completing freeCodeCamp's - *Foundational C# with Microsoft* - Developer Certification. Initially, I had plans of building some kind of sorting algorithm visualizer to piggyback off of the idea from [Clement Mihailescu](https://youtu.be/pFXYym4Wbkc?si=0TJOIc0Y_7DUY1-z) (aka AlgoExpert), but I became conflicted with this notion of copying someone else's project over creating something original and authentic that would be an expression of me. I consulted online forums that discussed the validity of building 'mundane' projects and the important learning experience you gain from reiterations of non-original works such as a social media clone. However, I also came across those saying that uniqueness most certainly helps people stand out from the crowd, as it shows passion and creativity.

- [How do you find ideas for personal projects...](https://www.reddit.com/r/learnprogramming/comments/kbziax/how_do_you_find_ideas_for_personal_projects_i/)
- [Do side projects have to be unique?](https://www.reddit.com/r/cscareerquestions/comments/74zcob/do_side_projects_have_to_be_unique/)
- [How original does a personal project have to be?](https://www.reddit.com/r/csMajors/comments/mn5g4s/how_original_does_a_personal_project_have_to_be/)

I even consulted Google's AI, [Gemini](https://gemini.google.com/app), to see what it would come up with.

Low and behold, I had a *Eureka!* moment when Gemini suggested that I should settle on a compromise, which meant building on a pre-existing idea but giving it an "original twist!" Instead of simply constructing a vanilla sorting algorithm visualizer like AlgoExpert, I would give it practical application by sorting real-life data that could be swapped out for other data sets connected to a database. This plethora of inspiration which had come about to me after giving it some serious thought and consultation, had finally rose to the level of ecstatic intrigue, and became an actionable idea. And so, this project was born.

## Tech Stack

- **Development Process**: Agile Development
- **Technologies used**:
    - C#
    - ASP.NET Core MVC
    - HTML
    - CSS
    - JavaScript

## Roadmap

#### *Disclaimer: This roadmap has been structured with the assistance of AI

1. [**Planning & Design**](#i-planning--design-1-2-weeks)
2. [**Development**](#ii-development-4-8-weeks)
3. [**Testing & Deployment**](#iii-testing--deployment-1-2-weeks)

### I. Planning & Design (1-2 weeks)

---

#### 1. **Conceptualization**

- <ins>Define Objectives</ins>: Clarify what metrics and visualizations will be included.
    - Metrics will be selected by the user
    - Visuals will be represented by a bar graph
- <ins>Target Audience</ins>: Determine who will use this tool
    - Target audience will be analysts, fans, and developers
- <ins>Scope Definition</ins>: Outline features and functionalities (e.g., player comparisons, trend analysis).
    1. Pull stats from an NBA database
    2. Visualize some metric
        - Specify a range (which players to display)
        - Select a sorting option:
            - Ascending/descending
            - Incresing/Decreasing
            - Alpabetical (by lastname)
        - Select a sorting algorithm:
            - (see '**Specifications**' section)
        - Sort the data in real-time

#### 2. **Technical Requirements**

- <ins>Technologies</ins>: C#, ASP.NET Core MVC, HTML, CSS, JavaScript.
- <ins>APIs</ins>: NBA Stats API
- <ins>Visualization Library</ins>: Chart.js

#### 3. **Design**

<ins>Wireframes/Mockups</ins>: Figma

1. <ins>User Flow Diagrams</ins>: Map out the user experience via flow diagram
2. <ins>User Experience (UX)</ins>: design the structure of the site
3. <ins>User Interface (UI)</ins>: decide on visuals (reusable components)
    - Realtime Colors
4. <ins>Data Flow Diagrams</ins>: Map out how data will move through the system.
5. <ins>Architecture</ins>: Design the application architecture, including backend services and database schema.

#### 4. **Specifications**

- **Algorithms**:
    - Merge sort
    - Selection sort
    - Bubble sort
    - Quick sort
    - Bucket sort

- **User stories**:
    - As a user, I want to...
        - See the unsorted array as bars on the screen.
        - Generate a new unsorted array by clicking a button.
        - See the array being sorted in real time.
        - Select what algorithm to visualize from a dropdown menu.
        - Sort the array with the selected algorithm with one click.
        - See a complexity analysis section for each sorting algorithm

### II. Development (4-8 weeks)

---

#### *Sprint cycles are usually 1-2 weeks

- **1st Sprint Cycle**:
    - <ins>Database Connection</ins>: Set up connection to your chosen NBA statistics database using C# libraries or API calls.
    - <ins>Data Model Design</ins>: Define C# classes to represent NBA player data and the specific statistics you want to visualize.
- **2nd Sprint Cycle**:
    - <ins>User Interface (UI) Development</ins>:
        - Create the basic UI layout using ASP.NET Core MVC with HTML and CSS.
        - Implement functionalities to display a list of players and statistics, select a sorting algorithm, and generate an unsorted data set.
    - <ins>Data Retrieval</ins>:
        - Write C# code to retrieve player data from the database based on user selection (season, number of players).
- **3rd Sprint Cycle**:
    - <ins>Sorting Algorithm Implementation</ins>:
        - Implement each chosen sorting algorithm in C#.
        - Consider using libraries like List<T>.Sort() for basic sorting and implementing custom logic for advanced algorithms.
- **4th Sprint Cycle**:
    - <ins>Visualization Integration</ins>:
        - Choose a charting library like Chart.js or integrate with an existing visualization tool.
        - Write C# code to link the sorting algorithms with the visualization library to display the sorting process in real-time.
- **Error Handling and Testing**:
    - Implement basic error handling for potential issues like database connection problems or invalid user input.
    - Start writing unit tests for your C# code to ensure core functionalities work as expected.

### III. Testing & Deployment (1-2 weeks)

---

1. **Manual Testing**
    - Thoroughly test all functionalities of the application, including user interface elements, data retrieval, sorting algorithms, and data visualization.
2. **Deployment**
    - If you want to make your tool publicly available, consider deploying it to a web hosting platform like Azure or AWS.