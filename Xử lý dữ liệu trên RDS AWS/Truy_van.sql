--RDS
/*Yêu cầu 1 */
select `asm-2-app`.Category,sum(`asm-2-review`.Sentiment_Subjectivity),sum(`asm-2-review`.Sentiment_Polarity) from `asm-2-app` inner join `asm-2-review`
                on `asm-2-app`.App=`asm-2-review`.App group by `asm-2-app`.Category
--[2022-09-22 09:37:22] 33 rows retrieved starting from 1 in 1 s 506 ms (execution: 1 s 482 ms, fetching: 24 ms)

/*Yêu cầu 2 */
select  a.Category , a.count_Negative ,b.count_Positive,c.count_Neutral
            from (select `asm-2-app`.Category, count(`asm-2-review`.Sentiment) as count_Negative
                  from `asm-2-app` inner join `asm-2-review`on `asm-2-app`.App=`asm-2-review`.App
                  where `asm-2-review`.Sentiment = 'Negative'
                  group by `asm-2-app`.Category,`asm-2-review`.Sentiment) a
            inner join
                 (select `asm-2-app`.Category, count(`asm-2-review`.Sentiment) as count_Positive
                  from `asm-2-app` inner join `asm-2-review`on `asm-2-app`.App=`asm-2-review`.App
                  where `asm-2-review`.Sentiment = 'Positive'
                  group by `asm-2-app`.Category,`asm-2-review`.Sentiment) b
            on a.Category = b.Category
            inner  join
                 (select `asm-2-app`.Category, count(`asm-2-review`.Sentiment) as count_Neutral
                  from `asm-2-app` inner join `asm-2-review`on `asm-2-app`.App=`asm-2-review`.App
                  where `asm-2-review`.Sentiment = 'Neutral'
                  group by `asm-2-app`.Category,`asm-2-review`.Sentiment) c
            on b.Category = c.Category
--RDS : [2022-09-22 09:53:05] 33 rows retrieved starting from 1 in 1 s 398 ms (execution: 1 s 372 ms, fetching: 26 ms)
--Local : (33 rows affected) Completion time: 2022-09-25T08:32:24.2955884+07:00


/*Yêu cầu 3 */
select s.Category , sum(s.word)as word_count , avg(s.price)as avg_Price from
            (select `asm-2-app`.Category,(LENGTH(`asm-2-review`.Translated_Review) - LENGTH(REPLACE(`asm-2-review`.Translated_Review, ' ', '')) + 1) as word,`asm-2-app`.Price as price
                from`asm-2-app` inner join `asm-2-review` on `asm-2-app`.App = `asm-2-review`.App
                where `asm-2-review`.Translated_Review != 'None') s
            group by s.Category order by word_count desc
--[2022-09-22 10:59:12] 33 rows retrieved starting from 1 in 1 s 21 ms (execution: 1 s 3 ms, fetching: 18 ms)