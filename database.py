import json
products = [
    {
        "id": 1,
        "name": "iPhone 15 Pro Max",
        "category": "phones",
        "price": 129999,
        "original": 144900,
        "rating": 5,
        "image": "https://th.bing.com/th/id/OIP.QQ_AhWpil9Da-IVorp_uegHaJM?w=142&h=180&c=7&r=0&o=7&dpr=1.3&pid=1.7&rm=3",
        "reviews": 247,
        "badge": "New"
    },
    {
        "id": 2,
        "name": "Samsung Galaxy S24 Ultra",
        "category": "phones",
        "price": 79999,
        "original": 89999,
        "rating": 4.6,
        "image": "https://th.bing.com/th/id/OIP.gy7G_wNmqgXpJPJXzjM4OgHaHa?w=188&h=188&c=7&r=0&o=7&dpr=1.3&pid=1.7&rm=3",
        "reviews": 189,
        "badge": "Sale"
    },
    {
        "id": 3,
        "name": "Sony WH-1000XM5",
        "category": "audio",
        "price": 26999,
        "original": 29999,
        "rating": 4.7,
        "image": "https://th.bing.com/th/id/OIP.gaF-Z--s-5gj8a9S1kkbBgHaHa?w=183&h=183&c=7&r=0&o=7&dpr=1.3&pid=1.7&rm=3",
        "reviews": 456,
        "badge": ""
    },
    {
        "id": 4,
        "name": "Apple AirPods Pro 2",
        "category": "audio",
        "price": 24999,
        "original": 26900,
        "rating": 4.5,
        "image": "https://th.bing.com/th/id/OIP.JfiZrRQPI2uxXG2zi0nRCgHaHa?w=183&h=183&c=7&r=0&o=7&dpr=1.3&pid=1.7&rm=3",
        "reviews": 378,
        "badge": "Hot"
    },
    {
        "id": 5,
        "name": "iPad Air M2 11\"",
        "category": "phones",
        "price": 69999,
        "original": 74900,
        "rating": 4.6,
        "image": "https://th.bing.com/th/id/OIP.9A3l5z4gyBr8VZvq4K5gPAHaIN?w=157&h=180&c=7&r=0&o=7&dpr=1.3&pid=1.7&rm=3",
        "reviews": 156,
        "badge": ""
    },
    {
        "id": 6,
        "name": "Logitech MX Master 3S",
        "category": "accessories",
        "price": 8999,
        "original": 10999,
        "rating": 4.4,
        "image": "https://th.bing.com/th/id/OIP.vIt86RX0CxaWYsMcNw5IPwHaGZ?w=272&h=183&c=7&r=0&o=7&dpr=1.3&pid=1.7&rm=3",
        "reviews": 289,
        "badge": "Sale"
    },
    {
        "id": 7,
        "name": "JBL Flip 6",
        "category": "audio",
        "price": 9999,
        "original": 11999,
        "rating": 3,
        "image": "https://th.bing.com/th/id/OIP.zJAAicMrDze_TmT9ysefxgHaHa?w=172&h=180&c=7&r=0&o=7&dpr=1.3&pid=1.7&rm=3",
        "reviews": 423,
        "badge": ""
    },
    {
        "id": 8,
        "name": "HP Victus 15",
        "category": "laptops",
        "price": 65000,
        "original": 72000,
        "rating": 4.2,
        "image": "https://th.bing.com/th/id/OIP.HDWsvwMmLmX-uc0LbX2PzQHaGe?w=221&h=193&c=7&r=0&o=7&dpr=1.3&pid=1.7&rm=3",
        "reviews": 4,
        "badge": ""
    },
    {
        "id": 9,
        "name": "INFINIX GT 20 PRO",
        "category": "phones",
        "price": 23000,
        "original": 25999,
        "rating": 4.1,
        "image": "https://th.bing.com/th/id/OIP._AR94VTNHbuGfh9IWV1lpgHaFp?w=245&h=187&c=7&r=0&o=7&dpr=1.3&pid=1.7&rm=3",
        "reviews": 5031,
        "badge": "Hot"
    },
    {
    "name": "HP AMD Ryzen 7 Octa Core - (16 GB/512 GB SSD/Windows 11 Home) 15-fc0761AU Laptop",
    "price": 61990,
    "rating": 4.0,
    "image": "https://rukminim2.flixcart.com/image/312/312/xif0q/computer/e/t/p/-original-imahhjyugkghz6yp.jpeg?q=70",
    "category": "laptops",
    "original": 61990,
    "reviews": 0,
    "badge": "",
    "id": 1
  },
  {
    "name": "HP AMD Ryzen 5 Quad Core 7520U - (16 GB/512 GB SSD/Windows 11 Home) 15-fc0156AU / 15-fc0690AU Thin and...",
    "price": 50990,
    "rating": 4.1443,
    "image": "https://rukminim2.flixcart.com/image/312/312/xif0q/computer/2/o/d/-original-imahg5fxrynh3hnw.jpeg?q=70",
    "category": "laptops",
    "original": 50990,
    "reviews": 0,
    "badge": "",
    "id": 2
  },
  {
    "name": "ASUS Vivobook Go 15 (2025) with Office 2024 + M365 Basic*, AMD Ryzen 3 Quad Core 7320U - (16 GB/512 GB...",
    "price": 37990,
    "rating": 4.191,
    "image": "https://rukminim2.flixcart.com/image/312/312/xif0q/computer/c/r/7/-original-imagpxgqbu5hmwzs.jpeg?q=70",
    "category": "laptops",
    "original": 37990,
    "reviews": 0,
    "badge": "",
    "id": 3
  },
  {
    "name": "ASUS Vivobook 15, with Backlit Keyboard, Intel Core i3 13th Gen 1315U - (8 GB/512 GB SSD/Windows 11 Ho...",
    "price": 47990,
    "rating": 4.32,
    "image": "https://rukminim2.flixcart.com/image/312/312/xif0q/computer/w/h/g/-original-imahg5fuxuw5afvh.jpeg?q=70",
    "category": "laptops",
    "original": 47990,
    "reviews": 0,
    "badge": "",
    "id": 4
  },
  {
    "name": "ASUS Vivobook 15, with Backlit Keyboard, Intel Core i3 13th Gen 1315U - (16 GB/512 GB SSD/Windows 11 H...",
    "price": 48990,
    "rating": 4.32,
    "image": "https://rukminim2.flixcart.com/image/312/312/xif0q/computer/y/k/g/-original-imahg5fyefftefqt.jpeg?q=70",
    "category": "laptops",
    "original": 48990,
    "reviews": 0,
    "badge": "",
    "id": 5
  },
  {
    "name": "HP 14 AI PC Intel Core Ultra 7 155H - (16 GB/512 GB SSD/Windows 11 Home) 14-ep1151TU/14-gr1036TU/14-ep...",
    "price": 78990,
    "rating": 4.1472,
    "image": "https://rukminim2.flixcart.com/image/312/312/xif0q/computer/o/9/k/-original-imahgry8nwkejmae.jpeg?q=70",
    "category": "laptops",
    "original": 78990,
    "reviews": 0,
    "badge": "",
    "id": 6
  },
  {
    "name": "HP 15 with Backlit Keyboard & Office 2024 AMD Ryzen 7 Octa Core 5825U - (16 GB/512 GB SSD/Windows 11 H...",
    "price": 59644,
    "rating": 4.2363,
    "image": "https://rukminim2.flixcart.com/image/312/312/xif0q/computer/c/j/s/-original-imahk7hhynx2zpdh.jpeg?q=70",
    "category": "laptops",
    "original": 59644,
    "reviews": 0,
    "badge": "",
    "id": 7
  },
  {
    "name": "ASUS Vivobook Go 15 (2025) with Office 2024 + M365 Basic*, Backlit Keyboard, AMD Ryzen 5 Quad Core 752...",
    "price": 48990,
    "rating": 4.21,
    "image": "https://rukminim2.flixcart.com/image/312/312/xif0q/computer/i/m/z/-original-imahgfdfjntmzjkh.jpeg?q=70",
    "category": "laptops",
    "original": 48990,
    "reviews": 0,
    "badge": "",
    "id": 8
  },
  {
    "name": "Lenovo IdeaPad Slim 3 Backlit Keyboard with MSO'2024 Intel Core i5 13th Gen 13420H - (24 GB/1 TB SSD/W...",
    "price": 76990,
    "rating": 4.4133,
    "image": "https://rukminim2.flixcart.com/image/312/312/xif0q/computer/o/a/w/-original-imahb85kfwupn2ay.jpeg?q=70",
    "category": "laptops",
    "original": 76990,
    "reviews": 0,
    "badge": "",
    "id": 9
  },
  {
    "name": "Acer Aspire 3 Intel Pentium Quad Core 12th Gen N100 - (16 GB/512 GB SSD/Windows 11 Home) A324-31 Thin ...",
    "price": 35990,
    "rating": 4.1721,
    "image": "https://rukminim2.flixcart.com/image/312/312/xif0q/computer/e/b/j/-original-imahg82bvd5ffceg.jpeg?q=70",
    "category": "laptops",
    "original": 35990,
    "reviews": 0,
    "badge": "",
    "id": 10
  },
  {
    "name": "HP OmniBook 7 Aero (Previously Pavilion) AMD Ryzen AI 5 Hexa Core AI 5 340 - (16 GB/512 GB SSD/Windows...",
    "price": 76990,
    "rating": 4.262,
    "image": "https://rukminim2.flixcart.com/image/312/312/xif0q/computer/b/i/r/-original-imahj7tqthpvhx7w.jpeg?q=70",
    "category": "laptops",
    "original": 76990,
    "reviews": 0,
    "badge": "",
    "id": 11
  },
  {
    "name": "Lenovo �IdeaPad Slim 5 WUXGA OLED Full Metal Body Intel Core i5 13th Gen 13420H - (16 GB/512 GB SSD/Wi...",
    "price": 69990,
    "rating": 4.49,
    "image": "https://rukminim2.flixcart.com/image/312/312/xif0q/computer/o/v/3/-original-imahfkh32rjbqrhj.jpeg?q=70",
    "category": "laptops",
    "original": 69990,
    "reviews": 0,
    "badge": "",
    "id": 12
  },
  {
    "name": "HP 15 (i3 14th Gen) Intel Core 3 100U - (8 GB/512 GB SSD/Windows 11 Home) 15-fd1253TU/ 15-fd1225TU Thi...",
    "price": 46990,
    "rating": 4.21,
    "image": "https://rukminim2.flixcart.com/image/312/312/xif0q/computer/j/w/o/-original-imahkjjf47u9vgs7.jpeg?q=70",
    "category": "laptops",
    "original": 46990,
    "reviews": 0,
    "badge": "",
    "id": 13
  },
  {
    "name": "ASUS Vivobook Go 15 (2025) with Office 2024 + M365 Basic*, AMD Ryzen 5 Quad Core 7520U - (8 GB/512 GB ...",
    "price": 46990,
    "rating": 4.543,
    "image": "https://rukminim2.flixcart.com/image/312/312/xif0q/computer/i/j/5/-original-imagnzg2rwxffejh.jpeg?q=70",
    "category": "laptops",
    "original": 46990,
    "reviews": 0,
    "badge": "",
    "id": 14
  },
  {
    "name": "Lenovo IdeaPad Slim 3 Backlit Intel Core i5 12th Gen 12450H - (16 GB/512 GB SSD/Windows 11 Home) 15IAH...",
    "price": 54990,
    "rating": 4.21,
    "image": "https://rukminim2.flixcart.com/image/312/312/xif0q/computer/c/c/e/-original-imahg5fytmgbbduv.jpeg?q=70",
    "category": "laptops",
    "original": 54990,
    "reviews": 0,
    "badge": "",
    "id": 15
  },
  {
    "name": "MSI Thin 15 Intel Core i5 13th Gen 13420H - (16 GB/512 GB SSD/Windows 11 Home/4 GB Graphics/NVIDIA GeF...",
    "price": 58990,
    "rating": 4.3104,
    "image": "https://rukminim2.flixcart.com/image/312/312/xif0q/computer/l/s/i/-original-imahg4pq9cq28wq2.jpeg?q=70",
    "category": "laptops",
    "original": 58990,
    "reviews": 0,
    "badge": "",
    "id": 16
  },
  {
    "name": "ASUS Vivobook Go 15 AMD Ryzen 5 Quad Core 7520U - (8 GB/512 GB SSD/Windows 11 Home) E1504FA-NJ133WS | ...",
    "price": 46990,
    "rating": 4.21,
    "image": "https://rukminim2.flixcart.com/image/312/312/xif0q/computer/f/6/r/-original-imahg53uvtcffmvf.jpeg?q=70",
    "category": "laptops",
    "original": 46990,
    "reviews": 0,
    "badge": "",
    "id": 17
  },
  {
    "name": "HP Intel Core i7 13th Gen 13620H - (16 GB/512 GB SSD/Windows 11 Home) 15-fr0046TU Thin and Light Lapto...",
    "price": 72990,
    "rating": 4.3967,
    "image": "https://rukminim2.flixcart.com/image/312/312/xif0q/computer/y/y/x/-original-imahgx8weecatg2f.jpeg?q=70",
    "category": "laptops",
    "original": 72990,
    "reviews": 0,
    "badge": "",
    "id": 18
  },
  {
    "name": "Acer Aspire Lite AMD Ryzen 3 Quad Core 5300U - (8 GB/512 GB SSD/Windows 11 Home) AL15-41 Thin and Ligh...",
    "price": 39990,
    "rating": 4.11,
    "image": "https://rukminim2.flixcart.com/image/312/312/xif0q/computer/b/k/d/-original-imahb2kbf2zdan3z.jpeg?q=70",
    "category": "laptops",
    "original": 39990,
    "reviews": 0,
    "badge": "",
    "id": 19
  },
  {
    "name": "Acer Aspire 3 Backlit AMD Ryzen 7 Octa Core 7730U - (16 GB/512 GB SSD/Windows 11 Home) Aspire AS15 - 4...",
    "price": 49990,
    "rating": 4.11,
    "image": "https://rukminim2.flixcart.com/image/312/312/xif0q/computer/2/q/t/-original-imahg5ftjkmg4m82.jpeg?q=70",
    "category": "laptops",
    "original": 49990,
    "reviews": 0,
    "badge": "",
    "id": 20
  },
  {
    "name": "Ultimus APEX Intel Celeron Dual Core 4mm Thin Bezel 180 Degree Hinge - (8 GB/512 GB SSD/Windows 11 Hom...",
    "price": 24999,
    "rating": 3.5106,
    "image": "https://rukminim2.flixcart.com/image/312/312/xif0q/computer/t/q/a/-original-imahdwj9e5kfcz9q.jpeg?q=70",
    "category": "laptops",
    "original": 24999,
    "reviews": 0,
    "badge": "",
    "id": 21
  },
  {
    "name": "DELL Inspiron 5440 (2026) (i3 14th Gen) Intel Core 3 14th Gen 100U - (8 GB/512 GB SSD/Windows 11 Home)...",
    "price": 40990,
    "rating": 3.831,
    "image": "https://rukminim2.flixcart.com/image/312/312/xif0q/computer/6/8/p/inspiron-5440-thin-and-light-laptop-dell-original-imahjsfmjxbvc7zr.jpeg?q=70",
    "category": "laptops",
    "original": 40990,
    "reviews": 0,
    "badge": "",
    "id": 22
  },
  {
    "name": "ASUS Vivobook Go 15 AMD Ryzen 5 Quad Core 7520U - (16 GB/512 GB SSD/Windows 11 Home) E1504FA-NJ5542WS ...",
    "price": 48990,
    "rating": 4.21,
    "image": "https://rukminim2.flixcart.com/image/312/312/xif0q/computer/f/6/r/-original-imahg53uvtcffmvf.jpeg?q=70",
    "category": "laptops",
    "original": 48990,
    "reviews": 0,
    "badge": "",
    "id": 23
  },
  {
    "name": "Acer Aspire 3 Intel Core i5 13th Gen 1334U - (16 GB/512 GB SSD/Windows 11 Home) A324-53 Thin and Light...",
    "price": 48990,
    "rating": 4.31,
    "image": "https://rukminim2.flixcart.com/image/312/312/xif0q/computer/1/e/v/-original-imahg53ufd4jgtqw.jpeg?q=70",
    "category": "laptops",
    "original": 48990,
    "reviews": 0,
    "badge": "",
    "id": 24
  },
  {
    "name": "MOTOROLA g06 power (Pantone tapestry, 64 GB)",
    "price": 9999,
    "rating": 4.312,
    "image": "https://rukminim2.flixcart.com/image/312/312/xif0q/mobile/u/b/9/-original-imahgctgvmt6kjyn.jpeg?q=70",
    "category": "phones",
    "original": 9999,
    "reviews": 0,
    "badge": "",
    "id": 25
  },
  {
    "name": "Ai+ Pulse 1 (Sparkle Red, 64 GB)",
    "price": 7999,
    "rating": 4.347,
    "image": "https://rukminim2.flixcart.com/image/312/312/xif0q/mobile/m/w/t/-original-imahhc4czn6fswwz.jpeg?q=70",
    "category": "phones",
    "original": 7999,
    "reviews": 0,
    "badge": "",
    "id": 26
  },
  {
    "name": "realme P4 Lite 5G (Mosaic Blue, 64 GB)",
    "price": 13499,
    "rating": 4.5492,
    "image": "https://rukminim2.flixcart.com/image/312/312/xif0q/mobile/b/n/k/-original-imahhngjaj95jctk.jpeg?q=70",
    "category": "phones",
    "original": 13499,
    "reviews": 0,
    "badge": "",
    "id": 27
  },
  {
    "name": "vivo T5x 5G (Cyber Green, 256 GB)",
    "price": 22999,
    "rating": 4.53,
    "image": "https://rukminim2.flixcart.com/image/312/312/xif0q/mobile/f/i/v/-original-imahhhfvqhmf7fgg.jpeg?q=70",
    "category": "phones",
    "original": 22999,
    "reviews": 0,
    "badge": "",
    "id": 28
  },
  {
    "name": "POCO C85 5G (Spring Green, 128 GB)",
    "price": 12999,
    "rating": 4.244,
    "image": "https://rukminim2.flixcart.com/image/312/312/xif0q/mobile/t/h/n/-original-imahgkfunztkbmqg.jpeg?q=70",
    "category": "phones",
    "original": 12999,
    "reviews": 0,
    "badge": "",
    "id": 29
  },
  {
    "name": "POCO C85x (Elite Black, 64 GB)",
    "price": 10999,
    "rating": 4.3204,
    "image": "https://rukminim2.flixcart.com/image/312/312/xif0q/mobile/g/u/c/-original-imahhdvguz822ftz.jpeg?q=70",
    "category": "phones",
    "original": 10999,
    "reviews": 0,
    "badge": "",
    "id": 30
  },
  {
    "name": "vivo T5x 5G (Cyber Green, 128 GB)",
    "price": 18999,
    "rating": 4.63,
    "image": "https://rukminim2.flixcart.com/image/312/312/xif0q/mobile/f/i/v/-original-imahhhfvqhmf7fgg.jpeg?q=70",
    "category": "phones",
    "original": 18999,
    "reviews": 0,
    "badge": "",
    "id": 31
  },
  {
    "name": "Ai+ Pulse 1 (Blue, 64 GB)",
    "price": 7999,
    "rating": 4.347,
    "image": "https://rukminim2.flixcart.com/image/312/312/xif0q/mobile/z/h/v/-original-imahgzhp9vgvyfkg.jpeg?q=70",
    "category": "phones",
    "original": 7999,
    "reviews": 0,
    "badge": "",
    "id": 32
  },
  {
    "name": "vivo T5x 5G (Star Silver, 128 GB)",
    "price": 18999,
    "rating": 4.63,
    "image": "https://rukminim2.flixcart.com/image/312/312/xif0q/mobile/z/m/e/-original-imahhhfv5ffnzjbv.jpeg?q=70",
    "category": "phones",
    "original": 18999,
    "reviews": 0,
    "badge": "",
    "id": 33
  },
  {
    "name": "MOTOROLA g06 power (Pantone Laurel Oak, 64 GB)",
    "price": 9999,
    "rating": 4.312,
    "image": "https://rukminim2.flixcart.com/image/312/312/xif0q/mobile/9/c/g/-original-imahgctgvra6qqwq.jpeg?q=70",
    "category": "phones",
    "original": 9999,
    "reviews": 0,
    "badge": "",
    "id": 34
  },
  {
    "name": "MOTOROLA g57 power 5G (Pantone Regatta, 128 GB)",
    "price": 14999,
    "rating": 4.434,
    "image": "https://rukminim2.flixcart.com/image/312/312/xif0q/mobile/z/u/l/-original-imahhqjwyzsjyfvn.jpeg?q=70",
    "category": "phones",
    "original": 14999,
    "reviews": 0,
    "badge": "",
    "id": 35
  },
  {
    "name": "Samsung M06 5G (Sage Green, 128 GB)",
    "price": 11299,
    "rating": 4.11,
    "image": "https://rukminim2.flixcart.com/image/312/312/xif0q/mobile/n/t/g/-original-imaha58mcdsfygaq.jpeg?q=70",
    "category": "phones",
    "original": 11299,
    "reviews": 0,
    "badge": "",
    "id": 36
  },
  {
    "name": "MOTOROLA g35 5G (Midnight Black, 128 GB)",
    "price": 11999,
    "rating": 4.21,
    "image": "https://rukminim2.flixcart.com/image/312/312/xif0q/mobile/z/q/m/g35-5g-pb3h0000in-motorola-original-imah7c6ykgz5rtgv.jpeg?q=70",
    "category": "phones",
    "original": 11999,
    "reviews": 0,
    "badge": "",
    "id": 37
  },
  {
    "name": "realme P4 Lite (Beach Gold, 64 GB)",
    "price": 9999,
    "rating": 4.41,
    "image": "https://rukminim2.flixcart.com/image/312/312/xif0q/mobile/j/t/n/-original-imahkkjrwzbwgf76.jpeg?q=70",
    "category": "phones",
    "original": 9999,
    "reviews": 0,
    "badge": "",
    "id": 38
  },
  {
    "name": "POCO C85 5G (Power Black, 128 GB)",
    "price": 12999,
    "rating": 4.244,
    "image": "https://rukminim2.flixcart.com/image/312/312/xif0q/mobile/k/b/h/-original-imahgkfukhsghycr.jpeg?q=70",
    "category": "phones",
    "original": 12999,
    "reviews": 0,
    "badge": "",
    "id": 39
  },
  {
    "name": "Ai+ Pulse 2 (Green, 128 GB)",
    "price": 8999,
    "rating": 4.3214,
    "image": "https://rukminim2.flixcart.com/image/312/312/xif0q/mobile/a/z/r/-original-imahh27g6cgsf8z3.jpeg?q=70",
    "category": "phones",
    "original": 8999,
    "reviews": 0,
    "badge": "",
    "id": 40
  },
  {
    "name": "MOTOROLA g57 power 5G (Pantone Fluidity, 128 GB)",
    "price": 14999,
    "rating": 4.434,
    "image": "https://rukminim2.flixcart.com/image/312/312/xif0q/mobile/1/k/r/-original-imahhqjwsngwkksu.jpeg?q=70",
    "category": "phones",
    "original": 14999,
    "reviews": 0,
    "badge": "",
    "id": 41
  },
  {
    "name": "Samsung M06 5G (Blazing Black, 128 GB)",
    "price": 11490,
    "rating": 4.11,
    "image": "https://rukminim2.flixcart.com/image/312/312/xif0q/mobile/h/y/x/-original-imaha58mehzvmk9w.jpeg?q=70",
    "category": "phones",
    "original": 11490,
    "reviews": 0,
    "badge": "",
    "id": 42
  },
  {
    "name": "MOTOROLA g35 5G (Guava Red, 128 GB)",
    "price": 12999,
    "rating": 4.212,
    "image": "https://rukminim2.flixcart.com/image/312/312/xif0q/mobile/o/8/n/-original-imahgjf9sdcnv2kb.jpeg?q=70",
    "category": "phones",
    "original": 12999,
    "reviews": 0,
    "badge": "",
    "id": 43
  },
  {
    "name": "MOTOROLA g35 5G (Leaf Green, 128 GB)",
    "price": 12999,
    "rating": 4.212,
    "image": "https://rukminim2.flixcart.com/image/312/312/xif0q/mobile/0/a/6/-original-imahgjf9phdnsc5b.jpeg?q=70",
    "category": "phones",
    "original": 12999,
    "reviews": 0,
    "badge": "",
    "id": 44
  },
  {
    "name": "realme P4 Lite (Sea Blue, 64 GB)",
    "price": 9999,
    "rating": 4.41,
    "image": "https://rukminim2.flixcart.com/image/312/312/xif0q/mobile/f/s/7/-original-imahkkjrz3qhsxps.jpeg?q=70",
    "category": "phones",
    "original": 9999,
    "reviews": 0,
    "badge": "",
    "id": 45
  },
  {
    "name": "OPPO K13 5G with 7000mAh and 80W SUPERVOOC Charger In-The-Box (Icy Purple, 128 GB)",
    "price": 22999,
    "rating": 4.587,
    "image": "https://rukminim2.flixcart.com/image/312/312/xif0q/mobile/f/k/e/-original-imahbfd4zqn9zazz.jpeg?q=70",
    "category": "phones",
    "original": 22999,
    "reviews": 0,
    "badge": "",
    "id": 46
  },
  {
    "name": "MOTOROLA Edge 60 Fusion 5G (PANTONE Zephyr, 128 GB)",
    "price": 20999,
    "rating": 4.41,
    "image": "https://rukminim2.flixcart.com/image/312/312/xif0q/mobile/4/a/e/-original-imahkcvgkwzd7u6p.jpeg?q=70",
    "category": "phones",
    "original": 20999,
    "reviews": 0,
    "badge": "",
    "id": 47
  },
  {
    "name": "vivo T4 Lite 5G Charger in the Box (Prism Blue, 64 GB)",
    "price": 12999,
    "rating": 4.45,
    "image": "https://rukminim2.flixcart.com/image/312/312/xif0q/mobile/a/a/x/-original-imahfkvfhcddfzvh.jpeg?q=70",
    "category": "phones",
    "original": 12999,
    "reviews": 0,
    "badge": "",
    "id": 48
  },
  {
    "name": "realme Narzo 80 Lite 5G (Onyx Black, 128 GB)",
    "price": 13279,
    "rating": 4.31,
    "image": "https://rukminim2.flixcart.com/image/312/312/xif0q/mobile/m/l/w/-original-imahgkgxmmzhxgzd.jpeg?q=70",
    "category": "phones",
    "original": 13279,
    "reviews": 0,
    "badge": "",
    "id": 52
  },
  {
    "name": "realme Narzo 80 Lite 4G (Beach Gold, 128 GB)",
    "price": 10999,
    "rating": 4.32,
    "image": "https://rukminim2.flixcart.com/image/312/312/xif0q/mobile/s/p/t/-original-imahgkgxmhadh95w.jpeg?q=70",
    "category": "phones",
    "original": 10999,
    "reviews": 0,
    "badge": "",
    "id": 53
  },
  {
    "name": "realme P4x 5G (Matte Silver, 128 GB)",
    "price": 17499,
    "rating": 4.49,
    "image": "https://rukminim2.flixcart.com/image/312/312/xif0q/mobile/v/z/7/-original-imahhmksfzcpkyky.jpeg?q=70",
    "category": "phones",
    "original": 17499,
    "reviews": 0,
    "badge": "",
    "id": 55
  },
  {
    "name": "realme P4 5G (Engine Blue, 128 GB)",
    "price": 19999,
    "rating": 4.422,
    "image": "https://rukminim2.flixcart.com/image/312/312/xif0q/mobile/r/4/p/-original-imahf47e6gzt3ggw.jpeg?q=70",
    "category": "phones",
    "original": 19999,
    "reviews": 0,
    "badge": "",
    "id": 56
  },
  {
    "name": "realme P3 Lite 5G (Onyx Black, 128 GB)",
    "price": 12999,
    "rating": 4.313,
    "image": "https://rukminim2.flixcart.com/image/312/312/xif0q/mobile/f/m/3/-original-imahjhasq75sat3h.jpeg?q=70",
    "category": "phones",
    "original": 12999,
    "reviews": 0,
    "badge": "",
    "id": 57
  },
  {
    "name": "realme P3 Lite 5G Charger in the Box (Lily White, 128 GB)",
    "price": 12999,
    "rating": 4.313,
    "image": "https://rukminim2.flixcart.com/image/312/312/xif0q/mobile/g/o/v/-original-imahfsgvr6fvsczs.jpeg?q=70",
    "category": "phones",
    "original": 12999,
    "reviews": 0,
    "badge": "",
    "id": 58
  },
  {
    "name": "realme Narzo 80 Lite 5G (Crystal Purple, 128 GB)",
    "price": 13321,
    "rating": 4.31,
    "image": "https://rukminim2.flixcart.com/image/312/312/xif0q/mobile/x/z/x/-original-imahgkgx3y8b4e6j.jpeg?q=70",
    "category": "phones",
    "original": 13321,
    "reviews": 0,
    "badge": "",
    "id": 60
  },
  {
    "name": "realme 16 Pro+ 5G (Master Grey, 256 GB)",
    "price": 45999,
    "rating": 4.5998,
    "image": "https://rukminim2.flixcart.com/image/312/312/xif0q/mobile/6/a/m/-original-imahj8yhhpt2aytf.jpeg?q=70",
    "category": "phones",
    "original": 45999,
    "reviews": 0,
    "badge": "",
    "id": 61
  },
  {
    "name": "realme C61 (Marble Black, 64 GB)",
    "price": 7249,
    "rating": 4.346,
    "image": "https://rukminim2.flixcart.com/image/312/312/xif0q/mobile/x/v/z/-original-imah28xpzzwz4fwg.jpeg?q=70",
    "category": "phones",
    "original": 7249,
    "reviews": 0,
    "badge": "",
    "id": 62
  },
  {
    "name": "realme P4 Lite 5G (Mosaic Blue, 128 GB)",
    "price": 16499,
    "rating": 4.7232,
    "image": "https://rukminim2.flixcart.com/image/312/312/xif0q/mobile/b/n/k/-original-imahhngjaj95jctk.jpeg?q=70",
    "category": "phones",
    "original": 16499,
    "reviews": 0,
    "badge": "",
    "id": 63
  },
  {
    "name": "realme 14 Pro+ 5G (Suede Grey, 256 GB)",
    "price": 25999,
    "rating": 4.421,
    "image": "https://rukminim2.flixcart.com/image/312/312/xif0q/mobile/1/o/t/-original-imahewbae6vyfvxz.jpeg?q=70",
    "category": "phones",
    "original": 25999,
    "reviews": 0,
    "badge": "",
    "id": 64
  },
  {
    "name": "realme P4 Power 5G (TransOrange, 256 GB)",
    "price": 28999,
    "rating": 4.53,
    "image": "https://rukminim2.flixcart.com/image/312/312/xif0q/mobile/m/c/l/-original-imahjzf6fu6bddkb.jpeg?q=70",
    "category": "phones",
    "original": 28999,
    "reviews": 0,
    "badge": "",
    "id": 65
  },
  {
    "name": "realme P3 Lite 5G Charger in the Box (Midnight Lily, 128 GB)",
    "price": 12999,
    "rating": 4.313,
    "image": "https://rukminim2.flixcart.com/image/312/312/xif0q/mobile/a/f/t/-original-imahfsgv98qsukvz.jpeg?q=70",
    "category": "phones",
    "original": 12999,
    "reviews": 0,
    "badge": "",
    "id": 66
  },
  {
    "name": "realme P3x 5G (Stellar Pink, 128 GB)",
    "price": 12999,
    "rating": 4.476,
    "image": "https://rukminim2.flixcart.com/image/312/312/xif0q/mobile/5/v/y/-original-imah9gtmsuutundb.jpeg?q=70",
    "category": "phones",
    "original": 12999,
    "reviews": 0,
    "badge": "",
    "id": 67
  },
  {
    "name": "realme P4x 5G (Elegant Pink, 128 GB)",
    "price": 18499,
    "rating": 4.43,
    "image": "https://rukminim2.flixcart.com/image/312/312/xif0q/mobile/6/r/a/-original-imahhmksypgekqhv.jpeg?q=70",
    "category": "phones",
    "original": 18499,
    "reviews": 0,
    "badge": "",
    "id": 68
  },
  {
    "name": "realme P4 Lite (Sea Blue, 128 GB)",
    "price": 10999,
    "rating": 4.41,
    "image": "https://rukminim2.flixcart.com/image/312/312/xif0q/mobile/f/s/7/-original-imahkkjrz3qhsxps.jpeg?q=70",
    "category": "phones",
    "original": 10999,
    "reviews": 0,
    "badge": "",
    "id": 69
  },
  {
    "name": "realme P4x 5G (Lake Green, 256 GB)",
    "price": 20499,
    "rating": 4.43,
    "image": "https://rukminim2.flixcart.com/image/312/312/xif0q/mobile/u/j/a/-original-imahhmksbeeumyau.jpeg?q=70",
    "category": "phones",
    "original": 20499,
    "reviews": 0,
    "badge": "",
    "id": 70
  },
  {
    "name": "realme P3 Ultra 5G (Neptune Blue, 128 GB)",
    "price": 25999,
    "rating": 4.421,
    "image": "https://rukminim2.flixcart.com/image/312/312/xif0q/mobile/1/q/x/-original-imahhua25wpbb9nf.jpeg?q=70",
    "category": "phones",
    "original": 25999,
    "reviews": 0,
    "badge": "",
    "id": 71
  },
  {
    "name": "realme Gt 7 (Icesense Blue, 256 GB)",
    "price": 36999,
    "rating": 4.4591,
    "image": "https://rukminim2.flixcart.com/image/312/312/xif0q/mobile/8/l/f/-original-imahjrpe4r7cfwu3.jpeg?q=70",
    "category": "phones",
    "original": 36999,
    "reviews": 0,
    "badge": "",
    "id": 72
  },
  {
    "name": "boAt Rockerz 450 Bluetooth Headphone",
    "price": 1299,
    "rating": 4.1,
    "image": "https://th.bing.com/th/id/OIP.Iz2sx0jtTFFo08qJe45WNgHaH0?w=185&h=195&c=7&r=0&o=7&dpr=1.3&pid=1.7&rm=3",
    "category": "audio",
    "original": 2990,
    "reviews": 52000,
    "badge": "Sale",
    "id": 201
  },
  {
  "id": 202,
  "name": "Sony WH-CH520 Wireless Headphone",
  "category": "audio",
  "price": 3490,
  "original": 5990,
  "rating": 4.3,
  "reviews": 12000,
  "badge": "Sale",
  "image": "https://th.bing.com/th/id/OIP.44ciNE8XxJXm84XpFy4NggHaLd?w=129&h=200&c=7&r=0&o=7&dpr=1.3&pid=1.7&rm=3"
  },
  {
  "id": 203,
  "name": "Logitech G102 Gaming Mouse",
  "category": "accessories",
  "price": 1495,
  "original": 2495,
  "rating": 4.4,
  "reviews": 35000,
  "badge": "Sale",
  "image": "https://th.bing.com/th/id/OIP.PhbUQYIkv5se0nQr9DKDWAHaHa?w=177&h=180&c=7&r=0&o=7&dpr=1.3&pid=1.7&rm=3"
  },
  {
  "id": 204,
  "name": "Cosmic Byte CB-GK-25 Mechanical Keyboard",
  "category": "accessories",
  "price": 2299,
  "original": 3999,
  "rating": 4.2,
  "reviews": 8900,
  "badge": "",
  "image": "https://th.bing.com/th/id/OIP.CEYn4_fJLr5vSD8P8Ld74wHaC_?w=317&h=141&c=7&r=0&o=7&dpr=1.3&pid=1.7&rm=3"
  },
  {
  "id": 205,
  "name": "boAt Airdopes 141 TWS Earbuds",
  "category": "audio",
  "price": 999,
  "original": 2990,
  "rating": 4.0,
  "reviews": 98000,
  "badge": "Hot",
  "image": "https://th.bing.com/th/id/OIP.uMky5HH9Dq6smht3ZlL3qgHaHS?w=199&h=195&c=7&r=0&o=7&dpr=1.3&pid=1.7&rm=3"
  },
  {
  "id": 206,
  "name": "Samsung Galaxy Watch 6",
  "category": "accessories",
  "price": 18999,
  "original": 26999,
  "rating": 4.5,
  "reviews": 5600,
  "badge": "Sale",
  "image": "https://th.bing.com/th/id/OIP.T3j9bagPmorFAF84-LykzgHaEK?w=331&h=186&c=7&r=0&o=7&dpr=1.3&pid=1.7&rm=3"
  }
]




# JSON se scraped products load karo
try:
    with open("flipkart_data.json", "r", encoding="utf-8") as f:
        scraped_products = json.load(f)

    for i, p in enumerate(scraped_products):
        p["id"] = 100 + i
        p["category"] = "audio"
        p["reviews"] = int(p.get("reviews", 0))
        p["badge"] = ""
        p["rating"] = float(p.get("rating", 4.0)) if p.get("rating") != "N/A" else 4.0
        p["price"] = int(str(p["price"]).replace("₹", "").replace(",", "")) if p.get("price") != "N/A" else 0
        p["original"] = p["price"]

    products.extend(scraped_products)
    print(f"✅ {len(scraped_products)} scraped products loaded!")
except Exception as e:
    print(f"⚠️ Scraped data load nahi hua: {e}")
