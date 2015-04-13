# Test Driven Development in Python

## 원본

- [Test Driven Development (TDD) in Python \- YouTube](https://www.youtube.com/watch?v=k50zqdXdYxc)

## 참고 자료

- [\[도서\] 테스트 주도 개발, 켄트 벡 저/김창준,강규영 공역, 9788966261024 | YES24 상품정보](http://www.yes24.com/24/goods/12246033?scode=032&OzSrank=3): 이 책이 기본 베이스

## TDD를 하면서 느낀 점

- 원래는 계산기를 TDD로 해보려고 했으나 계산기로 되어있는 예제 코드가 없어서 URL로 테스트 코드를 연습해 보게 됐다.
- TDD를 하면 내 코드를 신뢰할 수 있고 무엇보다 원본 소스를 바꾼 후에 여러가지 테스트를 수작업을 해야되는데 그런걸 신경 안써도 되니 굉장히 편하다.
- TDD, Logging은 정말 중요한 것 같다. Logging 같은 경우는 언제 사용해야 될지? 그걸 정하는 것도 하나의 이슈
  - 에러날만한 곳에 Logging
  - DB 접속하고 끝날 때 Logging
  - 함수 시작하고 끝날 때 Logging(내 프로그램 문제인지, OS나 다른 시스템 문제인지 파악하기 좋다)
- Refactoring은 TDD를 하면서 당연히 따라오게 된다. 가장 처음에 만든 테스트 코드로 빨간색을 보지만 최대한 빨리 녹색을 보고 여기에 여러가지 테스트 케이스를 넣고 최종적으로 리팩토링 하면 된다.
- 소스코드 원본 로직이 바뀌게 되면 테스트 코드들이 다 바뀔 때도 있다. 이런 삽질을 4~5번 하다보면 어떻게 잘 작성할지 감이 온다고 한다. 난 아직 못 느껴봄...
- [\[도서\] 클린 코드를 위한 테스트 주도 개발, 해리 J.W. 퍼시벌 저/김완섭 역, 9788994774916 | YES24 상품정보](http://www.yes24.com/24/goods/16886031?scode=032&OzSrank=1): 이 책도 조만간 뗄 생각이다. 

## 파이썬코리아 강남 스터디

- [계산기 TDD 기능 추가하기 전](https://gist.github.com/jonghokim/6683167?hc_location=ufi)
- [계산기 TDD 기능 추가 후](https://gist.github.com/haje01/6506093?hc_location=ufi)
- [3장에서 11장까지 예제코드](https://www.facebook.com/groups/291278291017913/?ref=browser#)
- 여기 예제가 있으니 직접 따라해보자.
- 최종 완성된 소스코드가 있다. step by step 이 아니라 따라하기는 약간 힘들 수 있지만.. 고수님들께 여쭤보니 직접 짜보라고 한다. 이제 동영상 보고 따라해 봤으면 실전 Field에서 뛰면서 이리 저리 깨져보면서 경험으로 체득하는게 가장 이해하는데 좋다고 한다.