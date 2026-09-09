with open('page-portfolio.html', 'r', encoding='utf-8') as f:
    content = f.read()

replacements = [
    ('images/portfolio/project1.jpg', 'images/portfolio/spark_streaming_thumb.svg'),
    ('images/portfolio/project2.jpg', 'images/portfolio/speech_ai_thumb.svg'),
    ('images/portfolio/project3.jpg', 'images/portfolio/bilstm_sentiment_thumb.svg'),
    ('images/portfolio/project4.jpg', 'images/portfolio/cross_lingual_spark_thumb.svg'),
    ('images/portfolio/project5.jpg', 'images/portfolio/graph_analytics_thumb.svg'),
    ('images/portfolio/project9.jpg', 'images/portfolio/cnn_vision_thumb.svg'),
    ('images/portfolio/project10.jpg', 'images/portfolio/microservice_gateway_thumb.svg'),
    ('images/portfolio/project11.jpg', 'images/portfolio/hadoop_cluster_thumb.svg'),
    ('images/portfolio/project12.jpg', 'images/portfolio/lockfree_hashtable_thumb.svg'),
    ('images/portfolio/project13.jpg', 'images/portfolio/ir_tokenizer_thumb.svg'),
    ('images/portfolio/project14.jpg', 'images/portfolio/skiplist_index_thumb.svg'),
]

for old_val, new_val in replacements:
    content = content.replace(old_val, new_val)

with open('page-portfolio.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated page-portfolio.html thumbnails successfully!")
