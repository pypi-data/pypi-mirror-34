BKM_PUBLIC_KEY = 'MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAuZj/TQ9ZRY5KnsA3HMPqbNwI32J+Bisyv7KX7IRJh5rN5LW3g7t6pulArLIEU3sn28ZQEQ+GCb9yvk6zIUoqKBqH0H+gvxOtsklOUkFRgh+/FghNDoe0OzkXTLjQKhh6MRMBR9l3cws9nA2cu+M5kw67F8j0+4SogHJ+VS1wA2kfWx58PNDIg9DtAVwmD1JbjAziPONv0wHSa8oNgia9Tx6ia6FS4nfjRNqpVqI0m2jIcG8yXt1OaBSazkuRlRepMtDVwMGF4xOWXuRVv+G5oiTsbOez9tQAcx+KH0W1Pn9Q9/zzOJyF9AS8J1UDE7c7rKwXGDnuTBU1BwdAGyB87QIDAQAB'

SSL_VERIFICATION = False

ENV_URLS = {
    'DEV': 'https://bex-api.finartz.com/v1/',
    'LOCAL': 'http://api.bex.dev/v1/',
    'SANDBOX': 'https://test-api.bkmexpress.com.tr/v1/',
    'PREPROD': 'https://preprod-api.bkmexpress.com.tr/v1/',
    'PRODUCTION': 'https://api.bkmexpress.com.tr/v1/'
}

BANK_CODE_MAP = {
    'albaraka': "0203",
    'akbank': "0046",
    'bankasya': "0208",
    'denizbank': "0134",
    'finansbank': "0111",
    'garanti': "0062",
    'halkbank': "0012",
    'hsbc': "0123",
    'isbank': "0064",
    'ingbank': "0099",
    'kuveytturk': "0205",
    'odeabank': "0146",
    'sekerbank': "0059",
    'teb': "0032",
    'tfkb': "0206",
    'vakifbank': "0015",
    'ykb': "0067",
    'ziraat': "0010"
}

VPOS_TEST_CONFS = {
                "0010": {
                    "vposUserId": "bkmtest",
                    "vposPassword": "TEST1691",
                    "extra": {
                        "ClientId": "190001691",
                        "storekey": "TRPS1691",
                        "orderId": "9073194"
                    },
                    "bankIndicator": "0010",
                    "serviceUrl": "http://srvirt01:7200/ziraat",
                    "preAuth": False
                },
                "0012": {
                    "vposUserId": "testapi",
                    "vposPassword": "TEST1234",
                    "extra": {
                        "ClientId": "500020009",
                        "storekey": "Ab123456",
                        "subMerchantName": "MERCHANT-1-AK"
                    },
                    "bankIndicator": "0012",
                    "serviceUrl": "http://srvirt01:7200/halkbank",
                    "preAuth": False
                },
                "0015": {
                    "vposUserId": "000000000011429",
                    "vposPassword": "BKMexpress",
                    "extra": {
                        "posno": "vp000263",
                        "uyeno": "000000000011429",
                        "islemyeri": "I",
                        "uyeref": "917250515"
                    },
                    "bankIndicator": "0015",
                    "serviceUrl": "http://srvirt01:7200/vpos724v3/",
                    "preAuth": False
                },
                "0032": {
                    "vposUserId": "bkmapi",
                    "vposPassword": "KUTU8520",
                    "extra": {
                        "ClientId": "401562930",
                        "storekey": "KUTU8520"
                    },
                    "bankIndicator": "0032",
                    "serviceUrl": "http://srvirt01:7200/teb",
                    "preAuth": False
                },
                "0046": {
                    "vposUserId": "akapi",
                    "vposPassword": "TEST1234",
                    "extra": {
                        "ClientId": "100111222",
                        "storekey": "TEST1234",
                        "subMerchantName": "MERCHANT-1-AK"
                    },
                    "bankIndicator": "0046",
                    "serviceUrl": "http://srvirt01:7200/akbank",
                    "preAuth": False
                },
                "0059": {
                    "vposUserId": "7000679",
                    "vposPassword": "123qweASD",
                    "extra": {
                        "terminalprovuserid": "PROVAUT",
                        "terminalmerchantid": "7000679",
                        "storekey": "12345678",
                        "terminalid": "30691297"
                    },
                    "bankIndicator": "0059",
                    "serviceUrl": "http://srvirt01:7200/VPServlet",
                    "preAuth": False
                },
                "0062": {
                    "vposUserId": "7000679",
                    "vposPassword": "123qweASD",
                    "extra": {
                        "terminalprovuserid": "PROVAUT",
                        "terminalmerchantid": "7000679",
                        "storekey": "12345678",
                        "terminalid": "30691297"
                    },
                    "bankIndicator": "0062",
                    "serviceUrl": "http://srvirt01:7200/VPServlet",
                    "preAuth": False
                },
                "0064": {
                    "vposUserId": "bkmapi",
                    "vposPassword": "KUTU8900",
                    "extra": {
                        "ClientId": "700655047520",
                        "storekey": "TEST123456",
                        "subMerchantName": "MERCHANT-1-AK"
                    },
                    "bankIndicator": "0064",
                    "serviceUrl": "http://srvirt01:7200/isbank",
                    "preAuth": False
                },
                "0067": {
                    "vposUserId": "bkm3d1",
                    "vposPassword": "12345",
                    "extra": {
                        "mid": "6706598320",
                        "tid": "67245089",
                        "posnetID": "4280"
                    },
                    "bankIndicator": "0067",
                    "serviceUrl": "http://srvirt01:7200/PosnetWebService/XML",
                    "preAuth": False
                },
                "0099": {
                    "vposUserId": "7000679",
                    "vposPassword": "123qweASD",
                    "extra": {
                        "terminalprovuserid": "PROVAUT",
                        "terminalmerchantid": "7000679",
                        "storekey": "12345678",
                        "terminalid": "30691297"
                    },
                    "bankIndicator": "0099",
                    "serviceUrl": "http://srvirt01:7200/VPServlet",
                    "preAuth": False
                },
                "0111": {
                    "vposUserId": "bkmapi",
                    "vposPassword": "TEST1234",
                    "extra": {
                        "ClientId": "600000120",
                        "storekey": "TEST1234",
                        "subMerchantName": "MERCHANT-NAME-FINANS",
                        "subMerchantId": "MERCHANT-ID",
                        "subMerchantPostalCode": "34000",
                        "subMerchantCity": "MERCHANT-CITY",
                        "subMerchantCountry": "MERCHANT-COUNTRY"
                    },
                    "bankIndicator": "0111",
                    "serviceUrl": "http://srvirt01:7200/finans",
                    "preAuth": False
                },
                "0123": {
                    "vposUserId": "a",
                    "vposPassword": "TEST1234",
                    "extra": {
                        "ClientId": "0004220"
                    },
                    "bankIndicator": "0123",
                    "serviceUrl": "https://vpostest.advantage.com.tr/servlet/cc5ApiServer",
                    "preAuth": False
                },
                "0134": {
                    "vposUserId": "1",
                    "vposPassword": "12345",
                    "extra": {
                        "ShopCode": "3123",
                        "UserCode": "InterTestApi",
                        "UserPass": "3",
                        "storeKey": "gDg1N"
                    },
                    "bankIndicator": "0134",
                    "serviceUrl": "http://srvirt01:7200/mpi/Default.aspx",
                    "preAuth": False
                },
                "0146": {
                    "vposUserId": "7000679",
                    "vposPassword": "123qweASD",
                    "extra": {
                        "terminalprovuserid": "PROVAUT",
                        "terminalmerchantid": "7000679",
                        "storekey": "12345678",
                        "terminalid": "30691297"
                    },
                    "bankIndicator": "0146",
                    "serviceUrl": "http://srvirt01:7200/VPServlet",
                    "preAuth": False
                },
                "0203": {
                    "vposUserId": "7000679",
                    "vposPassword": "123qweASD",
                    "extra": {
                        "terminalprovuserid": "PROVAUT",
                        "terminalmerchantid": "7000679",
                        "storekey": "12345678",
                        "terminalid": "30691297"
                    },
                    "bankIndicator": "0203",
                    "serviceUrl": "http://srvirt01:7200/VPServlet",
                    "preAuth": False
                },
                "0205": {
                    "vposUserId": "apiuser",
                    "vposPassword": "Api123",
                    "extra": {
                        "MerchantId": "2",
                        "CustomerId": "8736633",
                        "orderId": "852507088"
                    },
                    "bankIndicator": "0205",
                    "serviceUrl": "https://boatest.kuveytturk.com.tr/boa.virtualpos.services/Home/ThreeDModelGate",
                    "preAuth": False
                },
                "0206": {
                    "vposUserId": "",
                    "vposPassword": "",
                    "extra": {
                        "orgNo": "006",
                        "firmNo": "9470335",
                        "termNo": "955434",
                        "merchantKey": "HngvXM22",
                        "orderId": "674451441"
                    },
                    "bankIndicator": "0206",
                    "serviceUrl": "https://testserver1:15443/BKMExpressServices.asmx",
                    "preAuth": False
                },
                "0208": {
                    "vposUserId": "",
                    "vposPassword": "",
                    "extra": {
                        "MerchantId": "006100200140200",
                        "MerchantPassword": "12345678"
                    },
                    "bankIndicator": "208",
                    "serviceUrl": "http://srvirt01:7200/iposnet/sposnet.aspx",
                    "preAuth": False
                }
            }