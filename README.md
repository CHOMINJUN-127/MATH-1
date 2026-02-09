# Triangle Trigonometry Verification

## 📌 프로젝트 개요

이 프로젝트는 학교에서 진행한 **수학 주제탐구 발표**를 준비하는 과정에서 제작되었다.
당시 학습하고 있던 단원이 **삼각함수**였기 때문에, 교과서에서 배우는 개념을 단순한 계산에 그치지 않고 **실제 상황에 적용해 보고자** 이 주제를 선택하였다.

삼각함수는 거리와 각의 관계를 통해 위치를 추정할 수 있기 때문에, 이를 활용하면 **GPS와 같은 위치 추적 원리**를 수학적으로 설명할 수 있다고 판단하였다. 특히 여러 삼각함수 중에서도 **코사인 법칙은 두 거리와 그 사이의 각이 주어졌을 때 나머지 한 변을 계산할 수 있어,** 위성과 사용자 사이의 거리 계산에 효과적으로 활용할 수 있다.

이에 따라 본 프로젝트에서는 삼각형 구조를 가정하여 위성 A, 위성 B, 사용자 위치를 점으로 설정하고, **코사인 법칙과 사인 법칙을 이용해 각과 거리의 관계를 계산**하였다. 또한 이러한 수학적 계산 과정을 **파이썬 코드로 구현**하여 결과를 수치적으로 검증하고, 계산된 값이 실제 삼각형 구조와 일치하는지를 **기하적 시각화**를 통해 확인하는 것을 목표로 한다.

## 🎯 문제 설정

본 프로젝트에서는 GPS 위치 계산의 원리를 단순화하여, 한 평면 위의 삼각형 구조로 문제를 설정한다.
위성 A와 위성 B, 그리고 사용자 위치를 각각 삼각형의 세 꼭짓점으로 가정하고, 이들 사이의 거리와 각의 관계를 삼각함수로 분석한다.

구체적으로, 위성 A와 사용자 사이의 거리와 위성 B와 사용자 사이의 거리 중 일부 값이 주어져 있으며, 위성 A에서 관측되는 두 방향 사이의 각이

<img width="214" height="60" alt="image" src="https://github.com/user-attachments/assets/fbdc4d19-10ad-49c9-83be-bf40bf18fd6e" />


로 주어진 상황을 가정한다. 이때 삼각형의 변과 각은 다음과 같이 설정한다.

- 위성 A–사용자 사이의 거리: c
- 위성 B–사용자 사이의 거리: 𝑎
- 위성 A–위성 B 사이의 거리: 𝑏
                                      
이 문제의 목표는 주어진 거리와 각 정보를 바탕으로 **각 𝐵의 삼각함수 값,** 특히

<img width="262" height="67" alt="image" src="https://github.com/user-attachments/assets/aca1c137-acd6-43f4-afd5-cce255bf967f" />

를 계산하는 것이다.

이를 위해 **사인 법칙과 코사인 법칙을 각각 적용**하여 동일한 값을 얻을 수 있는지를 확인하고, 두 서로 다른 수학적 접근이 **같은 결과로 수렴함을 검증**하는 것을 핵심 문제로 설정한다. 또한 계산된 결과가 실제 삼각형 구조에서도 타당한지를 확인하기 위해, 파이썬을 이용한 **기하적 시각화**를 함께 수행한다.

## 🧠 접근 방법

이 프로젝트에서는 삼각형의 변과 각 사이의 관계를 분석하기 위해 **삼각함수의 기본 정리인 사인 법칙과 코사인 법칙을 핵심 도구로 사용**하였다.
단순히 하나의 공식을 적용해 값을 구하는 것이 아니라, **서로 다른 두 접근 방법이 동일한 결과를 도출하는지 검증**하는 방식으로 탐구를 진행하였다.

먼저, 주어진 각 ∠𝐴=60∘ 와 두 변의 길이를 이용하여 **사인 법칙**을 적용하고, 이를 통해 각 𝐵의 사인 값을 계산한다. 이후 이 값을 제곱하여 sin²B를 구하고, 
삼각함수의 기본 항등식

<img width="254" height="76" alt="image" src="https://github.com/user-attachments/assets/50a98271-0d24-45dd-b6d6-7b7684ac2020" />

을 이용해 cos²B를 도출한다.

다음으로, 동일한 삼각형에 대해 **코사인 법칙**을 적용하여 한 변의 길이를 먼저 계산한 뒤, 이를 다시 활용해 각 B의 코사인 값을 직접 구한다. 이 과정에서 얻은 COS² B 가 앞선 방에서 계산한 값과 일치하는지를 비교함으로써, 두 수학적 접근이 같은 결론에 도달함을 확인한다.

모든 계산 과정은 **파이썬으로 구현**하였으며, 실수 연산으로 인한 오차를 최소화하기 위해 가능한 경우 **분수 형태의 계산**을 유지하였다. 또한 계산된 결과를 turtle 모듈을 사용해 삼각형으로 시각화하여, 수치적 결과가 기하적 구조와도 일치함을 직관적으로 검증하였다.

## ✏️ 계산 방법 ①

첫 번째 방법에서는 삼각형의 **사인 법칙**을 이용하여 각 𝐵의 삼각함수 값을 계산한다.
사인 법칙은 삼각형에서 각의 사인 값과 그에 대응하는 변의 길이 사이의 비가 일정하다는 성질을 이용한 정리이다.

삼각형에서 사인 법칙은 다음과 같이 표현된다.

<img width="223" height="79" alt="image" src="https://github.com/user-attachments/assets/f7589e2b-6cb8-4e4c-bad6-414a8f0c796a" />

문제 설정에서 주어진 값은

<img width="306" height="64" alt="image" src="https://github.com/user-attachments/assets/1e158bcd-22cc-4767-aea0-6a99ab2881bf" />

이므로 이를 식에 대입하면,

<img width="221" height="83" alt="image" src="https://github.com/user-attachments/assets/c49b6021-1bdf-4c2e-beee-8788b58633cd" />

여기서

<img width="202" height="86" alt="image" src="https://github.com/user-attachments/assets/915cc834-2d0c-478b-8773-b664ef3f33f1" />

이므로,

<img width="277" height="94" alt="image" src="https://github.com/user-attachments/assets/6978d87a-ed63-4220-91bd-e17aff7bb1d8" />

이를 정리하면, 

<img width="224" height="103" alt="image" src="https://github.com/user-attachments/assets/64b6e730-4d6a-429a-b471-8c3359915ee8" />

이제 각 B의 사인 값을 제곱하여 sin²B를 구하면,

<img width="304" height="98" alt="image" src="https://github.com/user-attachments/assets/4dbdaa42-ba1a-4395-92bb-88f4594dfff3" />

다음으로 삼각함수의 기본 항등식

<img width="253" height="54" alt="image" src="https://github.com/user-attachments/assets/8c59691e-879a-45dc-a40c-6d5297edcd07" />

을 이용하면,

<img width="292" height="70" alt="image" src="https://github.com/user-attachments/assets/cdfabeef-eab9-49f9-a6dc-5e1133001215" />

따라서 사인 법칙을 이용한 계산 결과는

<img width="325" height="78" alt="image" src="https://github.com/user-attachments/assets/0bf2b1c1-27e5-4367-8188-df169ea251ce" />

이다.

이 결과는 이후 **코사인 법칙을 이용한 두 번째 방법**에서 얻은 값과 비교하여, 서로 다른 접근이 동일한 결론에 도달함을 확인하는 기준으로 사용된다.

## ✏️ 계산 방법 ②

## 🐢 기하적 시각화

## 🛠 사용 기술

## 📌 활용 가능성

