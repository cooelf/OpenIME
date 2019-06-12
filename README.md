

Dataset and codes accompanying the paper **[Open Vocabulary Learning for Neural Chinese Pinyin IME.](https://arxiv.org/abs/1811.04352)**

## Dataset

 Two processed corpora for IME evaluation, the People’s Daily corpus (PD) and the TouchPal corpus (TP) .

<table>
   <tr>
      <td></td>
      <td></td>
      <td>Chinese</td>
      <td>Pinyin</td>
   </tr>
   <tr>
      <td rowspan=5>PD</td>
      <td>MIUs</td>
      <td>5.04M</td>
      <td></td>
   </tr>
   <tr>
      <td>Word</td>
      <td>24.7M</td>
      <td>24.7M</td>
   </tr>
   <tr>
      <td>Vocab</td>
      <td>54.3K</td>
      <td>41.1K</td>
   </tr>
   <tr>
      <td>Target Vocab (train)</td>
      <td>2309</td>
      <td>-</td>
   </tr>
   <tr>
      <td>Target Vocab (dec)</td>
      <td>2168</td>
      <td>-</td>
   </tr>
   <tr>
      <td rowspan=5>TP</td>
      <td>MIUs</td>
      <td>689.6K</td>
       <td></td>
   </tr>
   <tr>
      <td>Word</td>
      <td>4.1M</td>
      <td>4.1M</td>
   </tr>
   <tr>
      <td>Vocab</td>
      <td>27.2K</td>
      <td>20.2K</td>
   </tr>
   <tr>
      <td>Target Vocab (train)</td>
      <td>2020</td>
      <td>-</td>
   </tr>
   <tr>
      <td>Target Vocab (dec)</td>
      <td>2009</td>
      <td>-</td>
   </tr>
</table>

.ali    target

.py    source

.adddict     training set

.test2k        test set

The full corpus and pre-trained vectors can be downloaded from https://drive.google.com/drive/folders/1v6QW7ULu-iYxU5uruiuSgYGmoXOcHAeX?usp=sharing

## Source Code

We also release our source codes to help others reproduce our result, which is modified from [OpenNMT](https://github.com/OpenNMT/OpenNMT) with similar usage. 

### Reference

If you use this repo please cite our paper:

```
@inproceedings{zhang2019acl-ime,
	title = "{Open Vocabulary Learning for Neural Chinese Pinyin IME}",
	author = "Zhang, Zhuosheng and Huang, Yafang and Zhao, Hai",
	booktitle = "Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics (ACL)",
	year = "2019",
}
```

