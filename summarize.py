import argparse
from collections import Counter
from pathlib import Path
import re


PATTERN = re.compile(r'[^\W\d_]+', re.UNICODE)
STOPWORDS = set('a an and are as at be been but by for from had has have he her his i if in is it its not of on or she that the their them they this to was were what when which who will with would you your'.split())


def summarize(text, count):
    sentences = re.split(r'(?<=[.!?])\s+', text.strip())
    sentences = [sentence for sentence in sentences if sentence.strip()]
    words = [[word for word in PATTERN.findall(sentence.lower()) if word not in STOPWORDS]
             for sentence in sentences]
    frequencies = Counter(word for group in words for word in set(group))
    ranked = sorted(
        enumerate(words),
        key=lambda pair: sum(frequencies[word] for word in set(pair[1])) / max(len(pair[1]), 1),
        reverse=True,
    )
    positions = sorted(index for index, _ in ranked[:count])
    return '\n'.join(sentences[position] for position in positions)


def main():
    parser = argparse.ArgumentParser(description='Extract high-scoring sentences from an English text file.')
    parser.add_argument('article', type=Path, nargs='?', default=Path(__file__).parent / 'TextSummarizer' / 'article.txt')
    parser.add_argument('--sentences', type=int, default=3)
    args = parser.parse_args()
    if args.sentences < 1:
        parser.error('--sentences must be positive.')
    try:
        summary = summarize(args.article.read_text(encoding='utf-8-sig'), args.sentences)
    except OSError as error:
        parser.error(str(error))
    if not summary:
        parser.error('The file has no text to summarize.')
    print(summary)


if __name__ == '__main__':
    main()
