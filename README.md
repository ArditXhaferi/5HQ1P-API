## Setup

#### Requirements

Install required packages

```
pip install -r requirements.txt
```

#### Folder Structure

The interpreter should be in the parent root of the project aka siblings.

![Folder Structure](example.png "Folder Structure")

## Serve API

This command serves our API

```bash
uvicorn main:app --reload
```

#### Endpoints

**Show User**
----
  Returns the interpretered result of 5HQ1P code.

* **URL**

  /compile-sq

* **Method:**

  `POST`
  
* **Form Params**

  text

* **Success Response:**

  * **Code:** 200 <br />
    **Content:** `[ results ]`

* **Sample Call:**

  ```php

    $client = new http\Client;
    $request = new http\Client\Request;

    $body = new http\Message\Body;
    $body->addForm([
      'text' => '~ Function for Fizzbuzz(kafesheqer) in 5HQ1P

    printo("Pershendetje Bote!")

    per fizzbuzz = 0 deri 51 tani
        nese fizzbuzz % 3 == 0 edhe fizzbuzz % 5 == 0 tani
            printo("fizzbuzz")
            vazhdo

        tjeter fizzbuzz % 3 == 0 tani
            printo("fizz")
            vazhdo

        tjeter fizzbuzz % 5 == 0 tani
            printo("buzz")
            vazhdo
        fund

        printo(fizzbuzz)
    fund'
    ], null);

    $request->setRequestUrl('http://127.0.0.1:8000/compile-sq');
    $request->setRequestMethod('POST');
    $request->setBody($body);

    $client->enqueue($request)->send();
    $response = $client->getResponse();

    echo $response->getBody();
  ```