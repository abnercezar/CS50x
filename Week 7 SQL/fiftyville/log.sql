-- Keep a log of any SQL queries you execute as you solve the mystery.

--Com base nas informações fornecidas no exercício, realizei minha primeira consulta
--na tabela "crime_scene_reports".
SELECT description FROM crime_scene_reports
WHERE year = 2021 AND month = 7 AND day = 28 AND street = "Humphrey Street";

--Após minha primeira consulta descobri que o roubo do pato ocorreu na padaria na rua Humphrey
-- ás 10:15 e que três testemunhas deram entrevistas "interviews".
SELECT transcript FROM interviews
WHERE year = 2021 AND month = 7 AND day = 28 AND transcript LIKE "%bakery%";

--Com base nas informações da primeira testemunha consultei a tabela de "people" e "bakery_security_logs"
SELECT name FROM people
JOIN bakery_security_logs ON bakery_security_logs.license_plate = people.license_plate
WHERE year = 2021 AND month = 7 AND day = 28 AND hour = 10 AND minute >= 15 AND minute <=25
AND activity = "exit";

--Com base nas informações da terceira testemunha realizei uma consulta na tabela "people", "passengers" e "airports"
SELECT name FROM people
JOIN passengers ON passengers.passport_number = people.passport_number
WHERE passengers.flight_id = (
SELECT id FROM flights
WHERE year = 2021 AND month = 7 AND day = 29 AND origin_airport_id = (
SELECT id FROM airports WHERE city = "Fiftyville")
ORDER BY hour, minute
LIMIT 1);

--Também fiz uma consulta para saber qual pessoa fizeram ligações com menos de um minuto de duração
--no dia 28 de julho de 2021.
SELECT name FROM people
JOIN phone_calls ON phone_calls.caller =  people.phone_number
WHERE year = 2021 AND month = 7 AND day = 28 AND duration < 60;

--Realizei uma consulta na tabela "airports" buscando na coluna de cidades e encontrei
--a cidade para onde o ladrão fugiu,  New York City.
SELECT city FROM airports
WHERE id = (SELECT destination_airport_id FROM flights
WHERE year = 2021 AND month = 7 AND day = 29 AND origin_airport_id = (
SELECT id FROM airports WHERE city = "Fiftyville")
ORDER BY hour, minute
LIMIT 1);


--Sabendo para onde o ladrão fugiu e suspeitando que o ladrão seria o Bruce realizei uma nova consulta na tabela "people"
--Onde o Bruce realizou a ligação, então descobri o número do telefone que ele ligou.
SELECT phone_number FROM people WHERE name = "Bruce";

--E por último realizei uma consulta no nome da pessoa na tabela "people" onde o número do
--telefone fosse igual ao número que o Bruce tinha ligado e cheguei ao nome do Robin.
SELECT name FROM people WHERE phone_number = (
SELECT receiver FROM phone_calls
WHERE year = 2021 AND month = 7 AND day = 28 AND duration < 60 AND caller = "(367) 555-5533");
