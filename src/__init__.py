import jieba
import wordcloud
import matplotlib.pyplot as plt


def cut_word():
    for year in range(2002, 2020):
        if year == 2017:
            continue

        # 进行分词
        file_origin_text = open("../input/西安政府工作报告/第十五组-西安政府工作报告-原始文本-" + str(year) + "年.txt")
        origin_text = file_origin_text.read()
        segs = jieba.cut(origin_text)
        seg_list = jieba.lcut(origin_text)
        file_cut_word = open("../output/西安政府工作报告_分词结果/第十五组-西安政府工作报告-分词结果-" + str(year) + "年.txt",
                             mode="w", encoding="utf-8")
        file_cut_word.write("/".join(segs))

        # 统计词频
        file_word_frequency = open("../output/西安政府工作报告_词频分析结果/第十五组-西安政府工作报告-词频分析结果-" + str(year) + "年.txt",
                                   mode="w", encoding="utf-8")
        word_frequency_map = {}
        for word in seg_list:
            if len(word) <= 1:
                continue
            if word not in word_frequency_map:
                word_frequency_map[word] = 1
            else:
                word_frequency_map[word] += 1
        frequency_set = set(word_frequency_map.values())
        frequency_list = list(frequency_set)
        frequency_list.sort(reverse=True)
        for frequency in frequency_list:
            for key in word_frequency_map:
                if word_frequency_map[key] == frequency:
                    file_word_frequency.write(key + " : " + str(frequency) + "\n")
        file_origin_text.close()
        file_cut_word.close()
        file_word_frequency.close()

        # 制作词云图
        wc = wordcloud.WordCloud(
            font_path='../input/simsun.ttf',
            max_words=200,  # 最多显示词数
            max_font_size=100  # 字体最大值
        )
        wc.generate_from_frequencies(word_frequency_map)
        plt.imshow(wc)  # 显示词云
        plt.axis('off')  # 关闭坐标轴
        plt.savefig("../output/西安政府工作报告_各年度词云图/第十五组-西安政府工作报告-词云图-" + str(year) + "年.jpg")


if __name__ == "__main__":
    cut_word()

# curl https://bootstrap.pypa.io/get-pip.py | python3
# 通过升级pip3 解决ssl版本过低问题