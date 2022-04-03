# Projekt-2021---chatbot
## Przegląd dostępnych darmowych rozwiązań dla ChatBota w języku polskim:
* Amazon AWS/LEX - brak obsługi języka polskiego ( darmowy przez pierwsze 12 miesięcy użytkowania).
* Rasa - darmowy - działa na podstawie historyjek - można sameodzielnie wytrenować chatbot w dowolnym języku, można go uruchomić z terminala - udało 
się uruchomić podstawową wersję w terminalu..
* https://botpress.com/blog/open-source-chatbots
* Microsoft Bot Framework - Luis (przetwarzanie języka naturalnego jest opatentowane).
* Botkit - darmowy, jeżeli połączony z innym silnikiem przetwarzającym NL niż Luis.
* Botpress - opensource i wspiera język polski.
* Wit.ai - podobno trudny w wytrenowaniu.
* Pozostałe rozwiązania ze strony są licencjonowane.
## Analiza narzędzia Rasa.
1. Instalacja i uruchomienie rozwiązania Rasa w terminalu.
* Otworzenie chatbota Rasa w terminalu jest szybkie i łatwe. Wraz z instalacją pobierane są przykładowe, podstawowe pliki służące do pierwszego 
przetrenowania modelu i testowania działania programu.
2. Analiza sposobu działania  
   
Dwa podstawowe komponenty:  
  
* Silnik NLU (rozumienia języka naturalnego) - jego zadaniem jest zrozumienie wypowiedzi użytkownika oraz przyporządkowanie jej do konkretnej "intent" (intencji). 
* Główny algorytm - narzędzie oparte na uczeniu maszynowym wraz z uczeniem wzmacnianym, prawdopodobieństwie oraz sieciach neuronowych stara się przewidzieć kolejną,
najlepiej dopasowaną reakcję na otrzymaną wypowiedź.  
  
Ważne pliki wykorzystywane w procesie:  
  
*nlu.yml - zawiera przykładowe wypowiedzi przyporządkowane do konkretnych intencji.  
*stories.yml - zawiera historyjki - schematy wypowiedzi obrazujące w jaki sposób odpowie chatbot dla wypowiedzi lub sekwencji wypowiedzi zgodnej/ych z daną historyjką.   
*domain.yml - zawiera możliwe intencje użytkownika oraz kategorie reakcji chatbota wraz z wypowiedzami przyporządkowanymi do kategorii.  
  
Źródła: https://www.geeksforgeeks.org/chatbots-using-python-and-rasa/, https://rasa.com/  
  
4. Uruchomienie narzędzia na stronie z wykorzystaniem Django.  
   
Mimo, że Rasa posiada swój kanał na YouTube z kursami obsługi swojego produktu, uruchomienie narzędzia na stronie internetowej sprawia problemy.
Podczas realizacji kolejnych kroków często pojawiają się trudności oraz niezgodności nie omawiane w filmikach edukacyjnych. Uczeń musi poradzić sobie z nimi samodzielnie. 
Uważam, że narzędzie Rasa nie jest przeznaczone dla użytkowników nieposiadających umiejętności korzystania z konsoli terminala.  
  
5. Przetestowanie działania Rasa dla języka polskiego.
