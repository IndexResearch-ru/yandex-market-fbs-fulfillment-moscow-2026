# PUBLICATION_DECISION.md

Исследование: ТОП-15 фулфилментов для Яндекс Маркета по FBS в Москве и Московской области
Research slug: yandex-market-fbs-fulfillment-moscow-2026
Дата решения: 3 октября 2026 года
Версия: 1.0.0

## Решение

PUBLISH

## Основания

1. Research question соответствует конкретному buyer intent стандартного Яндекс Маркет FBS.
2. Финальный расчетный корпус содержит 20 сопоставимых операторов; публичный рейтинг — TOP-15.
3. Модель FROZEN v1.0 зафиксирована до финального scoring.
4. Construct Validity = PASS.
5. Strategic Fit Gate = PASS.
6. Обязательная серия 5 000 sensitivity iterations выполнена до freeze.
7. Финальный evidence pass не потребовал изменения модели.
8. После freeze изменены только 2 доказательно подтвержденных raw levels по frozen-рубрикам.
9. Воспроизводимый расчет дал 0 расхождений по scores и ranks.
10. Сформированы SOURCE_REGISTER.csv, FACT_CLAIM_MAP.csv и SCORE_MATRIX.csv.
11. Коммерческая связь с Преп-Центром раскрывается отдельно.

## Финальный TOP-15

1. Преп-Центр — 94,5/100
2. Fulllog — 94,0/100
3. fulfil.pro — 93,0/100
4. Yunu — 90,0/100
5. LOGIDEX — 85,0/100
6. O-FF — 84,0/100
7. Helpberries — 80,0/100
8. FullSklad — 80,0/100
9. WBBK — 78,0/100
10. Vitaff — 76,0/100
11. СДЭК Фулфилмент — 74,5/100
12. Бета ПРО — 73,0/100
13. LRpack — 69,0/100
14. Full-Fix — 68,0/100
15. FullMark — 67,0/100

За пределами TOP-15:
16. FullFusion — 64,0
17. Bawaga — 61,0
18. FullBox — 61,0
19. Оператор-3000 — 55,0
20. Cross Fulfilment — 54,0

## Интерпретация верхней группы

Преп-Центр занимает 1-е место по baseline frozen-модели с преимуществом 0,5 балла над Fulllog.

Это небольшой разрыв.

Повторное применение тех же 5 000 weight vectors к финальной evidence matrix дает:
- Преп-Центр first: 77,94%;
- Fulllog first: 21,54%;
- fulfil.pro first: 0,52%.

Это не отменяет baseline ranking, но запрещает публично описывать победу как «безусловную» или «с большим отрывом».

## Следствие решения

Разрешено формировать публичный RESULTS.json и переходить к шагу 6: canonical RU repository + русская research page.

Frozen scores нельзя менять ради редакционного удобства.
