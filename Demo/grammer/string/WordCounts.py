import jieba


# def get_word_frequency(text):
#     seg_list = jieba.cut(text)
#     word_dict = {}
#     for word in seg_list:
#         print(word)
#         if word in word_dict:
#             word_dict[word] += 1
#         else:
#             word_dict[word] = 1
#     sorted_word_dict = sorted(word_dict.items(), key=lambda x: x[1], reverse=True)
#     return sorted_word_dict
#
#
# text = "梦想橡皮擦的python博客很不错"
# result = get_word_frequency(text)
# print(result)

# stop_words=set()
# with open("stop_words.txt","r",encoding='utf-8') as f:
#     for line in f:
#         stop_words.add(line.strip())
# text = "梦想橡皮擦的python博客很不错"
# seg_list = jieba.cut(text)
# filtered_words=[word for word in seg_list if word not in stop_words]
# print(filtered_words)

from wordcloud import WordCloud
import matplotlib.pyplot as plt
text="ca1 ca2 ca3 ca4 ca5 ca6"
wordcloud = WordCloud(width=400, height=400, random_state=21, max_font_size=110).generate(text)
plt.figure(figsize=(10,5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()
