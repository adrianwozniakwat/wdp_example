from src.NLP import predict_review_sentiment

def test_predict_review_sentiment():
    path = '/home/adrian/PycharmProjects/wdp_example2/src/Restaurant_Reviews.tsv'
    sentiment_str = 'I very much liked this restaurant'
    predict_review_sentiment(path)
