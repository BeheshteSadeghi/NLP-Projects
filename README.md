# Extractive Text Summarization

A small NLP baseline that selects important sentences from an English article and prints them in the original reading order. It uses sentence-level word frequency with an English stop-word list and runs locally using the Python standard library.

```sh
python summarize.py --sentences 3
python summarize.py path/to/article.txt --sentences 5
```

The included [sample article](TextSummarizer/article.txt) is the default input. [TextSummarizer.ipynb](TextSummarizer/TextSummarizer.ipynb) shows the original NLTK experiment. Sentence splitting uses punctuation and whitespace, so abbreviations and highly formatted text can affect the result.
