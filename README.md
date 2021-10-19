# Text Summarizer

### About the project

This project is offered as a service through a simple flask [website](https://summariser.rittikbasu.repl.co/) wherein a user can either provide a URL or enter text manually and get an elegant summary of the provided text. The underlying principal on which the algorithm works is extractive summarisation, where the important sentences or phrases from the original text are identified and extracted to form a summary.

<table>
  <tr>
    <td align="center">Landing Page</td>
     <td align="center">After choosing mode of input</td>
     <td align="center">Summary Page</td>
  </tr>
  <tr>
    <td><img src="images/Screenshot from 2021-10-19 21-04-16.png" width=300 height=480></td>
    <td><img src="images/Screenshot from 2021-10-19 20-48-10.png" width=300 height=480></td>
    <td><img src="images/Screenshot from 2021-10-19 20-48-31.png" width=300 height=480></td>
  </tr>
</table>

### How it works?
* We request the page source with urllib and then parse that page with BeautifulSoup and extract the text from the ```<p>``` tags.

* **Text Processing:** First the paragraphs are converted into sentences then we remove all special characters, numbers, punctuation, and stop words (words such as _is, an, a, the, for_ that do not add value to the meaning of a sentence)  from the extracted text.

* **Tokenization:** The text is divided into a series of tokens using the ```sent_tokenize()``` function of nltk. Tokenizing the sentences is done to get all the words present in the sentences.

* A frequency table of the words is created to evaluate the weighted occurrence frequency of the words. The approach of weighing is based on frequencies i.e. every word/term is assigned a weight using tf-idf (term frequency – inverted document frequency) approach. The **weight of a term = term frequency * inverse of document frequency.**

* We then substitute words with their weighted frequencies choosing all sentences above a certain weight threshold and ordering the selected sentences as they appear in the original article.

* Finally after getting all the required parameters we generate the summary.

### Prerequisites
* **urllib:** for requesting a webpage
* **bs4:** for parsing the web page
* **lxml:** for processing html and xml with python
* **nltk:** for performing natural language processing tasks


