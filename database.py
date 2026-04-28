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
        "id": 10,
        "name": "HP AMD Ryzen 7 Octa Core Laptop",
        "category": "laptops",
        "price": 61990,
        "original": 61990,
        "rating": 4.0,
        "image": "https://rukminim2.flixcart.com/image/312/312/xif0q/computer/e/t/p/-original-imahhjyugkghz6yp.jpeg?q=70",
        "reviews": 0,
        "badge": ""
    },
    {
        "id": 11,
        "name": "HP AMD Ryzen 5 Quad Core Laptop",
        "category": "laptops",
        "price": 50990,
        "original": 50990,
        "rating": 4.1,
        "image": "https://rukminim2.flixcart.com/image/312/312/xif0q/computer/2/o/d/-original-imahg5fxrynh3hnw.jpeg?q=70",
        "reviews": 0,
        "badge": ""
    },
    {
        "id": 12,
        "name": "ASUS Vivobook Go 15 Ryzen 3",
        "category": "laptops",
        "price": 37990,
        "original": 37990,
        "rating": 4.2,
        "image": "https://rukminim2.flixcart.com/image/312/312/xif0q/computer/c/r/7/-original-imagpxgqbu5hmwzs.jpeg?q=70",
        "reviews": 0,
        "badge": ""
    },
    {
        "id": 13,
        "name": "ASUS Vivobook 15 Core i3 8GB",
        "category": "laptops",
        "price": 47990,
        "original": 47990,
        "rating": 4.3,
        "image": "https://rukminim2.flixcart.com/image/312/312/xif0q/computer/w/h/g/-original-imahg5fuxuw5afvh.jpeg?q=70",
        "reviews": 0,
        "badge": ""
    },
    {
        "id": 14,
        "name": "ASUS Vivobook 15 Core i3 16GB",
        "category": "laptops",
        "price": 48990,
        "original": 48990,
        "rating": 4.3,
        "image": "https://rukminim2.flixcart.com/image/312/312/xif0q/computer/y/k/g/-original-imahg5fyefftefqt.jpeg?q=70",
        "reviews": 0,
        "badge": ""
    },
    {
        "id": 15,
        "name": "HP 14 AI PC Intel Core Ultra 7",
        "category": "laptops",
        "price": 78990,
        "original": 78990,
        "rating": 4.1,
        "image": "https://rukminim2.flixcart.com/image/312/312/xif0q/computer/o/9/k/-original-imahgry8nwkejmae.jpeg?q=70",
        "reviews": 0,
        "badge": ""
    },
    {
        "id": 16,
        "name": "HP 15 Ryzen 7 with Office 2024",
        "category": "laptops",
        "price": 59644,
        "original": 59644,
        "rating": 4.2,
        "image": "https://rukminim2.flixcart.com/image/312/312/xif0q/computer/c/j/s/-original-imahk7hhynx2zpdh.jpeg?q=70",
        "reviews": 0,
        "badge": ""
    },
    {
        "id": 17,
        "name": "ASUS Vivobook Go 15 Ryzen 5",
        "category": "laptops",
        "price": 48990,
        "original": 48990,
        "rating": 4.2,
        "image": "https://rukminim2.flixcart.com/image/312/312/xif0q/computer/i/m/z/-original-imahgfdfjntmzjkh.jpeg?q=70",
        "reviews": 0,
        "badge": ""
    },
    {
        "id": 18,
        "name": "Lenovo IdeaPad Slim 3 Core i5",
        "category": "laptops",
        "price": 76990,
        "original": 76990,
        "rating": 4.4,
        "image": "https://rukminim2.flixcart.com/image/312/312/xif0q/computer/o/a/w/-original-imahb85kfwupn2ay.jpeg?q=70",
        "reviews": 0,
        "badge": ""
    },
    {
        "id": 19,
        "name": "Acer Aspire 3 Pentium N100",
        "category": "laptops",
        "price": 35990,
        "original": 35990,
        "rating": 4.2,
        "image": "https://rukminim2.flixcart.com/image/312/312/xif0q/computer/e/b/j/-original-imahg82bvd5ffceg.jpeg?q=70",
        "reviews": 0,
        "badge": ""
    },
    {
        "id": 20,
        "name": "HP OmniBook 7 Aero Ryzen AI 5",
        "category": "laptops",
        "price": 76990,
        "original": 76990,
        "rating": 4.3,
        "image": "https://rukminim2.flixcart.com/image/312/312/xif0q/computer/b/i/r/-original-imahj7tqthpvhx7w.jpeg?q=70",
        "reviews": 0,
        "badge": ""
    },
    {
        "id": 21,
        "name": "Lenovo IdeaPad Slim 5 OLED Core i5",
        "category": "laptops",
        "price": 69990,
        "original": 69990,
        "rating": 4.5,
        "image": "https://rukminim2.flixcart.com/image/312/312/xif0q/computer/o/v/3/-original-imahfkh32rjbqrhj.jpeg?q=70",
        "reviews": 0,
        "badge": ""
    },
    {
        "id": 22,
        "name": "HP 15 Core i3 14th Gen",
        "category": "laptops",
        "price": 46990,
        "original": 46990,
        "rating": 4.2,
        "image": "https://rukminim2.flixcart.com/image/312/312/xif0q/computer/j/w/o/-original-imahkjjf47u9vgs7.jpeg?q=70",
        "reviews": 0,
        "badge": ""
    },
    {
        "id": 23,
        "name": "ASUS Vivobook Go 15 Ryzen 5 8GB",
        "category": "laptops",
        "price": 46990,
        "original": 46990,
        "rating": 4.5,
        "image": "https://rukminim2.flixcart.com/image/312/312/xif0q/computer/i/j/5/-original-imagnzg2rwxffejh.jpeg?q=70",
        "reviews": 0,
        "badge": ""
    },
    {
        "id": 24,
        "name": "Lenovo IdeaPad Slim 3 Core i5 12th Gen",
        "category": "laptops",
        "price": 54990,
        "original": 54990,
        "rating": 4.2,
        "image": "https://rukminim2.flixcart.com/image/312/312/xif0q/computer/c/c/e/-original-imahg5fytmgbbduv.jpeg?q=70",
        "reviews": 0,
        "badge": ""
    },
    {
        "id": 25,
        "name": "MSI Thin 15 Core i5 NVIDIA",
        "category": "laptops",
        "price": 58990,
        "original": 58990,
        "rating": 4.3,
        "image": "https://rukminim2.flixcart.com/image/312/312/xif0q/computer/l/s/i/-original-imahg4pq9cq28wq2.jpeg?q=70",
        "reviews": 0,
        "badge": ""
    },
    {
        "id": 26,
        "name": "Acer Aspire Lite Ryzen 3",
        "category": "laptops",
        "price": 39990,
        "original": 39990,
        "rating": 4.1,
        "image": "https://rukminim2.flixcart.com/image/312/312/xif0q/computer/b/k/d/-original-imahb2kbf2zdan3z.jpeg?q=70",
        "reviews": 0,
        "badge": ""
    },
    {
        "id": 27,
        "name": "Acer Aspire 3 Ryzen 7",
        "category": "laptops",
        "price": 49990,
        "original": 49990,
        "rating": 4.1,
        "image": "https://rukminim2.flixcart.com/image/312/312/xif0q/computer/2/q/t/-original-imahg5ftjkmg4m82.jpeg?q=70",
        "reviews": 0,
        "badge": ""
    },
    {
        "id": 28,
        "name": "Ultimus APEX Intel Celeron",
        "category": "laptops",
        "price": 24999,
        "original": 24999,
        "rating": 3.5,
        "image": "https://rukminim2.flixcart.com/image/312/312/xif0q/computer/t/q/a/-original-imahdwj9e5kfcz9q.jpeg?q=70",
        "reviews": 0,
        "badge": ""
    },
    {
        "id": 29,
        "name": "DELL Inspiron 5440 Core i3 14th Gen",
        "category": "laptops",
        "price": 40990,
        "original": 40990,
        "rating": 3.8,
        "image": "https://rukminim2.flixcart.com/image/312/312/xif0q/computer/6/8/p/inspiron-5440-thin-and-light-laptop-dell-original-imahjsfmjxbvc7zr.jpeg?q=70",
        "reviews": 0,
        "badge": ""
    },
    {
        "id": 30,
        "name": "Acer Aspire 3 Core i5 13th Gen",
        "category": "laptops",
        "price": 48990,
        "original": 48990,
        "rating": 4.3,
        "image": "https://rukminim2.flixcart.com/image/312/312/xif0q/computer/1/e/v/-original-imahg53ufd4jgtqw.jpeg?q=70",
        "reviews": 0,
        "badge": ""
    },
    {
        "id": 31,
        "name": "HP Intel Core i7 13th Gen",
        "category": "laptops",
        "price": 72990,
        "original": 72990,
        "rating": 4.4,
        "image": "https://rukminim2.flixcart.com/image/312/312/xif0q/computer/y/y/x/-original-imahgx8weecatg2f.jpeg?q=70",
        "reviews": 0,
        "badge": ""
    },
    {
        "id": 50,
        "name": "MOTOROLA g06 power",
        "category": "phones",
        "price": 9999,
        "original": 9999,
        "rating": 4.3,
        "image": "https://rukminim2.flixcart.com/image/312/312/xif0q/mobile/u/b/9/-original-imahgctgvmt6kjyn.jpeg?q=70",
        "reviews": 0,
        "badge": ""
    },
    {
        "id": 51,
        "name": "realme P4 Lite 5G 64GB",
        "category": "phones",
        "price": 13499,
        "original": 13499,
        "rating": 4.5,
        "image": "https://rukminim2.flixcart.com/image/312/312/xif0q/mobile/b/n/k/-original-imahhngjaj95jctk.jpeg?q=70",
        "reviews": 0,
        "badge": ""
    },
    {
        "id": 52,
        "name": "vivo T5x 5G 256GB",
        "category": "phones",
        "price": 22999,
        "original": 22999,
        "rating": 4.5,
        "image": "https://rukminim2.flixcart.com/image/312/312/xif0q/mobile/f/i/v/-original-imahhhfvqhmf7fgg.jpeg?q=70",
        "reviews": 0,
        "badge": ""
    },
    {
        "id": 53,
        "name": "POCO C85 5G 128GB",
        "category": "phones",
        "price": 12999,
        "original": 12999,
        "rating": 4.2,
        "image": "https://rukminim2.flixcart.com/image/312/312/xif0q/mobile/t/h/n/-original-imahgkfunztkbmqg.jpeg?q=70",
        "reviews": 0,
        "badge": ""
    },
    {
        "id": 54,
        "name": "MOTOROLA g57 power 5G",
        "category": "phones",
        "price": 14999,
        "original": 14999,
        "rating": 4.4,
        "image": "https://rukminim2.flixcart.com/image/312/312/xif0q/mobile/z/u/l/-original-imahhqjwyzsjyfvn.jpeg?q=70",
        "reviews": 0,
        "badge": ""
    },
    {
        "id": 55,
        "name": "Samsung M06 5G",
        "category": "phones",
        "price": 11299,
        "original": 11299,
        "rating": 4.1,
        "image": "https://rukminim2.flixcart.com/image/312/312/xif0q/mobile/n/t/g/-original-imaha58mcdsfygaq.jpeg?q=70",
        "reviews": 0,
        "badge": ""
    },
    {
        "id": 56,
        "name": "MOTOROLA g35 5G",
        "category": "phones",
        "price": 11999,
        "original": 11999,
        "rating": 4.2,
        "image": "https://rukminim2.flixcart.com/image/312/312/xif0q/mobile/z/q/m/g35-5g-pb3h0000in-motorola-original-imah7c6ykgz5rtgv.jpeg?q=70",
        "reviews": 0,
        "badge": ""
    },
    {
        "id": 57,
        "name": "OPPO K13 5G 128GB",
        "category": "phones",
        "price": 22999,
        "original": 22999,
        "rating": 4.6,
        "image": "https://rukminim2.flixcart.com/image/312/312/xif0q/mobile/f/k/e/-original-imahbfd4zqn9zazz.jpeg?q=70",
        "reviews": 0,
        "badge": ""
    },
    {
        "id": 58,
        "name": "MOTOROLA Edge 60 Fusion 5G",
        "category": "phones",
        "price": 20999,
        "original": 20999,
        "rating": 4.4,
        "image": "https://rukminim2.flixcart.com/image/312/312/xif0q/mobile/4/a/e/-original-imahkcvgkwzd7u6p.jpeg?q=70",
        "reviews": 0,
        "badge": ""
    },
    {
        "id": 59,
        "name": "realme Narzo 80 Lite 5G",
        "category": "phones",
        "price": 13279,
        "original": 13279,
        "rating": 4.3,
        "image": "https://rukminim2.flixcart.com/image/312/312/xif0q/mobile/m/l/w/-original-imahgkgxmmzhxgzd.jpeg?q=70",
        "reviews": 0,
        "badge": ""
    },
    {
        "id": 60,
        "name": "realme P4 5G 128GB",
        "category": "phones",
        "price": 19999,
        "original": 19999,
        "rating": 4.4,
        "image": "https://rukminim2.flixcart.com/image/312/312/xif0q/mobile/r/4/p/-original-imahf47e6gzt3ggw.jpeg?q=70",
        "reviews": 0,
        "badge": ""
    },
    {
        "id": 61,
        "name": "realme 16 Pro+ 5G 256GB",
        "category": "phones",
        "price": 45999,
        "original": 45999,
        "rating": 4.6,
        "image": "https://rukminim2.flixcart.com/image/312/312/xif0q/mobile/6/a/m/-original-imahj8yhhpt2aytf.jpeg?q=70",
        "reviews": 0,
        "badge": ""
    },
    {
        "id": 62,
        "name": "realme GT 7 256GB",
        "category": "phones",
        "price": 36999,
        "original": 36999,
        "rating": 4.5,
        "image": "https://rukminim2.flixcart.com/image/312/312/xif0q/mobile/8/l/f/-original-imahjrpe4r7cfwu3.jpeg?q=70",
        "reviews": 0,
        "badge": ""
    },
    {
        "id": 101,
        "name": "Apple iPhone 17 Pro Max 256GB",
        "category": "phones",
        "price": 149900,
        "original": 149900,
        "rating": 4.9,
        "image": "https://rukminim2.flixcart.com/image/312/312/xif0q/mobile/0/p/g/-original-imahft6cfwg6yta2.jpeg?q=70",
        "reviews": 0,
        "badge": "New"
    },
    {
        "id": 102,
        "name": "Apple iPhone 17 256GB",
        "category": "phones",
        "price": 82900,
        "original": 82900,
        "rating": 4.7,
        "image": "https://rukminim2.flixcart.com/image/312/312/xif0q/mobile/s/t/g/-original-imahft5gqkxzyeqa.jpeg?q=70",
        "reviews": 0,
        "badge": "New"
    },
    {
        "id": 103,
        "name": "Apple iPhone 17e 256GB",
        "category": "phones",
        "price": 64900,
        "original": 64900,
        "rating": 4.9,
        "image": "https://rukminim2.flixcart.com/image/312/312/xif0q/mobile/x/w/8/-original-imahh652uegnztz3.jpeg?q=70",
        "reviews": 0,
        "badge": "New"
    },
    {
        "id": 104,
        "name": "Apple iPhone 16 128GB",
        "category": "phones",
        "price": 69900,
        "original": 69900,
        "rating": 4.6,
        "image": "https://rukminim2.flixcart.com/image/312/312/xif0q/mobile/g/l/q/-original-imahgfmzdbnzzjjg.jpeg?q=70",
        "reviews": 0,
        "badge": ""
    },
    {
        "id": 105,
        "name": "Apple iPhone 16 Pro Max 256GB",
        "category": "phones",
        "price": 144990,
        "original": 144990,
        "rating": 4.7,
        "image": "https://rukminim2.flixcart.com/image/312/312/xif0q/mobile/r/8/8/-original-imahggevcrkzezzv.jpeg?q=70",
        "reviews": 0,
        "badge": ""
    },
    {
        "id": 106,
        "name": "Apple iPhone 16e 128GB",
        "category": "phones",
        "price": 59900,
        "original": 59900,
        "rating": 4.5,
        "image": "https://rukminim2.flixcart.com/image/312/312/xif0q/mobile/1/p/c/-original-imah9khhnfvstqka.jpeg?q=70",
        "reviews": 0,
        "badge": ""
    },
    {
        "id": 201,
        "name": "boAt Rockerz 450 Bluetooth Headphone",
        "category": "audio",
        "price": 1299,
        "original": 2990,
        "rating": 4.1,
        "image": "https://th.bing.com/th/id/OIP.Iz2sx0jtTFFo08qJe45WNgHaH0?w=185&h=195&c=7&r=0&o=7&dpr=1.3&pid=1.7&rm=3",
        "reviews": 52000,
        "badge": "Sale"
    },
    {
        "id": 202,
        "name": "Sony WH-CH520 Wireless Headphone",
        "category": "audio",
        "price": 3490,
        "original": 5990,
        "rating": 4.3,
        "image": "https://th.bing.com/th/id/OIP.44ciNE8XxJXm84XpFy4NggHaLd?w=129&h=200&c=7&r=0&o=7&dpr=1.3&pid=1.7&rm=3",
        "reviews": 12000,
        "badge": "Sale"
    },
    {
        "id": 205,
        "name": "boAt Airdopes 141 TWS Earbuds",
        "category": "audio",
        "price": 999,
        "original": 2990,
        "rating": 4.0,
        "image": "https://th.bing.com/th/id/OIP.uMky5HH9Dq6smht3ZlL3qgHaHS?w=199&h=195&c=7&r=0&o=7&dpr=1.3&pid=1.7&rm=3",
        "reviews": 98000,
        "badge": "Hot"
    },
    {
        "id": 203,
        "name": "Logitech G102 Gaming Mouse",
        "category": "accessories",
        "price": 1495,
        "original": 2495,
        "rating": 4.4,
        "image": "https://th.bing.com/th/id/OIP.PhbUQYIkv5se0nQr9DKDWAHaHa?w=177&h=180&c=7&r=0&o=7&dpr=1.3&pid=1.7&rm=3",
        "reviews": 35000,
        "badge": "Sale"
    },
    {
        "id": 204,
        "name": "Cosmic Byte CB-GK-25 Mechanical Keyboard",
        "category": "accessories",
        "price": 2299,
        "original": 3999,
        "rating": 4.2,
        "image": "https://th.bing.com/th/id/OIP.CEYn4_fJLr5vSD8P8Ld74wHaC_?w=317&h=141&c=7&r=0&o=7&dpr=1.3&pid=1.7&rm=3",
        "reviews": 8900,
        "badge": ""
    },
    {
        "id": 206,
        "name": "Samsung Galaxy Watch 6",
        "category": "accessories",
        "price": 18999,
        "original": 26999,
        "rating": 4.5,
        "image": "https://th.bing.com/th/id/OIP.T3j9bagPmorFAF84-LykzgHaEK?w=331&h=186&c=7&r=0&o=7&dpr=1.3&pid=1.7&rm=3",
        "reviews": 5600,
        "badge": "Sale"
    },
    {
    "id": 401,
    "name": "Razer DeathAdder V3 Gaming Mouse",
    "category": "accessories",
    "price": 5499,
    "original": 6999,
    "rating": 4.6,
    "reviews": 11203,
    "badge": "",
    "image": "https://th.bing.com/th/id/OIP.wXoTNxiXoAgt7YmgLsz0FQHaEK?w=317&h=180&c=7&r=0&o=7&dpr=1.3&pid=1.7&rm=3"
  },
  {
    "id": 402,
    "name": "Logitech G502 X Gaming Mouse",
    "category": "accessories",
    "price": 6499,
    "original": 8499,
    "rating": 4.5,
    "reviews": 8732,
    "badge": "Sale",
    "image": "https://th.bing.com/th/id/OIP.PUrULofeRMAkXPussQKhsgHaFj?w=246&h=184&c=7&r=0&o=7&dpr=1.3&pid=1.7&rm=3"
  },
  {
    "id": 403,
    "name": "HyperX Pulsefire Haste 2",
    "category": "accessories",
    "price": 3999,
    "original": 5499,
    "rating": 4.4,
    "reviews": 5421,
    "badge": "",
    "image": "https://th.bing.com/th/id/OIP.AP7XJQXJ069iUfgB4Q7b2QHaEK?w=222&h=180&c=7&r=0&o=7&dpr=1.3&pid=1.7&rm=3"
  },
  {
    "id": 404,
    "name": "Keychron K2 Mechanical Keyboard",
    "category": "accessories",
    "price": 7499,
    "original": 8999,
    "rating": 4.5,
    "reviews": 6321,
    "badge": "",
    "image": "https://th.bing.com/th/id/OIP.qcdW6TvlRH6a-eVeKfztbwHaEK?w=259&h=180&c=7&r=0&o=7&dpr=1.3&pid=1.7&rm=3"
  },
  {
    "id": 405,
    "name": "Razer BlackWidow V4 Keyboard",
    "category": "accessories",
    "price": 8999,
    "original": 11999,
    "rating": 4.6,
    "reviews": 4231,
    "badge": "Hot",
    "image": "https://th.bing.com/th/id/OIP.x7r66iM8gTWrjmpLyDiyugHaEl?w=250&h=180&c=7&r=0&o=7&dpr=1.3&pid=1.7&rm=3"
  },
  {
    "id": 406,
    "name": "Cosmic Byte Firefly RGB Keyboard",
    "category": "accessories",
    "price": 1999,
    "original": 2999,
    "rating": 4.2,
    "reviews": 19832,
    "badge": "Sale",
    "image": "https://th.bing.com/th/id/OIP.P3CW8vgII6GdHRsFVtZ_aQHaEl?w=253&h=180&c=7&r=0&o=7&dpr=1.3&pid=1.7&rm=3"
  },
  {
    "id": 408,
    "name": "Bose QuietComfort 45 Headphone",
    "category": "audio",
    "price": 24990,
    "original": 32990,
    "rating": 4.7,
    "reviews": 8921,
    "badge": "",
    "image": "https://th.bing.com/th/id/OIP.IgjW4IKMj7s3nHKNHSWrFQHaJz?w=145&h=192&c=7&r=0&o=7&dpr=1.3&pid=1.7&rm=3"
  },
  {
    "id": 409,
    "name": "JBL Tune 770NC Headphone",
    "category": "audio",
    "price": 6999,
    "original": 9999,
    "rating": 4.3,
    "reviews": 12043,
    "badge": "Sale",
    "image": "https://th.bing.com/th/id/OIP.m39DBOOCS-1LEbU7eKPe-AHaHa?w=186&h=186&c=7&r=0&o=7&dpr=1.3&pid=1.7&rm=3"
  },
  {
    "id": 410,
    "name": "boAt Rockerz 550 Headphone",
    "category": "audio",
    "price": 1799,
    "original": 3990,
    "rating": 4.1,
    "reviews": 52341,
    "badge": "Hot",
    "image": "https://th.bing.com/th/id/OIP.c6v8dh4t_aaq7sKgKwo3tAHaHa?w=176&h=180&c=7&r=0&o=7&dpr=1.3&pid=1.7&rm=3"
  },
  {
    "id": 411,
    "name": "Apple Watch Series 9 45mm",
    "category": "accessories",
    "price": 44900,
    "original": 48900,
    "rating": 4.8,
    "reviews": 9832,
    "badge": "New",
    "image": "https://th.bing.com/th/id/OIP.DVQRLVEKGaAFoTuADWolswHaIw?w=143&h=180&c=7&r=0&o=7&dpr=1.3&pid=1.7&rm=3"
  },
  {
    "id": 412,
    "name": "Samsung Galaxy Watch 6 Classic",
    "category": "accessories",
    "price": 32999,
    "original": 39999,
    "rating": 4.5,
    "reviews": 6743,
    "badge": "",
    "image": "https://th.bing.com/th/id/OIP.ho3z735I9VvG3n99qY0biQHaIt?w=159&h=187&c=7&r=0&o=7&dpr=1.3&pid=1.7&rm=3"
  },
  {
    "id": 413,
    "name": "Noise ColorFit Pro 5 Smartwatch",
    "category": "accessories",
    "price": 3999,
    "original": 6999,
    "rating": 4.1,
    "reviews": 28432,
    "badge": "Sale",
    "image": "https://th.bing.com/th/id/OIP.KXUW1AwYswYmJnYf6lge9gHaEK?w=297&h=180&c=7&r=0&o=7&dpr=1.3&pid=1.7&rm=3"
  },
  {
    "id": 414,
    "name": "Garmin Forerunner 255 Smartwatch",
    "category": "accessories",
    "price": 29999,
    "original": 34999,
    "rating": 4.6,
    "reviews": 3421,
    "badge": "",
    "image": "https://th.bing.com/th/id/OIP.zW7w67tFegGdZaoMbGGQUQHaI_?w=152&h=185&c=7&r=0&o=7&dpr=1.3&pid=1.7&rm=3"
  },
  {
    "id": 415,
    "name": "Boat Wave Flex Smartwatch",
    "category": "accessories",
    "price": 1799,
    "original": 3990,
    "rating": 4.0,
    "reviews": 41230,
    "badge": "Hot",
    "image": "https://th.bing.com/th/id/OIP.lMnAzynBMP7d_Mkl0QegoQHaEJ?w=301&h=180&c=7&r=0&o=7&dpr=1.3&pid=1.7&rm=3"
  },
  {
    "name": "Samsung Galaxy F16 5G (Bling Black, 128 GB)",
    "price": 13999,
    "rating": 4.21,
    "image": "https://rukminim2.flixcart.com/image/312/312/xif0q/mobile/b/6/n/-original-imahcqcwz7msj6rj.jpeg?q=70",
    "category": "phones",
    "original": 13999,
    "reviews": 0,
    "badge": "",
    "id": 101
  },
  {
    "name": "Samsung Galaxy F06 5G (Bahama Blue, 128 GB)",
    "price": 14999,
    "rating": 4.223,
    "image": "https://rukminim2.flixcart.com/image/312/312/xif0q/mobile/v/o/d/-original-imahfvrmfkwybeyc.jpeg?q=70",
    "category": "phones",
    "original": 14999,
    "reviews": 0,
    "badge": "",
    "id": 102
  },
  {
    "name": "Samsung Galaxy F16 5G (Glam Green, 128 GB)",
    "price": 13999,
    "rating": 4.21,
    "image": "https://rukminim2.flixcart.com/image/312/312/xif0q/mobile/z/6/a/-original-imahcrefkxrezmry.jpeg?q=70",
    "category": "phones",
    "original": 13999,
    "reviews": 0,
    "badge": "",
    "id": 103
  },
  {
    "name": "Samsung Galaxy F16 5G (Glam Green, 128 GB)",
    "price": 15499,
    "rating": 4.23,
    "image": "https://rukminim2.flixcart.com/image/312/312/xif0q/mobile/g/a/j/-original-imahcqcwhvvxsrgd.jpeg?q=70",
    "category": "phones",
    "original": 15499,
    "reviews": 0,
    "badge": "",
    "id": 104
  },
  {
    "name": "Tecno Pova Curve 5G (Neon Cyan, 128 GB)",
    "price": 17999,
    "rating": 4.41,
    "image": "https://rukminim2.flixcart.com/image/312/312/xif0q/mobile/m/y/n/-original-imahctmx6yhzhghw.jpeg?q=70",
    "category": "phones",
    "original": 17999,
    "reviews": 0,
    "badge": "",
    "id": 105
  },
  {
    "name": "realme 15T 5G (Silk Blue, 128 GB)",
    "price": 22999,
    "rating": 4.37,
    "image": "https://rukminim2.flixcart.com/image/312/312/xif0q/mobile/p/6/5/-original-imahfkfyshxg28wu.jpeg?q=70",
    "category": "phones",
    "original": 22999,
    "reviews": 0,
    "badge": "",
    "id": 106
  },
  {
    "name": "Samsung Galaxy F17 5G (Neo Black, 128 GB)",
    "price": 19499,
    "rating": 4.3141,
    "image": "https://rukminim2.flixcart.com/image/312/312/xif0q/mobile/r/b/h/-original-imahftgfzdzfpgft.jpeg?q=70",
    "category": "phones",
    "original": 19499,
    "reviews": 0,
    "badge": "",
    "id": 107
  },
  {
    "name": "Samsung Galaxy F17 5G (Violet Pop, 128 GB)",
    "price": 17999,
    "rating": 4.2154,
    "image": "https://rukminim2.flixcart.com/image/312/312/xif0q/mobile/h/b/h/-original-imahftgfjn6a9kpw.jpeg?q=70",
    "category": "phones",
    "original": 17999,
    "reviews": 0,
    "badge": "",
    "id": 108
  },
  {
    "name": "Coming Soon",
    "price": 16999,
    "rating": 4.347,
    "image": "https://rukminim2.flixcart.com/image/312/312/l0igvww0/mobile/y/j/4/-original-imagcaaw4d7bv7pj.jpeg?q=70",
    "category": "phones",
    "original": 16999,
    "reviews": 0,
    "badge": "",
    "id": 109
  },
  {
    "name": "Samsung Galaxy F17 5G (Violet Pop, 128 GB)",
    "price": 18720,
    "rating": 4.3141,
    "image": "https://rukminim2.flixcart.com/image/312/312/xif0q/mobile/h/b/h/-original-imahftgfjn6a9kpw.jpeg?q=70",
    "category": "phones",
    "original": 18720,
    "reviews": 0,
    "badge": "",
    "id": 110
  },
  {
    "name": "Samsung Galaxy F17 5G (Neo Black, 128 GB)",
    "price": 17999,
    "rating": 4.2154,
    "image": "https://rukminim2.flixcart.com/image/312/312/xif0q/mobile/r/b/h/-original-imahftgfzdzfpgft.jpeg?q=70",
    "category": "phones",
    "original": 17999,
    "reviews": 0,
    "badge": "",
    "id": 111
  },
  {
    "name": "realme 15T 5G (Silk Blue, 128 GB)",
    "price": 26999,
    "rating": 4.37,
    "image": "https://rukminim2.flixcart.com/image/312/312/xif0q/mobile/f/t/7/-original-imahhy8pvryffj5p.jpeg?q=70",
    "category": "phones",
    "original": 26999,
    "reviews": 0,
    "badge": "",
    "id": 112
  },
  {
    "name": "Coming Soon",
    "price": 14999,
    "rating": 4.478,
    "image": "https://rukminim2.flixcart.com/image/312/312/xif0q/mobile/k/u/n/-original-imagzjhwtfthcmzz.jpeg?q=70",
    "category": "phones",
    "original": 14999,
    "reviews": 0,
    "badge": "",
    "id": 113
  },
  {
    "name": "Coming Soon",
    "price": 12999,
    "rating": 4.44,
    "image": "https://rukminim2.flixcart.com/image/312/312/xif0q/mobile/4/h/e/-original-imagzjhwmsamexfk.jpeg?q=70",
    "category": "phones",
    "original": 12999,
    "reviews": 0,
    "badge": "",
    "id": 114
  },
  {
    "name": "Coming Soon",
    "price": 16999,
    "rating": 4.347,
    "image": "https://rukminim2.flixcart.com/image/312/312/l0igvww0/mobile/o/q/q/-original-imagcaaw5zg6amp5.jpeg?q=70",
    "category": "phones",
    "original": 16999,
    "reviews": 0,
    "badge": "",
    "id": 115
  },
  {
    "name": "Samsung Galaxy F14 5G (GOAT Green, 128 GB)",
    "price": 18490,
    "rating": 4.21,
    "image": "https://rukminim2.flixcart.com/image/312/312/xif0q/mobile/g/n/k/-original-imagtyxb86ddjhzh.jpeg?q=70",
    "category": "phones",
    "original": 18490,
    "reviews": 0,
    "badge": "",
    "id": 116
  },
  {
    "name": "Samsung Galaxy F17 5G (Violet Pop, 128 GB)",
    "price": 21950,
    "rating": 4.0,
    "image": "https://rukminim2.flixcart.com/image/312/312/xif0q/mobile/d/s/c/-original-imahfvrhbvhfccp2.jpeg?q=70",
    "category": "phones",
    "original": 21950,
    "reviews": 0,
    "badge": "",
    "id": 117
  },
  {
    "name": "Coming Soon",
    "price": 15999,
    "rating": 4.41,
    "image": "https://rukminim2.flixcart.com/image/312/312/xif0q/mobile/u/1/h/-original-imagpfbvfu4p55n4.jpeg?q=70",
    "category": "phones",
    "original": 15999,
    "reviews": 0,
    "badge": "",
    "id": 118
  },
  {
    "name": "Motorola Edge 40 Neo (Black Beauty, 128 GB)",
    "price": 27999,
    "rating": 4.36,
    "image": "https://rukminim2.flixcart.com/image/312/312/xif0q/mobile/p/r/r/edge-40-neo-payj0002in-motorola-original-imagtkzh8zrvp3uj.jpeg?q=70",
    "category": "phones",
    "original": 27999,
    "reviews": 0,
    "badge": "",
    "id": 119
  },
  {
    "name": "Coming Soon",
    "price": 18999,
    "rating": 4.334,
    "image": "https://rukminim2.flixcart.com/image/312/312/l0igvww0/mobile/9/a/w/-original-imagcaaw5gzbdtxj.jpeg?q=70",
    "category": "phones",
    "original": 18999,
    "reviews": 0,
    "badge": "",
    "id": 120
  },
  {
    "name": "Google Pixel 10 Pro (Moonstone, 256 GB)",
    "price": 109999,
    "rating": 4.6448,
    "image": "https://rukminim2.flixcart.com/image/312/312/xif0q/mobile/6/o/a/-original-imahfjsfumzzvyzz.jpeg?q=70",
    "category": "phones",
    "original": 109999,
    "reviews": 0,
    "badge": "",
    "id": 121
  },
  {
    "name": "vivo T2x 5G (Marine Blue, 128 GB)",
    "price": 12999,
    "rating": 4.44,
    "image": "https://rukminim2.flixcart.com/image/312/312/xif0q/mobile/k/u/n/-original-imagzjhwtfthcmzz.jpeg?q=70",
    "category": "phones",
    "original": 12999,
    "reviews": 0,
    "badge": "",
    "id": 122
  },
  {
    "name": "vivo T2x 5G (Aurora Gold, 128 GB)",
    "price": 14999,
    "rating": 4.478,
    "image": "https://rukminim2.flixcart.com/image/312/312/xif0q/mobile/c/s/x/-original-imagzjhwaaewgj8r.jpeg?q=70",
    "category": "phones",
    "original": 14999,
    "reviews": 0,
    "badge": "",
    "id": 123
  },
  {
    "name": "Coming Soon",
    "price": 18999,
    "rating": 4.334,
    "image": "https://rukminim2.flixcart.com/image/312/312/l0igvww0/mobile/y/j/4/-original-imagcaaw4d7bv7pj.jpeg?q=70",
    "category": "phones",
    "original": 18999,
    "reviews": 0,
    "badge": "",
    "id": 124
  }
]

import os

# Load scraped products
try:
    json_path = os.path.join(os.path.dirname(__file__), "flipkart_data.json")
    with open(json_path, "r", encoding="utf-8") as f:
        scraped_products = json.load(f)

    for p in scraped_products:
        if p.get("name") in ["Login", "Cart", "More", "Trending", "Currently unavailable"]:
            continue
        if isinstance(p.get("price"), str):
            try:
                p["price"] = int(p["price"].replace("₹", "").replace(",", ""))
            except:
                p["price"] = 0
        p["original"] = p.get("original", p.get("price", 0))
        if isinstance(p.get("rating"), str):
            try:
                p["rating"] = float(p["rating"])
            except:
                p["rating"] = 4.0
        p["reviews"] = p.get("reviews", 0)
        p["badge"] = p.get("badge", "")
        products.append(p)

    print(f"✅ {len(scraped_products)} scraped products loaded!")
except Exception as e:
    print(f"⚠️ Scraped data load nahi hua: {e}")

print(f"Total products: {len(products)}")


