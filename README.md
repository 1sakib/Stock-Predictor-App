<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a id="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->




<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
    </li>
    <li><a href="#use">Usage</a></li>
    <li><a href="#contact">Contact</a></li>
    
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About Project - Stock Predictor App

![Product Name Screen Shot][product-screenshot]https://stock-predictor-app-with-trends.streamlit.app/

In this project, I created an application that can predict a stock's closed prices over a specified period of time.
I use an open-source machine learning model called Prophet that reads and analyzes stock data to produce its predictions.

How it works : 

The user would input the stock ticker of any stock and the application would download its stock data via the yfinance library.
The downloaded data would be put into a format that the Prophet model can read.
The Prophet model would analyze the data and produce a table of data that has the future prices of the stock in however
many years the user specified.
The graph of the predictions and trend of the prices would be shown using the Plotly library at the end.

Click here for the application : [https://stock-predictor-app-with-trends.streamlit.app]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

The yfinance (Yahoo Finance) Python library was imported as well.

* [Python][Python-url] 
* [Streamlit][Streamlit-url] 
* [Prophet][Prophet-url] 
* [Plotly][Plotly-url] 


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

Please run these commands in the terminal.

Install all the libraries : 
* streamlit
  ```sh
  pip install streamlit
  ```
* plotly
  ```sh
  pip install plotly
  ```
* yfinance
  ```sh
  pip install yfinance
  ```
* prophet
  ```sh
  pip install Prophet
  ```
* pandas
  ```sh
  pip install pandas
  ```


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Use

The most practical unique use of this predictor is more so in the trends that the application produces.

The yearly trend in the bottom of the page of the application showcases around what time of the year is the best/worst time
to invest into stocks; which is really useful.

<p align="right">(<a href="#readme-top">back to top</a>)</p>




<!-- CONTACT -->
## Contact

Sakib Uddin - ([https://www.linkedin.com/in/1sakib-uddin/]) - 1sakib.uddin@gmail.com

<p align="right">(<a href="#readme-top">back to top</a>)</p>





<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[product-screenshot]: images/streamlit-screenshot.png
[Python-url]: https://www.python.org
[Streamlit-url]: https://streamlit.io
[Plotly-url]: https://plotly.com
[Prophet-url]: https://facebook.github.io/prophet
