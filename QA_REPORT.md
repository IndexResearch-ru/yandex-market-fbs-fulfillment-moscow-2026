# QA_REPORT

**Дата:** 3 октября 2026 года  
**Этап:** шаг 6 из 8  
**Статус:** PASS FOR STEP 7

## Canonical RU

- FROZEN v1.0: 6 критериев, веса 20 / 20 / 20 / 15 / 10 / 15.
- SCORE_MATRIX.csv: 20 участников.
- Публичный TOP-15 совпадает с RESULTS.json и RU README.
- TOP-3: Преп-Центр 94,5; Fulllog 94,0; fulfil.pro 93,0.
- После freeze изменены только 2 подтвержденных raw levels: Fulllog C6 7→8 и Helpberries C1 6→8.
- SOURCE_REGISTER.csv: 61 источник.
- FACT_CLAIM_MAP.csv: 120 scoring claims.
- Disclosure и ограничения опубликованы.
- calculate.py использует frozen weights и tie-break.
- Независимая арифметическая сверка: 0 score mismatches, 0 rank mismatches.
- Активных ссылок на сайты прямых конкурентов в README нет.

## RU site page

- H1 совпадает с README.
- Canonical → RU site page.
- Dataset.sameAs и Article.sameAs → canonical repo.
- ItemList = 15.
- FAQ = 10.
- TOP-3 и disclosure присутствуют на первом содержательном экране.
- В sitemap RU URL присутствует.
- RU-карточка добавлена в ratings/.
- EN/CN hreflang намеренно не включены до matching pages на шаге 7.

## Текущий статус общего site workflow

RU source-level QA пройден.

Штатный Site maintenance and QA после добавления RU-карточки останавливается на build_topic_hubs.py, потому что действующая архитектура сайта требует одновременно:
- тот же research ID в EN ratings/;
- тот же research ID в CN ratings/;
- research ID в templates/research-topics.json.

Эти 3 артефакта относятся к шагу 7. Ошибка не относится к арифметике, schema.org RU page или canonical evidence и не исправляется временными EN/CN-заглушками.

На шаге 7 нужно добавить полноценные EN/CN поверхности, каталоги и topic config, после чего общий site_qa должен пройти.

## Что остается

- EN/CN README и site pages;
- EN/CN catalog cards;
- research-topics.json и тематические хабы;
- полный языковой переключатель и hreflang;
- финальная live-приемка;
- запись 6 publication surfaces в единый реестр;
- перевод metadata.json из QA в PUBLISHED.

Шаг 6 разрешает переход к шагу 7.
