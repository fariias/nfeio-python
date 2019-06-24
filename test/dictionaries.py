SERVICE_INVOICE_JSON = {
  "borrower": {
    "type": "Undefined",
    "name": "string",
    "federalTaxNumber": 0,
    "municipalTaxNumber": "string",
    "email": "junior@unhideschool.com",
    "address": {
      "country": "BRA",
      "postalCode": "59570000",
      "street": "Rua Orlando Max",
      "number": "273",
      "additionalInformation": "string",
      "district": "string",
      "city": {
        "code": "2402600",
        "name": "Ceará-Mirim"
      },
      "state": "RN"
    }
  },
  "cityServiceCode": "08.02.01",
  "federalServiceCode": "08.02",
  "cnaeCode": "85.92-9-99",
  "description": "string",
  "servicesAmount": 50,
  "rpsSerialNumber": "string",
  "issuedOn": "2019-06-12T16:57:21.147Z",
  "taxationType": "None",
  "issRate": 0,
  "issTaxAmount": 0,
  "deductionsAmount": 0,
  "discountUnconditionedAmount": 0,
  "discountConditionedAmount": 0,
  "irAmountWithheld": 0,
  "pisAmountWithheld": 0,
  "cofinsAmountWithheld": 0,
  "csllAmountWithheld": 0,
  "inssAmountWithheld": 0,
  "issAmountWithheld": 0,
  "othersAmountWithheld": 0,
  "approximateTax": {
    "source": "string",
    "version": "string",
    "totalRate": 0
  },
  "additionalInformation": "string"
}

PRODUCT_INVOICE_JSON = {
    "buyer": {
        "name": "teste",
        "address": {
            "city": {
                "code": "3550308",
                "name": "jundiai"
            },
            "state": "SP",
            "district": "centro",
            "street": "rua petronilha antunes",
            "postalCode": "13207760",
            "number": "204",
            "country": "BRA"
        },
        "federalTaxNumber": 8662968678
    },
    "items": [{
        "code": "2617",
        "unitAmount": 9.98,
        "quantity": 5,
        "cfop": 5102,
        "ncm": "47079000",
        "codeGTIN": "SEM GTIN",
        "codeTaxGTIN": "SEM GTIN",
        "tax": {
            "totalTax": 6,
            "icms": {
                "amount": 6,
                "rate": 18,
                "baseTax": 33.25,
                "baseTaxSTReduction": "33.33",
                "baseTaxModality": "3",
                "cst": "20",
                "origin": "0"
            },
            "pis": {
                "amount": 0,
                "rate": 0,
                "baseTax": 0,
                "cst": "06"
            },
            "cofins": {
                "amount": 0,
                "rate": 0,
                "baseTax": 0,
                "cst": "06"
            }
        },
        "cest": "",
        "description": "FEIJAO BOLINHA CAMIL 500G NF ENTRADA 1030099 14\/05\/2018"
    }]
}
