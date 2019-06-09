# rtfm_backend

API:

* IN: ip:port/api/transact  POST Payment OUT: 200 OK, 403(forbidden) - No Money

* IN: ip:port/api/recent_payments GET RecentPaymentRequest OUT: 200 OK RecentPaymentResponce  

* IN: ip:port/api/open_session GET {'driver_id'=id of driver, 'transport_id' = id of transport} OUT: 200 OK, {'session_id': id of opened session}

* IN ip:port/api/close_session GET {'session_id'=id of sessition to be closed} OUT: 200 OK

* IN ip:port/api/valid_list GET OUT: 200 OK, ClientValidationList model 

* IN ip:port/api/user_info POST UserInfoRequest OUT: 200 OK, UserInfoResponce

* IN ip:port/api/price POST GetPriceRequest OUT: 200 OK, GetPriceResponce

* IN ip:port/api/sync_transactions POST TransactionSyncRequest OUT: 200 OK

* IN ip:port/api/refil POST RefilRequest OUT: 200 OK

