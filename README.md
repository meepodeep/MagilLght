# MagilLght

## A mini spotlight that follows your hand around your desk.

![image](https://github.com/user-attachments/assets/5dbddb67-c66c-4a26-867a-15dece6ae748)

## Why does this exist

I have had a problem for a while now when soldering, where I cant hold a light on the thing im trying to work on while im working on it. This makes it difficult to see smaller components and also makes me waste time trying to find a light. This project is made to solve both of these problems by being always wall mounted like a lamp but also able to pinpoint certain spots where I acctually need light and not take up as much space as a lamp. The lock feature also enables me to take better pictures of projects with accurate lighting.

![image](https://github.com/user-attachments/assets/90190c67-08f9-4226-9453-c525f748d65b)

# How build
1. Solder the wires in the diagram shown
2. ![image](https://github.com/user-attachments/assets/65ba14b9-b966-40db-b354-f1f6e1ff4833)
3. insert the servo into the baseplate and screw it in
4. ![image](https://github.com/user-attachments/assets/fddc5a86-b1a2-4517-86dc-a97fa5c8f571)
5. Screw the rpi 5 into the baseplate with m2.5 screws
6. Route the servo cables above the Ethernet port.
7. ![image](https://github.com/user-attachments/assets/37f5a1ea-404f-41f5-a734-8c18f2a6e56a)
8. Screw the lid on the pi using m3 screws
9. ![image](https://github.com/user-attachments/assets/380aadef-4c64-4055-b0c1-ac8fccaf7c8b)
10. screw the x axis mount onto the servo for the x axis
11. ![image](https://github.com/user-attachments/assets/92251da3-3bff-48bd-8402-33a532ccbda9)
12. Screw the y axis servo into the x axis mount
13. ![image](https://github.com/user-attachments/assets/acae9916-237c-481c-abb3-37c6b25a4433)
14. screw the y axis onto the y axis servo
15. insert the flashlight into the hole and screw in the securing screw
# Software setup
1. Install python 3.12 on the pi
2. Install these packages: numpy, cv2m, and mediapipe.
3. Run the Python script in the code folder.

# BOM


|Item| Quantity | Price | Use | Link|
|----|----------|-------|-----|-----|
|Pi 5 8gb| x1| $90.66 | Run the opencv script and process the images| https://www.adafruit.com/product/5813 |
| type c breakout |x1| $2.67| power the servos through usbc| https://www.aliexpress.us/item/3256808829339214.html?spm=a2g0o.productlist.main.22.4930GWB2GWB2ps&aem_p4p_detail=20250703101441141114911712760001660515&algo_pvid=85a4cea9-4091-4730-b320-862f67157527&algo_exp_id=85a4cea9-4091-4730-b320-862f67157527-19&pdp_ext_f=%7B%22order%22%3A%2230%22%2C%22eval%22%3A%221%22%7D&pdp_npi=4%40dis%21USD%211.32%211.32%21%21%219.39%219.39%21%40210337bc17515628815418898e53ee%2112000047587097902%21sea%21US%214381910819%21X&curPageLogUid=movmMgraFrpv&utparam-url=scene%3Asearch%7Cquery_from%3A&search_p4p_id=20250703101441141114911712760001660515_5|
| servos 14g | x2 |$15.36 | Rotate the light| https://www.aliexpress.us/item/3256807738151389.html?spm=a2g0o.cart.0.0.46bc38dah12Lfn&mp=1&pdp_npi=5%40dis%21USD%21USD%208.16%21USD%207.68%21%21USD%207.68%21%21%21%402101c67a17515650089913422e006b%2112000042865409658%21ct%21US%214381910819%21%212%210&gatewayAdapt=glo2usa |
|Logitech c720 | x1 |owned | be a camera |https://www.amazon.com/Logitech-Desktop-Widescreen-Calling-Recording/dp/B004FHO5Y6?source=ps-sl-shoppingads-lpcontext&ref_=fplfs&psc=1&smid=ATVPDKIKX0DER&gQT=1 | 
|m3 hardware| x4 | owned | screw together the case and secure the light|
|m2.5 hardware | x4 | owned | mount the pi|
|flashlight | x1 | owned | https://www.18650batterystore.com/products/tactical-flashlight-by-18650-battery-store|
| total | | $108.69 | | |
