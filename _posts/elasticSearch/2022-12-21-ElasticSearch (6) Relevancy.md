---
layout: single

header:
  teaser: /assets/images/logo/elasticSearch.png
  overlay_image: /assets/images/logo/elasticSearch.png
  overlay_filter: linear-gradient(rgba(255, 0, 0, 0.5), rgba(0, 255, 255, 0.5))
  caption: "Photo credit: [**Unsplash**](https://unsplash.com)"
  actions:
    - label: "Github"
      url: "https://github.com/renine94"

title: "[ES] 검색에서 스코어를 결정하는 Relevancy"
excerpt: "🚀 ES에서 스코어(점수)가 계산되는 원리에 대해 알아보자. (BM25, TF, IDF, Field Length)"

categories: elasticSearch
tag: [es, elasticSearch, relevancy, score, bm25, TF, IDF]

toc: true
toc_label: "📕 목차"
toc_icon: "null"
toc_sticky: true

sidebar:
  nav: "docs"
---

# Relevancy

> Relevancy 은 연관성, 관련성 정도로 해석되는데, 여기서는 "정확도" 라는 의미로 얘기하도록 하겠습니다.



- RDBMS
  - 쿼리 조건에 부합하는 지만 판단하여 결과를 가져온다.
  - 각 결과들이 얼마나 정확한지에 대한 판단 불가능
- ElasticSearch
  - 풀텍스트 검색엔진이기 때문에, 검색 결과가 입력된 검색조건과 얼마나 정확하게 일치하는지 계산 가능
  - 계산하는 알고리즘을 가지고 있다. (BM25)
  - **이 정확도를 기반으로 사용자가 가장 원하는 결과를 먼저 보여줄 수 있다.**
  - 이 정확도를 `relevancy` 라고 한다.



## 01. 스코어 (Score) 점수

ES 검색결과에 스코어 점수가 표시되며, 이 점수는 검색조건과 얼마나 일치하는지를 나타낸다.<br>점수가 높은 순으로 결과를 보여준다.

```json
// quick dog 를 포함한 도큐먼트 검색

GET my_index/_search
{
  "query": {
    "match": {
      "message": "quick dog"
    }
  }
}
```



위처럼 ES 에 검색을 하게 되면, 관련 도큐먼트들이 추출되고, 전체 검색 결과가 score 값을 기준으로 높은값부터 보여지게 됩니다.<br>ES 에서는 이 점수를 계산하기 위해 **BM25** (Best Matching) 라는 알고리즘을 이용합니다.



- BM25 계산식

![image-20221221164345425](../../assets/images/posts/2022-12-21-ElasticSearch (6) Relevancy/image-20221221164345425.png)



위 계산이 복잡해보이지만,

- **TF**
  - Term빈도, 많이 매칭될수록 점수 업
- **IDF**
  - 전체 인덱스에서 해당 Term이 많을수록 점수 다운
- **Field Length**
  - 길이가 긴 문장보다 짧은곳에서 Term이 매칭되면 점수가 업



계산에는 크게 위 3가지 요소가 사용됩니다.





## 02. TF (Term Frequency)

> 단어의 빈도

도큐먼트 내에 검색된 텀(term) 이 더 많을수록 점수가 높아지는 것을 말합니다.

포함하고 있는 term이 증가할수록 아래 그래프와 같이 TF 값도 증가를 하며, BM25 알고리즘에서는 최대 25까지 증가합니다.<br>즉, 25 이상 부터는 TF 점수의 변화가 없습니다.

![BM25 TF Score](https://1535112035-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-Ln04DaYZaDjdiR_ZsKo%2F-LnoG1RY615gm8v0Jxha%2F-LnoG53-nth6Y7BZkpSG%2F5.3-02-tf.png?alt=media&token=62435b47-79d9-4e73-99df-5940a598ba4b)





## 03. IDF (Inverse Document Frequency)

> 전체 index에 포함된 term이 증가할수록 IDF 는 감소한다.



"쥬라기 공원" 검색시,

- "쥬라기 가 포함된 검색결과 10개
- "공원" 이 포함된 검색결과 100개



흔한 단어인 **공원** 보다는 희소한 단어인 **쥬라기**가 검색에 더 중요한 term일 가능성이 높습니다.<br>검색한 term을 포함하고 있는 도큐먼트 개수가 많을수록 그 텀의 자신의 점수가 감소하는 것을 IDF 라고 합니다.

![IDF](../../assets/images/posts/2022-12-21-ElasticSearch (6) Relevancy/assets%2F-Ln04DaYZaDjdiR_ZsKo%2F-LnoGdUUoWZAUrQnYksL%2F-LnoIEr8c1Ghixk14w02%2F5.3-03-idf.png)





## 04. Field Length

도큐먼트에서 필드 길이가 긴 필드보다 짧은 필드에 있는 term의 비중이 더 클 것입니다.<br>텍스트 길이가 긴 내용보다는 텍스트 길이가 짧은 제목 필드에 검색어를 포함하고 있는 블로그 포스트가 더 점수가 높게 나타납니다.



**즉, 짧은문장에서 일치하면 점수가 더 높다.**















