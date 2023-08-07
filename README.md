# Thesis-WeiHsiang-Huang-AnEnsembleModelIntegratingNoiseAndEdgeInformation
中文手寫字辨識之新方法：結合雜訊與 邊緣資訊之集成式模型
+ 研究生：黃煒翔

# 使用說明
+ 可直接在Jupyter NotebooK上執行(建議)
+ 若以cmd執行
```sh
ipython
%run 基準模型.ipynb
```
+ 也可以將程式碼轉成py檔後執行
```sh
python3 基準模型.py
```

# 程式碼說明
+ Code資料夾下包含基準模型、椒鹽模型、高斯模型和邊緣模型的訓練程式碼
  + 基準模型.ipynb：使用原始影像進行訓練
  + 椒鹽模型.ipynb：使用加入椒鹽雜訊的影像進行訓練
  + 高斯模型.ipynb：使用加入高斯雜訊的影像進行訓練
+ 基準模型資料夾下包含Edge-O和Edge-F的訓練程式碼，並使用通道結合影像進行訓練
  + 通道結合影像有三種：
    + RG_CANNY(原論文上的方法)：使用CANNY邊緣資訊與原始影像的RG通道結合的影像
    + CANNY：三個通道都是CANNY邊緣資訊的影像
    + CTG：使用CANNY邊緣資訊、Threshold(二值化)和GrayScale(灰階)結合的影像
+ merge_channel.py：該程式碼可將輸入影像轉成通道結合影像
+ my_transforms.py：該程式碼可將雜訊加入到原始影像內
---
+ recognition.ipynb：訓練完後，可使用該程式碼進行測試
+ predictor.py：recognition.ipynb會import該程式碼。該程式碼會將輸入影像進行預測
+ evaluator.py：recognition.ipynb會import該程式碼。該程式碼會計算正確率

# 資料集
本研究共使用四種資料集進行實驗
+ G9HW資料集
+ LRRC資料集
+ CASIA資料集
+ ICDAR13測試集
