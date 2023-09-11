# 中文手寫字辨識＿結合雜訊與邊緣資訊之集成式模型
+ 論文名稱：中文手寫字辨識之新方法：結合雜訊與邊緣資訊之集成式模型(An Ensemble Model Integrating Noise And Edge Information)
+ 研究生：黃煒翔
+ 與台師大和會考中心合作，協助開發中文手寫字辨識系統，並將應用於國中會考作文辨識上。本研究目的為解決字跡潦草及帶有雜訊的影像導致辨識降低的問題。透過結合雜訊、手寫字邊緣資訊提高模型的泛化能力，再透過集成式方法進一步提升整體效能。此研究方法測試於ICDAR中文手寫辨識競賽獲得96.97%的正確率，提高了2.2%。

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

# ICDAR2013 Test Datasets
| Architecture                | Top1 Accuracy(%) |
| -------------------         |:-------------:   |
| Fujitsu[[1]](./README.md#References)                      | 94.77            | 
| IDSIAnn[[2]](./README.md#References)                      | 94.42            |
| MCDNN[[3]](./README.md#References)                        | 95.79            |
| ATR-CNN Voting[[4]](./README.md#References)               | 96.06            |
| EnsembleHCCRGoogLeNet-10[[5]](./README.md#References)     | 96.74            |
| DenseRAN[[6]](./README.md#References)                     | 96.66            | 
| GoogleNet-ResNet[[7]](./README.md#References)             | 97.03            | 
| Google-ResNet+triplet loss[[8]](./README.md#References)   | 97.03            | 
| ResNet+Center loss[[9]](./README.md#References)           | 97.03            | 
| Ensemble Model with noise and edge information(ours)          | 96.97            |

## References
[1] Yin, F., Wang, Q. F., Zhang, X. Y., & Liu, C. L. (2013, August). ICDAR 2013 Chinese handwriting recognition competition. 
In 2013 12th international conference on document analysis and recognition (pp. 1464-1470). IEEE.

[2] Yin, F., Wang, Q. F., Zhang, X. Y., & Liu, C. L. (2013, August). ICDAR 2013 Chinese handwriting recognition competition. 
In 2013 12th international conference on document analysis and recognition (pp. 1464-1470). IEEE.

[3] Cireşan, D., & Meier, U. (2015, July). Multi-column deep neural networks for offline handwritten Chinese character classification. 
In 2015 international joint conference on neural networks (IJCNN) (pp. 1-6). IEEE.

[4] Wu, C., Fan, W., He, Y., Sun, J., & Naoi, S. (2014, September). Handwritten character recognition by alternately trained relaxation convolutional neural network. In 2014 14th International Conference on Frontiers in Handwriting Recognition (pp. 291-296). IEEE.

[5] Zhong, Z., Jin, L., & Xie, Z. (2015, August). High performance offline handwritten chinese character recognition using googlenet and directional feature maps. In 2015 13th international conference on document analysis and recognition (ICDAR) (pp. 846-850). IEEE.

[6] Wang, W., Zhang, J., Du, J., Wang, Z. R., & Zhu, Y. (2018, August). Denseran for offline handwritten chinese character recognition. In 2018 16th International Conference on Frontiers in Handwriting Recognition (ICFHR) (pp. 104-109). IEEE.

[7] Cheng, C., Zhang, X. Y., Shao, X. H., & Zhou, X. D. (2016, October). Handwritten Chinese character recognition by joint classification and similarity ranking. 
In 2016 15th International Conference on Frontiers in Handwriting Recognition (ICFHR) (pp. 507-511). IEEE.
