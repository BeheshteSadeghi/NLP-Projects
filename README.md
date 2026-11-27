# Extractive Text Summarizer

Selects representative English sentences from a local text file without external dependencies.

[Run the project](#quick-start) · [Verification](#verification) · [Files](#repository-map)

| | |
| --- | --- |
| Stack | Python standard library |
| Entry point | [`summarize.py`](summarize.py) |
| Focus | nlp · extractive-summarization · python · cli |

## How it works

`Text file → sentence segmentation → scoring → source-order summary`

## Quick start

```sh
python summarize.py --sentences 3
python summarize.py path/to/article.txt --sentences 5
```

The included [sample article](TextSummarizer/article.txt) is the default input. [TextSummarizer.ipynb](TextSummarizer/TextSummarizer.ipynb) shows the original NLTK experiment. Sentence splitting uses punctuation and whitespace, so abbreviations and highly formatted text can affect the result.

## Verification

The CLI runs on the included sample without credentials or package installation.

## Repository map

| Path | Purpose |
| --- | --- |
| [`summarize.py`](summarize.py) | CLI |
| [`TextSummarizer/TextSummarizer.ipynb`](TextSummarizer/TextSummarizer.ipynb) | Initial notebook |
| [`TextSummarizer/article.txt`](TextSummarizer/article.txt) | Sample input |

## Scope

Sentence splitting is punctuation-based and is sensitive to abbreviations and formatting.
