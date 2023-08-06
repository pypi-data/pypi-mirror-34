![pyRKO](https://raw.githubusercontent.com/Quantumke/files/master/pyRKO.png)

*The more time you spend contemplating what you should have done... you lose valuable time planning what you can and will do.- lil wayne*
## MPESAWRAPPER 

##### VERSION 2.0

##### THE UNOFFICIAL MPESA API 

This Library Covers

1. B2C
2. B2B
3. C2B

###### INSTALLATION

``pip install mpesawrapper``


after installation

go to the root of your project 

cd /your-path/
touch .env

paste and fill the following 

======================================
```ini
consumer_key=

b2cInitiatorName=

b2cShortcode=

b2cTimeoutUrl=

b2cResultUrl=

b2bInitiator=

b2bShortcode=

b2bTimeoutURL=

b2bResultURL=

MEShortcode=

MECallBackURL=

MEpasskey=

reversalInitiator=

reversalinit_password=

reverseShortcode=

reversResultURL=

reverseQueueTimeOutURL=

sqInitiator=

sqResultURL=

sqQueueTimeOutURL=

sqinit_password=
```

######  NOTE sq stands for status query
######  NOTE ME stands for mpesa express


======================================

`mpesa requires a valid public key certificate get this from mpesa portal, save it as pubkey.pem in the root directory of your project`
### B2C
This api facillitates business sending money directly to it's customers,
This maybe termed as a *withdrawal*

```python
from  mpesawrapper import B2CHandler
B2CHandler().handle(amount=10,mobile_number='2547********')
```

### B2B

This api facillitates business sending  money to other busineses

```python
from mpesawrapper import B2bHandler
B2bHandler().handle(amount=10,
command='',senderType='',recieverType='',recipient='')
```
NOTES:
##### command
BusinessPayBill

BusinessBuyGoods

DisburseFundsToBusiness

BusinessToBusinessTransfer

BusinessTransferFromMMFToUtility

BusinessTransferFromUtilityToMMF

MerchantToMerchantTransfer

MerchantTransferFromMerchantToWorking

MerchantServicesMMFAccountTransfer

AgencyFloatAdvance

##### senderType

use 2 for Till Number

use 4 for Organization short code

#### recieverType

use 2 for Till Number

use 4 for Organization short code

#### recipient

This is the shortcode/till number recieving the funds

### C2B
This works as a notification method for payments made to a shortcode via ussd
One has to register urls with mpesa for this to work

```python
from mpesawrapper import c2bHandler
c2bHandler().handler(ShortCode='',ConfirmationURL='',ValidationURL='')
```

### LIPA NA MPESA
1. Make transaction

```python
from  mpesawrapper import MpesaExpressHandler
MpesaExpressHandler().handle(mobile_number='2547********',amount=10)
```

2. Query Transaction Status

The result of the above will give *CheckoutRequestID* in the response object
this will fill CheckoutRequestID in the request below

```python
from  mpesawrapper import  MpesaExpressQueryHandler
MpesaExpressQueryHandler().handle(CheckoutRequestID='')
```

### Reversals

```python
from  mpesawrapper import reversalHandler
reversalHandler().handle(amount=10,remarks='',mpesaTransactionID='')
```

### Status Query

```python
from mpesawrapper import statusQueryHandler
statusQueryHandler().handle(mpesaTransactionID='',initiator='')
```
initiator is what platform the transaction happened

use 1 for  MSISDN

use 2 for  Till Number

use 4 for  Organization short code