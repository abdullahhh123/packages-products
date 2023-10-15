# packages-products
APIs that contain [ USER , PACKAGES , SUBSCRIPTION ]

ENDPOINTS --  [ 'api/packages' ,'api/packages/<str:pk>/'  ,  'api/package/post' , 'make-order' , 'register' , 'login' , 'user' , 'logout']

'api/packages' 		 	--- SHOWS ALL PACKAGES
'api/packages/<str:pk>/'  	--- SHOWS A PACKAGE SEARCHING BY A NAME
'api/package/post'  		--- CREATING A NEW PACKAGE
'make-order'			--- CREATING AN ORDER [ SUBSCRIPTION ]  


TABLES : 	[  PACKAGE , SUBSCRIPTION , USER ]

PACKAGE 	FIELDs ---- 	product_price , product_name 
SUBSCRIPTION    FIELDs ----	package_ids , user_id 


DATABASE USER ------ POSTGRES 

