{
    "rasa_nlu_data": {
      "regex_features":[
        {
          "name": "greet",
          "pattern": "hey[^\\s]*"
        }
      ],
      "entity_synonyms": [
        {
          "value": "Apple",
          "synonyms": ["APPLE", "AAPL"]
        },
        {
          "value": "Google",
          "synonyms": ["GOOGLE", "GOOG"]
        },
        {
          "value": "Facebook",
          "synonyms": ["FACEBOOK", "FB"]
        },
        {
          "value": "Microsoft",
          "synonyms": ["MICROSOFT", "MSFT"]
        },
        {
          "value": "ALIBABA",
          "synonyms": ["alibaba", "Alibaba", "BABA"]
        },
        {
          "value": "Tesla",
          "synonyms": ["TESLA", "TSLA"]
        },
        {
          "value": "BAIDU",
          "synonyms": ["Baidu", "baidu", "BIDU"]
        },
        {
          "value": "Amazon",
          "synonyms": ["AMAZON", "AMZN"]
        },
        {
          "value": "WalMart",
          "synonyms": ["walmat", "WALMAT", "WMT"]
        },
        {
          "value": "AT&T",
          "synonyms": ["T"]
        },
        {
          "value": "Coca-Cola",
          "synonyms": ["coca-cola", "CCE"]
        },
        {
          "value": "Intel",
          "synonyms": ["intel", "INTC"]
        }
      ],
      "common_examples": [
        {
          "text": "hey",
          "intent": "greet",
          "entities": []
        },
        {
          "text": "hey there",
          "intent": "greet",
          "entities": []
        },
        {
          "text": "hello",
          "intent": "greet",
          "entities": []
        },
        {
          "text": "hi",
          "intent": "greet",
          "entities": []
        },
        {
          "text": "What's the opening price of Apple?",
          "intent": "get_open",
          "entities": [
            {
              "start:": 28,
              "end": 33,
              "value": "Apple",
              "entity": "organization"
            }
          ]
        },
        {
          "text": "the opening price of Google",
          "intent": "get_open",
          "entities": [
            {
              "start:":21,
              "end": 27,
              "value": "Google",
              "entity": "organization"
            }
          ]
        },
        {
          "text": "Show me the opening price of Facebook.",
          "intent": "get_open",
          "entities": [
            {
              "start:": 29,
              "end": 37,
              "value": "Facebook",
              "entity": "organization"
            }
          ]
        }
          ]
    }
}