# answer.engine (answer dot engine)

**answer.engine** is an AI-powered answer engine that answers users' queries by crawling the web in real time. It is built on top of Google Search and Gemini.

**Key components:**
1. Search engine.
2. Web scraper.
3. Chunking & embedding.
4. Language model.

**Things happening under the hood**

The search engine component of answer.engine crawls through the web to find and rank the web pages that match the user's query. We are using Google Search to get the most relevant URLs. The web scraper then takes these URLs and scrapes the contents of the websites asynchronously. The scraped raw text is often noisy and might contain junk data. To remove this junk data and pass the relevant content to the language model, we chunk the text with some overlap and create embeddings of each chunk. We then use these embeddings to calculate the cosine similarity and get the most relevant chunks for the user's query. Finally, we pass only a certain number of top N chunks as context to the language model, which uses that context to answer the user's query. Chunking and embedding also help reduce the input prompt tokens, which enhances the input prompt cost-efficiency.

The average retrieval time for a simple query is 3 seconds, while a complex query takes  ~10 seconds and a very uncommon query takes ~18 seconds. And the main goal here is to reduce these retrieval times.

**How to use this**

**streamlit app:** 

<a href="https://answerdotengine.streamlit.app/" target="_blank">
  <img src="https://drive.google.com/uc?export=view&id=1KDxCwWOzvi7JftyOd1LWHhFFtzgNbVhO" alt="answer.engine" width="35" height="35">
</a>


or


```
!git clone https://github.com/jagadeeshjr5/answerdotengine.git
python src/answerengine.py
```

**Parameters**

Number of references (Default 5): The maximum number of URLs to fetch (up to 10). Decreasing this will perform a narrower search, while increasing it will perform a wider search.

Percentage of context (Default 50%): The percentage of scraped text to be sent to the language model for answering the user's query. The hypothesis here is that 30% of the given raw scraped text is junk, and only about 50% truly contributes to answering the query.


Tweaking these parameters will change the answer.engine's output behaviour.


**What's next?**

1. Agents
2. Access to multiple live datasources and APIs.
3. Memory module.
4. Session history caching.
5. Knowledge caching.
6. Advanced web scraper.
7. Multimodality
8. More search engines
9. Much more...

**Socials**

<a href="https://www.linkedin.com/in/jagadeeshreddyjr5" target="_blank">
  <img src="https://drive.google.com/uc?export=view&id=1pV2htPGXsvMXONeFv_qdyHMkn_TgYp5U" alt="LinkedIn" width="25" height="25">
</a>
