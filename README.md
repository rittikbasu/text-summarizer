# Text Summarizer

### About the project
Summarisation is very challenging because when we as humans summarize a piece of text, we usually read it entirely to develop our understanding, and then write a summary highlighting its main points. Since computers lack human knowledge and language capability, it makes automatic text summarization a very difficult and non-trivial task.

For this project I'm using the **extractive summarization** approach where we identify the important sentences or phrases from the original text and extract only those from the text. Those extracted
sentences would be our summary. The below diagram illustrates how extractive summarization works.
<p align="center">
<img src="https://lh3.googleusercontent.com/trCR1Oav-Io888npW16rRzcB6hRMcXJrJemLK2znK9mC5ODoUX7NG9Sjn45JXzLEl8ERm4QoGHpwBxntFVzhJ4ITraVsYogslm1_TR_KkvdmSiINpVxr-uBGBbNcK_EI6OuRFfU" align="center" width="350" title="extractive summarization">
</p>

### Prerequisites
* **urllib:** for requesting a webpage
* **bs4:** for parsing the web page
* **lxml:** for processing html and xml with python
* **nltk:** for performing natural language processing tasks

### How it works?
* Convert the paragraph into sentences
* Text Processing
* Tokenization and Preprocessing
* Evaluate the weighted occurrence frequency of the words
* Substitute words with their weighted frequencies
